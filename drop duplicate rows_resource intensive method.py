import pandas as pd

# Create the DataFrame
customers = pd.DataFrame({
    'customer_id': [1, 2, 3, 4, 5, 6],
    'name': ['Ella', 'David', 'Zachary', 'Alice', 'Finn', 'Violet'],
    'email': ['emily@example.com', 'michael@example.com', 'sarah@example.com', 
              'john@example.com', 'john@example.com', 'alice@example.com']
})

# Initialize an empty DataFrame to hold unique rows
customers_output = pd.DataFrame(columns=customers.columns)

# Loop through each row using iterrows()
for index, row in customers.iterrows():
    flag = False
    
    # Check if the email already exists in the output DataFrame
    for output_index, output_row in customers_output.iterrows():
        if row['email'] == output_row['email']:
            flag = True
            break
    
    # If no duplicate, append the row to customers_output
    if not flag:
        customers_output = pd.concat([customers_output, pd.DataFrame([row])], ignore_index=True)

# Display the result
print(customers_output)