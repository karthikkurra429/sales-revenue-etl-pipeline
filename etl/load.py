from sqlalchemy import create_engine
from transform import transform_data
from extract import extract_data

def load_data():
    """
    Load transformed data into PostgreSQL
    """
    # 1️⃣ Extract data
    sales, customers, products = extract_data()

    # 2️⃣ Transform data
    transformed = transform_data(sales, customers, products)

    # 3️⃣ Create database connection
    # Replace username, password, host, port, database_name
    engine = create_engine(
    'postgresql+psycopg2://karthikkurra@localhost:5432/sales_db'
)

    # 4️⃣ Load data into table 'sales_fact'
    transformed.to_sql('sales_fact', engine, if_exists='replace', index=False)

    print("✅ Data loaded successfully into PostgreSQL!")

# 5️⃣ Run script if executed directly
if __name__ == "__main__":
    load_data()
