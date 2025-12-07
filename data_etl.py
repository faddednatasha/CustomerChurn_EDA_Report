import pandas as pd
import sqlite3
import os

# Define file paths
DATABASE_NAME = 'customer_analytics.db'
INPUT_FILE_PATH = 'data/non_churn_customers.csv'
DB_PATH = os.path.join('data', DATABASE_NAME)
TABLE_NAME = 'loyal_customers'

def load_data(file_path: str) -> pd.DataFrame:
    """Loads the pre-saved, filtered customer data."""
    if not os.path.exists(file_path):
        print("Error: Input file for ETL not found.")
        return None
    return pd.read_csv(file_path)

def etl_to_sql(df: pd.DataFrame, db_path: str, table_name: str):
    """
    Connects to the database and loads the DataFrame into the specified table.
    """
    if df is None:
        return

    conn = None
    try:
        conn = sqlite3.connect(db_path)
        
        # --- THE CORE ETL OPERATION: pandas.to_sql() ---
        # if_exists='replace': Drops the table and recreates it, ensuring a clean load.
        # index=False: Prevents Pandas from writing the DataFrame index as a column.
        df.to_sql(table_name, conn, if_exists='replace', index=False)
        
        # --- VERIFICATION STEP (SQL Query) ---
        cursor = conn.cursor()
        cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
        row_count = cursor.fetchone()[0]
        
        print(f"\n✅ ETL Successful! Total records loaded into '{table_name}': {row_count}")

    except sqlite3.Error as e:
        print(f"Error during data loading (ETL): {e}")
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    df_to_load = load_data(INPUT_FILE_PATH)
    etl_to_sql(df_to_load, DB_PATH, TABLE_NAME)
