import sys


filename=sys.argv[1]
f=open(filename, 'r')
print f   #will only print <open file 'date1.py', mode 'r' at 0x7ff1755dc420>
print('\n\n------START of the script------- \n\n ' + str(f.read()) + '------END of the script------\n\n')
