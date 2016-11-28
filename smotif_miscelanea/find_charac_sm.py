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

files = glob.glob("./smotif_cen_db/*.db") #List of strings in that folder with that termination
#print files

print "\nNumber of files: %-6d"% (len(files))
print "\n"
count_file = 0
no_of_data_entries = 0
Data_ = []
store_sm_data = {}
i = 5

for file in files:
    count_file = count_file + 1
    data = readPickle(file)
    num_entries = len(data)
    len_structure1 = data[0][0][2] - data[0][0][1] + 1
    len_structure2 = data[0][0][4] - data[0][0][3] + 1
    Data_ = 'file num.: %5d  smotif: %-9s   Entries: %5d lenght 1st: %3d lenght 2nd: %3d '% (count_file, file[16:-3], num_entries, len_structure1, len_structure2)
    print Data_
    store_sm_data[file] = num_entries, len_structure1, len_structure2
    #print store_sm_data[file]
    no_of_data_entries = no_of_data_entries + num_entries
    i = i + 1

out_file = open('./Pickle_files/smotifs_data.p', 'w')
pickle.dump(store_sm_data, out_file)
out_file.close()
print 'Number of data entries: %7d'% (no_of_data_entries)
