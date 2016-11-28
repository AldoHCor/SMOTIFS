import os, sys
in_file = open('excel.txt', 'r')
print in_file
a = []
i = 0
with in_file as f:
    content = f.readlines()
    a[i] = content
    i =+ 1
print a
