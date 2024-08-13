n =[[False,True,True,True,False],  #[0,1,1,1,0],
    [True,True,True,True,False],   #[1,1,1,1,0],
    [False,True,False,True,True],  #[0,1,0,1,1],
    [False,False,True,True,False], #[0,0,1,1,0],
    [False,True,True,True,False]]  #[0,1,1,1,0]]

nSoulucionV = list()
nSoulucionH = list()

counter = 0

for i in range(len(n)):
    tempList = []
    for j in n[i]:
        if j:
            counter += 1
        elif (counter):
            tempList.append(counter)
            counter = 0
    if (counter):
        tempList.append(counter)
        counter = 0
    
    nSoulucionV.append(tempList)


for i in range(len(n[0])):
    tempList = []
    for j in n[i]:
        if j:
            counter += 1
        elif (counter):
            tempList.append(counter)
            counter = 0
    if (counter):
        tempList.append(counter)
        counter = 0
    
    nSoulucionH.append(tempList)


print(nSoulucionV)
print(nSoulucionH)