import pandas as pd
import os

# --- Configuration (Load the data saved) ---
FILE_PATH = 'data/synthetic_churn_data.csv' 

def load_data(file_path: str) -> pd.DataFrame:
    """Loads the pre-saved data from the data folder."""
    if not os.path.exists(file_path):
        print("🚨 Error: Data file not found. Run Day 1 script first!")
        return None
    return pd.read_csv(file_path)

def perform_data_checks(df: pd.DataFrame):
    """
    Performs basic data checks to identify data types and missing values.
    """
    if df is None:
        return

    print("=" * 40)
    print("Data Quality Check Report")
    print("=" * 40)

    # 1. Total Rows and Columns (Shape)
    print(f"Total Rows: {df.shape[0]}")
    print(f"Total Columns: {df.shape[1]}")
    
    # 2. Check Column Data Types (Crucial for identifying text columns that should be numbers)
    print("\n--- Column Data Types (Dtypes) ---")
    print(df.dtypes) 
    # NOTE: You may notice all your numeric columns (Tenure, Charges) are correctly reported as float/int 
    # since we created them this way. In real-world data, they often appear as 'object' (string/text).

    # 3. Check for Missing Values (Nulls)
    print("\n--- Missing Value Count ---")
    # This command calculates the count of nulls for every column
    missing_data = df.isnull().sum()
    
    # Filter and print ONLY columns that have 1 or more missing values
    columns_with_nulls = missing_data[missing_data > 0]
    
    if columns_with_nulls.empty:
        print("🎉 No missing values found in the current dataset.")
    else:
        print("Columns with Missing Values (Needs cleaning):")
        print(columns_with_nulls.sort_values(ascending=False))

    print("\n--- Data Check Complete ---")


if __name__ == "__main__":
    # --- Execute the Data Check ---
    raw_df = load_data(FILE_PATH)
    perform_data_checks(raw_df)
    
