import pandas as pd
from sqlalchemy import create_engine, text

# Database Connection
engine = create_engine("postgresql+psycopg2://postgres:postgres123@postgres:5432/ecommerce_db")

def run_silver_layer():
    df = pd.read_csv("/opt/airflow/data/olist_orders_dataset.csv")
    
    # Cleaning Logic
    date_columns = ['order_purchase_timestamp', 'order_approved_at']
    for col in date_columns:
        df[col] = pd.to_datetime(df[col])
    
    # ERROR FIX: Manual Drop with Transaction
    with engine.begin() as conn:
        conn.execute(text("CREATE SCHEMA IF NOT EXISTS silver;"))
        conn.execute(text("DROP TABLE IF EXISTS silver.orders_cleaned;"))
        df.to_sql('orders_cleaned', conn, schema='silver', if_exists='append', index=False)
    
    print("Silver Layer: Success!")

def run_gold_layer():
    # Silver se data read karna
    df = pd.read_sql("SELECT * FROM silver.orders_cleaned", engine)
    
    # Gold Logic (Aggregation/Filtering)
    gold_df = df[['order_id', 'customer_id', 'order_status', 'order_purchase_timestamp']]
    
    with engine.begin() as conn:
        conn.execute(text("CREATE SCHEMA IF NOT EXISTS gold;"))
        conn.execute(text("DROP TABLE IF EXISTS gold.fact_orders;"))
        gold_df.to_sql('fact_orders', conn, schema='gold', if_exists='append', index=False)
    
    print("Gold Layer: Ready for Power BI!")