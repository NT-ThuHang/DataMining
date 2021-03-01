"""
    Argument syntax:
        python delete_same_instances.py input.csv --output=output.csv
    Example:
         python delete_same_instances.py house-prices.csv --output=request6.csv
"""


# Load the convenient packages
import csv
import sys

from SupportFunction import isNaN

input = sys.argv[1]
output = sys.argv[2].split("=")[1]

# get dataset
inputfile = open(input, 'r')
outputfile = open(output,'w',newline='')
dataset = csv.reader(inputfile)
writer = csv.writer(outputfile)
NumberOfAttribute = 0
close = []
for row in dataset:
    if (row not in close):
        close.append(row)
        writer.writerow(row)
inputfile.close()
outputfile.close()
