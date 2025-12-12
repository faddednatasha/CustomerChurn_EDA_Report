import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Define file paths
INPUT_FILE_PATH = 'data/non_churn_customers.csv'
OUTPUT_IMAGE_PATH = 'reports/correlation_heatmap.png'

def load_data(file_path):
    """Loads the final cleaned data."""
    if not os.path.exists(file_path):
        print("Error: Input file for analysis not found.")
        return None
    return pd.read_csv(file_path)

def perform_correlation_analysis(df):
    """
    Calculates the correlation matrix and generates a heatmap.
    """
    if df is None:
        return

    # 1. Select only numeric columns for correlation
    # We use Tenure and MonthlyCharges to see if they are related
    numeric_df = df.select_dtypes(include=['float64', 'int64'])
    
    # 2. Calculate the correlation matrix
    # Values close to 1 mean strong positive relationship
    # Values close to -1 mean strong negative relationship
    corr_matrix = numeric_df.corr()
    
    print("\n--- Correlation Matrix ---")
    print(corr_matrix)

    # 3. Create a directory for reports if it doesn't exist
    os.makedirs(os.path.dirname(OUTPUT_IMAGE_PATH), exist_ok=True)

    # 4. Generate the Heatmap
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
    
    plt.title('Feature Correlation Heatmap (Loyal Customers)')
    
    # 5. Save the plot
    plt.savefig(OUTPUT_IMAGE_PATH)
    plt.close()
    
    print(f"\n✅ Correlation Heatmap saved to {OUTPUT_IMAGE_PATH}")
    print("This visualization helps identify if tenure and charges move together.")

if __name__ == "__main__":
    df = load_data(INPUT_FILE_PATH)
    if df is not None:
        perform_correlation_analysis(df)
