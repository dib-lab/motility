#!/usr/bin/env python

# Do your tamo stuff.


import datetime
import TAMO

from TAMO import MotifTools

print "This works!"


sequencestarttime = datetime.datetime.now( )
sequence = ""

with open ("/u/trosko/projects/data/ecoliMG1655.fa") as indatafile:
	indatafile.readline()
	for line in indatafile:
		sequence += line.strip()
	
sequenceendtime = datetime.datetime.now( )


print "tamo exact matches!"
starttime = datetime.datetime.now( )
starttimetata = datetime.datetime.now( )

ms1 = MotifTools.Motif_from_text('TATAA')
print ms1.oneletter
print ms1.scan(sequence) 
ms1r = MotifTools.Motif_from_text('AATAT')
print ms1r.oneletter
print ms1r.scan(sequence) 
ms1c = MotifTools.Motif_from_text('ATATT')
print ms1c.oneletter
print ms1c.scan(sequence) 
ms1rc = MotifTools.Motif_from_text('TTATA')
print ms1rc.oneletter
print ms1rc.scan(sequence) 

endtimetata = datetime.datetime.now( )
starttimesmall = datetime.datetime.now( )

ms2= MotifTools.Motif_from_text('GTTCGGCG')
print ms2.oneletter
print ms2.scan(sequence) 
ms2c= MotifTools.Motif_from_text('CAAGCCGC')
print ms2c.oneletter
print ms2c.scan(sequence) 
ms2r= MotifTools.Motif_from_text('GCGGCTTG')
print ms2r.oneletter
print ms2r.scan(sequence) 
ms2rc= MotifTools.Motif_from_text('CGCCGAAC')
print ms2rc.oneletter
print ms2rc.scan(sequence) 

endtimesmall = datetime.datetime.now( )
starttimemedium = datetime.datetime.now( )
ms12= MotifTools.Motif_from_text('TTTTTAAAAAAA')
print ms12.oneletter
print ms12.scan(sequence) 
ms12c= MotifTools.Motif_from_text('AAAAATTTTTTT')
print ms12c.oneletter
print ms12c.scan(sequence) 
ms12r= MotifTools.Motif_from_text('TTTTTTTAAAAA')
print ms12r.oneletter
print ms12r.scan(sequence) 
ms12rc= MotifTools.Motif_from_text('AAAAAAATTTTT')
print ms12rc.oneletter
print ms12rc.scan(sequence) 

endtimemedium = datetime.datetime.now( )
starttimelarge = datetime.datetime.now( )
ms23= MotifTools.Motif_from_text('TTACCACGATATTGGGCAGC')
print ms23.oneletter
print ms23.scan(sequence) 
ms23c= MotifTools.Motif_from_text('AATGGTGCTATAACCCGTCG')
print ms23c.oneletter
print ms23c.scan(sequence) 
ms23r= MotifTools.Motif_from_text('CGACGGGTTATAGCACCATT')
print ms23r.oneletter
print ms23r.scan(sequence) 
ms23rc= MotifTools.Motif_from_text('GCTGCCCAATATCGTGGTAA')
print ms23rc.oneletter
print ms23rc.scan(sequence) 
endtimelarge = datetime.datetime.now( )
starttimeverylarge = datetime.datetime.now( )

ms24= MotifTools.Motif_from_text('TAATAATCCAACTAGTTGCATCATACAACTAATAAACGTGGTGAATCCAATTGTCGAGATTTATTTTTTA')
print ms24.oneletter
print ms24.scan(sequence) 
ms24c= MotifTools.Motif_from_text('CTTCTTCGGTTGATCAACGTAGTATGTTGATTATTTGCACCACTTAGGTTAACAGCTCTAAATAAAAAAT')
print ms24c.oneletter
print ms24c.scan(sequence) 
ms24r= MotifTools.Motif_from_text('ATTTTTTATTTAGAGCTGTTAACCTAAGTGGTGCAAATAATCAACATACTACGTTGATCAACCTAATAAT')
print ms24r.oneletter
print ms24r.scan(sequence) 
ms24rc= MotifTools.Motif_from_text('TAAAAAATAAATCTCGACAATTGGATTCACCACGTTTATTAGTTGTATGATGCAACTAGTTGGATTATTA')
print ms24rc.oneletter
print ms24rc.scan(sequence) 
endtimeverylarge = datetime.datetime.now( )

endtime = datetime.datetime.now( )

print "end TAMO exact matches!"
print sequenceendtime - sequencestarttime

print endtimetata - starttimetata
print endtimesmall - starttimesmall
print endtimemedium - starttimemedium
print endtimelarge - starttimelarge
print endtimeverylarge - starttimeverylarge
print endtime - starttime
