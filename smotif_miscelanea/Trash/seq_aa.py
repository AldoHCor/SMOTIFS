import os, sys, copy
in_file = open('peptides.txt', 'r')
print in_file
a = []
i = 0
b = {}
countA = 0
countR = 0
countN = 0
countD = 0
countC = 0
countQ = 0
countE = 0
countG = 0
countH = 0
countI = 0
countL = 0
countK = 0
countM = 0
countF = 0
countP = 0
countS = 0
countT = 0
countW = 0
countY = 0
countV = 0
k = 0

with in_file as f:
    content = f.readlines()
    a.append(content)

print len(a[0])

while i < len(a[0]):
    a[0][i] = a[0][i][:-1]
    i = i + 1

del a[0][-1]

print a

for j in range(0,len(a[0])):
    for k in range(0,len(a[0][k])):
        if a[0][j][k] == 'A':
            countA = countA + 1
        if a[0][j][k] == 'R':
            countR = countR + 1
        if a[0][j][k] == 'N':
            countN = countN + 1
        if a[0][j][k] == 'D':
            countD = countD + 1
        if a[0][j][k] == 'C':
            countC = countC + 1
        if a[0][j][k] == 'Q':
            countQ = countQ + 1
        if a[0][j][k] == 'E':
            countE = countE + 1
        if a[0][j][k] == 'G':
            countG = countG + 1
        if a[0][j][k] == 'H':
            countH = countH + 1
        if a[0][j][k] == 'I':
            countI = countI + 1
        if a[0][j][k] == 'L':
            countL = countL + 1
        if a[0][j][k] == 'K':
            countK = countK + 1
        if a[0][j][k] == 'M':
            countM = countM + 1
        if a[0][j][k] == 'F':
            countF = countF + 1
        if a[0][j][k] == 'P':
            countP = countP + 1
        if a[0][j][k] == 'S':
            countS = countS + 1
        if a[0][j][k] == 'T':
            countT = countT + 1
        if a[0][j][k] == 'W':
            countW = countW + 1
        if a[0][j][k] == 'Y':
            countY = countY + 1
        if a[0][j][k] == 'V':
            countV = countV + 1

#for b in sorted(file_, key=file_.get, reverse = True):

print 'A', countA
print 'R', countR
print 'N', countN
print 'D', countD
print 'C', countC
print 'Q', countQ
print 'E', countE
print 'G', countG
print 'H', countH
print 'I', countI
print 'L', countL
print 'K', countK
print 'M', countM
print 'F', countF
print 'P', countP
print 'S', countS
print 'T', countT
print 'W', countW
print 'Y', countY
print 'V', countV

'''
#------------------------------------------------------------------------------
import os, sys, copy
in_file = open('peptides.txt', 'r')
print in_file
a = []
i = 0
b = {}
count2 = 0
with in_file as f:
    content = f.readlines()
    a.append(content)

print len(a[0])

while i < len(a[0]):
    a[0][i] = a[0][i][:-1]
    i = i + 1

del a[0][-1]

print a

for i in range(len(a[0])):
    count = 0
    for j in range(len(a[0])):
        for k in range(len(a[0][j])):
            if str(a[0][i][k]) in str(a[0][j]):
                count = count + 1
        if count == 7:
            count2 = count2 + 1
    b[a[0][i]] = count2
    count2 = 0

#for b in sorted(file_, key=file_.get, reverse = True):

print b
'''
