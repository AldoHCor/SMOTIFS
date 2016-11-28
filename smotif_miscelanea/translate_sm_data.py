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


#a = raw_input('name of file: ')
a = 'smotifs_data.p'
data = readPickle(a)
data = OrderedDict(data)

data_entries = {}
data_len = {}
i = 1
entries = []
len_ = []
for file in data:
    data_entries[file] = data[file][0]
    data_len[file] = data[file][1] + data[file][2]

out_file_en = open('List_by_entries', 'w')

for file in sorted(data_entries, key=data_entries.get, reverse = True):

    print i, file, data_entries[file]
    a = [file, data_entries[file]]
    entries.append(a)
    i = i + 1

for item in entries:
    out_file_en.write('%s \n'% item)
out_file_en.close()

out_file_len = open('List_by_lenght', 'w')
i = 1

for file in sorted(data_len, key=data_len.get, reverse = True):
    print i, file, data_len[file]
    b = [file, data_len[file]]
    len_.append(b)
    i = i + 1

for item in len_:
    out_file_len.write('%s \n'% item)
out_file_len.close()
