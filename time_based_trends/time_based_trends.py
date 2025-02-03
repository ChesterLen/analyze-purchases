from clean_data.clean_data import df
import matplotlib.pyplot as plt

df['YearMonth'] = df['Transaction Date'].dt.to_period('M')

monthly_sales = df.groupby('YearMonth')['Total Purchase'].sum()

plt.figure(figsize=(10, 6))
monthly_sales.plot(kind='line')
plt.title('Monthly Sales Trends')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.grid(True)
plt.xticks(rotation=45)
plt.show()