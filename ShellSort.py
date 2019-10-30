import random

def swap(num1, num2):
    return num2, num1

def sort(list):
    swapPerformed = False
    middle = len(list) // 2
    leftMarker = 0
    rightMarker = leftMarker + middle
    while(rightMarker - leftMarker > 1 or swapPerformed == True):
        swapPerformed = False
        while(rightMarker < len(list)):
            if(list[leftMarker] > list[rightMarker]):
                list[leftMarker], list[rightMarker] = swap(list[leftMarker], list[rightMarker])
                swapPerformed = True
            rightMarker += 1
            leftMarker += 1
        if(middle > 1):
            middle -=1
            leftMarker = 0
            rightMarker = leftMarker + middle
        else:
            leftMarker = 0
            rightMarker = 1
    return list

def main():
    for j in range(1000):
        mylist = []
        for i in range(10000):
            mylist.append(random.randint(0,100000))
        mylist = sort(mylist)

    
main()