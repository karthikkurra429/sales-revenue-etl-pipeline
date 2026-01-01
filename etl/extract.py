import pandas as pd

def extract_data():
    sales = pd.read_csv("data/raw/sales.csv")
    customers = pd.read_csv("data/raw/customers.csv")
    products = pd.read_csv("data/raw/products.csv")
    return sales, customers, products

if __name__ == "__main__":
    sales, customers, products = extract_data()
    print("Sales rows:", len(sales))
    print("Customers rows:", len(customers))
    print("Products rows:", len(products))