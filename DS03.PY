# Final Code for Business Sales Dashboard from E-commerce Data

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Set a clean style for all plots
sns.set_style("whitegrid")
plt.style.use('fivethirtyeight')

# --- 1. Data Simulation ---
# Simulates a realistic e-commerce dataset for analysis.
np.random.seed(42)
dates = pd.date_range(start='2025-01-01', end='2025-06-30', freq='D')
num_records = len(dates) * 5

product_categories = ['Electronics', 'Home & Kitchen', 'Apparel', 'Books', 'Sports']
product_names = {
    'Electronics': ['Laptop', 'Smartphone', 'Headphones', 'Smartwatch', 'Camera'],
    'Home & Kitchen': ['Blender', 'Coffee Maker', 'Air Fryer', 'Toaster', 'Stand Mixer'],
    'Apparel': ['T-shirt', 'Jeans', 'Jacket', 'Sneakers', 'Hoodie'],
    'Books': ['Sci-Fi Novel', 'Cookbook', 'History Book', 'Fantasy Series', 'Biography'],
    'Sports': ['Dumbbells', 'Yoga Mat', 'Running Shoes', 'Water Bottle', 'Gym Bag']
}

data = []
for _ in range(num_records):
    date = np.random.choice(dates)
    category = np.random.choice(product_categories)
    product = np.random.choice(product_names[category])
    sales_per_unit = np.random.uniform(10, 500)
    quantity = np.random.randint(1, 5)
    total_sales = sales_per_unit * quantity
    data.append([date, category, product, total_sales, quantity])

df = pd.DataFrame(data, columns=['Order_Date', 'Product_Category', 'Product_Name', 'Sales', 'Quantity'])

# --- 2. Data Cleaning & Preprocessing ---
# In a real-world scenario, you would load data from a CSV:
# df = pd.read_csv('your_ecommerce_data.csv')

# Convert 'Order_Date' to datetime objects and set as index
df['Order_Date'] = pd.to_datetime(df['Order_Date'])
df.set_index('Order_Date', inplace=True)

# --- 3. Key Metric Calculation & Trend Analysis ---
# Identify best-selling products by total sales
best_selling_products = df.groupby('Product_Name')['Sales'].sum().sort_values(ascending=False).head(10)

# Identify high-revenue categories by total sales
best_selling_categories = df.groupby('Product_Category')['Sales'].sum().sort_values(ascending=False)

# Analyze monthly sales trends
monthly_sales = df['Sales'].resample('M').sum()

# Print key metrics and findings
print("--- Sales Metrics ---")
print(f"Total Sales: ${df['Sales'].sum():,.2f}")
print(f"Total Quantity Sold: {df['Quantity'].sum():,}")
print(f"Total Orders: {df.shape[0]:,}")
print("\n--- Top 10 Best-Selling Products by Sales ---")
print(best_selling_products.round(2))
print("\n--- Sales by Product Category ---")
print(best_selling_categories.round(2))
print("\n--- Monthly Sales Trend ---")
print(monthly_sales.round(2))

# --- 4. Visualization for the Dashboard ---
# Create a bar chart and a pie chart to visualize the findings.

# Plot 1: Bar chart for Top 10 Best-Selling Products
plt.figure(figsize=(12, 7))
sns.barplot(x=best_selling_products.values, y=best_selling_products.index, palette='rocket')
plt.title('Top 10 Best-Selling Products by Sales', fontsize=16)
plt.xlabel('Total Sales ($)', fontsize=12)
plt.ylabel('Product Name', fontsize=12)
plt.tight_layout()
plt.show()

# Plot 2: Pie chart for Sales Breakdown by Product Category
plt.figure(figsize=(8, 8))
plt.pie(best_selling_categories, labels=best_selling_categories.index, autopct='%1.1f%%', startangle=140, colors=sns.color_palette('pastel'))
plt.title('Sales Breakdown by Product Category', fontsize=16)
plt.ylabel('')
plt.tight_layout()
plt.show()

# Plot 3: Line chart for Monthly Sales Trend
plt.figure(figsize=(12, 7))
monthly_sales.plot(kind='line', marker='o', color='forestgreen')
plt.title('Monthly Sales Trend', fontsize=16)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Total Sales ($)', fontsize=12)
plt.grid(True)
plt.tight_layout()
plt.show()
