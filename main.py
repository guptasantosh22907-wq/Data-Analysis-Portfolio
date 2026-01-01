# Customer Behavior Analysis Project
# Analyze customer purchase patterns using Python (Pandas, Matplotlib, Seaborn)

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -------------------------------
# Step 1: Load CSV file (encoding fixed)
data = pd.read_csv(r"C:\Users\User\PycharmProjects\data1\Online_Retail.csv", encoding='latin1')

# Quick look at first 5 rows
print("First 5 rows of the dataset:")
print(data.head())

# Check data info
print("\nData Info:")
print(data.info())

# Check missing values
print("\nMissing values in each column:")
print(data.isnull().sum())

# -------------------------------
# Step 2: Clean the data
# Remove rows with missing CustomerID
data = data.dropna(subset=['CustomerID'])

# Remove duplicate rows
data = data.drop_duplicates()

# Convert InvoiceDate to datetime
data['InvoiceDate'] = pd.to_datetime(data['InvoiceDate'])

# Convert CustomerID to integer
data['CustomerID'] = data['CustomerID'].astype(int)

# -------------------------------
# Step 3: Analyze customer behavior

# a) Number of orders per customer
orders_per_customer = data.groupby('CustomerID')['InvoiceNo'].nunique().sort_values(ascending=False)
print("\nTop 10 customers by number of orders:")
print(orders_per_customer.head(10))

# b) Total quantity purchased per customer
quantity_per_customer = data.groupby('CustomerID')['Quantity'].sum().sort_values(ascending=False)
print("\nTop 10 customers by quantity purchased:")
print(quantity_per_customer.head(10))

# c) Total spending per customer
data['TotalPrice'] = data['Quantity'] * data['UnitPrice']
total_spent_per_customer = data.groupby('CustomerID')['TotalPrice'].sum().sort_values(ascending=False)
print("\nTop 10 customers by total spending:")
print(total_spent_per_customer.head(10))

# -------------------------------
# Step 4: Visualize customer behavior

# Top 10 customers by total spending
plt.figure(figsize=(10,5))
total_spent_per_customer.head(10).plot(kind='bar', color='purple')
plt.title('Top 10 Customers by Total Spending')
plt.ylabel('Total Spending (£)')
plt.xlabel('CustomerID')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Distribution of number of orders per customer
plt.figure(figsize=(10,5))
sns.histplot(orders_per_customer, bins=30, color='green')
plt.title('Distribution of Orders per Customer')
plt.xlabel('Number of Orders')
plt.ylabel('Number of Customers')
plt.tight_layout()
plt.show()

# Distribution of total quantity purchased per customer
plt.figure(figsize=(10,5))
sns.histplot(quantity_per_customer, bins=30, color='blue')
plt.title('Distribution of Quantity Purchased per Customer')
plt.xlabel('Total Quantity Purchased')
plt.ylabel('Number of Customers')
plt.tight_layout()
plt.show()

