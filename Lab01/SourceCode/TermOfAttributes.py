"""
    Argument syntax:
        python TermOfAttributes.py input.csv --term_name=TermName --term ... --output=output.csv
    Example:
         python TermOfAttributes.py house-prices.csv --term_name=Term1 --term ( id * lotFrontage + MSSubClass) / Id --output=request8.csv

    (*) Note: there must be a space between the operand and the operator
"""

import sys
import csv
from SupportFunction import getDataset, list_attributes,Sum,Subtract,Multiple,Divide

input = sys.argv[1]
output = sys.argv[len(sys.argv) - 1].split("=")[1]
term_name = sys.argv[2].split("=")[1]


# A utility function to return  precedence of a given operator
# Higher returned value means  higher precedence
def Prec(c):
    if (c == "+" or c == "-"):
        return 1
    elif (c == "*" or c == "/"):
        return 2
    return -1


# get dataset
dataset = getDataset(input)
attributes = list_attributes(dataset)

# convert Infix to Postfix
Postfix = []
stack = []
for index in range(4, len(sys.argv) - 1, 1):
    item = sys.argv[index]
    if (item not in ['(', ')', '+', '-', '*', '/', '^']):
        Postfix.append(item)
    else:
        if (item == "("):
            stack.append(item)
        elif (item == ")"):
            while (len(stack) != 0):
                x = stack.pop()
                if (x == '('):
                    break
                Postfix.append(x)
        else:
            if (len(stack) == 0):
                stack.append(item)
            else:
                check = False
                while (len(stack) != 0):
                    x = stack.pop()
                    if (x != '(' and Prec(x) >= Prec(item)):
                        Postfix.append(x)
                    else:
                        stack.append(x)
                        stack.append(item)
                        check = True
                        break
                if (check == False):
                    stack.append(item)
while (len(stack)!=0):
    x=stack.pop()
    if (x!=')' and x!=')'):
        Postfix.append(x)
#compute the term
stack2 = []
for item in Postfix:
    if (len(item)>1):
        for attribute in attributes:
            if (attribute.lower()==item.lower()):
                stack2.append(dataset[attribute])
                break
    else:
        if (item=="+"):
            y = stack2.pop()
            x = stack2.pop()
            stack2.append(Sum(x,y))
        elif (item=="-"):
            y = stack2.pop()
            x = stack2.pop()
            stack2.append(Subtract(x,y))
        elif (item=="*"):
            y = stack2.pop()
            x = stack2.pop()
            stack2.append(Multiple(x,y))
        elif (item=="/"):
            y = stack2.pop()
            x = stack2.pop()
            stack2.append(Divide(x,y))

result = stack2.pop()

#write file
inputfile = open(input, 'r')
outputfile = open(output,'w',newline='')
dataset = csv.reader(inputfile)
writer = csv.writer(outputfile)

index=0
for row in dataset:
    if (index == 0):
        row.append(term_name)
        writer.writerow(row)
        index +=1
        continue

    row.append(str(result[index-1]))
    writer.writerow(row)
    index += 1
inputfile.close()
outputfile.close()
