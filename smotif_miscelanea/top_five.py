import sys, os, pickle, glob, numpy

def readPickle(filename):
   """
   read pickle objects
   :param filename:
   :return:
   """
   if os.path.isfile(filename):
       fin = open(filename,'r')
       data = pickle.load(fin)
       fin.close()
       return data
   else:
       return False

files = glob.glob("./smotif_cen_db/*.db")
smotif_len = []
np_smotif_len = numpy.array(smotif_len)
i = 1

for file in files:
    data = readPickle(file) 
    entry = data[0]
    first = entry[0]
    H_long = first[2]+first[4]-first[3]-first[1]
    np_smotif_len[i] = H_long
    i = i+1
