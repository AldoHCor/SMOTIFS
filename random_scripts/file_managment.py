#filename=raw_input('File name:')
f=open('workfile.txt', 'r')
""
    #JUST READ
print f   #will only print <open file 'date1.py', mode 'r' at 
print('\n------START of the script------- \n\n ' + str(f.read()) + '\n------END of the script------\n')
print('script file')

""

""" #----------------find things in a file------------
        #Using fnmatch
import fnmatch
lst = ['this','is','just','a','test']
filtered = fnmatch.filter(lst, 'th?s')
print (filtered)
"""
        #Close file afterward
f.close()
print('is the file close?  ' + str(f.closed))
