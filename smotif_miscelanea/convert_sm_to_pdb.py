import sys, os, pickle
sys.path.append("./qcp_rmsd/")
import qcp

def readPickle(filename):
    if os.path.isfile(filename):
        fin = open(filename, 'r')
        print fin
        data = pickle.load(fin)
        fin.close()
        return data
    else:
        print 'No such file'
        return False

smotif_db_path = './smotif_cen_db/'
#smotif_name = 'hh_68_36'
smotif_name = raw_input('smotif name: \n (Ex. hh_5_62) ')
smotif_db_path = smotif_db_path + smotif_name + '.db'
file_ = readPickle(smotif_db_path)
os.mkdir('./smotifs_pdb/'+ smotif_name + '/')

m = len(file_)
n = 0

while (m > n):
    smotif = file_[n]
    prot_name, se1_st, se1_fn, se2_in, se2_fn = smotif[0][0],smotif[0][1], smotif[0][2], smotif[0][3], smotif[0][4]
    print '\nSmotif taken from protein: %s \nsec. Structure #1 in residues %d to %d \nSec. structure #2 in residues %d to %d '%(prot_name, se1_st, se1_fn, se2_in, se2_fn)

    loop_len = se2_in - se1_fn - 1
    print 'The lenght of the loop is %d\n' %(loop_len)

    #creates a file .pdb with the smotif's name
    filename2 = './smotifs_pdb/' + smotif_name + '/' + smotif_name + '_' + smotif[0][0] + '.pdb'
    out_file = open(filename2, 'w')
    print out_file

    i = 0
    k = 1
    num_at = 1 #Arbitrary in this case
    j = len(smotif[k])

    while j > i:
        #access, format and write to pdb
        atom_type = smotif[k][i][2]
        aa_res = smotif[k][i][1]
        aa_res_num = smotif[k][i][0]
        x = smotif[k][i][3]
        y = smotif[k][i][4]
        z = smotif[k][i][5]
        pdb_line ="%-6s%5d  %-2s%5s%2s%4d%1s   %8.3f%8.3f%8.3f%6.2f%6.2f          %2s%2s"%('ATOM', num_at, atom_type, aa_res, 'A', aa_res_num, ' ', x, y, z, 1.0, 30.0, '', '\n')
        out_file.write(pdb_line)

        i = i + 1
        num_at = num_at + 1 #num_at equal to number of atoms in the beginiing of chain

        if  i == j and k != 2:
            num_at = num_at + 5*loop_len
            i = 0
            k = 2
            j = len(smotif[k])
    n = n + 1
