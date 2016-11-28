import sys, os, glob, pickle, copy, random
from shutil import copyfile

i = 0
broken_files = open("true_broken.txt", 'r')

print broken_files
lines = broken_files.readlines()
for line in lines:
    #print line[2:9] #Broken definitions

    src = "./s100_pdbs/" + line[2:9] + ".pdb"
    storing = "./all_broken_pdb_files/" + line[2:9] + ".pdb"
    run = "cp "+src+" "+ storing
    print run, i
    os.system(run)
    i += 1
#    if i > 10:# Test
#       break

print i
broken_files.close()
