import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("sales_data.csv")

# Total sales by product
product_sales = df.groupby('Product')['Sales'].sum()
print(product_sales)

# Sales by month
monthly_sales = df.groupby('Month')['Sales'].sum()

# Plot monthly sales
monthly_sales.plot(kind='bar')
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()

# Insight
print("Top performing product:", product_sales.idxmax())
