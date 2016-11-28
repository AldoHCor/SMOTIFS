import sys, os, pickle



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



smotif_type = 'hh_16_18.db'

#./smotif_cen_db/hh_16_18.db 1656 115
smotif_db_path = "./smotif_cen_db/"

filename = smotif_db_path + smotif_type

print filename

data = readPickle(filename)

entry = data[0]
print len(entry)
#First entry, three arrays, 1st description, 2nd and 3rt are the smotifs.
print len(data)
#How many times does this smotif appear in the data base
print "\n\n\n"
#print data 

#Will print all entries 

for array in entry:
    print array
