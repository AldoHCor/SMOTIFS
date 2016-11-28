import sys, os, pickle, glob
from collections import OrderedDict

def readPickle(filename):
    """
    read pickle objects
    :param filename:
    :return:
    """
    if os.path.isfile(filename):
        fin = open(filename, 'r')
        print fin
        data = pickle.load(fin)
        fin.close()
        return data
    else:
        return False


pickle = raw_input("Pickle file:")
A = readPickle(pickle)
print A
B = "filename"
outfile = open(B,'w')
# sdkmsdkmdclsmpasmcpaocmp
