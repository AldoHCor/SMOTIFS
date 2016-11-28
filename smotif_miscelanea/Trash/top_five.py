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

i = 0
files = glob.glob("./smotif_cen_db/*.db")
Sm_len = {}
Final = [][]
for file in files:
    data = readPickle(file)
    entry = data[0]
    first = entry[0]
    H_long = first[2]+first[4]-first[3]-first[1]
    Sm_len[file] = H_long

for key, value in sorted(Sm_len.iteritems(), key=lambda (k,v): (v,k)):
    print "%s: %s" % (key, value)
    Final[]   = key

print sorted(Sm_len.keys())
#for filename in sorted(Sm_len):
6er6er6
#   print filename,

#np_smotif_len = numpy.array(smotif_len)
#print np_smotif_len.shape
#L_len = np_smotif_len[:,1]
#print L_len
