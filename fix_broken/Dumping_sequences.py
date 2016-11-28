import pickle

AA_dic = {'ALA': 'A', 'ARG': 'R', 'ASN': 'N', 'ASP': 'D', 'ASX': 'B', 'CYS': 'C', 'GLU': 'E', 'GLN': 'Q',
          'GLX': 'Z', 'GLY': 'G', 'HIS': 'H', 'ILE': 'I', 'LEU': 'L', 'LYS': 'K', 'MET': 'M', 'PHE': 'F',
          'PRO': 'P', 'SER': 'S', 'THR': 'T', 'TRP': 'W', 'TYR': 'Y', 'VAL': 'V'}

break_dic = {}

broken_pdb_list = []

broken_files = open("files_in_broken.txt", 'r')

for line in broken_files:
    #  print line
    storing = "./fixable_pdb_files/" + line[:-5] + ".pdb"
    broken_pdb_list.append(storing)

broken_files.close()

AA = 'A'                                      # Amino acid added to the breaks in the chain

for x in range(0, len(broken_pdb_list)):      # iterates in the names of the broken pdb files

    broken_protein = broken_pdb_list[x]          # At fix_broken
    pdb_file = open(broken_protein, "r")
    file_list = pdb_file.readlines()
    pdb_file.close()

    breaks_list = []
    ca_list = []
    file_list2 = []
    new_seq = []
    old_seq = []

    # iterates in the pdb file, each line example:
    # ATOM   2071  N   VAL A 432      30.949  34.393  10.112  1.00 23.66

    for i in range(0, len(file_list)):

        if file_list[i][12:16] == " CA ":  # " CA ", in that format to work
            ca_list.append(file_list[i])

    # iterates in the pdb file, each line example:
    # ATOM   2071  CA   VAL A 432      30.949  34.393  10.112  1.00 23.66

    j = 1

    for i in range(0, len(ca_list)-1):
        # Generate list of [ where are they broken, how many residues ]

        res_num1 = int(ca_list[i][22:26])
        res_num2 = int(ca_list[j][22:26])
        diff_res = abs(res_num1 - res_num2)
        aa = ca_list[i][17:20]                # Where ca_list[i][17:20] refers to the current amino acid
        #  print aa
        aa = AA_dic[aa]
        #  print aa
        old_seq.append(aa)
        new_seq.append(aa)

        if diff_res <= 5 and diff_res != 1:   # Gap in sequence
            breaks_list.append(res_num1)      # where is broken
            breaks_list.append(diff_res)      # len of the break
            new_seq.append(AA*diff_res)       # Adds the number of amino acids of the break

        j += 1

    # last AA
    aa = ca_list[-1][17:20]
    aa = AA_dic[aa]
    old_seq.append(aa)
    new_seq.append(aa)

    new_seq = ''.join(new_seq)
    old_seq = ''.join(old_seq)

    #  pickle dump and show the list
    break_dic[broken_protein[9:-4]] = breaks_list

    '''
    print "-", broken_protein[9:-4], breaks_list, "\n"
    '''

    #  Write it in a PIR text file

    old = ">" + "P1;" + broken_protein[9:-4] + "_old" + "\n" + "sequence: " + broken_protein[9:-4] + "::::::::" \
          + "\n" + old_seq + '*'
    print old
    new = ">" + "P1;" + broken_protein[9:-4] + "_new" + "\n" + "sequence:" + broken_protein[9:-4] + "::::::::" \
          + "\n" + new_seq + '*'
    print new

    save_new = open("./modeller_work/sequences/" + broken_protein[9:-4] + "_new" + ".seq", "w")
    save_new.write(new)
    save_new.close()

pickle.dump(break_dic, open("breaks_all.p", "wb"))

'''
PIR

A sequence in PIR format consists of:

One line starting with a ">" (greater-than) sign, followed by a two-letter code describing the sequence type
(P1, F1, DL, DC, RL, RC, or XX), followed by a semicolon, followed by the sequence identification code
(the database ID-code).

One line containing a textual description of the sequence.
One or more lines containing the sequence itself. The end of the sequence is marked by a "*" (asterisk) character.

Sequence type	      code
Protein (complete)	   P1
Protein (fragment)	   F1
DNA (linear)	       DL
DNA (circular)   	   DC
RNA (linear)     	   RL
RNA (circular)   	   RC
tRNA	               N5
'''