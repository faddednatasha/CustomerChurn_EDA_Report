import sqlite3
import os

# Define file paths
DATABASE_NAME = 'customer_analytics.db'
DB_PATH = os.path.join('data', DATABASE_NAME)
TABLE_NAME = 'loyal_customers'

def run_analytical_query(db_path: str):
    """
    Connects to the database and runs the aggregation query.
    """
    conn = None
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # --- THE CORE ANALYTICAL SQL QUERY ---
        # Group By: Summarizes the average charge for each Contract_Type group.
        analytical_query = f"""
        SELECT 
            Contract_Type,
            AVG(MonthlyCharges) AS Average_Monthly_Charge,
            COUNT(CustomerID) AS Total_Customers
        FROM 
            {TABLE_NAME}
        GROUP BY 
            Contract_Type;
        """

        print("Executing Query: Average Monthly Charges by Contract Type...")
        cursor.execute(analytical_query)
        results = cursor.fetchall()
        
        # Print results neatly
        print("-" * 50)
        print("| Contract Type      | Avg Monthly Charge | Total Customers |")
        print("-" * 50)
        for row in results:
            print(f"| {row[0]:<18} | ${row[1]:<18.2f} | {row[2]:<15} |")
        print("-" * 50)

    except sqlite3.Error as e:
        print(f"Error running SQL query: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    if os.path.exists(DB_PATH):
        run_analytical_query(DB_PATH)
    else:
        print(f"Database file not found at {DB_PATH}. Please run Day 6 and Day 7 scripts first.")
