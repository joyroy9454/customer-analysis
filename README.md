# Customer Churn Analysis - Basic Portfolio Project

This repository contains a basic analysis of customer churn data for a telecommunications company. The project demonstrates data cleaning, exploratory analysis, and visualization skills.

## Project Overview

This project analyzes customer churn data to identify patterns and factors that influence whether customers leave (churn) or stay with the service. The analysis includes data cleaning and basic visualization.

## Business Problem

Telecommunication companies face significant revenue loss due to customer churn. Understanding why customers leave and identifying at-risk customers is crucial for developing effective retention strategies and maintaining profitability.

## Dataset Description

The dataset contains customer information from a telecommunications company, including:

- Basic demographics (age, gender, region)  
- Subscription details (plan type, payment method)
- Customer behavior metrics (days since last login, service calls, monthly spend)
- Target variable: Churn (0 = stayed, 1 = churned)

## Data Cleaning Summary

The original dataset required extensive cleaning:

- Standardized gender values (Male, Female, Non-Binary, Unknown)
- Normalized region names to consistent capitalization
- Cleaned subscription plan categories (Basic, Pro, Plus)
- Standardized payment method descriptions
- Converted numeric fields to proper types
- Handled missing values in age and other columns

## Installation and Setup

### Requirements

This project requires:
- Python 3.8+
- pandas
- matplotlib
- numpy

### Installation Steps

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/customer-churn-analysis.git
   cd customer-churn-analysis
   ```

2. Install required packages:
   ```bash
   pip install pandas matplotlib seaborn NumPy
   ```

3. Run the analysis:
   ```bash
   notebooks/01_Data_Cleaning.ipynb
   notebooks/02_Customer_Churn_Analysis.ipynb
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

![Churn by Age] (https://github.com/joyroy9454/customer-churn-analysis/blob/main/Images/churn_by_age.png)

*Churn by Age: Comparative analysis of churn rates across different Ages. *

![Churn by Subscription Plan](https://github.com/joyroy9454/customer-churn-analysis/blob/main/Images/churn_by_subscription_plan.png)

*Churn by Subscription Plan: How churn varies across different subscription tiers.*

## Project Structure

```
customer-churn-analysis/
├── data/
│   ├── Customer-churn.csv
│   └── Customer-churn-cleaned.csv
notebooks/
│   ├── 01_Data_Cleaning.ipynb
│   └── 02_Customer_Churn_Analysis.ipynb
├── images/
│   ├── age_distribution.png         # Age distribution chart
│   ├── gender_distribution.png      # Gender distribution chart
│   ├── subscription_distribution.png # Subscription plan pie chart
│   ├── payment_method_distribution.png # Payment method distribution
│   ├── monthly_spend_distribution.png # Monthly spend histogram
│   ├── churn_by_Age.png           # Churn by Age analysis
│   └── churn_by_subscription_plan.png # Churn by subscription plan
├── reports/
│   └── customer_churn_report.md      # Detailed analysis report
├── README.md                        # Project documentation
├── requirements.txt                 # Python dependencies
└── LICENSE                          # Project license
```



This project was created as part of a portfolio demonstration for data analysis and visualization work.


For questions or feedback about this project, please refer to the project documentation or contact the repository maintainer.

The visualizations above provide a comprehensive overview of the customer churn analysis, highlighting key patterns and insights that can inform business decisions.
