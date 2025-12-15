# 📊 Customer Churn Analysis Portfolio: End-to-End Business Reporting

## 📌 Project Overview

This project showcases a complete **Exploratory Data Analysis (EDA)** and **Basic Reporting** workflow on a customer dataset, a fundamental task in Business Analytics. The core objective is to demonstrate proficiency in data preparation, quality assurance, fundamental SQL reporting, and the ability to generate **actionable business insights** from raw data.

The project is structured to move the data through a full lifecycle:
**Data Preparation → Data Storage → Reporting & Visualization.**

## 🛠️ Tools and Technologies

The following technologies were utilized to complete the analysis:

* **Python:** For data cleaning, feature engineering, and reporting.
    * `pandas` (Core library for data manipulation).
    * `matplotlib` / `seaborn` (For creating visualizations and reports).
* **SQL (SQLite):** For structured data storage, retrieval, and complex segmentation queries.

***
## 💡 Methodology and Workflow

### 1. Data Acquisition & Cleaning
* **Source:** A synthetic dataset simulating customer information...
* **Preparation:** Missing data was handled by **filling with the column mean** and non-numeric characters were **removed via string manipulation** to ensure data integrity.

### 2. SQL Storage and Querying
* The fully cleaned data was loaded into a local **SQLite database**.
* **Analytical Queries** were written using `GROUP BY` and `CASE` statements to perform aggregation and **customer segmentation** (Rookie, Mid-Term, Veteran).

### 3. Analysis, Visualization, and Reporting
* **Descriptive Statistics:** Key metrics, such as the average customer **Tenure** and **Monthly Charges**, were calculated.
* **Visualization:** A **histogram** of charges and a **bar chart** comparing contract distributions were created to support analytical findings.

***

## 🎯 Key Business Insights

Based on the analysis and visualizations generated, the following critical insights were derived:

1.  **Dominant Contract Structure:** The **[Two year]** contract type is overwhelmingly the most popular, representing the highest stable customer value.
2.  **Pricing and Tenure Relationship:** The **Average Monthly Charge** is **[Insert Mean MonthlyCharges]**, and a **[Insert Correlation Value]** correlation exists between tenure and charges, suggesting higher fees correlate with higher loyalty.
3.  **Customer Loyalty Benchmark:** The average customer tenure is **[Insert Mean Tenure_Months]** months, establishing a clear benchmark for evaluating customer retention effectiveness.

***


## 📂 Repository Contents

| File/Folder | Purpose |
| :--- | :--- |
| `create_data.py` | Python script for data generation and primary cleaning. |
| `reporting_sql.py` | Python script containing SQL connectivity and analytical queries. |
| `visualization.py` | Python script for generating charts and final reports. |
| `data/` | Contains the `synthetic_churn_data.csv` file. |
| `requirements.txt` | Lists all necessary Python dependencies. |
