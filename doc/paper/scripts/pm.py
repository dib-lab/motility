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

sites = [ 'AGATAA',
	  'TGATAA',
	  'AGATAG' ]

print motility.make_iupac_motif(sites)

pwm = motility.make_pwm(sites)
print pwm.max_score(), pwm.min_score()

print pwm.find(sequence, 10.57)

for site in ['AGATAA', 'TGATAA', 'AGATAG']:
	print site, pwm.calc_score(site)

matrix_tuple = ((1, 0, 0, 1),
		(0, 0, 1, 0),
		(1, 0, 0, 0),
		(0, 0, 0, 1),
		(1, 0, 0, 0),
		(1, 0, 1, 0))


matrix = motility.PWM(matrix_tuple)

matrix.generate_sites_over(5)

#print matrix.find(sequence, 6.0)


endtimeiupac = datetime.datetime.now( )

endtime = datetime.datetime.now( )

print "end Motility iupac matches!"
print sequenceendtime - sequencestarttime

print endtimeiupac - starttimeiupac
print endtime - starttime

