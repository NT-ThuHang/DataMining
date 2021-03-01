"""
    Argument syntax:
        python delete_mising_column.py input.csv --missing_rate=missing_rate --output=output.csv
    Example:
         python delete_mising_column.py house-prices.csv --missing_rate=50 --output=request5.csv
"""

# Load the convenient packages
import sys

from SupportFunction import getDataset, getNumberOfAttributes, getNumberOfInstances,list_NumberOfMissing,list_attributes

input = sys.argv[1]
missing_rate = int(sys.argv[2].split("=")[1]) / 100
output = sys.argv[3].split("=")[1]

# get dataset

dataset = getDataset(input)
NumberOfInstances = getNumberOfInstances(dataset)
NumberOfAttributes = getNumberOfAttributes(dataset)
NumberOfMissing = list_NumberOfMissing(dataset)
attributes = list_attributes(dataset)

for attribute in attributes:
    if (NumberOfMissing[attribute]>missing_rate*NumberOfAttributes):
        del dataset[attribute]

dataset.to_csv(output)