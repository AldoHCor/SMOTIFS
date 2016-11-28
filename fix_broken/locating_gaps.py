import math
from shutil import copyfile


def distance(c1, c2): # Takes two lists with the x-y-z coordinates
    x_dist = (c1[0] - c2[0])**2
    y_dist = (c1[1] - c2[1])**2
    z_dist = (c1[2] - c2[2])**2
    return math.sqrt(x_dist + y_dist + z_dist)

count_diff = 0
count_diff2 = 0
i = 0
j = 1
gaps1 = []
gaps2 = []
coor1 =[0, 0, 0]
coor2 =[0, 0, 0]

broken_list = []

broken_files = open("true_broken.txt", 'r')
# print broken_files

for line in broken_files:
    storing = "./all_broken_pdb_files/" + line[2:9] + ".pdb"
    broken_list.append(storing)

broken_files.close()
# print len(broken_list)


for x in range(0, len(broken_list) ):

    gaps1 = []
    gaps2 = []

    broken_prot = broken_list[x]  #This is suppose to be at /fix_broken
    pdb_file = open(broken_prot, "r")
    file_list = pdb_file.readlines()

    #for line in pdb_file:
    #    file_list.append(line)

    pdb_file.close()
    j = 1
    ca_list = []

    for i in range(0, len(file_list)-1):

        res_num1 = int(file_list[i][22:26])
        res_num2 = int(file_list[j][22:26])
        # print res_num1
        # print res_num2
        diff_res = abs(res_num1 - res_num2)
        if diff_res > 1:
            # Gap in sequence
            gaps1.append(res_num1)
            gaps1.append(res_num2)
        j += 1

        if file_list[i][12:16] == " CA ":  # " CA ", in that format to work
            ca_list.append(file_list[i])

    i = 0
    j = 0
    print str(broken_list[x][9:-3]) + "pdb"  # Which protein
    dist_cutoff = 4 # Distance cutoff between ca atoms
    for i in range(0, len(ca_list)-1):
        j = i + 1
        coor1[0], coor1[1], coor1[2] = float(ca_list[i][30:38]), float(ca_list[i][38:46]), float(ca_list[i][46:54])
        coor2[0], coor2[1], coor2[2] = float(ca_list[j][30:38]), float(ca_list[j][38:46]), float(ca_list[j][46:54])
        dist = distance(coor1, coor2)
        if dist > 4:
            gaps2.append(int(ca_list[i][22:26]))
            gaps2.append(int(ca_list[j][22:26]))
            # print ca_list[i][22:26], ca_list[i][12:16], dist #residue number, atom CA, distance between ca, ex:   212  CA  3.83122304223

    # print "\nNumeration is broken after these residues:\n", gaps1, '\n'
    # print "Distance is bigger than ", dist_cutoff, "A after these residues:\n", gaps2
    # Compare gaps1 and gaps2
    state = cmp(gaps1,gaps2)
    # print "same? ", state, "\n\n"

    if state == 0:

            src = "./s100_pdbs/" + broken_list[x][9:-4] + ".pdb"
            storing = "./fixable_pdbs/" + broken_list[x][9:-4] + ".pdb"
            # print "Copying", src,"to", storing, "\n"
            copyfile(src, storing)

    if gaps2 == [] and gaps1 != []:
        count_diff2 += 1
    if state != 0:
        count_diff += 1


# print "Number of diff", count_diff, "Of which", count_diff2, "are equal to [] with gaps2"
    # if x == 100000:
    #    break
