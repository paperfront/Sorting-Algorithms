import random

def sort(list):
    if(len(list) > 1):        
        pivot = random.randint(0, len(list) - 1)
        pivotValue = list[pivot]
        list.pop(pivot)
        leftCounter = 0
        rightCounter = len(list) - 1
        while(leftCounter < rightCounter):
            while(list[leftCounter] < pivotValue and leftCounter < rightCounter):
                leftCounter += 1
            while(list[rightCounter] > pivotValue and rightCounter > leftCounter):
                rightCounter -= 1
            if(list[leftCounter] == list[rightCounter] and leftCounter != rightCounter):
                leftCounter += 1
                rightCounter -= 1
            elif(leftCounter < rightCounter ):
                temp = list[leftCounter]
                list[leftCounter] = list[rightCounter]
                list[rightCounter] = temp


        if(list[rightCounter] > pivotValue):    
            leftList, rightList = sort(list[:rightCounter]), sort(list[rightCounter:]) 
        else:
            leftList, rightList = sort(list[:rightCounter + 1]), sort(list[rightCounter + 1:])
        list = leftList
        list.append(pivotValue)
        list += rightList
        return list
    else:
        return list
    
def main():
    mylist = []
    for i in range(100000):
        mylist.append(random.randint(0,1000000))
    print("Unsorted List:")
    print(mylist)
    mylist = sort(mylist)
    print("Sorted List:")
    print(mylist)


main()