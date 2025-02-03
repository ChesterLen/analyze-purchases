from clean_data.clean_data import df

df['Prev Purchase Date'] = df.groupby('Customer ID')['Transaction Date'].shift(1)
df['Time Between Purchases'] = (df['Transaction Date'] - df['Prev Purchase Date']).dt.days

avg_time_between_purchases = df[df['Time Between Purchases'] > 0].groupby('Customer ID')['Time Between Purchases'].mean()

repeat_customers = avg_time_between_purchases[avg_time_between_purchases <= 30].count()
total_customers = df['Customer ID'].nunique()

print(f"Repeat Customers within 30 days: {repeat_customers} out of {total_customers}")
