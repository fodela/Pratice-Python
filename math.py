# ntegers in Python can be as big as the bytes in your machine's memory. There is no limit in size as there is:  (c++ int) or  (C++ long long int).

# As we know, the result of  grows really fast with increasing .

# Let's do some calculations on very large integers.

# Task
# Read four numbers, , , , and , and print the result of .

# Input Format
# Integers , , , and  are given on four separate lines, respectively.

# Constraints




# Output Format
# Print the result of  on one line.

# Sample Input

# 9
# 29
# 7
# 27

# Enter your code here. Read input from STDIN. Print output to STDOUT
a = int(input())
b = int(input())
c = int(input())
d = int(input())

print((a**b)+(c**d))