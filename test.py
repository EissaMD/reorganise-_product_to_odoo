import pandas as pd

# Sample DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'San Francisco', 'Los Angeles']}
df = pd.DataFrame(data)

# Display the original DataFrame
print("Original DataFrame:")
print(df)

# Inserting new columns in the middle
new_columns = ['Occupation', 'Salary']
new_values = [['Engineer','Engineer','Engineer'], [80000, 90000, 90000]]

# Specify the position (index) where you want to insert the new columns
position = 2

# Use the insert method to add a new column at the specified position
df.insert(loc=0, column=new_columns[0], value=new_values[0])

# Add a new column with the same length as the DataFrame for 'Salary'
df.insert(loc=2, column=new_columns[1], value=new_values[1])

# Display the DataFrame after inserting new columns
print("\nDataFrame after inserting new columns:")
print(df)
