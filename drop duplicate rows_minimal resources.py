import pandas as pd

# Create the DataFrame
customers = pd.DataFrame({
    'customer_id': [1, 2, 3, 4, 5, 6],
    'name': ['Ella', 'David', 'Zachary', 'Alice', 'Finn', 'Violet'],
    'email': ['emily@example.com', 'michael@example.com', 'sarah@example.com', 
              'john@example.com', 'john@example.com', 'alice@example.com']
})
print(customers.drop_duplicates(subset = ["email"]))