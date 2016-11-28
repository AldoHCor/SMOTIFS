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

condition = True
condition2 = True
i = 0
out_file_ = open('./guide.txt', 'w')
while condition == True:
    R = raw_input('Pickle file: \n(for dictionary')
    R = './Pickle_files/' + R
    if os.path.isfile(R):
        file_ = readPickle(R)
        #[1] For sorted  dictionaries
        for file in sorted(file_, key=file_.get, reverse = True):
            print ('%-30s   %s')%(file, file_[file])
            inf = ('%-30s   %s \n')%(file, file_[file])
            out_file_.write(inf)
        #[2] For arrays
        #for file in file_:
        #    print file_[i]
        #    i = i + 1

        #[3] For anything
        #print file_
        #print R, type(file_), '\n\n'
        out_file_.close()
    else:
        print 'Not here or typo'

    condition2 = True

    while condition2 == True:
        P = raw_input('Would you like to \nread another file? y/n ')
        if P == 'y':
            print 'Again'
            condition2 = False
        else:
            if P == 'n':
                condition2 = False
                condition = False
