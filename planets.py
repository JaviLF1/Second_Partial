#First stepp Gather all data
#Using a for i in and .append stor the data and show it in order 
#divide the data in a specific number 
#show the results


cubicmeterslist=[]
sunvolume=1.4*10**27

print('Hi, Im supercomonproblembotsolver 2.0')
print('That is why today I will be healping you to know how many time yours favorites planets can fit in the Sun')
print('For how many planets you what to know about?')
numbplanets=input()


for i in range(0,int(numbplanets)):
  print('OK, for the planet numbre',int(i)+1,',give me its volume in cubic meters')
  cubicmeters=input()
  cubicmeterslist.append(cubicmeters)

for i in range(0,int(numbplanets)):
  result=float(sunvolume)/float(cubicmeterslist[i])
  print('The planet number',int(i)+1,'fits in the sun',result,'times')
