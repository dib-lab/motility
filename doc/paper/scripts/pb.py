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

print "Biopyhton Pam matches!"

from Bio.Seq import Seq

from Bio.Alphabet import IUPAC

starttime = datetime.datetime.now( )

starttimepam = datetime.datetime.now( )

s1 = Motif.Motif(alphabet=IUPAC.unambiguous_dna)
s1.add_instance(Seq("AGATAA",s1.alphabet))
s1.add_instance(Seq("AGATAG",s1.alphabet))
s1.add_instance(Seq("TGATAA",s1.alphabet))
s1.add_instance(Seq("TGATAG",s1.alphabet))
test_seq=Seq(sequence, s1.alphabet)

for pos, score, in s1.search_pwm(test_seq, threshold=9.72):
	print pos, score, #seq.tostring()

def rev(s) : return s[::-1]

rev_test_seq = rev(test_seq)

for pos, score, in s1.search_pwm(rev_test_seq, threshold=9.72):
	print pos, score, #seq.tostring()

endtimepam = datetime.datetime.now( )
endtime = datetime.datetime.now( )

print sequenceendtime - sequencestarttime

print endtimepam - starttimepam
print endtime - starttime
