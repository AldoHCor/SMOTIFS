import sys, os, pickle



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



smotif_type = 'hh_5_6.db'

smotif_db_path = "./smotif_cen_db/"

filename = smotif_db_path + smotif_type

print filename

data = readPickle(filename)


#print data

entry = data[0]
print  len(entry)
print "\n\n                <-- len(entry)    array --->                                   \n\n "

for array in entry:
    print array
    print "\n\n"


"""

sys.path

A list of strings that specifies the search path for modules. Initialized from the environment variable PYTHONPATH, plus an installation-dependent default.

As initialized upon program startup, the first item of this list, path[0], is the directory containing the script that was used to invoke the Python interpreter. If the script directory is not available (e.g. if the interpreter is invoked interactively or if the script is read from standard input), path[0] is the empty string, which directs Python to search modules in the current directory first. Notice that the script directory is inserted before the entries inserted as a result of PYTHONPATH.

os.path.isfile(path).

Return True if path is an existing regular file.
This follows symbolic links, so both islink() and isfile() can be true for the same path.


pickle.load(file)

Read a string from the open file object file and interpret it as a pickle data stream, reconstructing and returning the original object hierarchy. This is equivalent to Unpickler(file).load().

"""
