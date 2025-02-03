import matplotlib.pyplot as plt
from sales_analysis import sales_analysis

sales_analysis.sales_by_region.plot(kind='bar', figsize=(10, 6), color='skyblue')
plt.title('Total Sales by Region')
plt.xlabel('Region')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.show()

sales_analysis.top_products.plot(kind='bar', figsize=(10, 6), color='lightcoral')
plt.title('Top 5 Products by Revenue')
plt.xlabel('Product ID')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.show()