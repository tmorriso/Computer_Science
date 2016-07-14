# !/user/bin/python3
# Tom Morrison
# September 11, 2015
# Assignment 3
# Election Results Problem: input file using command line arguments, read in data from a election poll, format the output nicely.

import sys

resultsInfo = []

dictionary = {}
resultsFile = open(sys.argv[1],"r") 

for line in resultsFile:
	resultsInfo = line.split(" ")
	firstName = resultsInfo[0]
	lastName = resultsInfo[1]
	fullName = firstName +' '+ lastName #need a space
	#print(fullName)
	resultsInfo[2] = int(resultsInfo[2].strip())
	resultsInfo[3] = int(resultsInfo[3].strip())
	resultsInfo[4] = int(resultsInfo[4].strip())
	resultsInfo[5] = int(resultsInfo[5].strip())
	#print(resultsInfo[2])
	totalVotes = resultsInfo[2]+resultsInfo[3]+resultsInfo[4]+resultsInfo[5]
	#print(totalVotes)

	dictionary[fullName] = totalVotes
resultsFile.close()
#print(dictionary)
values = dictionary.values()
keys = dictionary.keys()
percent = 0
total = 0
winner = 0
for key in keys:
	total += dictionary[key]
	#print(dictionary[key])
#print(total)
# Insert Headers
l1 = '=========='
l2 = '====='
l3 = '======='
c = 'Candidates'
v = 'Votes'
p = 'Percent'
print(c.center(15), v.rjust(8), p.rjust(10))
print(l1.center(15), l2.rjust(8), l3.rjust(10))
for key in keys: 
	percent=(dictionary[key]/total)*100
	rndPercent=round(percent)
	print(key.center(15), str(dictionary[key]).rjust(8), str(rndPercent).rjust(8),"%")

for key in keys: 
	if dictionary[key] > winner:
		winner = dictionary[key]
		name = key
print('\nThe winner is',name, 'with', winner, 'votes!\n')
print("Total votes polled:", total)
	



