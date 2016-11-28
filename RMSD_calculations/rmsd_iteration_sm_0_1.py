import sys,os, glob, pickle, copy, random
sys.path.append("/home/biocomp/Documents/qcp_rmsd/")
import qcp

#calculate RMSD for any two given Motifs

def readPickle(filename):
    """
    read pickle objects
    :param filename:
    :return: array of arrays
    """
    if os.path.isfile(filename):
        fin = open(filename, 'r')
        data = pickle.load(fin)
        fin.close()
        return data
    else:
        return False

def qcp_rmsd(entry1,entry2, cutoff):
    """
    calculate RMSD between the two Smotifs
    :param S1:smotif1 data array, S2:smotif2 data array
    :return float(rmsd)
    """

    frag_a = entry1[1] + entry1[2]
    frag_b = entry2[1] + entry2[2]
    rmsd = qcp.rmsdQCP(frag_a,frag_b)
    if rmsd < cutoff:
        print entry1[0], entry2[0], rmsd
    return rmsd

cutoff = 0.1 #same
cutoff_ = str(cutoff)
counter_all = 0 #number of rmsd calculated globally
os.mkdir('./database_' + 'cutoff_' + cutoff_ + '/')


Definitions = glob.glob("./smotif_cen_db/*.db") #List of strings in that folder with that termination

print 'Cutoff of ', cutoff
#print each name

for file in Definitions:
    print file

    smotif = readPickle(file)

    pos = 0
    num_iteration = 1
    print 'initial entries: ', len(smotif)

    counter = 0 #how many rmsd were calculated
    while pos < (len(smotif)-1):
        print 'Iteration: ', num_iteration, 'Position:', pos
        num_iteration = num_iteration + 1
        t = []

        csmotif = smotif[pos]
        same = 0 #same been the number of redundant smotifs for that entry
        for i in range(0, len(smotif)):
            rmsd = qcp_rmsd(csmotif, smotif[i], cutoff) #Prints subjects and rmsd
            counter +=1
            counter_all +=1
            round(rmsd, 2)

            if i == pos:
                t.append(smotif[i])
            if rmsd >= cutoff:
                t.append(smotif[i])
            if rmsd < cutoff:
                same = same + 1

        print 'Redundant entries for ' + str(csmotif[0][0]) + ' is ' + str(same-1)

        if len(t) == 0:
            R = random.randint(0,len(smotif)-1)
            print len(smotif[R])
            smotif = copy.deepcopy(smotif[R])
            print 'all redundant', smotif[0][0]
            break

        smotif = copy.deepcopy(t)

        print '\ncurrent lenght: ', len(smotif)

        if pos >= len(smotif)-1:
            print 'Done'
            break

        pos = pos + 1

    print 'Final lenght: ', len(smotif)

    for i in range(0, len(smotif)):
        print smotif[i][0]

    file = file[15:]
    print file, 'number of rmsd calculated: ', str(counter) + '\n\n\n'
    storing = './database_' + 'cutoff_' + cutoff_ + file
    out_file = open(storing, 'w')
    pickle.dump(smotif, out_file)
    out_file.close()

print 'Total rmsd calculated: ', counter_all
