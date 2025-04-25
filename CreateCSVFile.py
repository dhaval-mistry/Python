import pandas as pd

data = {
    'Product': ['Product A', 'Product B', 'Product C'],
    'Quantity': [10, 20, 30],
    'Price': [15.5, 25.0, 35.75]
}

df = pd.DataFrame(data)
df.to_csv("Sales_data.csv", index=False )