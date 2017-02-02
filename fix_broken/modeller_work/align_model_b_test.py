from modeller import *
from modeller.automodel import *  # Load the auto model class

broken_files = open("files_in_broken2.txt", 'r')

# print line
name = "1a7aB01"  # 1a1vA03
print name
env = environ()
aln = alignment(env)

mdl = model(env, file=name, model_segment=('FIRST:B', 'LAST:B'))
aln.append_model(mdl, align_codes=name, atom_files=name + '.pdb')
aln.append(file=name + '_new.seq', align_codes=name + '_new')
aln.align2d()
aln.write(file='temp_query_' + name + '.ali', alignment_format='PIR')

#  model-fast

log.verbose()
env = environ()
# directories for input atom files
env.io.atom_files_directory = ['.', './atom_files']
env.io.hetatm = True
a = automodel(env, alnfile="temp_query_" + name + ".ali", knowns=name, sequence=name + "_new")
a.starting_model = 1
a.ending_model = 1
a.make()
# make the homology model
