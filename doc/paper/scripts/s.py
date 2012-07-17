#!/usr/bin/env python

import datetime

starttime = datetime.datetime.now( )
sequence = ""

with open ("/u/trosko/projects/data/ecoliMG1655.fa") as indatafile:
	indatafile.readline()
	for line in indatafile:
		sequence += line.strip()
	
endtime = datetime.datetime.now( )

print endtime - starttime

print "python exact matches!"

starttime = datetime.datetime.now( )

foundlocations = []
index = 0 

while (True) : 
	index = sequence.find("TATAA",index)
	if index == -1 : break
	foundlocations.append(index)
	index+=1

print "TATAA " , foundlocations

foundlocations = []
index = 0 

while (True) : 
	index = sequence.find("AATAT",index)
	if index == -1 : break
	foundlocations.append(index)
	index+=1

print "AATAT " , foundlocations



while (True) : 
	index = sequence.find("TTATA",index)
	if index == -1 : break
	foundlocations.append(index)
	index+=1

print "TTATA " , foundlocations



while (True) : 
	index = sequence.find("ATTAA",index)
	if index == -1 : break
	foundlocations.append(index)
	index+=1

print "ATTAA " , foundlocations


foundlocations = []
index = 0 

while (True) : 
	index = sequence.find("GTTCGGCG",index)
	if index == -1 : break
	foundlocations.append(index)
	index+=1 

print "GTTCGGCG " , foundlocations

foundlocations = []
index = 0 

while (True) : 
	index = sequence.find("GCGGCTTG",index)
	if index == -1 : break
	foundlocations.append(index)
	index+=1 

print "GCGGCTTG " , foundlocations

foundlocations = []
index = 0 

while (True) : 
	index = sequence.find("CAAGCCGC",index)
	if index == -1 : break
	foundlocations.append(index)
	index+=1 

print "CAAGCCGC " , foundlocations

foundlocations = []
index = 0 

while (True) : 
	index = sequence.find("CGCCGAAC",index)
	if index == -1 : break
	foundlocations.append(index)
	index+=1 

print "CGCCGAAC " , foundlocations


foundlocations = []
index = 0 

while (True) : 
	index = sequence.find("TTTTTAAAAAAA",index)
	if index == -1 : break
	foundlocations.append(index)
	index+=1

print "TTTTTAAAAAAA " , foundlocations

foundlocations = []
index = 0 

while (True) : 
	index = sequence.find("AAAAAAATTTTT",index)
	if index == -1 : break
	foundlocations.append(index)
	index+=1

print "AAAAAAATTTTT " , foundlocations

foundlocations = []
index = 0 

while (True) : 
	index = sequence.find("AAAAATTTTTTT",index)
	if index == -1 : break
	foundlocations.append(index)
	index+=1

print "AAAAATTTTTTT " , foundlocations

foundlocations = []
index = 0 

while (True) : 
	index = sequence.find("TTTTTTTAAAAA",index)
	if index == -1 : break
	foundlocations.append(index)
	index+=1

print "TTTTTTTAAAAA " , foundlocations


foundlocations = []
index = 0 
while (True) : 
	index = sequence.find("TTACCACGATATTGGGCAGC",index)
	if index == -1 : break
	foundlocations.append(index)
	index+=1

print "TTACCACGATATTGGGCAGC " , foundlocations

foundlocations = []
index = 0 
while (True) : 
	index = sequence.find("CGACGGGTTATAGCACCATT",index)
	if index == -1 : break
	foundlocations.append(index)
	index+=1

print "CGACGGGTTATAGCACCATT " , foundlocations


foundlocations = []
index = 0 
while (True) : 
	index = sequence.find("AATGGTGCTATAACCCGTCG",index)
	if index == -1 : break
	foundlocations.append(index)
	index+=1

print "AATGGTGCTATAACCCGTCG " , foundlocations


foundlocations = []
index = 0 
while (True) : 
	index = sequence.find("GCTGCCCAATATCGTGGTAA",index)
	if index == -1 : break
	foundlocations.append(index)
	index+=1

print "GCTGCCCAATATCGTGGTAA " , foundlocations


foundlocations = []
index = 0 

while (True) : 
	index = sequence.find("TAATAATCCAACTAGTTGCATCATACAACTAATAAACGTGGTGAATCCAATTGTCGAGATTTATTTTTTA",index)
	if index == -1 : break
	foundlocations.append(index)
	index+=1

print "TAATAATCCAACTAGTTGCATCATACAACTAATAAACGTGGTGAATCCAATTGTCGAGATTTATTTTTTA " , foundlocations

foundlocations = []
index = 0 

while (True) : 
	index = sequence.find("CTTCTTCGGTTGATCAACGTAGTATGTTGATTATTTGCACCACTTAGGTTAACAGCTCTAAATAAAAAAT",index)
	if index == -1 : break
	foundlocations.append(index)
	index+=1

print "TAATAATCCAACTAGTTGCATCATACAACTAATAAACGTGGTGAATCCAATTGTCGAGATTTATTTTTTA " , foundlocations

foundlocations = []
index = 0 

while (True) : 
	index = sequence.find("ATTTTTTATTTAGAGCTGTTAACCTAAGTGGTGCAAATAATCAACATACTACGTTGATCAACCTAATAAT",index)
	if index == -1 : break
	foundlocations.append(index)
	index+=1

print "ATTTTTTATTTAGAGCTGTTAACCTAAGTGGTGCAAATAATCAACATACTACGTTGATCAACCTAATAAT " , foundlocations

foundlocations = []
index = 0 

while (True) : 
	index = sequence.find("TAAAAAATAAATCTCGACAATTGGATTCACCACGTTTATTAGTTGTATGATGCAACTAGTTGGATTATTA",index)
	if index == -1 : break
	foundlocations.append(index)
	index+=1

print "TAAAAAATAAATCTCGACAATTGGATTCACCACGTTTATTAGTTGTATGATGCAACTAGTTGGATTATTA " , foundlocations



endtime = datetime.datetime.now( )
print endtime - starttime

print "python exact matches!"

