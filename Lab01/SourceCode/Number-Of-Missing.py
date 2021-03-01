"""
    Argument syntax:
        python Number-Of-Missing.py input.csv
    Example:
         python Number-Of-Missing.py house-prices.csv
"""

# Load the convenient packages
import sys
from SupportFunction import getDataset, list_NumberOfMissing
from pprint import  pprint
dataset = getDataset(sys.argv[1])

#Print result
print("Attribute are missed data:")
NumberOfMissing = list_NumberOfMissing(dataset)
for attribute in NumberOfMissing:
    if (NumberOfMissing[attribute]>0):
        print(attribute," : ",NumberOfMissing[attribute])

