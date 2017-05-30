from __future__ import division, print_function
import numpy as np 
import matplotlib.pyplot as plt
import math as math
from random import random, seed

########### Function Definitions ###########
def PlateAppearence(Player,Bases):
	spinnerarray = np.empty([len(Player[2:10])],float)
	scorechange = 0
	outchange = 0
	hitchange = 0
	B1del, B2del, B3del, HRdel,BBdel,HBPdel,Kdel,FOPGOdel=0,0,0,0,0,0,0,0
	for i in range(len(Player[2:10])):
		if i==0:
			spinnerarray[i]=Player[i+2]
		else:
			spinnerarray[i]=spinnerarray[i-1]+Player[i+2]
	event = random()
	while event<=spinnerarray[0]:
		hitchange += 1
		B1del = 1 
		if Bases==[0,0,0,0]:
			Bases = [1,0,0,0]
			break
		if Bases==[1,0,0,0]:
			Bases = [1,1,0,0]
			break
		if Bases==[0,1,0,0]:
			Bases = [1,0,1,0]
			break
		if Bases==[0,0,1,0]:
			Bases = [1,0,0,0]
			scorechange+=1
			break
		if Bases==[1,1,0,0]:
			Bases = [1,1,1,0]
			break
		if Bases==[1,0,1,0]:
			Bases = [1,1,0,0]
			scorechange+=1
			break
		if Bases==[0,1,1,0]:
			Bases = [1,0,1,0]
			scorechange+=1
			break
		if Bases==[1,1,1,0]:
			Bases = [1,1,1,0]
			scorechange+=1
			break
	while event>spinnerarray[0] and event<=spinnerarray[1]:
		hitchange += 1
		B2del = 1
		if Bases==[0,0,0,0]:
			Bases = [0,1,0,0]
			break
		if Bases==[1,0,0,0]:
			Bases = [0,1,1,0]
			break
		if Bases==[0,1,0,0]:
			Bases = [0,1,0,0]
			scorechange+=1
			break
		if Bases==[0,0,1,0]:
			Bases = [0,1,0,0]
			scorechange+=1
			break
		if Bases==[1,1,0,0]:
			Bases = [0,1,1,0]
			scorechange+=1
			break
		if Bases==[1,0,1,0]:
			Bases = [0,1,1,0]
			scorechange+=1
			break
		if Bases==[0,1,1,0]:
			Bases = [0,1,0,0]
			scorechange+=2
			break
		if Bases==[1,1,1,0]:
			Bases = [0,1,1,0]
			scorechange+=2
			break
	while event>spinnerarray[1] and event<=spinnerarray[2]:
		hitchange += 1
		B3del = 1
		if Bases==[0,0,0,0]:
			Bases = [0,0,1,0]
			break
		if Bases==[1,0,0,0]:
			Bases = [0,0,1,0]
			scorechange+=1
			break
		if Bases==[0,1,0,0]:
			Bases = [0,0,1,0]
			scorechange+=1
			break
		if Bases==[0,0,1,0]:
			Bases = [0,0,1,0]
			scorechange+=1
			break
		if Bases==[1,1,0,0]:
			Bases = [0,0,1,0]
			scorechange+=2
			break
		if Bases==[1,0,1,0]:
			Bases = [0,0,1,0]
			scorechange+=2
			break
		if Bases==[0,1,1,0]:
			Bases = [0,0,1,0]
			scorechange+=2
			break
		if Bases==[1,1,1,0]:
			Bases = [0,0,1,0]
			scorechange+=3
			break
	while event>spinnerarray[2] and event<=spinnerarray[3]:
		hitchange += 1
		HRdel = 1
		if Bases==[0,0,0,0]:
			Bases = [0,0,0,0]
			scorechange+=1
			break
		if Bases==[1,0,0,0]:
			Bases = [0,0,0,0]
			scorechange+=2
			break
		if Bases==[0,1,0,0]:
			Bases = [0,0,0,0]
			scorechange+=2
			break
		if Bases==[0,0,1,0]:
			Bases = [0,0,0,0]
			scorechange+=2
			break
		if Bases==[1,1,0,0]:
			Bases = [0,0,0,0]
			scorechange+=3
			break
		if Bases==[1,0,1,0]:
			Bases = [0,0,0,0]
			scorechange+=3
			break
		if Bases==[0,1,1,0]:
			Bases = [0,0,0,0]
			scorechange+=3
			break
		if Bases==[1,1,1,0]:
			Bases = [0,0,0,0]
			scorechange+=4
			break
	while event>spinnerarray[3] and event<=spinnerarray[4]:
		BBdel = 1
		if Bases==[0,0,0,0]:
			Bases = [1,0,0,0]
			break
		if Bases==[1,0,0,0]:
			Bases = [1,1,0,0]
			break
		if Bases==[0,1,0,0]:
			Bases = [1,1,0,0]
			break
		if Bases==[0,0,1,0]:
			Bases = [1,0,1,0]
			break
		if Bases==[1,1,0,0]:
			Bases = [1,1,1,0]
			break
		if Bases==[1,0,1,0]:
			Bases = [1,1,1,0]
			break
		if Bases==[0,1,1,0]:
			Bases = [1,1,1,0]
			break
		if Bases==[1,1,1,0]:
			Bases = [1,1,1,0]
			scorechange+=1
			break
	if event>spinnerarray[4] and event<=spinnerarray[5]:
		HBPdel = 1
		if Bases==[0,0,0,0]:
			Bases = [1,0,0,0]
		if Bases==[1,0,0,0]:
			Bases = [1,1,0,0]
		if Bases==[0,1,0,0]:
			Bases = [1,1,0,0]
		if Bases==[0,0,1,0]:
			Bases = [1,0,1,0]
		if Bases==[1,1,0,0]:
			Bases = [1,1,1,0]
		if Bases==[1,0,1,0]:
			Bases = [1,1,1,0]
		if Bases==[0,1,1,0]:
			Bases = [1,1,1,0]
		if Bases==[1,1,1,0]:
			Bases = [1,1,1,0]
			scorechange+=1
	if event>spinnerarray[5] and event<=spinnerarray[6]:
		Bases = Bases
		Kdel = 1
		outchange+=1
	if event>spinnerarray[6] and event<=spinnerarray[7]:
		Bases = Bases
		FOPGOdel = 1
		outchange+=1
	return Bases, outchange, scorechange, hitchange,B1del, B2del, B3del, HRdel,BBdel,HBPdel,Kdel,FOPGOdel


def CheckWin(Inning,AwayRuns,HomeRuns):
	if Inning<9.6 and Inning>9.4 and HomeRuns>AwayRuns:
		return True
	elif Inning<10.1 and Inning>9.9 and HomeRuns<AwayRuns:
		return True
	elif Inning<10.1 and Inning>9.9 and HomeRuns>AwayRuns:
		return True
	else:
		return False

def ExtrasCheckWin(InningNumCounter,AwayRuns,HomeRuns):
	if InningNumCounter<18:
		return False
	if InningNumCounter%2==0 and HomeRuns>AwayRuns:
		return True
	elif InningNumCounter%2==1 and HomeRuns>AwayRuns:
		return True
	elif InningNumCounter%2==1 and AwayRuns>HomeRuns:
		return True
	else:
		return False
		






#############################################



######### PLAYERS ######################
Away = np.empty([9,11],float)
Home = np.empty([9,11],float)

for i in range(9):
	Away[i,0]=i+1
	Home[i,0]=i+1

Home[:,1] = [3,8,24,41,28,9,4,34,1]
Away[:,1] = [41,22,12,20,26,7,8,4,30]

Away[0,2:10] = [83,31,3,34,99,2,99,332]
Away[1,2:10] = [100,41,4,23,60,6,146,296]
Away[2,2:10] = [134,30,3,15,57,5,88,334]
Away[3,2:10] = [76,23,2,12,33,5,106,235]
Away[4,2:10] = [76,22,1,34,78,5,194,230]
Away[5,2:10] = [21,11,1,9,9,2,69,140]
Away[6,2:10] = [72,25,5,8,23,3,70,205]
Away[7,2:10] = [33,9,0,7,15,3,49,140]
Away[8,2:10] = [58,18,5,14,36,4,112,114]
for i in range(len(Away[:,0])):
	Away[i,10] = np.sum(Away[i,2:10])

Home[0,2:10] = [117,29,4,28,45,13,115,325]
Home[1,2:10] = [79,28,2,31,50,4,179,251]
Home[2,2:10] = [118,31,1,38,75,4,116,291]
Home[3,2:10] = [111,22,0,27,50,4,90,303]
Home[4,2:10] = [82,35,2,22,49,3,128,191]
Home[5,2:10] = [70,25,44,18,28,3,111,183]
Home[6,2:10] = [87,14,5,4,36,3,69,170]
Home[7,2:10] = [54,9,1,12,23,2,109,159]
Home[8,2:10] = [89,26,0,4,28,8,50,298]
for i in range(len(Home[:,0])):
	Home[i,10] = np.sum(Home[i,2:10])

Homeprobs = np.empty([9,10],float)
Awayprobs = np.empty([9,10],float)

Homeprobs[:,0:2] = Home[:,0:2]
Awayprobs[:,0:2] = Away[:,0:2]
for i in range(len(Home[:,0])):
	Homeprobs[i,2:10] = Home[i,2:10]/Home[i,10]
	Awayprobs[i,2:10] = Away[i,2:10]/Away[i,10]
###########################################

'''
###### CHECK CASE TEAMS #######
###############################

Awayprobs = np.empty([9,10])
Homeprobs = np.empty([9,10])

for i in range(9):
	Awayprobs[i,:] = np.array([i+1,i+1,0.2,0.2,0.1,0.1,0.1,0.1,0.1,0.1],float)
	Homeprobs[i,:] = np.array([i+1,i+1,0.2,0.2,0.1,0.1,0.1,0.1,0.1,0.1],float)
################################
'''




##### SIMULATION HAPPENS HERE #####
###################################
### RANDOM SEED FOR DEBUGGING #####
###    USE WITH CAUTION       #####
#seed(10)
###################################

HomeWin = 0
AwayWin = 0
TieGames = 0

for i in range(1000):
	GameDone = False
	Inning = 1 
	InningNumCounter = 0
	BoxScore = np.empty([2,11])
	HomeScore = 0
	AwayScore = 0
	HomeHits = 0
	AwayHits = 0
	BBCounter = 0
	HBPCounter = 0
	SingleCounter = 0
	DoubleCounter = 0
	TripleCounter = 0 
	HRCounter = 0
	KCounter = 0
	FOPGOCounter = 0
	while GameDone==False:
		HomeInningRuns = 0
		AwayInningRuns = 0

		TopOuts = 0
		Bases = [0,0,0,0]
		battercounter = 0
		while TopOuts < 3:
			BatterNum = battercounter%9
			Bases,outchange,scorechange,hitchange, B1del, B2del, B3del, HRdel,BBdel,HBPdel,Kdel,FOPGOdel = PlateAppearence(Awayprobs[BatterNum,:],Bases)
			AwayScore += scorechange
			AwayInningRuns += scorechange
			TopOuts += outchange
			AwayHits += hitchange
			battercounter += 1
			SingleCounter += B1del
			DoubleCounter += B2del
			TripleCounter += B3del
			HRCounter += HRdel
			BBCounter += BBdel
			HBPCounter += HBPdel
			KCounter += Kdel
			FOPGOCounter += FOPGOdel
		if InningNumCounter<= 16:
			BoxScore[0,Inning-1] = AwayInningRuns
		BoxScore[0,9] = AwayScore
		BoxScore[0,10] = AwayHits
		Inning += 0.5
		InningNumCounter += 1
		if Inning<9.6 and Inning>9.4 and BoxScore[0,9]<BoxScore[1,9]:
			GameDone = True
			HomeWin += 1
			break
		if InningNumCounter>16 and BoxScore[0,9]<BoxScore[1,9]:
			GameDone = True
			HomeWin += 1 
			break
		BottomOuts = 0
		Bases = [0,0,0,0]
		battercounter = 0
		while BottomOuts < 3:
			BatterNum = battercounter%9
			Bases,outchange,scorechange, hitchange, B1del, B2del, B3del, HRdel,BBdel,HBPdel,Kdel,FOPGOdel = PlateAppearence(Homeprobs[BatterNum,:],Bases)
			HomeScore += scorechange
			HomeInningRuns += scorechange
			BottomOuts += outchange
			HomeHits += hitchange
			battercounter += 1
			SingleCounter += B1del
			DoubleCounter += B2del
			TripleCounter += B3del
			HRCounter += HRdel
			BBCounter += BBdel
			HBPCounter += HBPdel
			KCounter += Kdel
			FOPGOCounter += FOPGOdel
		if InningNumCounter<=17:
			BoxScore[1,Inning-1] = HomeInningRuns
		BoxScore[1,9] = HomeScore
		BoxScore[1,10] = HomeHits
		Inning += 0.5
		InningNumCounter += 1
		if InningNumCounter>=17 and BoxScore[0,9]<BoxScore[1,9]:
			GameDone = True
			HomeWin += 1
			break
		if InningNumCounter>=17 and BoxScore[0,9]>BoxScore[1,9]:
			GameDone = True
			AwayWin += 1
			break
	#print("1B",' ','2B', ' ', '3B', ' ', 'HR', ' ', 'BB', ' ', 'HBP',' ', 'K',' ', 'FOPGO')
	#print(SingleCounter,' ',DoubleCounter,'  ',TripleCounter,'  ',HRCounter,'  ',BBCounter,'  ',HBPCounter,'  ',KCounter,'  ',FOPGOCounter)
	#print(BoxScore)
	#print(AwayWin, HomeWin,InningNumCounter)

	
print("Number of Away Wins",AwayWin,"    ","Number of Home Wins",HomeWin)
########################################
####### SIMULATION ENDS HERE ###########























