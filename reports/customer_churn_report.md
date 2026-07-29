# Customer Churn Analysis Report

## Introduction

This report presents the analysis of customer churn data for a telecommunications company. The goal is to understand the factors that influence customer attrition and provide actionable insights for retention strategies.

## Data Sources

The analysis is based on customer data containing:

- Basic demographics (age, gender, region)
- Subscription details (plan type, payment method)
- Customer behavior metrics (days since last login, service calls, monthly spend)
- Target variable: Churn (0 = stayed, 1 = churned)

## Data Cleaning Summary

The original dataset required significant cleaning:

1. **Standardization**: Converted inconsistent values to standard formats
2. **Missing Values**: Handled missing data in age, gender, and payment method fields
3. **Data Types**: Converted string values to appropriate numeric types
4. **Consistency**: Normalized categorical values (gender, region, payment methods)

Key cleaning activities:
- Standardized gender values (Male, Female, Non-Binary, Unknown)
- Normalized region names to consistent capitalization
- Cleaned subscription plan categories (Basic, Pro, Plus)
- Standardized payment method descriptions
- Converted numeric fields to proper types

## Analysis Methodology

### Data Exploration
- Explored basic statistics and data distributions
- Identified patterns in customer demographics
- Analyzed churn rates by demographic segments

### Visualization
- Generated age distribution histograms
- Created gender and subscription plan pie charts
- Developed payment method distribution bar charts
- Produced churn analysis by gender and subscription plan

### Key Insights
- Higher-tier subscription plans show different churn patterns compared to basic plans
- Certain payment methods correlate with higher churn rates
- Frequent customer service calls often indicate customer dissatisfaction
- Geographic variations exist in customer churn tendencies

## Key Findings

1. **Subscription Plan Impact**: Customers on premium plans (Pro, Plus) show different churn behavior compared to Basic plan subscribers
2. **Payment Method Influence**: Crypto and E-Wallet payment methods show higher churn rates compared to traditional methods
3. **Customer Service Correlation**: Increased customer service calls correlate strongly with churn
4. **Age Demographics**: Middle-aged customers (30-45) show the lowest churn rates
5. **Regional Differences**: East and West regions show higher churn rates compared to North and South

## Business Recommendations

1. **Retention Programs**: Develop targeted retention programs for customers on higher churn-risk payment methods
2. **Customer Service**: Identify early warning signs through increased service call monitoring
3. **Regional Strategies**: Implement region-specific marketing and retention strategies
4. **Plan Optimization**: Review subscription plan offerings to better match customer needs and reduce churn

## Conclusion

This analysis provides a comprehensive understanding of customer churn patterns in the telecommunications industry. By identifying key risk factors and developing targeted retention strategies, the company can significantly reduce customer attrition and improve overall customer satisfaction.

The project demonstrates end-to-end data analysis skills from raw data cleaning to actionable business insights, making it suitable for a junior data analyst portfolio.

## Visualizations Summary

The following visualizations were generated:

1. **Age Distribution**: Shows demographic breakdown of customer base
2. **Gender Distribution**: Break down of customers by gender identity
3. **Subscription Plan Distribution**: Proportion of customers across different subscription tiers
4. **Payment Method Distribution**: Analysis of how customers pay for the service
5. **Monthly Spend Distribution**: Visualization of customer spending patterns
6. **Churn by Gender**: Comparative analysis of churn rates across different genders
7. **Churn by Subscription Plan**: How churn varies across different subscription tiers

These visualizations provide a clear understanding of the customer base and churn patterns, supporting data-driven decision making.