import pandas as pd
import matplotlib.pyplot as plt
import os
import seaborn as sns # Used for slightly enhanced visualization style

# Define file paths
INPUT_FILE_PATH = 'data/non_churn_customers.csv'
OUTPUT_IMAGE_PATH = 'reports/contract_type_bar_chart.png'

def load_data(file_file_path: str) -> pd.DataFrame:
    """Loads the final cleaned data."""
    if not os.path.exists(file_file_path):
        print("Error: Input file for visualization not found.")
        return None
    return pd.read_csv(file_file_path)

def create_bar_chart(df: pd.DataFrame):
    """
    Generates and saves a bar chart comparing customer counts by Contract Type.
    """
    if df is None:
        return

    column_name = 'Contract_Type'
    
    # 1. Create a directory for reports if it doesn't exist
    os.makedirs(os.path.dirname(OUTPUT_IMAGE_PATH), exist_ok=True)

    # 2. CALCULATE COUNTS
    # value_counts() is the perfect Pandas method for this task
    contract_counts = df[column_name].value_counts()
    
    # 3. GENERATE PLOT
    plt.figure(figsize=(9, 6))
    
    # Create the bar plot using Seaborn (sns.barplot) for a professional look
    sns.barplot(x=contract_counts.index, y=contract_counts.values, palette="viridis")
    
    # 4. Add labels and title
    plt.title('Customer Count by Contract Type (Loyal Base)')
    plt.xlabel('Contract Type')
    plt.ylabel('Number of Customers')
    plt.xticks(rotation=0) # Keeps labels readable
    plt.grid(axis='y', alpha=0.5)

    # 5. Save the plot
    plt.savefig(OUTPUT_IMAGE_PATH)
    plt.close()
    
    print(f"\n✅ Bar chart saved successfully to {OUTPUT_IMAGE_PATH}")
    print("This visual provides an immediate understanding of contract distribution.")

if __name__ == "__main__":
    df = load_data(INPUT_FILE_PATH)
    if df is not None:
        create_bar_chart(df)
