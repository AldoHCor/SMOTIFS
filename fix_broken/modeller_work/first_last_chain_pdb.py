
broken_files = open("../files_in_broken.txt", 'r')
counter_diff = 0
list_ = []
for line in broken_files:

    f = open("../fix_broken/s100_pdbs/" + line[:-1], 'rb')
    lines = f.readlines()
    if lines:
        first_chain = lines[0][21:22]
        last_chain = lines[-1][21:22]
    f.close()
    if first_chain != last_chain:
        counter_diff += 1

    if first_chain not in list_:
        list_.append(first_chain)

    if last_chain not in list_:
        list_.append(last_chain)

    # print first_chain, last_chain

print counter_diff
print list_
