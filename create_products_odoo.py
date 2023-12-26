import pandas as pd

def create_single_product():
    pass
    

# Read the Excel file into a pandas DataFrame
file_name = "p2_with_sizes"
df = pd.read_excel(file_name+'.xlsx')
headers = ("Name"	,"Product Type"	,"Product Attributes/ Attribute"	,"Product Attributes / Value")
rows = []
for index, row in df.iterrows():
    row_dict = row.to_dict()
    row = ["","","",""]
    is_first=True
    for key,value in row_dict.items():
        if key in ("Product Name (EN)"):
            row[0]= value
            row[1]= "Storable Product"
            continue
        elif key in ("Product Name (AR)","Year") or pd.isna(value):
            continue
        if is_first is False:
            row = ["","","",""]
        row[2]=key
        row[3]=value
        rows.append(row)
        is_first=False

df = pd.DataFrame(rows, columns = headers) 
df.to_excel(file_name+'_final.xlsx',index=False)
    