from clean_data.clean_data import df
import pandas as pd
import numpy as np

df['Transaction Date'] = pd.to_datetime(df['Transaction Date'])

customer_spending = df.groupby('Customer ID')['Total Purchase'].sum()

customer_frequency = df.groupby('Customer ID')['Transaction Date'].nunique()

customer_summary = pd.DataFrame({
    'Total Spending': customer_spending,
    'Purchase Frequency': customer_frequency
})

customer_summary['Segment'] = pd.cut(
    customer_summary['Total Spending'],
    bins=[0, 100, 500, 1000, 5000, np.inf],
    labels=['Low Value', 'Medium Value', 'High Value', 'VIP', 'Super VIP']
)

customer_summary.to_csv('customer_summary.csv')
