import random

def getMax(list):
    maximum = 0
    for number in list:
        if(number > maximum):
            maximum = number
    return maximum

def sort(list):
    w, h = 0, 10;
    tempArray = [[0 for x in range(w)] for y in range(h)] 
    counter = -1
    mymax = getMax(list)
    maxLength = len(str(mymax))
    
    while(-counter <= maxLength):
        for number in list:
            if(len(str(number)) < -counter):
                tempArray[0].append(number)   
            else:
                tempArray[int(str(number)[counter])].append(number)
        counter -= 1
        list = []
        for lists in tempArray:
            list += lists
        tempArray = [[0 for x in range(w)] for y in range(h)] 
    print(list)
    
mylist = []
for i in range(0,100):
    mylist.append(random.randint(1,10000))
sort(mylist)