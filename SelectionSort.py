import random


def sort(list):
    counter = len(list) - 1
    while(counter > 0):
        maximum = list[0]
        index = 0
        for i in range(0, counter + 1):
            if(list[i] > maximum):
                maximum = list[i]
                index = i
        temp = list[index]
        list[index] = list[counter]
        list[counter] = temp
        counter -= 1
    return(list)
    

def main():
    mylist = []
    for i in range(0, 10000):
        mylist.append(random.randint(0, 1000))
    print(sort(mylist))

main()