import sys, os, pickle, numpy



def readPickle(filename):
    """
    read pickle objects
    :param filename:
    :return:
    """
    if os.path.isfile(filename):
        # Filename is     ./smotif_cen_db/hh_5_62.db
        fin = open(filename, 'r')
        data = pickle.load(fin)
        fin.close()
        return data
    else:
        return False

#Wich smotif are we converting
smotif_type = 'hh_5_62.db'

smotif_db_path = "./smotif_cen_db/"

filename = smotif_db_path + smotif_type

print 'source file is ', filename

data = readPickle(filename)

entry = data[0]


print 'From protein: ', entry[0]

print entry, '\n\n' #three objects, desc., 1st estruc., 2nd estruc.

print entry[2], '\n\n' #2nd struc.

print entry[1][0], '\n\n' #whole inf about 1st atom

print entry[1][0][1], '\n\n' #one data of inf. about 1 atom
'''
list_ = []

i = len(entry[1])
num_at = 2279
j = 0
k = 0
z = 1

#Distance between smotifs
dist_between_smotifs = entry[0][3] - entry[0][2]

#Creates a nested list that stores atoms information
while k != 2:
    while i > 0:
        atom_type = entry[z][j][2]
        w_aa = entry[z][j][1]
        num_aa = entry[z][j][0]
        coor_x = entry[z][j][3]
        coor_y = entry[z][j][4]
        coor_z = entry[z][j][5]
        list_.append([['ATOM', (num_at), atom_type, w_aa, num_aa, coor_x, coor_y, coor_z]])
        j = j + 1
        i = i - 1
        num_at = num_at + 1

    num_at = num_at + dist_between_smotifs  #plus the distance between smotifs
    j = 0
    i = len(entry[2])
    k = k + 1
    z = z + 1

print 'total lenght of the smotif: ',len(list_)
print list_[0]
print list_[0][0][-1]
#print list_[0][6]
#print list_[-1]

#Formats the information input list_, nested

i = 0
list = []
while i < len(list_):
    pdb_line ="%-6s%5d  %-2s%5s%2s%4d%1s   %8.3f%8.3f%8.3f%6.2f%6.2f          %2s%2s" %('ATOM', list_[i][0][1], list_[i][0][2], list_[i][0][3], 'A', list_[i][0][4],'', list_[i][0][5], list_[i][0][6],list_[i][0][7],1.0,30.0,'','')
    list.append(pdb_line)
    i = i + 1

#Output formated list

#write in the file
#Write in filename

filename2 = "./" + smotif_type[0:-3] + ".pdb"
print "output file name is:", filename2

out_file = open(filename2, 'w')

#Loop: for each line

i = 0

while i < len(list): #To be replace with nested list
    #Create formated list from nested list
    current_line = str(list[i]) #Formated string
    out_file.write(current_line)
    out_file.write('\n')
    i = i + 1

out_file.close()
    #Do not chance current_line, i
'''
