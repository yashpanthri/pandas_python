import pandas as pd

# Create the first DataFrame (df1)
df1 = pd.DataFrame({
    'student_id': [1, 2, 3],
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [20, 21, 22]
})

# Create the second DataFrame (df2)
df2 = pd.DataFrame({
    'student_id': [4, 5, 6],
    'name': ['David', 'Eva', 'Frank'],
    'age': [23, 24, 25]
})

result = pd.concat([df1, df2], ignore_index=True)
print(result)