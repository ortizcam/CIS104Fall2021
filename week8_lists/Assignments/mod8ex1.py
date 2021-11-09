list = ['x', 'y', 'z']#example list
def chop():#Defining Chop
    del list[0]#delete first item in list
    del list[-1]#delete last item in list
def middle():#Defining middle
    nl = chop() #Creating empty list
    #chop() #Running chop funciton
    #nl.append(list) #A
    print(nl)

middle()
