# Finding Numbers in a Haystack

# In this assignment you will read through and parse a file with text and numbers.
# You will extract all the numbers in the file and compute the sum of the numbers.

# Data Files
# We provide two files for this assignment.
# One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.

# Sample data: http://py4e-data.dr-chuck.net/regex_sum_42.txt (There are 90 values with a sum=445833)
# Actual data: http://py4e-data.dr-chuck.net/regex_sum_38794.txt (There are 90 values and the sum ends with 360)

import re

ls_of_num = []
with open('regex_sum_38794.txt') as file:
    for line in file:
        line = re.findall(r'\d+', line)
        for num in line:
            ls_of_num.append(int(num))
print(f'Sum of numbers in actual data is {sum(ls_of_num)}')
