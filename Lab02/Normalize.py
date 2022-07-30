# -----------------------------------------------------------------------------------------------------------#
#                                     Nguyen Thi Thu Hang - 18120027                                         #
#                                       Pham Thi Hoai Hien - 18120173                                        #
# ============================================================================================================#
# TOPIC: Code Binning Data                                                                                   #
# Argument syntax:                                                                                           #
# python Normalize.py input.csv output.csv -m "Method" -a "FirstAttribute" -a "SecondAttribute"              #
# Example: python Normalize.py churn.csv output.csv -m minmax -a all                                         #
# -----------------------------------------------------------------------------------------------------------#

import argparse
import pandas as pd
import numpy as np
def getDataset(filename):
    return pd.read_csv(filename)

def MinMax(Dataset,AttributeList):
    for attribute in AttributeList:

        if (not np.issubsctype(Dataset[attribute].dtype, np.number)):
            print(attribute, " isn't Numeric")
            continue

        dmin = min(Dataset[attribute])
        dmax = max(Dataset[attribute])

        temp_array = np.array(Dataset[attribute], dtype=np.float64)

        for index in range(len(Dataset[attribute])):
            temp_array[index]=round((Dataset[attribute][index]-dmin)/(dmax-dmin),3)
        Dataset[attribute]=temp_array

def ZScore(Dataset,AttributeList):
    for attribute in AttributeList:

        if (not np.issubsctype(Dataset[attribute].dtype, np.number)):
            print(attribute, " isn't Numeric")
            continue

        mean = np.mean(Dataset[attribute])
        std = np.std(Dataset[attribute])

        temp_array = np.array(Dataset[attribute], dtype=np.float64)


        for index in range(len(Dataset[attribute])):
            temp_array[index]=round((Dataset[attribute][index]-mean)/std,3)

        Dataset[attribute]=temp_array
def ListOfAttribute(Data, command):
    if (len(command) == 1 and command[0] == "all"):
        return list(Data.columns.values)
    else:
        attributes = []
        for i in command:
            check = False
            for j in list(Data.columns.values):
                if (i.lower() == j.lower()):
                    attributes.append(j)
                    check = True
                    break
            if (check != True):
                print(i + "isn't available")
        return attributes

def main(args):
    Dataset = getDataset(args.input)
    AttributeList = ListOfAttribute(Dataset, args.attribute)
    if (args.Method == "minmax"):
        MinMax(Dataset, AttributeList)
    elif (args.Method == "zscore"):
        ZScore(Dataset, AttributeList)
    Dataset.to_csv(args.output,index = False)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        "Min-max and Z-score normalizationsExamples: $python \"D:\\path\\to\\Binning.py\" \"D:\\path\\to\\input.csv\" \"D:\\path\\to\\output.csv\" -a\"FisrtAtt\" -m \"Method\" -a\"SecondAtt\" ")
    parser.add_argument("input", type=None, help="The input's name")
    parser.add_argument("output", type=None, help="The output's name")
    parser.add_argument("-m", "--Method", choices=["minmax", "zscore"], help="Method of Normalized")
    parser.add_argument("-a", "--attribute", action="append", help="The specified attribute to process")

    args = parser.parse_args()
    main(args)
