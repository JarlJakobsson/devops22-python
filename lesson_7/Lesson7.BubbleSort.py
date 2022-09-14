mylist = [6,8,2,4,3,9,22,41,1,0]
def swap_func(listname, pos):
    listname[pos], listname[pos+1] = listname[pos+1], listname[pos]
    return

def compare(a, b):
    return a > b

def bubblesort(mylist):
    swapped = False
    for i in range(len(mylist)-1, 0, -1):
        print(mylist)
        for j in range(i):    
            if compare(mylist[j], mylist[j+1]):
                swap_func(mylist, j)
                swapped = True
        if not swapped:
            print(mylist)
            break       
    print(mylist)
    return

bubblesort(mylist)
