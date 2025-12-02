import pandas as pd
import os

def create_synthetic_data() -> pd.DataFrame:
    """
    Generates a small, mock dataset for customer churn analysis.
    This simulates the data we would normally load from a CSV.
    """
    print("Generating synthetic data for the project...")
    
    # 1. Define the data structure using lists of values
    data = {
        'CustomerID': ['C1001', 'C1002', 'C1003', 'C1004', 'C1005', 'C1006', 'C1007', 'C1008', 'C1009', 'C1010'],
        'Tenure_Months': [24, 1, 58, 2, 72, 12, 45, 18, 60, 3], # How long customer has stayed
        'MonthlyCharges': [55.50, 78.90, 110.20, 20.00, 19.95, 85.45, 99.00, 35.80, 105.00, 75.25],
        'Contract_Type': ['One year', 'Month-to-month', 'Two year', 'Month-to-month', 'Two year', 'One year', 'Two year', 'Month-to-month', 'Two year', 'Month-to-month'],
        'Churn': ['No', 'Yes', 'No', 'Yes', 'No', 'No', 'No', 'Yes', 'No', 'Yes'] # Target variable
    }
    
    # 2. Create the Pandas DataFrame
    df = pd.DataFrame(data)
    
    # 3. Save the synthetic data to a file for use and beyond
    try:
        if not os.path.exists('data'):
            os.makedirs('data')
        df.to_csv('data/synthetic_churn_data.csv', index=False)
        print("✅ Data saved to data/synthetic_churn_data.csv")
    except Exception as e:
        print(f"Error saving file: {e}")
    
    return df

if __name__ == "__main__":
    # --- Execute the Data Creation ---
    raw_df = create_synthetic_data()

    if raw_df is not None:
        # This output serves as the evidence of your successful commit task!
        print("\n--- Initial Data Snapshot (Day 1 Proof) ---")
        print(f"Total Rows: {len(raw_df)}")
        print(f"Total Columns: {raw_df.shape[1]}")
        print("\nFirst 5 Rows:")
        print(raw_df.head())
        print("-" * 30)

