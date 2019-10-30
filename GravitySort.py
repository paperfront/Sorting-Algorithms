import random

def getMax(list):
    maximum = 0
    for number in list:
        if(number > maximum):
            maximum = number
    return maximum

def sort(list):
    maximum = getMax(list)
    ogLength = len(list)
    storage = [0] * maximum
    for i in list:
        counter = 0
        while(counter < i):
            storage[counter] += 1
            counter += 1
    list = []
    while(storage[0] != 0):
        counter2 = 0
        for k in range(0, len(storage)):
            if(storage[k] != 0):
                storage[k] -= 1
                counter2 += 1
            else:
                break
        list.append(counter2)
     
    while(len(list) < ogLength):
        list.append(0)
    return list
        
mylist = []
for i in range(100):
    mylist.append(random.randint(0,100000))
print("Unsorted List:")
print(mylist)
mylist = sort(mylist)
mylist.reverse()
print("Sorted List:")
print(mylist)
        