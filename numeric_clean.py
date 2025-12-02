import pandas as pd
import os
import numpy as np

# Define file paths for loading and saving data
INPUT_FILE_PATH = 'data/synthetic_churn_data.csv' 
OUTPUT_FILE_PATH = 'data/cleaned_data_step3.csv' 

def load_data(file_path: str) -> pd.DataFrame:
    """Loads the pre-saved data."""
    if not os.path.exists(file_path):
        print("Error: Input file not found.")
        return None
    # Load the data, forcing the 'MonthlyCharges' column to be read as a string 
    # to better simulate dirty data coming from a raw source.
    df = pd.read_csv(file_path, dtype={'MonthlyCharges': str}) 
    return df

def clean_and_convert_numeric(df: pd.DataFrame) -> pd.DataFrame:
    """
    Simulates a data quality issue and then corrects the column type.
    """
    if df is None:
        return None

    column_name = 'MonthlyCharges'

    # --- SIMULATE ERROR: Inject a non-numeric character (e.g., a currency symbol) ---
    # This simulates data that would fail type conversion
    df.loc[df.index[:3], column_name] = '$ ' + df.loc[df.index[:3], column_name]
    
    # Check the data type before cleaning
    print(f"Dtype before cleaning: {df[column_name].dtype}")

    # --- CLEANING STEP 1: Remove all non-numeric characters ---
    # Remove the '$' symbol and any leading/trailing spaces
    df[column_name] = df[column_name].str.replace('$', '', regex=False).str.replace(' ', '', regex=False)
    
    # --- CLEANING STEP 2: Convert the cleaned column to a numeric type ---
    # The errors='coerce' argument is key: it forces any remaining text values to NaN (Not a Number/missing value)
    df[column_name] = pd.to_numeric(df[column_name], errors='coerce')

    # Check the data type after conversion
    print(f"Dtype after cleaning: {df[column_name].dtype}")
    
    return df

if __name__ == "__main__":
    df = load_data(INPUT_FILE_PATH)
    cleaned_df = clean_and_convert_numeric(df)

    if cleaned_df is not None:
        print("\nCleaned Data Sample:")
        print(cleaned_df[[column_name, 'Contract_Type']].head())

        # Save the result for the next analysis step
        cleaned_df.to_csv(OUTPUT_FILE_PATH, index=False)
        print(f"\nSuccessfully cleaned and saved data to {OUTPUT_FILE_PATH}")
