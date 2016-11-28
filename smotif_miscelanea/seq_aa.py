import os, sys, copy
in_file = open('peptides.txt', 'r')
print in_file
a = []
i = 0
with in_file as f:
    content = f.readlines()
    a.append(content)

print a
print len(a[0])

while i < len(a[0]):
    a[0][i] = a[0][i][:-1]
    i = i + 1

del a[0][-1]

print a
