import pandas as pd
import os

# Define file path
INPUT_FILE_PATH = 'data/non_churn_customers.csv'
OUTPUT_REPORT_PATH = 'reports/descriptive_statistics.txt'

def load_data(file_file_path: str) -> pd.DataFrame:
    """Loads the final cleaned data."""
    if not os.path.exists(file_file_path):
        print("Error: Input file for statistics not found.")
        return None
    return pd.read_csv(file_file_path)

def generate_summary_statistics(df: pd.DataFrame):
    """
    Calculates and prints key descriptive statistics for numeric columns.
    """
    if df is None:
        return

    # Select only the numeric columns for descriptive statistics
    numeric_cols = ['Tenure_Months', 'MonthlyCharges']
    
    # 1. Use the powerful .describe() method
    stats_report = df[numeric_cols].describe().T # .T transposes for a cleaner view
    
    # 2. Print to console (for immediate proof)
    print("\n--- Descriptive Statistics Report (Loyal Customers) ---")
    print(stats_report)

    # 3. Save the report to a text file (for easy reference in the portfolio)
    os.makedirs(os.path.dirname(OUTPUT_REPORT_PATH), exist_ok=True)
    with open(OUTPUT_REPORT_PATH, 'w') as f:
        f.write("Descriptive Statistics Report (Loyal Customers):\n\n")
        f.write(stats_report.to_string())
    
    print(f"\n✅ Summary statistics saved to {OUTPUT_REPORT_PATH}")
    print("These values (mean, min, max) will be used for final insights.")


if __name__ == "__main__":
    df = load_data(INPUT_FILE_PATH)
    if df is not None:
        generate_summary_statistics(df)
