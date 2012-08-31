#!/usr/bin/env python

# Do your motility stuff.




import datetime
import motility, Bio, TAMO

from Bio import Motif

print "This works!"


sequencestarttime = datetime.datetime.now( )
sequence = ""

with open ("/u/trosko/projects/data/ecoliMG1655.fa") as indatafile:
	indatafile.readline()
	for line in indatafile:
		sequence += line.strip()
	
sequenceendtime = datetime.datetime.now( )

print "Motility exact matches!"

starttime = datetime.datetime.now( )
starttimetata = datetime.datetime.now( )

print motility.find_exact(sequence, "TATAA")
print motility.find_exact(sequence, "ATATT")
print motility.find_exact(sequence, "TTATA")
endtimetata = datetime.datetime.now( )
starttimesmall = datetime.datetime.now( )
print motility.find_exact(sequence, "GTTCGGCG")
print motility.find_exact(sequence, "CAAGCCGC")
print motility.find_exact(sequence, "CGCCGAAC")
endtimesmall = datetime.datetime.now( )
starttimemedium = datetime.datetime.now( )
print motility.find_exact(sequence, "TTTTTAAAAAAA")
print motility.find_exact(sequence, "AAAAATTTTTTT")
print motility.find_exact(sequence, "AAAAAAATTTTT")
endtimemedium = datetime.datetime.now( )
starttimelarge = datetime.datetime.now( )
print motility.find_exact(sequence, "TTACCACGATATTGGGCAGC")
print motility.find_exact(sequence, "AATGGTGCTATAACCCGTCG")
print motility.find_exact(sequence, "GCTGCCCAATATCGTGGTAA")
endtimelarge = datetime.datetime.now( )
starttimeverylarge = datetime.datetime.now( )
print motility.find_exact(sequence, "TAATAATCCAACTAGTTGCATCATACAACTAATAAACGTGGTGAATCCAATTGTCGAGATTTATTTTTTA")
print motility.find_exact(sequence, "CTTCTTCGGTTGATCAACGTAGTATGTTGATTATTTGCACCACTTAGGTTAACAGCTCTAAATAAAAAAT")
print motility.find_exact(sequence, "TAAAAAATAAATCTCGACAATTGGATTCACCACGTTTATTAGTTGTATGATGCAACTAGTTGGATTATTA")
endtimeverylarge = datetime.datetime.now( )

endtime = datetime.datetime.now( )

print "end Motility exact matches!"
print sequenceendtime - sequencestarttime

print endtimetata - starttimetata
print endtimesmall - starttimesmall
print endtimemedium - starttimemedium
print endtimelarge - starttimelarge
print endtimeverylarge - starttimeverylarge
print endtime - starttime

