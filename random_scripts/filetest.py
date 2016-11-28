import sys,os

filename = open(sys.argv[1],'r')
lines = filename.readlines()
filename.close()

for line in lines:
    pass


print len(lines)

count = 0
for i in range(0,len(lines)):
    if lines[i]=='\n':
        count +=1


print count
