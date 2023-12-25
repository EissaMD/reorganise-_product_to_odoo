import pandas as pd

# Read the Excel file into a pandas DataFrame
file_name = "p2"
df = pd.read_excel(file_name+'.xlsx')

# Create a dictionary to store unique values for each column
unique_columns_dict = {}

# Get unique values for each column
for column in df.columns:
    unique_columns_dict[column] = set(df[column])

data = {
    "Attribute"     :[],
    "Values/Value"  :[],
}
# Print or use the unique columns dictionary
for column, unique_values in unique_columns_dict.items():
    if column in ("Product Name (EN)","Product Name (AR)",):
        continue
    first_value = unique_values.pop()
    data["Attribute"].append(column)
    data["Values/Value"].append(first_value)
    for value in unique_values:
        data["Attribute"].append("")
        data["Values/Value"].append(value)

df = pd.DataFrame(data)
df.to_excel(file_name+'_attribute.xlsx')