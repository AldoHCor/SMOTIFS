import sys, os, pickle, numpy



def readPickle(filename):
    """
    read pickle objects
    :param filename:
    :return:
    """
    if os.path.isfile(filename):
        # Filename is     ./smotif_cen_db/hh_5_39.db
        fin = open(filename, 'r')
        data = pickle.load(fin)
        fin.close()
        return data
    else:
        return False

#Wich smotif are we converting
smotif_type = 'hh_5_6.db'

smotif_db_path = "./smotif_cen_db/"

filename = smotif_db_path + smotif_type

print filename

data = readPickle(filename)

entry = data[0]


#Retrieve Data


#Format Data


#Write in filename

filename2 = "./" + smotif_type[0:-3] + ".pdb"
print "output file name is:", filename2

out_file = open(filename2, 'w')







#Loop: for each line

test_list = [1,2,3,4,5]
i = 0

while i < len(test_list): #To be replace with nested list
    #Create formated list from nested list
    current_line = "first line" #Formated string
    out_file.write(current_line)
    out_file.write('\n')
    i = i + 1

out_file.close()
    #Do not chance current_line, i
    #Chance test_list, "current_line"
