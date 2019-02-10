import sys
import time
import json
import math
import numpy as np

##usage: python steffenv4.py <total rows> <first class rows> <economy rows> <family/special needs rows> <general rows> <baggage loading factor>

numrows = int(sys.argv[1])
numfirst = int(sys.argv[2])
numpriority = float(sys.argv[3])
bagfactor = float(sys.argv[4])


##calculate priority rows needed
numfam = int(math.ceil(numpriority/6.0))


##currently 2 class config

econrows = numrows - numfirst
generalrows = econrows-numfam


bagrows = int(bagfactor*generalrows)


print ("total number of rows is " + str(numrows))
print ("number of first class rows is " + str(numfirst))
print ("number of economy rows is " + str(econrows))
print ("number of family/disabled/special rows is " + str(numfam))
print ("number of general economy rows is " + str(generalrows))
print ("number of rows with bags is " + str(bagrows))

step = generalrows-bagrows

nobaggedrows = np.linspace(numfirst+numfam+1,numrows-1,step, dtype = int).tolist()

print(nobaggedrows)



groupz = []
groupfirst = []
group0 = []
group1 = []
group2 = []
group3 = []
group4 = []
group5 = []
group6 = []
group7 = []
group8 = []
group9 = []
group10 = []
group11 = []
group12 = []
bagged = []
nobagged = []
seatstatus = []


for i in range (1,numfirst+1):
    groupfirst.append(str(i) +':'+ 'A')
    bagged.append(str(i) +':'+ 'A')
    seat = {"id" : str(i) +':'+ 'A', "status": "free", "type": "window"}
    seatstatus.append(seat)
    
    groupfirst.append(str(i) +':'+ 'B')
    bagged.append(str(i) +':'+ 'B')
    seat = {"id" : str(i) +':'+ 'B', "status": "free", "type": "aisle"}
    seatstatus.append(seat)
    
    groupfirst.append(str(i) +':'+ 'E')
    bagged.append(str(i) +':'+ 'E')
    seat = {"id" : str(i) +':'+ 'E', "status": "free", "type": "aisle"}
    seatstatus.append(seat)
    
    groupfirst.append(str(i) +':'+ 'F')
    bagged.append(str(i) +':'+ 'F')
    seat = {"id" : str(i) +':'+ 'F', "status": "free", "type": "window"}
    seatstatus.append(seat)


for i in range (1,numfam+1):
    group0.append(str(i+numfirst) +':'+ 'A')
    bagged.append(str(i+numfirst) +':'+ 'A')
    seat = {"id" : str(i+numfirst) +':'+ 'A', "status": "free", "type": "window"}
    seatstatus.append(seat)
    
    group0.append(str(i+numfirst) +':'+ 'B')
    bagged.append(str(i+numfirst) +':'+ 'B')
    seat = {"id" : str(i+numfirst) +':'+ 'B', "status": "free", "type": "middle"}
    seatstatus.append(seat)
    group0.append(str(i+numfirst) +':'+ 'C')
    bagged.append(str(i+numfirst) +':'+ 'C')
    seat = {"id" : str(i+numfirst) +':'+ 'C', "status": "free", "type": "aisle"}
    seatstatus.append(seat)

    group0.append(str(i+numfirst) +':'+ 'F')
    bagged.append(str(i+numfirst) +':'+ 'F')
    seat = {"id" : str(i+numfirst) +':'+ 'F', "status": "free", "type": "window"}
    seatstatus.append(seat)
    group0.append(str(i+numfirst) +':'+ 'E')
    bagged.append(str(i+numfirst) +':'+ 'E')
    seat = {"id" : str(i+numfirst) +':'+ 'E', "status": "free", "type": "middle"}
    seatstatus.append(seat)
    group0.append(str(i+numfirst) +':'+ 'D')
    bagged.append(str(i+numfirst) +':'+ 'D')
    seat = {"id" : str(i+numfirst) +':'+ 'D', "status": "free", "type": "aisle"}
    seatstatus.append(seat)



for i in range (1,numrows+1-numfirst-numfam):

    if (i+numfirst+numfam) in nobaggedrows:
        print("no bags")
        print (str(i+numfirst+numfam))
        nobagged.append(str(i+numfirst+numfam) +':'+ 'A')
        seat = {"id" : str(i+numfirst+numfam) +':'+ 'A', "status": "free", "type": "window"}
        seatstatus.append(seat)

        nobagged.append(str(i+numfirst+numfam) +':'+ 'B')
        seat = {"id" : str(i+numfirst+numfam) +':'+ 'B', "status": "free", "type": "middle"}
        seatstatus.append(seat)
        
        nobagged.append(str(i+numfirst+numfam) +':'+ 'C')
        seat = {"id" : str(i+numfirst+numfam) +':'+ 'C', "status": "free", "type": "aisle"}
        seatstatus.append(seat)
        nobagged.append(str(i+numfirst+numfam) +':'+ 'F')
        seat = {"id" : str(i+numfirst+numfam) +':'+ 'F', "status": "free", "type": "window"}
        seatstatus.append(seat)
        nobagged.append(str(i+numfirst+numfam) +':'+ 'E')
        seat = {"id" : str(i+numfirst+numfam) +':'+ 'E', "status": "free", "type": "middle"}
        seatstatus.append(seat)
        nobagged.append(str(i+numfirst+numfam) +':'+ 'D')
        seat = {"id" : str(i+numfirst+numfam) +':'+ 'D', "status": "free", "type": "aisle"}
        seatstatus.append(seat)
    else:
        bagged.append(str(i+numfirst+numfam) +':'+ 'A')
        seat = {"id" : str(i+numfirst+numfam) +':'+ 'A', "status": "free", "type": "window"}
        seatstatus.append(seat)
        bagged.append(str(i+numfirst+numfam) +':'+ 'B')
        seat = {"id" : str(i+numfirst+numfam) +':'+ 'B', "status": "free", "type": "middle"}
        seatstatus.append(seat)
                
        bagged.append(str(i+numfirst+numfam) +':'+ 'C')
        seat = {"id" : str(i+numfirst+numfam) +':'+ 'C', "status": "free", "type": "aisle"}
        seatstatus.append(seat)
        bagged.append(str(i+numfirst+numfam) +':'+ 'F')
        seat = {"id" : str(i+numfirst+numfam) +':'+ 'F', "status": "free", "type": "window"}
        seatstatus.append(seat)
        bagged.append(str(i+numfirst+numfam) +':'+ 'E')
        seat = {"id" : str(i+numfirst+numfam) +':'+ 'E', "status": "free", "type": "middle"}
        seatstatus.append(seat)
        bagged.append(str(i+numfirst+numfam) +':'+ 'D')
        seat = {"id" : str(i+numfirst+numfam) +':'+ 'D', "status": "free", "type": "aisle"}
        seatstatus.append(seat)
    
    if i%2 == 1:
        group1.append(str(i+numfirst+numfam) +':'+ 'A')
        seat = {"id" : str(i+numfirst+numfam) +':'+ 'A', "status": "free", "type": "window"}
        seatstatus.append(seat)
        group5.append(str(i+numfirst+numfam) +':'+ 'B')
        seat = {"id" : str(i+numfirst+numfam) +':'+ 'B', "status": "free", "type": "middle"}
        seatstatus.append(seat)
        group9.append(str(i+numfirst+numfam) +':'+ 'C')
        seat = {"id" : str(i+numfirst+numfam) +':'+ 'C', "status": "free", "type": "aisle"}
        seatstatus.append(seat)

        group2.append(str(i+numfirst+numfam) +':'+ 'F')
        seat = {"id" : str(i+numfirst+numfam) +':'+ 'F', "status": "free", "type": "window"}
        seatstatus.append(seat)
        group6.append(str(i+numfirst+numfam) +':'+ 'E')
        seat = {"id" : str(i+numfirst+numfam) +':'+ 'E', "status": "free", "type": "middle"}
        seatstatus.append(seat)
        group10.append(str(i+numfirst+numfam) +':'+ 'D')
        seat = {"id" : str(i+numfirst+numfam) +':'+ 'D', "status": "free", "type": "aisle"}
        seatstatus.append(seat)
    else:
        group3.append(str(i+numfirst+numfam) +':'+ 'A')
        seat = {"id" : str(i+numfirst+numfam) +':'+ 'A', "status": "free", "type": "window"}
        seatstatus.append(seat)
        group7.append(str(i+numfirst+numfam) +':'+ 'B')
        seat = {"id" : str(i+numfirst+numfam) +':'+ 'B', "status": "free", "type": "middle"}
        seatstatus.append(seat)
        group11.append(str(i+numfirst+numfam) +':'+ 'C')
        seat = {"id" : str(i+numfirst+numfam) +':'+ 'C', "status": "free", "type": "aisle"}
        seatstatus.append(seat)

        group4.append(str(i+numfirst+numfam) +':'+ 'F')
        seat = {"id" : str(i+numfirst+numfam) +':'+ 'F', "status": "free", "type": "window"}
        seatstatus.append(seat)
        group8.append(str(i+numfirst+numfam) +':'+ 'E')
        seat = {"id" : str(i+numfirst+numfam) + 'E', "status": "free", "type": "middle"}
        seatstatus.append(seat)
        group12.append(str(i+numfirst+numfam) +':'+ 'D')
        seat = {"id" : str(i+numfirst+numfam) +':'+ 'D', "status": "free", "type": "aisle"}
        seatstatus.append(seat)

groupz.append(groupfirst)
groupz.append(group0)
groupz.append(group1)
groupz.append(group2)
groupz.append(group3)
groupz.append(group4)
groupz.append(group5)
groupz.append(group6)
groupz.append(group7)
groupz.append(group8)
groupz.append(group9)
groupz.append(group10)
groupz.append(group11)
groupz.append(group12)
groupz.append(bagged)
groupz.append(nobagged)



gnames = ['groupfirst','group0','group1','group2','group3','group4','group5','group6','group7','group8','group9','group10','group11','group12','bagged', 'nobagged']

groups = dict(zip(gnames,groupz))

##print (groups)

groupsjson = json.dumps(groups)

##print (groupsjson)


with open("boarding_groups.json","w") as f:
  f.write(groupsjson)

print (seatstatus)

seatstatusjson = json.dumps(seatstatus)

with open("seat_status.json","w") as f:
  f.write(seatstatusjson)


