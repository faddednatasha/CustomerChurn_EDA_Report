import sqlite3
import os

# Define the name of your local database file
DATABASE_NAME = 'customer_analytics.db'

def create_connection(db_file: str):
    """Creates a database connection to the SQLite database specified by db_file."""
    conn = None
    try:
        # If the file doesn't exist, sqlite3 creates it.
        conn = sqlite3.connect(db_file)
        print(f"Connection successful! Database file: {db_file}")
        return conn
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
        return None

def create_customer_table(conn: sqlite3.Connection):
    """
    Creates the 'loyal_customers' table structure (schema) in the database.
    """
    if conn is None:
        return

    # 1. Define the SQL command to create the table. 
    # The columns match the cleaned data from Day 5.
    create_table_sql = """
    CREATE TABLE IF NOT EXISTS loyal_customers (
        CustomerID TEXT PRIMARY KEY,
        Tenure_Months INTEGER,
        MonthlyCharges REAL,
        Contract_Type TEXT,
        Churn TEXT
    );
    """
    
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
        conn.commit()
        print("\n✅ Table 'loyal_customers' created successfully (or already exists).")
    except sqlite3.Error as e:
        print(f"Error creating table: {e}")


if __name__ == "__main__":
    # Ensure the database is created in the data directory
    db_path = os.path.join('data', DATABASE_NAME)

    # 1. Connect to the database
    conn = create_connection(db_path)

    # 2. Define and execute the table creation
    if conn is not None:
        create_customer_table(conn)
        conn.close()
