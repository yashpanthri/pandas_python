import pandas as pd

# Create the DataFrame
products = pd.DataFrame({
    'name': ['Wristwatch', 'WirelessEarbuds', 'Golfclubs', 'Printer'],
    'quantity': [None, None, 779, 849],
    'price': [135, 821, 9319, 3051]
})

# Fill missing values in the 'quantity' column with 0
products['quantity'] = products['quantity'].fillna(0)
# print(products['quantity'].fillna(0, inplace=True))
# Display the updated DataFrame
print(products)