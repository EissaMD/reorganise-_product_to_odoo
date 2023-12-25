import pandas as pd
import re
file_name = "p2"
data = pd.read_excel(file_name+'.xlsx')

new_columns = {
    "Width"         :[],
    "Aspect Ratio"  :[],
    "Rim"           :[],
}
data.sort_values(by=['Group No'], ascending=True)
for index in data.index:
    cell = data["Size"][index]
    segmentation = cell.count("-")+cell.count("R")+cell.count("X")+cell.count("L")
    if segmentation >=2:
        match = re.search("^(\d+\.?\d*)-?X?(\d*\.?\d*)?-?(R?L?\d+\.?\d*)",cell)
    elif segmentation==1: 
        match = re.search("^(\d+\.?\d*)-?X?(R?L?\d+\.?\d*)$",cell)
    if match is None:
        continue
    no_match = len(match.groups()) 
    if no_match <2:
        print("less than 2")
    new_columns["Width"].append(        match[1])
    if segmentation==1: 
        new_columns["Rim"].append(          match[2])
        new_columns["Aspect Ratio"].append( "")
    else:
        new_columns["Aspect Ratio"].append( match[2])
        new_columns["Rim"].append(          match[3])
data.insert(3,"Width"       ,new_columns["Width"])
data.insert(4,"Aspect Ratio",new_columns["Aspect Ratio"])
data.insert(5,"Rim"         ,new_columns["Rim"])
data.to_excel(file_name+'_output.xlsx')