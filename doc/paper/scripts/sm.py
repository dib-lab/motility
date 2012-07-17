#!/usr/bin/env python

# Do your motility stuff.




import datetime
import motility, Bio, TAMO

from Bio import Motif

print "This works!"


starttime = datetime.datetime.now( )
sequence = ""

with open ("/u/trosko/projects/data/ecoliMG1655.fa") as indatafile:
	indatafile.readline()
	for line in indatafile:
		sequence += line.strip()
	
endtime = datetime.datetime.now( )

print endtime - starttime


print "Motility exact matches!"

starttime = datetime.datetime.now( )

print motility.find_exact(sequence, "TATAA")
print motility.find_exact(sequence, "ATATT")
print motility.find_exact(sequence, "TTATA")
print motility.find_exact(sequence, "GTTCGGCG")
print motility.find_exact(sequence, "CAAGCCGC")
print motility.find_exact(sequence, "CGCCGAAC")
print motility.find_exact(sequence, "TTTTTAAAAAAA")
print motility.find_exact(sequence, "AAAAATTTTTTT")
print motility.find_exact(sequence, "AAAAAAATTTTT")
print motility.find_exact(sequence, "TAATAATCCAACTAGTTGCATCATACAACTAATAAACGTGGTGAATCCAATTGTCGAGATTTATTTTTTA")
print motility.find_exact(sequence, "CTTCTTCGGTTGATCAACGTAGTATGTTGATTATTTGCACCACTTAGGTTAACAGCTCTAAATAAAAAAT")
print motility.find_exact(sequence, "TAAAAAATAAATCTCGACAATTGGATTCACCACGTTTATTAGTTGTATGATGCAACTAGTTGGATTATTA")

endtime = datetime.datetime.now( )
print endtime - starttime

print "end Motility exact matches!"

