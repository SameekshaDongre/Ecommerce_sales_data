python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('ecommerce_data.csv')

# Data cleaning
df['order_date'] = http://pd.to_datetime(df['order_date'])
df['product_price'] = df['product_price'].str.replace('$', '').astype(float)
df['total_sales'] = df['product_price'] * df['quantity']

# Basic analysis
total_revenue = df['total_sales'].sum()
total_orders = df['order_id'].nunique()
average_order_value = total_revenue / total_orders

# Top selling products
top_products = df.groupby('product_name')['quantity'].sum().sort_values(descending=True).head(10)

# Sales by month
monthly_sales = df.resample('M', on='order_date')['total_sales'].sum()

# Customer analysis
customer_stats = df.groupby('customer_id').agg({
    'order_id': 'count',
    'total_sales': 'sum'
}).rename(columns={'order_id': 'order_count', 'total_sales': 'total_spent'})

customer_stats['average_order_value'] = customer_stats['total_spent'] / customer_stats['order_count']

# Save processed data
http://df.to_csv('processed_ecommerce_data.csv', index=False)
http://customer_stats.to_csv('customer_stats.csv')

# # Visualizations
# plt.figure(figsize=(12, 6))
# monthly_sales.plot()
# plt.title('Monthly Sales Trend')
# plt.xlabel('Date')
# plt.ylabel('Total Sales')
# plt.savefig('monthly_sales_trend.png')

# plt.figure(figsize=(12, 6))
# top_products.plot(kind='bar')
# plt.title('Top 10 Selling Products')
# plt.xlabel('Product Name')
# plt.ylabel('Quantity Sold')
# plt.xticks(rotation=45, ha='right')
# plt.tight_layout()
# plt.savefig('top_selling_products.png')

# print(f"Total Revenue: ${total_revenue:.2f}")
# print(f"Total Orders: {total_orders}")
# print(f"Average Order Value: ${average_order_value:.2f}")