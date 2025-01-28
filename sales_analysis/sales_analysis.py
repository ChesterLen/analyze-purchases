from clean_data.clean_data import df

top_products = df.groupby('Product ID')['Total Purchase'].sum().nlargest(5)
sales_by_category = df.groupby('Product Category')['Total Purchase'].sum()
sales_by_region = df.groupby('Region')['Total Purchase'].sum()

top_products.to_csv('top_products.csv')
sales_by_category.to_csv('sales_by_category.csv')
sales_by_region.to_csv('sales_by_region.csv')