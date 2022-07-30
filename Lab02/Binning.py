# -----------------------------------------------------------------------------------------------------------#
#                                     Nguyen Thi Thu Hang - 18120027                                         #
#                                       Pham Thi Hoai Hien - 18120173                                        #
#============================================================================================================#
# TOPIC: Code Binning Data                                                                                   #
# Argument syntax:                                                                                           #
# python Binning.py input.csv output.csv -a "FirstAttribute" -a "SecondAttribute" -b /*The Number of Bin*/   #
# Example: python Binning.py churn.csv output.csv -a all -b 3                                                #
# -----------------------------------------------------------------------------------------------------------#
import argparse
import numpy as np
import pandas as pd


def getDataset(filename):
    data = pd.read_csv(filename, dtype=None)
    return data


def Binning(Dataset, AttributeList, NumOfBin):
    for attribute in AttributeList:
        if (attribute == "Area Code"):
            continue
        if (not np.issubsctype(Dataset[attribute].dtype, np.number)):
            print(attribute, " isn't Numeric")
            continue
        Norminal = []
        if NumOfBin == 2:
            Norminal = ["Low", "High"]
        elif NumOfBin == 3:
            Norminal = ["Low", "Medium", "High"]
        elif NumOfBin == 5:
            Norminal = ["VeryLow", "Low", "Medium", "High", "VeryHigh"]

        dmin = min(Dataset[attribute])
        dmax = max(Dataset[attribute])
        Bin = []
        Bin.append(dmin)
        d = round((dmax - dmin + 1) / NumOfBin, 2)
        for i in range(NumOfBin):
            Bin.append(Bin[i] + d - 1)
        Bin[NumOfBin] = dmax
        temp_array = [''] * len(Dataset[attribute])

        for index in range(len(Dataset[attribute])):
            for Bin_index in range(NumOfBin):
                if (Bin[Bin_index] <= Dataset[attribute][index] and Dataset[attribute][index] < Bin[Bin_index + 1]):
                    temp_array[index]=Norminal[Bin_index]
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
    Binning(Dataset, AttributeList, args.NumOfBin)
    Dataset.to_csv(args.output, index=False)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="To Binning Numeric type. Examples: $python \"D:\\path\\to\\Binning.py\" \"D:\\path\\to\\input.csv\" \"D:\\path\\to\\output.csv\" -a\"FisrtAtt\" -a\"SecondAtt\" -b 5")
    parser.add_argument("input", type=None, help="The input's name")
    parser.add_argument("output", type=None, help="The output's name")
    parser.add_argument("-a", "--attribute", action="append", help="The specified attribute to process")
    parser.add_argument("-b", "--NumOfBin", type=int, choices=[2, 3, 5], help="Number of bins for binning")
    args = parser.parse_args()
    main(args)
