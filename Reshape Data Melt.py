import pandas as pd

# Create the DataFrame
report = pd.DataFrame({
    'product': ['Umbrella', 'SleepingBag'],
    'quarter_1': [417, 800],
    'quarter_2': [224, 936],
    'quarter_3': [379, 93],
    'quarter_4': [611, 875]
})

# Use melt() to reshape the data
melted_report = pd.melt(report, id_vars=['product'], value_vars=['quarter_1', 'quarter_2', 'quarter_3', 'quarter_4'],
                        var_name='quarter', value_name='sales')

print(melted_report)