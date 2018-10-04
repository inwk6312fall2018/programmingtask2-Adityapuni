file=open('Crime.csv')
lineA=[]	
lineB=[]
dict={}	#take crime id as key and crime name as value

def histogram(s):
	"""to check s in string"""
	d={}
	for c in s:
		d[c]=1+d.get(c,0)
	return d

"""make list of all words"""
for line in file:
	line.strip()
	for i in line.split(','):
		lineA.append(i)

"""all crime ID"""
i=16
while i<len(lineA):
	lineB.append(lineA[i])
	i+=9
dic=histogram(lineB) # dict of crime ID , and repetation of it

"""make dict of Crime Id vs Crime name"""
lineD=line(dic.keys())
for i in range(len(lineA)):
	if lineA[i] in lineD:
		dict[lineA[i]]=lineA[i+1].strip()

"""print table"""
print("{0:25s} {1:25s} {2:1s}".format('Crime type','Crime ID','Crime Count'))
for key,value in dic.items():
	if key in dict.keys():
print("{0:25} {1:25} {2:1}".format(dict[key],key,dic[key]))
