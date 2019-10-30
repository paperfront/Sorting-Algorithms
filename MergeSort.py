import random

def merge(list1, list2):
    sortedMerge = []
    leftCounter = 0
    rightCounter = 0
    while(leftCounter < len(list1) and rightCounter < len(list2)):
        if(list1[leftCounter] <= list2[rightCounter]):
            sortedMerge.append(list1[leftCounter])
            leftCounter += 1
        else:
            sortedMerge.append(list2[rightCounter])
            rightCounter += 1
    while(leftCounter < len(list1)):
        sortedMerge.append(list1[leftCounter])
        leftCounter += 1
    while(rightCounter < len(list2)):
        sortedMerge.append(list2[rightCounter])
        rightCounter += 1
    return sortedMerge        

def sort(list):
    if(len(list) > 2):
        middle = len(list) // 2
        leftList = list[0:middle]
        rightList = list[middle:len(list)]
        leftList = sort(leftList)
        rightList = sort(rightList)
        finalList = merge(leftList, rightList)
        return finalList
    elif(len(list) == 2):
        if(list[0] > list[1]):
            temp = list[1]
            list[1] = list[0]
            list[0] = temp
            return list
        else:
            return list
    else:
        return list

def main():
    myboi = []
    for i in range(0, 1000):
        myboi.append(random.randint(1, 10000))
    print(sort(myboi))

    
main()