"""Data cleaning script for customer churn analysis"""

import csv
import os
from pathlib import Path


def load_and_clean_data(original_path, cleaned_path):
    """Load and clean the customer churn dataset"""
    
    # Load the original data
    print(f"Loading original data from {original_path}")
    
    with open(original_path, 'r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        original_data = list(reader)
    
    print(f"Original dataset: {len(original_data)} records")
    
    # Clean the data
    cleaned_data = []
    
    for i, row in enumerate(original_data, 1):
        cleaned_row = {}
        
        # Clean Customer_ID
        cleaned_row['Customer_ID'] = str(row.get('Customer_ID', '')).strip()
        
        # Clean Gender - standardize values
        gender = str(row.get('Gender', '')).strip().lower()
        if gender in ['', 'unknown', 'unknwn']:
            cleaned_row['Gender'] = 'Unknown'
        elif gender in ['male']:
            cleaned_row['Gender'] = 'Male'
        elif gender in ['female']:
            cleaned_row['Gender'] = 'Female'
        elif gender in ['non-binary']:
            cleaned_row['Gender'] = 'Non-Binary'
        else:
            cleaned_row['Gender'] = gender.capitalize()
        
        # Clean Region - standardize values
        region = str(row.get('Region', '')).strip().lower()
        cleaned_row['Region'] = region.capitalize()
        
        # Clean Subscription_Plan - standardize values
        plan = str(row.get('Subscription_Plan', '')).strip().lower()
        cleaned_row['Subscription_Plan'] = plan.capitalize()
        
        # Clean Payment_Method - standardize values
        payment = str(row.get('Payment_Method', '')).strip().lower()
        cleaned_row['Payment_Method'] = payment.capitalize()
        
        # Clean Age - convert to numeric or None
        age = row.get('Age', '').strip()
        cleaned_row['Age'] = float(age) if age else None
        
        # Clean Days_Since_Last_Login
        days = row.get('Days_Since_Last_Login', '').strip()
        cleaned_row['Days_Since_Last_Login'] = int(float(days)) if days else None
        
        # Clean Customer_Service_Calls
        calls = row.get('Customer_Service_Calls', '').strip()
        cleaned_row['Customer_Service_Calls'] = float(calls) if calls else None
        
        # Clean Monthly_Spend
        spend = row.get('Monthly_Spend', '').strip()
        cleaned_row['Monthly_Spend'] = float(spend) if spend else None
        
        # Clean Churn - convert to numeric
        churn = row.get('Churn', '').strip()
        cleaned_row['Churn'] = int(float(churn)) if churn else 0
        
        cleaned_data.append(cleaned_row)
    
    print(f"Cleaned dataset: {len(cleaned_data)} records")
    
    # Save cleaned data
    with open(cleaned_path, 'w', newline='', encoding='utf-8') as file:
        fieldnames = ['Customer_ID', 'Gender', 'Region', 'Subscription_Plan', 
                     'Payment_Method', 'Age', 'Days_Since_Last_Login', 
                     'Customer_Service_Calls', 'Monthly_Spend', 'Churn']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(cleaned_data)
    
    print(f"Cleaned data saved to {cleaned_path}")
    return cleaned_data


if __name__ == "__main__":
    # Define paths
    original_path = "/tmp/project_extracted/customer churn.csv"
    cleaned_path = "/opt/data/customer-churn-analysis/data/customer_churn_cleaned.csv"
    
    # Create data directory
    Path(cleaned_path).parent.mkdir(parents=True, exist_ok=True)
    
    # Run cleaning
    data = load_and_clean_data(original_path, cleaned_path)
    
    print("\nCleaning completed!")
    print(f"\nSample of cleaned data (first 5 rows):")
    for i, row in enumerate(data[:5], 1):
        print(f"\nRow {i}:")
        for key, value in row.items():
            print(f"  {key}: {value}")