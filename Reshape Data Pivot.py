import pandas as pd

# Create the DataFrame
weather = pd.DataFrame({
    'city': ['Jacksonville', 'Jacksonville', 'Jacksonville', 'Jacksonville', 
             'ElPaso', 'ElPaso', 'ElPaso', 'ElPaso'],
    'month': ['January', 'February', 'March', 'April', 'January', 'March', 'April', 'May'],
    'temperature': [13, 23, 38, 5, 20, 26, 12, 43]
})

print(weather.pivot(index='month', columns='city', values='temperature'))