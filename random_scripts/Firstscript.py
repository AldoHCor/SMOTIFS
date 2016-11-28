seq = raw_input("Paste the sequence") #"ATGtgtattcctgtgacatgctgctagctagctagATCGAA"
print seq.upper()
print seq.lower()

# lenght = str(len(sequence))
# print "the lenght of the sequence is " + lenght

print "the lenght of the sequence is " + str(len(seq))     #Print by concatenating

print "the lenght of the sequence is %s" % (len(seq))      #Print using %s

car = raw_input("Specifications: ")
print "Las especificaciones son: %s," % (car)
Res = raw_input("es correcto? Y/N")
from datetime import datetime
print datetime