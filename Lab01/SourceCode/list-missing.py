"""
    Argument syntax:
        python list-missing.py input.csv
    Example:
         python list-missing.py house-prices.csv
"""


# Load the convenient packages
import sys
import SupportFunction
from pprint import  pprint
dataset = SupportFunction.getDataset(sys.argv[1])

#Print result
print("Attribute are missed data:")
#pprint(SupportFunction.list_missing(dataset))
pprint(SupportFunction.list_attributes(dataset))