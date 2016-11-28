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

R = 'smotifs_data.p'
file_ = readPickle(R)
#print file_['./smotif_cen_db/hh_39_29.db']
array_ = []
data_dic = {}

for file in sorted(file_, key=file_.get, reverse = True):
    len_ = file_[file][2] + file_[file][1]
    entries = file_[file][0]
    array_.append([file, len_, entries])
    data_dic[file] = (len_, entries)

out_file_dic = open('smotifs_data_dic.p', 'w')
print out_file_dic
pickle.dump(data_dic, out_file_dic)
out_file_dic.close()

out_file_array = open('smotifs_data_array.p', 'w')
print out_file_array
pickle.dump(array_, out_file_array)
out_file_array.close()
