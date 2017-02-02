from modeller import *
from modeller.automodel import *  # Load the auto model class

broken_files = open("files_in_broken4.txt", 'r')

for line in broken_files:

    # Alignments
    f = open("./templates/" + line[:-1], 'rb')
    line_ = f.readline()
    chain = line_[21:22]
    f.close()

    name = line[:-5]  # 1a1vA03
    f_ = "FIRST:" + chain
    l_ = "LAST:" + chain
    env = environ()
    aln = alignment(env)
    mdl = model(env, file="./templates/" + name, model_segment=(f_, l_))
    aln.append_model(mdl, align_codes=name, atom_files=name + '.pdb')
    aln.append(file="./sequences/" + name + '_new.seq', align_codes=name + '_new')
    aln.align2d()
    aln.write(file='./alignments/' + 'temp_query_' + name + '.ali', alignment_format='PIR')

    # Model

    log.verbose()
    env = environ()

    # directories for input atom files
    env.io.atom_files_directory = ['.', './atom_files']
    env.io.hetatm = True
    a = automodel(env, alnfile="./alignments/" + "/temp_query_" + name + ".ali",      # alignment filename
                  knowns=name,                                                        # codes of the templates
                  sequence=name + "_new")                                             # code of the target

    a.starting_model = 1
    a.ending_model = 1

    # make the homology model
    a.make()
