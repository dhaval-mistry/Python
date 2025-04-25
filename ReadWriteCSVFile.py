
import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv('sales_data.csv')

# Calculate total sales
df['Total Sales'] = df['Quantity'] * df['Price']
total_sales = df.groupby('Product')['Total Sales'].sum().reset_index()

# Plot the data
plt.figure(figsize=(10, 6))
plt.bar(total_sales['Product'], total_sales['Total Sales'], color='skyblue')
plt.xlabel('Product')
plt.ylabel('Total Sales')
plt.title('Total Sales by Product')
plt.xticks(rotation=45)
plt.show()
