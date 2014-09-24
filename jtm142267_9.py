#!/usr/bin/env python

##############################  TASK 1 ##########################

#########  METHOD  TO  OUTPUT  MOOD ######### 

def maximum(a):
	maxIndex = 0
	maxim = a[0]	
	for i in range(0,7):
		if a[i] > maxim :
			maxim = a[i]
			maxIndex = i
	if maxIndex == 0:
		return "Happy"
	if maxIndex == 1:
		return "Sad"
	if maxIndex == 2:
		return "Sarcastic"
	if maxIndex == 3:
		return "Surprised"
	if maxIndex == 4:
		return "Crooked"
	if maxIndex == 5:
		return "Neutral"
	if maxIndex == 6:
		return "Angry"

# Actual Task 1 Code #

file = open('/home/shobhit/Assignment_9/Assignment9/content.txt','r')

A=[0,0,0,0,0,0,0]
B=[0,0,0,0,0,0,0]
C=[0,0,0,0,0,0,0]
E=[0,0,0,0,0,0,0]
G=[0,0,0,0,0,0,0]

for line in file:
	for word in line.split():
		if line[0]=="A":
			if (word==":D") or (word==":)"):
				A[0] = A[0] + 1
			if (word == ":(") or (word == ":'("):
				A[1] = A[1] + 1
			if (word ==":P") or (word == ":p") or (word == ";)"):
				A[2] = A[2] + 1
			if (word==":-o") or (word=="O_O"):
				A[3] = A[3] + 1
			if (word=="B-)") or (word==";)"):
				A[4] = A[4] + 1
			if (word==":/") or (word=="=_="):
				A[5] = A[5] + 1
			if (word=="x-(") or (word==">_<"):
				A[6] = A[6] + 1
				
		
		if line[0] == "B":
			if (word==":)") or (word==":D"):
				B[0] = B[0] + 1
			if (word==":(") or (word==":'("):
				B[1] = B[1] + 1
			if (word==":P") or (word==":p") or (word==";)"):
				B[2] = B[2] + 1
			if (word==":-o") or (word=="O_O"):
				B[3] = B[3] + 1
			if (word=="B-)") or (word==";)"):
				B[4] = B[4] + 1
			if (word==":/") or (word=="=_="):
				B[5] = B[5] + 1
			if (word=="x-(") or (word==">_<"):
				B[6] = B[6] + 1
	
		if line[0] == "C":
			if (word==":)") or (word==":D"):
				C[0] = C[0] + 1
			if (word==":(") or (word==":'("):
				C[1] = C[1] + 1
			if (word==":P") or (word==":p") or (word==";)"):
				C[2] = C[2] + 1
			if (word==":-o") or (word=="O_O"):
				C[3] = C[3] + 1
			if (word=="B-)") or (word==";)"):
				C[4] = C[4] + 1
			if (word==":/") or (word=="=_="):
				C[5] = C[5] + 1
			if (word=="x-(") or (word==">_<"):
				C[6] = C[6] + 1
	
		if line[0] == "E":
			if (word==":)") or (word==":D"):
				E[0] = E[0] + 1
			if (word==":(") or (word==":'("):
				E[1] = E[1] + 1
			if (word==":P") or (word==":p") or (word==";)"):
				E[2] = E[2] + 1
			if (word==":-o") or (word=="O_O"):
				E[3] = E[3] + 1
			if (word=="B-)") or (word==";)"):
				E[4] = E[4] + 1
			if (word==":/") or (word=="=_="):
				E[5] = E[5] + 1
			if (word=="x-(") or (word==">_<"):
				E[6] = E[6] + 1
	
		if line[0] == "G":
			if (word==":)") or (word==":D"):
				G[0] = G[0] + 1
			if (word==":(") or (word==":'("):
				G[1] = G[1] + 1
			if (word==":P") or (word==":p") or (word==";)"):
				G[2] = G[2] + 1
			if (word==":-o") or (word=="O_O"):
				G[3] = G[3] + 1
			if (word=="B-)") or (word==";)"):
				G[4] = G[4] + 1
			if (word==":/") or (word=="=_="):
				G[5] = G[5] + 1
			if (word=="x-(") or (word==">_<"):
				G[6] = G[6] + 1
	
print "A : ",maximum(A)
print "B : ",maximum(B)
print "C : ",maximum(C)
print "E : ",maximum(E)
print "G : ",maximum(G)
file.close()


############################ TASK 2 ############################

file = open('/home/shobhit/Assignment_9/Assignment9/content.txt','r')

emoHappy = 0
emoSad = 0
emoSarcastic = 0
emoSurprised = 0
emoCrooked = 0
emoNeutral = 0
emoAngry = 0
Total = 0

for line in file:
	if " :D" in line:
		 emoHappy = emoHappy + 1
	if " :)" in line: 
		emoHappy = emoHappy + 1
	if ":'(" in line:
		 emoSad = emoSad + 1
	if ":(" in line:
		 emoSad = emoSad + 1
	if ' :P' in line: 
		emoSarcastic = emoSarcastic + 1
	if ' :p' in line:
		 emoSarcastic = emoSarcastic + 1
	if ' ;)' in line: 
		emoSarcastic = emoSarcastic + 1
		emoCrooked = emoCrooked + 1
	if ' :-o' in line: 
		emoSurprised = emoSurprised + 1
	if ' O_O' in line:
		 emoSurprised = emoSurprised + 1
	if ' B-)' in line:
		 emoCrooked = emoCrooked + 1
	if " :-/" in line: 
		emoNeutral = emoNeutral + 1
	if "=_=" in line: 
		emoNeutral = emoNeutral + 1
	if "x-(" in line: 
		emoAngry = emoAngry + 1
	if ">_<" in line:
		 emoAngry = emoAngry + 1

Total = emoHappy + emoSad + emoSarcastic + emoCrooked + emoSurprised + emoCrooked + emoNeutral + emoAngry

print "Mood_Happy :",emoHappy*100.0/Total," %"
print "Mood_Sad :",emoSad*100.0/Total," %"
print "Mood_Surprised :",emoSurprised*100.0/Total," %"
print "Mood_Sarcastic :",emoSarcastic*100.0/Total," %"
print "Mood_Crooked :",emoCrooked*100.0/Total," %"
print "Mood_Neutral :",emoNeutral*100.0/Total," %"
print "Mood_Angry :",emoAngry*100.0/Total," %"

file.close()

################################################################################################################################

## Writing in a file


f=open("/home/shobhit/Assignment_9/Assignment9/output.txt",'w')
f.write(" -----------OUTPUT FILE ----------"+"\n")
f.write("A : "+maximum(A)+"\n")
f.write("B : "+maximum(B)+"\n")
f.write("C : "+maximum(C)+"\n")
f.write("E : "+maximum(E)+"\n")
f.write("G : "+maximum(G)+"\n")
f.write("------------------------------------------------------------------------------------"+"\n")
f.write("Mood_Happy:"+str(float(emoHappy*100/Total))+"\n")
f.write("Mood_Sad:"+str(float(emoSad*100/Total))+"\n")
f.write("Mood_Sarcastic:"+str(float(emoSarcastic*100/Total))+"\n")
f.write("Mood_Surprised:"+str(float(emoSurprised*100/Total))+"\n")
f.write("Mood_Crook:"+str(float(emoCrooked*100/Total))+"\n")
f.write("Mood_Neutral:"+str(float(emoNeutral*100/Total))+"\n")
f.write("Mood_Angry:"+str(float(emoAngry*100/Total))+"\n")
f.write("---------------------------------------------------------------------------------------")
f.close()

