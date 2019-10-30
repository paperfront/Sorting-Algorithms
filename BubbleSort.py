import random
import numpy as np

def sort(list):
    n = 0
    swapPerformed = False
    while(True):
        while (n <= len(list) - 2):
            if (list[n] > list[n + 1]):
                list[n], list[n+1] = swap(list[n], list[n+1])
                swapPerformed = True
            n += 1
        if(swapPerformed == False):
            return list
        n = 0
        swapPerformed = False
        
    
    
def swap(x, y):
    temp = x
    x = y
    y = temp
    return(x, y)
    
    
def main():
    mylist = np.empty(1)
    mylist[0] = random.randint(0, 100)
    for i in range(0,100):
        mylist = np.append(mylist, random.randint(1, 100))
    print(mylist)
    mylist = sort(mylist)
    print("")
    print(mylist)
    
main()

