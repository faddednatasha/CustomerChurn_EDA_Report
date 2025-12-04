import pandas as pd
import os

# Define file paths for loading and saving data
INPUT_FILE_PATH = 'data/cleaned_data_step4.csv' 
OUTPUT_FILE_PATH = 'data/non_churn_customers.csv'

def load_data(file_path: str) -> pd.DataFrame:
    """Loads the pre-saved data."""
    if not os.path.exists(file_path):
        print("Error: Input file for filtering not found.")
        return None
    return pd.read_csv(file_path)

def filter_data_by_churn_status(df: pd.DataFrame) -> pd.DataFrame:
    """
    Filters the DataFrame to include only customers who did NOT churn ('No').
    """
    if df is None:
        return None

    target_column = 'Churn'
    filter_value = 'No' # Targeting loyal customers

    # 1. Check current counts before filtering
    print(f"Total customers before filtering: {len(df)}")
    print(f"Distribution: \n{df[target_column].value_counts()}")

    # 2. PERFORM BOOLEAN FILTERING (the core operation)
    # df[df[column] == value] creates a new DataFrame based on the condition
    loyal_customers_df = df[df[target_column] == filter_value].copy()
    
    # 3. Check counts after filtering
    print(f"\nTotal customers remaining after filtering ({target_column} == '{filter_value}'): {len(loyal_customers_df)}")
    
    return loyal_customers_df

if __name__ == "__main__":
    df = load_data(INPUT_FILE_PATH)
    filtered_df = filter_data_by_churn_status(df)

    if filtered_df is not None:
        # Save the result for the next phase (SQL Integration)
        filtered_df.to_csv(OUTPUT_FILE_PATH, index=False)
        print(f"\nSuccessfully filtered and saved loyal customer data to {OUTPUT_FILE_PATH}")
