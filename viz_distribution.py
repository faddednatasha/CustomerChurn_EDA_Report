import pandas as pd
import matplotlib.pyplot as plt
import os

# Define file paths
INPUT_FILE_PATH = 'data/non_churn_customers.csv'
OUTPUT_IMAGE_PATH = 'reports/monthly_charges_histogram.png'

def load_data(file_path: str) -> pd.DataFrame:
    """Loads the final cleaned data."""
    if not os.path.exists(file_path):
        print("Error: Input file for visualization not found.")
        return None
    return pd.read_csv(file_path)

def create_histogram(df: pd.DataFrame):
    """
    Generates and saves a histogram for the MonthlyCharges column.
    """
    if df is None:
        return

    column_name = 'MonthlyCharges'
    
    # 1. Create a directory for reports if it doesn't exist
    os.makedirs(os.path.dirname(OUTPUT_IMAGE_PATH), exist_ok=True)

    # 2. GENERATE PLOT
    plt.figure(figsize=(8, 5))
    
    # Use the built-in Pandas plotting function for simplicity
    df[column_name].hist(bins=15, edgecolor='black', color='skyblue')
    
    # 3. Add labels and title for professionalism
    plt.title('Distribution of Monthly Charges (Loyal Customers)')
    plt.xlabel('Monthly Charges ($)')
    plt.ylabel('Frequency (Customer Count)')
    plt.grid(axis='y', alpha=0.5)

    # 4. Save the plot
    plt.savefig(OUTPUT_IMAGE_PATH)
    plt.close()
    
    print(f"\n✅ Histogram saved successfully to {OUTPUT_IMAGE_PATH}")
    print("The plot shows how customer charges are spread (e.g., if they cluster at low or high prices).")


if __name__ == "__main__":
    df = load_data(INPUT_FILE_PATH)
    if df is not None:
        create_histogram(df)
