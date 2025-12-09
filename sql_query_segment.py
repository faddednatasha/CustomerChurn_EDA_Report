import sqlite3
import os


# Define file paths
DATABASE_NAME = 'customer_analytics.db'
DB_PATH = os.path.join('data', DATABASE_NAME)
TABLE_NAME = 'loyal_customers'

def run_segmentation_query(db_path: str):
    """
    Connects to the database and runs the segmentation query using a CASE statement.
    """
    conn = None
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # --- THE CORE ANALYTICAL SQL QUERY ---
        # The CASE statement assigns a segment based on Tenure_Months
        analytical_query = f"""
        SELECT 
            Contract_Type,
            COUNT(CASE WHEN Tenure_Months <= 12 THEN 1 END) AS Rookie_Customers,
            COUNT(CASE WHEN Tenure_Months > 12 AND Tenure_Months <= 48 THEN 1 END) AS MidTerm_Customers,
            COUNT(CASE WHEN Tenure_Months > 48 THEN 1 END) AS Veteran_Customers
        FROM 
            {TABLE_NAME}
        GROUP BY 
            Contract_Type;
        """

        print("Executing Query: Loyal Customer Segmentation by Tenure and Contract Type...")
        cursor.execute(analytical_query)
        results = cursor.fetchall()
        
        # Print results neatly
        print("-" * 75)
        print("| Contract Type      | Rookie (<=12 Mo) | Mid-Term (1-4 Yr) | Veteran (>4 Yr) |")
        print("-" * 75)
        for row in results:
            print(f"| {row[0]:<18} | {row[1]:<16} | {row[2]:<17} | {row[3]:<15} |")
        print("-" * 75)

    except sqlite3.Error as e:
        print(f"Error running SQL query: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    if os.path.exists(DB_PATH):
        run_segmentation_query(DB_PATH)
    else:
        print(f"Database file not found at {DB_PATH}. Please ensure previous setup scripts have run.")
