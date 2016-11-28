import sys, os, pickle, glob


def readPickle(filename):
    """
    read pickle objects
    :param filename:
    :return:
    """
    if os.path.isfile(filename):
        fin = open(filename, 'r')
        data = pickle.load(fin)
        fin.close()
        return data
    else:
        return False

files = glob.glob("./smotif_cen_db/*.db")
#print files 
print "\nnumber of files:"
print len(files)
print "\n\n"
count_file = 0
no_of_data_entries = 0


for file in files:
    count_file = count_file+1
    data = readPickle(file) 
    print file, count_file, len(data)
    tentries = len(data)
    no_of_data_entries = no_of_data_entries + tentries


print no_of_data_entries 
