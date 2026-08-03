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
- seaborn
- numpy

### Installation Steps

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/customer-churn-analysis.git
   cd customer-churn-analysis
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install required packages:
   ```bash
   pip install pandas matplotlib seaborn numpy
   ```

4. Run the analysis:
   ```bash
   python src/cleaning.py
   python src/visualization.py
   ```

## Visualizations

Key visualizations created for this project include:

![Age Distribution](https://github.com/joyroy9454/customer-churn-analysis/blob/main/Images/output.png)

*Age Distribution of Customers: Shows the demographic breakdown of the customer base.*

![Gender Distribution](images/gender_distribution.png)

*Gender Distribution of Customers: Break down of customers by gender identity.*

![Subscription Plan Distribution](images/subscription_distribution.png)

*Subscription Plan Distribution: Proportion of customers across different subscription tiers.*

![Payment Method Distribution](images/payment_method_distribution.png)

*Payment Method Distribution: Analysis of how customers pay for the service.*

![Monthly Spend Distribution](images/monthly_spend_distribution.png)

*Monthly Spend Distribution: Visualization of customer spending patterns.*

![Churn by Gender](images/churn_by_gender.png)

*Churn by Gender: Comparative analysis of churn rates across different genders.*

![Churn by Subscription Plan](images/churn_by_subscription_plan.png)

*Churn by Subscription Plan: How churn varies across different subscription tiers.*

## Project Structure

```
customer-churn-analysis/
├── data/
│   ├── original_dataset.csv          # Original customer data
│   └── cleaned_dataset.csv          # Cleaned and processed data
├── src/
│   ├── cleaning.py                  # Data cleaning and preprocessing script
│   └── visualization.py             # Data visualization and analysis script
├── images/
│   ├── age_distribution.png         # Age distribution chart
│   ├── gender_distribution.png      # Gender distribution chart
│   ├── subscription_distribution.png # Subscription plan pie chart
│   ├── payment_method_distribution.png # Payment method distribution
│   ├── monthly_spend_distribution.png # Monthly spend histogram
│   ├── churn_by_gender.png           # Churn by gender analysis
│   └── churn_by_subscription_plan.png # Churn by subscription plan
├── reports/
│   └── customer_churn_report.md      # Detailed analysis report
├── README.md                        # Project documentation
├── requirements.txt                 # Python dependencies
├── .gitignore                       # Git ignore patterns
└── LICENSE                          # Project license
```

## Files Overview

- **cleaning.py**: Script to clean and preprocess the raw customer data
- **visualization.py**: Complete visualization suite showing key patterns and insights
- **customer_churn_report.md**: Detailed analysis and business recommendations
- **requirements.txt**: Python package dependencies

## Project Status

✅ Data cleaning completed  
✅ Visualizations generated  
✅ Business insights documented  
✅ Portfolio-ready structure created  

This project was created as part of a portfolio demonstration for data analysis and visualization work.

![Age Distribution](images/age_distribution.png)

## Contact

For questions or feedback about this project, please refer to the project documentation or contact the repository maintainer.

The visualizations above provide a comprehensive overview of the customer churn analysis, highlighting key patterns and insights that can inform business decisions.
