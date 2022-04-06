# imports the regular expression library and the mean function
import re
from statistics import mean

# creates a list to hold the numbers
ls = list()

# prompts the user for a file name.
fhandle = open(input('Enter a file name: '))

#extracts the lines that have the "New Revision" denotation and appends the numbers in those lines to a new list.
for line in fhandle:
    line = line.rstrip()
    lst = re.findall('New Revision: ([0-9]+)', line)
    # if len(lst)>0:
    #     print(lst)
    ls = ls + lst

nl = [int(x) for x in ls] #list comprehension
# print(nl)
print(int(mean(nl)))