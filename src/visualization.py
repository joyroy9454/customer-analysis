"""Visualization script for customer churn analysis"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from pathlib import Path

# Set up the visualization style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = [10, 6]
plt.rcParams['font.size'] = 10


def generate_visualizations(data_path, images_dir):
    """Generate all key visualizations and save them as PNG files"""
    
    # Load cleaned data
    print(f"Loading data from {data_path}")
    df = pd.read_csv(data_path)
    
    # Create images directory if it doesn't exist
    Path(images_dir).mkdir(parents=True, exist_ok=True)
    
    # Create visualizations
    visualizations = []
    
    # 1. Age Distribution Histogram
    plt.figure(figsize=(10, 6))
    plt.hist(df['Age'].dropna(), bins=20, color='#3498db', alpha=0.7, edgecolor='black')
    plt.title('Age Distribution of Customers')
    plt.xlabel('Age')
    plt.ylabel('Number of Customers')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    age_dist_path = os.path.join(images_dir, 'age_distribution.png')
    plt.savefig(age_dist_path, dpi=300, bbox_inches='tight')
    plt.close()
    visualizations.append(('Age Distribution', age_dist_path, 'Distribution of customer ages'))
    
    # 2. Gender Distribution Bar Chart
    plt.figure(figsize=(10, 6))
    gender_counts = df['Gender'].value_counts()
    bars = plt.bar(gender_counts.index, gender_counts.values, color=['#3498db', '#e74c3c', '#f39c12'])
    plt.title('Gender Distribution of Customers')
    plt.xlabel('Gender')
    plt.ylabel('Number of Customers')
    plt.grid(True, alpha=0.3, axis='y')
    
    # Add value labels on bars
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height,
                f'{int(height)}', ha='center', va='bottom')
    
    plt.tight_layout()
    gender_path = os.path.join(images_dir, 'gender_distribution.png')
    plt.savefig(gender_path, dpi=300, bbox_inches='tight')
    plt.close()
    visualizations.append(('Gender Distribution', gender_path, 'Breakdown of customers by gender'))
    
    # 3. Subscription Plan Distribution
    plt.figure(figsize=(10, 6))
    plan_counts = df['Subscription_Plan'].value_counts()
    explode = (0.1, 0.1, 0.1)
    wedges, texts, autotexts = plt.pie(plan_counts.values, labels=plan_counts.index, 
                                     explode=explode, autopct='%1.1f%%',
                                     colors=['#3498db', '#2ecc71', '#f39c12'])
    plt.title('Subscription Plan Distribution')
    plt.axis('equal')
    plt.tight_layout()
    subscription_path = os.path.join(images_dir, 'subscription_distribution.png')
    plt.savefig(subscription_path, dpi=300, bbox_inches='tight')
    plt.close()
    visualizations.append(('Subscription Plan Distribution', subscription_path, 'Proportion of customers by subscription type'))
    
    # 4. Payment Method Distribution
    plt.figure(figsize=(10, 6))
    payment_counts = df['Payment_Method'].value_counts()
    bars = plt.bar(range(len(payment_counts)), payment_counts.values, 
                   color=plt.cm.Set3(range(len(payment_counts))))
    plt.title('Payment Method Distribution')
    plt.xlabel('Payment Method')
    plt.ylabel('Number of Customers')
    plt.xticks(range(len(payment_counts)), payment_counts.index, rotation=45)
    plt.grid(True, alpha=0.3, axis='y')
    
    # Add value labels on bars
    for i, bar in enumerate(bars):
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height,
                f'{int(height)}', ha='center', va='bottom')
    
    plt.tight_layout()
    payment_path = os.path.join(images_dir, 'payment_method_distribution.png')
    plt.savefig(payment_path, dpi=300, bbox_inches='tight')
    plt.close()
    visualizations.append(('Payment Method Distribution', payment_path, 'Breakdown of customers by payment method'))
    
    # 5. Monthly Spend Distribution
    plt.figure(figsize=(10, 6))
    plt.hist(df['Monthly_Spend'].dropna(), bins=20, color='#2ecc71', alpha=0.7, edgecolor='black')
    plt.title('Monthly Spend Distribution')
    plt.xlabel('Monthly Spend ($)')
    plt.ylabel('Number of Customers')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    spend_path = os.path.join(images_dir, 'monthly_spend_distribution.png')
    plt.savefig(spend_path, dpi=300, bbox_inches='tight')
    plt.close()
    visualizations.append(('Monthly Spend Distribution', spend_path, 'Distribution of customer monthly spending'))
    
    # 6. Churn by Gender (Stacked Bar)
    plt.figure(figsize=(10, 6))
    churn_gender = df.groupby(['Gender', 'Churn']).size().unstack(fill_value=0)
    churn_gender.plot(kind='bar', stacked=True, color=['#2ecc71', '#e74c3c'])
    plt.title('Customer Churn by Gender')
    plt.xlabel('Gender')
    plt.ylabel('Number of Customers')
    plt.legend(['Not Churned', 'Churned'])
    plt.grid(True, alpha=0.3, axis='y')
    plt.tight_layout()
    churn_gender_path = os.path.join(images_dir, 'churn_by_gender.png')
    plt.savefig(churn_gender_path, dpi=300, bbox_inches='tight')
    plt.close()
    visualizations.append(('Churn by Gender', churn_gender_path, 'Stacked bar showing churn rates by gender'))
    
    # 7. Churn by Subscription Plan (Stacked Bar)
    plt.figure(figsize=(10, 6))
    churn_plan = df.groupby(['Subscription_Plan', 'Churn']).size().unstack(fill_value=0)
    churn_plan.plot(kind='bar', stacked=True, color=['#2ecc71', '#e74c3c'])
    plt.title('Customer Churn by Subscription Plan')
    plt.xlabel('Subscription Plan')
    plt.ylabel('Number of Customers')
    plt.legend(['Not Churned', 'Churned'])
    plt.grid(True, alpha=0.3, axis='y')
    plt.tight_layout()
    churn_plan_path = os.path.join(images_dir, 'churn_by_subscription_plan.png')
    plt.savefig(churn_plan_path, dpi=300, bbox_inches='tight')
    plt.close()
    visualizations.append(('Churn by Subscription Plan', churn_plan_path, 'Stacked bar showing churn rates by subscription plan'))
    
    return visualizations


if __name__ == "__main__":
    # Define paths
    data_path = "/opt/data/customer-churn-analysis/data/customer_churn_cleaned.csv"
    images_dir = "/opt/data/customer-churn-analysis/images"
    
    print("Generating customer churn visualizations...")
    
    # Generate visualizations
    vis_results = generate_visualizations(data_path, images_dir)
    
    print(f"\nGenerated {len(vis_results)} visualizations!")
    print("\nVisualization files created:")
    for name, path, description in vis_results:
        print(f"  • {name}: {path}")
        print(f"    Description: {description}")
    
    print("\nVisualization generation completed!")