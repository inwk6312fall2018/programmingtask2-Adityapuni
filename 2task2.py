def list_crimes():#crime numbers
 data = open("Crime.csv","r") # reading data from csv
 d = dict()
 line = []
 for line in data:
    line=line.strip()
    array = line.split(',')
    line.append(array[-1])  #appending data (crime name)
 for i in line: #looping list
    if(i not in d):  #checking list
      d[i]=1         # if no exists appending  
    else:
      d[i]+=1           # if  exists adding count value
 print ("{:<8} {:<25}".format('Key','Label'))# tabular format 
 for k, v in d.items():   # printing tabular format
    label= v
    print("{:<8} {:<15}".format(k, label))
       
 
list_crimes() # calling function
