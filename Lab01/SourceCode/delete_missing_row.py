"""
    Argument syntax:
        python delete_missing_row.py input.csv --missing_rate=missing_rate --output=output.csv
    Example:
         python delete_missing_row.py house-prices.csv --missing_rate=50 --output=request4.csv
"""

# Load the convenient packages
import csv
import sys

from SupportFunction import isNaN

input = sys.argv[1]
missing_rate = int(sys.argv[2].split("=")[1]) / 100
output = sys.argv[3].split("=")[1]

# get dataset
inputfile = open(input, 'r')
outputfile = open(output,'w',newline='')
dataset = csv.reader(inputfile)
writer = csv.writer(outputfile)
NumberOfAttribute = 0

for row in dataset:
    if (NumberOfAttribute == 0):
        NumberOfAttribute = len(row)
        writer.writerow(row)
        continue
    NumOfMissing = 0
    for i in row:
        if (isNaN(i)):
            NumOfMissing += 1
    if (NumOfMissing< missing_rate*NumberOfAttribute):
        writer.writerow(row)
inputfile.close()
outputfile.close()