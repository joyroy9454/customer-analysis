# Customer Churn Analysis using Python and Matplotlib

This repository presents an exploratory data analysis (EDA) project on customer churn using Python, Pandas, NumPy, and Matplotlib. The project focuses on cleaning raw customer data, exploring customer characteristics, and visualizing churn-related patterns to better understand customer behavior.

## Project Overview

Customer churn is one of the biggest challenges for subscription-based businesses. This project demonstrates a complete beginner-friendly workflow including data cleaning, exploratory data analysis, customer behavior analysis, visualization, and business insights.

## Business Problem

Customer churn can reduce business growth and increase customer acquisition costs. By exploring customer demographics and behavior, businesses can better understand factors related to churn and improve customer retention strategies.

## Dataset Description

The dataset contains customer information from a telecommunications company, including:

- Basic demographics (age, gender, region)  
- Subscription details (plan type, payment method)
- Customer behavior metrics (days since last login, service calls, monthly spend)
- Target variable: Churn (0 = stayed, 1 = churned)

## Data Cleaning Summary

- Filled missing values in **Payment Method**
- Replaced unrealistic age values using the median age
- Filled missing values in the **Age** column
- Removed invalid and extreme values from **Monthly Spend**
- Corrected negative values in **Customer Service Calls**
- Standardized **Region** and **Subscription Plan** names
- Removed duplicate records
- Converted categorical columns to appropriate data types
- Saved the cleaned dataset for further analysis and visualization
  
## Installation and Setup

### Requirements

This project requires:
- Python 3.8+
- pandas
- matplotlib
- numpy
- Jupyter Notebook

### Installation Steps

1. Clone this repository:
   ```bash
   git clone https://github.com/joyroy9454/customer-churn-analysis.git
   cd customer-churn-analysis
   ```

2. Install required packages:
   ```bash
   pip install pandas matplotlib seaborn NumPy
   ```

3. Open:
   ```bash
   src/01_Data_Cleaning.ipynb
   src/02_Customer_Churn_Analysis.ipynb
   ```

## Visualizations

Key visualizations created for this project include:

![Age Distribution](https://github.com/joyroy9454/customer-churn-analysis/blob/main/Images/age_distribution.png)

*Age Distribution of Customers: Shows the demographic breakdown of the customer base.*

![Gender Distribution](https://github.com/joyroy9454/customer-churn-analysis/blob/main/Images/gender_distribution.png)

*Gender Distribution of Customers: Break down of customers by gender identity.*

![Subscription Plan Distribution](https://github.com/joyroy9454/customer-churn-analysis/blob/main/Images/subscription_distribution.png)

*Subscription Plan Distribution: Proportion of customers across different subscription tiers.*

![Payment Method Distribution](https://github.com/joyroy9454/customer-churn-analysis/blob/main/Images/payment_method_distribution.png)

*Payment Method Distribution: Analysis of how customers pay for the service.*

![Monthly Spend Distribution](https://github.com/joyroy9454/customer-churn-analysis/blob/main/Images/monthly_spend_distribution.png)

*Monthly Spend Distribution: Visualization of customer spending patterns.*

![Churn by Age](https://github.com/joyroy9454/customer-churn-analysis/blob/main/Images/churn_by_age.png)

*Churn by Age: Comparative analysis of churn rates across different Ages.*

![Churn by Subscription Plan](https://github.com/joyroy9454/customer-churn-analysis/blob/main/Images/churn_by_subscription_plan.png)

*Churn by Subscription Plan: How churn varies across different subscription tiers.*

## Project Structure

```
customer-churn-analysis/
├── Images/
│   ├── age_distribution.png
│   ├── gender_distribution.png
│   ├── subscription_distribution.png
│   ├── payment_method_distribution.png
│   ├── monthly_spend_distribution.png
│   ├── churn_by_age.png
│   └── churn_by_subscription_plan.png
│
├── data/
│   ├── customer churn.csv
│   └── customer_churn_cleaned.csv
|
src/
│   ├── 01_Data_Cleaning.ipynb
│   └── 02_Customer_Churn_Analysis.ipynb
|
├── reports/
│   └── customer_churn_report.md    
│
├── LICENSE
├── README.md
└── requirements.txt
```



This project was created as part of a portfolio demonstration for data analysis and visualization work.


The visualizations above provide a comprehensive overview of the customer churn analysis, highlighting key patterns and insights that can inform business decisions.
