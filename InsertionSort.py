import random

def insert(list, item):
    tempList = list    
    indexList = []
    for i in range(0, len(list)):
        indexList.append(i)
    while(len(tempList) > 1):
        middle = len(tempList) // 2        
        if(item < tempList[middle]):
            tempList = tempList[:middle]
            indexList = indexList[:middle]
        elif(item > tempList[middle]):
            indexList = indexList[middle:]
            tempList = tempList[middle:]
        else:
            list.insert(indexList[middle], item)
            return list
    if(item > tempList[0]):
        list.insert(indexList[0] + 1, item)
    else:
        list.insert(indexList[0], item)
    return(list)

def sort(list):
    sortedList = list[0:1]
    for i in range(1, len(list)):
        insert(sortedList, list[i])
    return sortedList
        
def main():
    mylist = []
    for i in range(0, 10000):
        mylist.append(random.randint(0, 10000))
    mylist = sort(mylist)
    print(mylist)
    
main()