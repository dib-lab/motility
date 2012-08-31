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
starttimeiupac = datetime.datetime.now( )

print motility.find_iupac(sequence, "WGATAR")
endtimeiupac = datetime.datetime.now( )

endtime = datetime.datetime.now( )

print "end Motility iupac matches!"
print sequenceendtime - sequencestarttime

print endtimeiupac - starttimeiupac
print endtime - starttime

