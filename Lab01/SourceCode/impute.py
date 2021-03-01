"""
    Argument syntax:
        python impute.py input.csv --method=method --columns column1 column2 column3 ... --output=output.csv
    Example:
         python impute.py house-prices.csv --method=MeAns --columns ID lotFrontage alley --output=request3.csv
"""

# Load the convenient packages
import sys

from SupportFunction import isNaN, MODE, MEANS, MEDIAN, getDataset, getTypeOfAttributes, list_NumberOfMissing, \
    getNumberOfInstances, list_attributes, getNumberOfAttributes

# construct the parser argument and parse the argument
method = sys.argv[2].split("=")[1]
method = method.lower()
methods = ['means','median','mode']
if (method not in methods):
    print("Method is invalid")
    exit(0)
output = sys.argv[len(sys.argv) - 1].split("=")[1]
column = []
for index in range(4, len(sys.argv) - 1, 1):
    column.append(sys.argv[index])

# Load dataset
dataset = getDataset(sys.argv[1])

TypeOfAttributes = getTypeOfAttributes(dataset)  # constaint attribute and type of data
NumberOfMissing = list_NumberOfMissing(dataset)  # get the number of missed data
NumOfInstances = getNumberOfInstances(dataset)
NumOfAttributes = getNumberOfAttributes(dataset)
attributes = list_attributes(dataset)


def FillMissingData(method, columns):
    index_Of_Column = -1
    for index in range(len(attributes)):
        if (str(attributes[index]).lower() == columns.lower()):
            index_Of_Column = index
            break
    if (index_Of_Column == -1):
        print(columns + "is Invalid")
        return

    method = method.lower()
    attribute = attributes[index_Of_Column]
    type = TypeOfAttributes[attribute]
    if (NumberOfMissing[attribute] == 0):
        return

    if ((method == "means" or method == "median") and type == 3):
        print("Type of " + columns + "is categorical. Using method MODE to fill missing data")
        return

    if (method == "mode" and (type == 1 or type == 2)):
        print("Type of " + columns + "is numeric. Using method MEANS or MEDIAN to fill missing data")
        return

    if (type == 4):
        if (method == "means"):
            dataset[attribute][0] = 0
            type = 1
            NumberOfMissing[attribute] -= 1
        elif (method == "median"):
            dataset[attribute][0] = 0.0
            type = 2
            NumberOfMissing[attribute] -= 1
        elif (method == "mode"):
            dataset[attribute][0] = "NULL"
            type = 3
            NumberOfMissing[attribute] -= 1

    while (NumberOfMissing[attribute] > 0):  # Update data until Number Of Missing Data = 0
        if (type == 1 and method == "means"):  # type = 1 means type of data is int or int64
            for index in range(NumOfInstances):
                if (isNaN(dataset[attribute][index])):
                    dataset[attribute][index] = int(MEANS(dataset[attribute]))
                    NumberOfMissing[attribute] -= 1
                    if (NumberOfMissing[attribute] == 0):
                        return
        elif (type == 1 and method == "median"):
            for index in range(NumOfInstances):
                if (isNaN(dataset[attribute][index])):
                    dataset[attribute][index] = int(MEDIAN(dataset[attribute]))
                    NumberOfMissing[attribute] -= 1
                    if (NumberOfMissing[attribute] == 0):
                        return
        elif (type == 2 and method == "means"):  # type = 2 means type of data is float or float64
            for index in range(NumOfInstances):
                if (isNaN(dataset[attribute][index])):
                    dataset[attribute][index] = MEANS(dataset[attribute])
                    NumberOfMissing[attribute] -= 1
                    if (NumberOfMissing[attribute] == 0):
                        return
        elif (type == 2 and method == "median"):  # type = 2 means type of data is float or float64
            for index in range(NumOfInstances):
                if (isNaN(dataset[attribute][index])):
                    dataset[attribute][index] = MEDIAN(dataset[attribute])
                    NumberOfMissing[attribute] -= 1
                    if (NumberOfMissing[attribute] == 0):
                        return
        elif (type == 3 and method == "mode"):
            for index in range(NumOfInstances):
                if (isNaN(dataset[attribute][index])):
                    dataset[attribute][index] = MODE(dataset[attribute])
                    NumberOfMissing[attribute] -= 1
                    if (NumberOfMissing[attribute] == 0):
                        return

for col in column:
    FillMissingData(method,col)

dataset.to_csv(output)