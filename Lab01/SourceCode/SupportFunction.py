# 18120027_Nguyen Thi Thu Hang
# 18120178_Pham Thi Hoai Hien
# Load the convenient packages
import numpy as np
import pandas as pd
import math

# Load dataset
def getDataset(filename):
    dataset = pd.read_csv(filename)
    return dataset


def getNumberOfInstances(dataset):
    return dataset.shape[0]


def getNumberOfAttributes(dataset):
    return dataset.shape[1]

# get list of attribute in dataset
def list_attributes(dataset):
    return list(dataset)


# To check num is NaN?
def isNaN(num):
    return num != num


# To check each element of array is NaN
def isNaN_Array(array):
    Array = []
    for x in array:
        Array.append(isNaN(x))
    return Array


# detect the attribute is missed data
def list_missing(dataset):
    List_Missing = []  # to contains the name of attribute is missed data
    attributes = list_attributes(dataset)  # get list of Attribute
    NumOfInstances = getNumberOfInstances(dataset)  # get the number of Instances
    for attribute in attributes:  # Check each of attributes
        for index in range(NumOfInstances):  # Check each of element
            if (isNaN(dataset[attribute][index])):  # If value of element is NaN
                List_Missing.append(attribute)  # add attribute to List-Missing
                break
    return List_Missing


# get the number of missed data
def list_NumberOfMissing(dataset):
    NumberOfMissing = {}  # constaint attribute and number of missing data
    attributes = list_attributes(dataset)  # get list of Attribute
    NumOfInstances = getNumberOfInstances(dataset)  # get the number of Instances
    for attribute in attributes:  # Check each of attributes
        MissingArray = isNaN_Array(dataset[attribute])  # IsNaN ~ 1      NotIsNaN ~ 0
        NumOfMiss = 0
        for index in range(NumOfInstances):
            NumOfMiss += int(MissingArray[index])
        NumberOfMissing[attribute] = NumOfMiss
    return NumberOfMissing


# get MEANS value of Array
def MEANS(array):
    sum = 0
    NumOfValues = 0
    Array = isNaN_Array(array)
    for i in range(array.shape[0]):
        if (Array[i] == False):
            sum += array[i]
            NumOfValues += 1
    return round((sum / NumOfValues), 2)


# get MEDIAN value of Array
def MEDIAN(array):
    Array = isNaN_Array(array)
    ValuesOfArray = []
    for i in range(array.shape[0]):
        if (isNaN(array[i]) == False):
            ValuesOfArray.append(array[i])
    ValuesOfArray.sort()
    N = int(len(ValuesOfArray) / 2)
    if (N % 2 == 0):
        return (ValuesOfArray[N - 1] + ValuesOfArray[N]) / 2
    else:
        return ValuesOfArray[N]


# get MODE value of Array
def MODE(array):
    ValueOfArray = {}
    Array = isNaN_Array(array)
    for i in range(array.shape[0]):
        if (isNaN(array[i]) == False):
            if array[i] in ValueOfArray:
                ValueOfArray[array[i]] += 1
            else:
                ValueOfArray[array[i]] = 1
    max = 0
    result = ''
    for Values in ValueOfArray:
        if (max < ValueOfArray[Values]):
            max = ValueOfArray[Values]
            result = Values
    return result


# find Type of Attributes
# convention:
# type = 1 : int or int64
# type = 2 : float or float64
# type = 3 : categorical
# type = 4: Number Of Missing Data equal Number Of Instances
def getTypeOfAttributes(dataset):
    TypeOfAttributes = {}  # constaint attribute and type of data
    attributes = list_attributes(dataset)  # get list of Attribute
    NumberOfMissing = list_NumberOfMissing(dataset)  # get the number of missed data
    NumOfInstances = getNumberOfInstances(dataset)
    for attribute in attributes:
        if (NumberOfMissing[attribute] == NumOfInstances):
            TypeOfAttributes[attribute] = 4
            continue
        for index in range(NumOfInstances):
            if (isNaN(dataset[attribute][index]) == False):
                if (type(dataset[attribute][index]) == int or type(dataset[attribute][index]) == np.int64):
                    TypeOfAttributes[attribute] = 1
                elif (type(dataset[attribute][index]) == float or type(dataset[attribute][index]) == np.float64):
                    TypeOfAttributes[attribute] = 2
                else:
                    TypeOfAttributes[attribute] = 3
                break
    return TypeOfAttributes


# standardlized_data
def standardlized_data_by_MINMAX_Method(dataset, attribute, newMAX, newMIN):
    # initialization min and max values for dataset[attribute]
    min = dataset[attribute][0]
    max = dataset[attribute][0]
    NumberOfInstances = getNumberOfInstances(dataset)
    #find max and min values
    for index in range(NumberOfInstances):
        if (isNaN(dataset[attribute][index]) == False):
            if (dataset[attribute][index] > max):
                max =dataset[attribute][index]
            elif (dataset[attribute][index] < min):
                min = dataset[attribute][index]
    min = float(min)
    max = float(max)
    #standardized data
    tmp_array = []
    for index in range(NumberOfInstances):
        if (isNaN(dataset[attribute][index]) == False):
            tmp_array.append(round(float((float(dataset[attribute][index]) - min) / (max - min)*(newMAX-newMIN) + newMIN),3))
        else:
            tmp_array.append(dataset[attribute][index])
    dataset[attribute]=tmp_array
def standardlized_data_by_ZScore_Method(dataset, attribute):
    means = MEANS(dataset[attribute])
    #compute variance
    NumberOfInstances = getNumberOfInstances(dataset)
    N =  NumberOfInstances - list_NumberOfMissing(dataset)[attribute]
    variance = 0
    for index in range(NumberOfInstances):
        if (isNaN(dataset[attribute][index]) == False):
            variance +=float(pow(float(dataset[attribute][index]-means),2) / N)
    #compute Standard Deviation
    Standard_Deviation = math.sqrt(variance)

    tmp_array = []
    for index in range(NumberOfInstances):
        if (isNaN(dataset[attribute][index]) == False):
            tmp_array.append(round(float((float(dataset[attribute][index])-means)/Standard_Deviation),3))
        else:
            tmp_array.append(dataset[attribute][index])
    dataset[attribute]=tmp_array

#Compute Sum of 2 attributes
def Sum(array1, array2):
    tmp_aray = [] # Create temporary array
    N = len(array1) # Number of Instances
    for i in range(N):
        if (isNaN(array1[i])==False and isNaN(array2[i])==False): # If 2 values of 2 attributes not NaN then compute sum of 2 values
            tmp_aray.append(array1[i]+array2[i])
        else: #If either value is NaN or both are NaN, we will assign the value of the temporary array as NaN
            if (isNaN(array1[i])):
                tmp_aray.append(array1[i])
            else:
                tmp_aray.append(array2[i])
    return tmp_aray

#Compute Subtract of 2 attributes
def Subtract(array1,array2):
    tmp_aray = []  # Create temporary array
    N = len(array1)  # Number of Instances
    for i in range(N):
        if (isNaN(array1[i]) == False and isNaN(array2[i]) == False):  # If 2 values of 2 attributes not NaN then compute subtract of 2 values
            tmp_aray.append(array1[i] - array2[i])
        else:  # If either value is NaN or both are NaN, we will assign the value of the temporary array as NaN
            if (isNaN(array1[i])):
                tmp_aray.append(array1[i])
            else:
                tmp_aray.append(array2[i])
    return tmp_aray

#Compute Multiply 2 attributes
def Multiple(array1,array2):
    tmp_aray = []  # Create temporary array
    N = len(array1)  # Number of Instances
    for i in range(N):
        if (isNaN(array1[i]) == False and isNaN(array2[i]) == False):  # If 2 values of 2 attributes not NaN then compute multiply of 2 values
            tmp_aray.append(array1[i] * array2[i])
        else:  # If either value is NaN or both are NaN, we will assign the value of the temporary array as NaN
            if (isNaN(array1[i])):
                tmp_aray.append(array1[i])
            else:
                tmp_aray.append(array2[i])
    return tmp_aray

#Compute Divide 2 attributes
def Divide(array1,array2):
    tmp_aray = []  # Create temporary array
    N = len(array1)  # Number of Instances
    for i in range(N):
        if (isNaN(array1[i]) == False and isNaN(array2[i]) == False):  # If 2 values of 2 attributes not NaN then compute divide of 2 values
            tmp_aray.append(array1[i] / array2[i])
        else:  # If either value is NaN or both are NaN, we will assign the value of the temporary array as NaN
            if (isNaN(array1[i])):
                tmp_aray.append(array1[i])
            else:
                tmp_aray.append(array2[i])
    return tmp_aray