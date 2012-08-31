#!/usr/bin/env python

# Do your tamo stuff.


import datetime
import TAMO
import motility

from TAMO import MotifTools

print "This works!"


sequencestarttime = datetime.datetime.now( )
sequence = ""

with open ("/u/trosko/projects/data/ecoliMG1655.fa") as indatafile:
	indatafile.readline()
	for line in indatafile:
		sequence += line.strip()
	
sequenceendtime = datetime.datetime.now( )


print "tamo IUPAC matches!"
starttime = datetime.datetime.now( )
starttimeiupac = datetime.datetime.now( )

ms1 = MotifTools.Motif_from_text('WGATAR')
print ms1.oneletter
#print ms1.scan(sequence) 
print ms1.maxscore, ms1.maxscore *0.8

print ms1.bestscan(sequence) 
pamlist =  ms1.bestseqs(9.72) 

print "Howdy"
#
if pamlist :
	pammember = pamlist.pop()

sites = ['XXXXXXXXXX', 'XXXXXXXXXX', 'XXXXXXXXXX', 'XXXXXXXXXX' ]

i = 0
while pammember :
	foundseq = pammember[1]
	sites[i] = foundseq 
	i = i + 1
	print foundseq  
	if pamlist:
		pammember = pamlist.pop()
	else:
		pammember = []


Iupaqseq = motility.make_iupac_motif(sites)
print Iupaqseq 

tqs = MotifTools.Motif_from_text(Iupaqseq)
print tqs.oneletter
print tqs.scan(sequence) 

def rev(s) : return s[::-1]

Iupaqseq = rev(Iupaqseq)
print Iupaqseq

tqs2 = MotifTools.Motif_from_text(Iupaqseq)
print tqs2.oneletter
print tqs2.scan(sequence) 

endtimeiupac = datetime.datetime.now( )

endtime = datetime.datetime.now( )

print "end TAMO PAM  matches!"
print sequenceendtime - sequencestarttime

print endtimeiupac - starttimeiupac
print endtime - starttime
