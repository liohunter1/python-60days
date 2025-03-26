# Day 11: Python Practice
import pandas as pd

print("Day 11 - Python 60 Days Challenge")

class Customer:
    def __init__(self, name, phone, address):
        # Convert all inputs to strings safely
        self.name = str(name) if pd.notna(name) else "N/A"
        self.phone = str(phone) if pd.notna(phone) else "N/A"
        self.address = str(address) if pd.notna(address) else "N/A"

    def get_details(self):
        return f"Customer: {self.name}, Phone: {self.phone}, Address: {self.address}"

def load_customers_from_excel(filename):
    try:
        # Reading the Excel file
        df = pd.read_excel(filename)
        
        # Clean column names by stripping whitespace
        df.columns = df.columns.str.strip()
        
        # Convert relevant columns to string type
        string_columns = ['CLIENT NAME', 'PHONE NO', 'APARTMENT']
        for col in string_columns:
            df[col] = df[col].astype(str)
        
        # Filter out rows with empty or 'nan' client names
        df = df[~df['CLIENT NAME'].isin(['nan', '', 'NaN'])]
        df = df.drop_duplicates(subset=['CLIENT NAME'])
        
        # Create Customer objects from excel data
        customers = []
        for _, row in df.iterrows():
            customer = Customer(
                name=row['CLIENT NAME'],
                phone=row['PHONE NO'],
                address=row['APARTMENT']
            )
            customers.append(customer)
        return customers
        
    except FileNotFoundError:
        print(f"❌ Error: File '{filename}' not found")
        return []
    except Exception as e:
        print(f"❌ Error reading Excel file: {e}")
        print("\nAvailable columns (after cleaning):")
        try:
            print(df.columns.tolist())
        except:
            pass
        return []

def main():
    # Load and display customer details
    excel_file = "Imperial.xlsx"
    print(f"\n📂 Loading customers from: {excel_file}")
    customers = load_customers_from_excel(excel_file)
    
    if customers:
        # Sort customers by name for better display
        customers.sort(key=lambda x: x.name)
        print(f"\n📋 Found {len(customers)} unique customers:")
        print("-" * 50)
        for customer in customers:
            print(customer.get_details())
    else:
        print("❌ No customers loaded")

if __name__ == "__main__":
    main()