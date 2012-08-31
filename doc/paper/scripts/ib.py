#!/usr/bin/env python

# Do your Biopython stuff.


import datetime
import Bio

from Bio import Motif
from Bio.Alphabet import IUPAC


print "This works!"


sequencestarttime = datetime.datetime.now( )
sequence = ""

with open ("/u/trosko/projects/data/ecoliMG1655.fa") as indatafile:
	indatafile.readline()
	for line in indatafile:
		sequence += line.strip()
	
sequenceendtime = datetime.datetime.now( )

#
# This is from BioPython
#
#

print "Biopyhton exact matches!"

from Bio.Seq import Seq

from Bio.Alphabet import IUPAC

starttime = datetime.datetime.now( )

starttimeiupac = datetime.datetime.now( )

s1 = Motif.Motif(alphabet=IUPAC.unambiguous_dna)
s1.add_instance(Seq("AGATAA",s1.alphabet))
s1.add_instance(Seq("AGATAG",s1.alphabet))
s1.add_instance(Seq("TGATAA",s1.alphabet))
s1.add_instance(Seq("TGATAG",s1.alphabet))
test_seq=Seq(sequence, s1.alphabet)
for pos,seq in s1.search_instances(test_seq):
	print pos,seq.tostring()

endtimeiupac = datetime.datetime.now( )
endtime = datetime.datetime.now( )

print sequenceendtime - sequencestarttime

print endtimeiupac - starttimeiupac
print endtime - starttime
