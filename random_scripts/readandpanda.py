import pandas as pd
filename=raw_input('file name: ')
with open(filename,'r') as f:
for line in  f:
        s=(s + f.readline())
print (s)
