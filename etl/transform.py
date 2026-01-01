import pandas as pd

def transform_data(sales, customers, products):
    """
    Transform raw data into a cleaned and enriched dataset
    """
    # 1. Convert order_date and signup_date to datetime
    sales['order_date'] = pd.to_datetime(sales['order_date'])
    customers['signup_date'] = pd.to_datetime(customers['signup_date'])

    # 2. Merge sales with customer data
    sales_customers = pd.merge(sales, customers, on='customer_id', how='left')

    # 3. Merge with product data
    full_data = pd.merge(sales_customers, products, on='product_id', how='left')

    # 4. Calculate revenue and profit
    full_data['revenue'] = full_data['quantity'] * full_data['unit_price']
    full_data['profit'] = full_data['revenue'] - (full_data['quantity'] * full_data['cost_price'])

    # 5. Optional: sort by order_date
    full_data = full_data.sort_values(by='order_date')

    return full_data

# Test transform function
if __name__ == "__main__":
    from extract import extract_data
    sales, customers, products = extract_data()
    transformed = transform_data(sales, customers, products)
    print(transformed)
