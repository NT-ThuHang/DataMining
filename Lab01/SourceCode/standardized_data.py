"""
    Argument syntax:
        python standardized_data.py input.csv --method=method --columns column1 column2 column3 ... --output=output.csv
    Example:
         python standardized_data.py house-prices.csv --method=MINMAX --columns ID lotFrontage alley --output=request7.csv
"""

# Load the convenient packages
import sys
from SupportFunction import getDataset,getTypeOfAttributes,list_attributes, standardlized_data_by_MINMAX_Method, standardlized_data_by_ZScore_Method

input = sys.argv[1]
output = sys.argv[len(sys.argv)-1].split("=")[1]
method = sys.argv[2].split("=")[1]
method=method.lower()

dataset = getDataset(input)
attributes = list_attributes(dataset)
TypeOfAttribute = getTypeOfAttributes(dataset)
columns = []
for index in range(4,len(sys.argv)-1,1):
    check=False
    for attribute in attributes:
        if (attribute.lower()==sys.argv[index].lower()):
            columns.append(attribute)
            check=True
            break
    if (check==False):
        print(sys.argv[index] + " is Invalid")

for col in columns:
    if (TypeOfAttribute[col]>2):
        print(col + " isn't Numeric")
        columns.remove(col)

if (method=="minmax"):
    for col in columns:
        standardlized_data_by_MINMAX_Method(dataset,col,1.0,0.0)
elif (method=="zscore"):
    for col in columns:
        standardlized_data_by_ZScore_Method(dataset,col)
else:
    print("methods available are MinMax or ZScore")
    exit(0)
dataset.to_csv(output)