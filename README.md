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
* **Source:** A synthetic dataset simulating customer information (e.g., tenure, charges, contract type, and churn status) was created and loaded into a **Pandas DataFrame**.
* **Preparation:** Initial data quality checks were performed to inspect data types and identify missing values. Problematic numeric columns were converted, and missing data was handled by **[Insert specific method used, e.g., filling with the mean value]** to ensure data integrity.
* **Filtering:** The cleaned data was filtered to create specific subsets for analysis (e.g., separating churning vs. non-churning customers).

### 2. SQL Storage and Querying
* The fully cleaned and processed data was loaded into a local **SQLite database**.
* **Analytical Queries** were written to segment and aggregate the data. This included basic commands to calculate **averages** and **counts**, demonstrating ability to work with relational data.

### 3. Analysis, Visualization, and Reporting
* **Descriptive Statistics:** Key metrics, such as the minimum, maximum, and average customer **Tenure** and **Monthly Charges**, were calculated to establish benchmarks.
* **Visualization:** Charts were generated to visualize the distribution of core metrics (e.g., a **histogram** of monthly charges) and the breakdown of categorical features (e.g., a **bar chart** of different contract types).

***

## 🎯 Key Business Insights

Based on the analysis and visualizations generated, the following critical insights were derived:

1.  **Contract Distribution:** Analysis of customer contract types revealed **[Insert finding, e.g., a high dependency on flexible Month-to-Month contracts]**. This highlights a potential area for business focus to encourage longer-term commitments.
2.  **Charge Characteristics:** The average monthly charge was found to be **[Insert calculated average charge]**. The distribution analysis showed **[Insert observation, e.g., two distinct peaks in pricing tiers]**, suggesting opportunities for targeted pricing strategies.
3.  **Customer Loyalty:** Calculation of the average customer tenure (**[Insert calculated average tenure]** months) provides a clear benchmark for evaluating the effectiveness of retention programs.

***

## 📂 Repository Contents

| File/Folder | Purpose |
| :--- | :--- |
| `create_data.py` | Python script for data generation and primary cleaning. |
| `reporting_sql.py` | Python script containing SQL connectivity and analytical queries. |
| `visualization.py` | Python script for generating charts and final reports. |
| `data/` | Contains the `synthetic_churn_data.csv` file. |
| `requirements.txt` | Lists all necessary Python dependencies. |
