import sys,os, glob, pickle
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

def qcp_rmsd(entry1,entry2):
    """
    calculate RMSD between the two Smotifs
    :param S1:smotif1 data array, S2:smotif2 data array
    :return float(rmsd)
    """

    print entry1[0], entry2[0]

    frag_a = entry1[1]+entry1[2]
    frag_b = entry2[1]+entry2[2]

    rmsd = qcp.rmsdQCP(frag_a,frag_b)

    return rmsd

def main():

    smotifs = readPickle('/home/biocomp/qcp_rmsd/db_and_pdb/db/sh_12_30.db')

    for i in range(0, len(smotifs)-1):
        entry1 = smotifs[i]
        entry2 = smotifs[i+1]
        rmsd = qcp_rmsd(entry1, entry2)
        print ('rmsd: %-3.3f')% rmsd

if __name__ == '__main__':
    main()
