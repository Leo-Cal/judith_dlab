def state_process(string):
    #MUDAR PROLOG PRA FICAR COM ; ENTRE OS "ON"

#for testing purposes, uncomment line below
    #string = "on(a,b);on(b,table);on(c,table)"


#Separate the string representing the state into 3 Strings,
#each representing the state of one block (string1 -> A, string2 -> B, string3 -> C)
    i = string.find(";")
    string1 = string[:i]
    print(string1)

    string = string[i+1:]

    i = string.find(";")
    string2 = string[:i]
    print(string2)

    string3 = string[i+1:]
    print(string3)

#Process the strings to get the matricial coordinates of each block
    processor(string1,string2,string3)

    return 0


def processor(string1,string2,string3) :
    """receives 3 strings, each representing the state of one block, as especified above,
    and returns the matricial coordinates of each block"""

    #Initializing variables
    i1=i2=i3=j1=j2=j3 = 5

    #Finding which block is on the table
    i = string1.find(",")
    if string1[i+1:] == "table)" :
        j1 = 0
        i1 = 0

    i = string2.find(",")
    if string2[i+1:] == "table)" :
        j2 = 0
        i2 = 1

    i = string3.find(",")
    if string3[i+1:] == "table)" :
        j3 = 0
        i3 = 2

#---------------------------If A is not on table:----------------------------#
    if j1 != 0 :

        i = string1.find(",")
        #If A is over B:
        if string1[i+1:] == "b)" :
            #If B is on table:
            if j2 == 0:
                i1 = i2
                j1 = j2 + 1
            #If B is not on table (B is over C):
            if j2 != 0 :
                i2 = string2.find(",")
                if string2[i2+1:] == "c)" :
                    j2 = 1
                    j1 = j2 + 1
                    j3 = 0
                    i1 = i2 = i3 = 2

        #If A is over C
        if string1[i+1:] == "c)" :
            #If C is on table:
            if j3 == 0:
                i1 = i3
                j1 = j3 + 1
            #If C is not on table (C is over B):
            if j3 != 0:
                i3 = string3.find(",")
                if string3[i3+1:] == "b)" :
                    j1 = 2
                    j2 = 0
                    j3 = 1
                    i1 = i2 = i3 = 1


#--------------------------If B is not on table: ------------------------#
    if j2 != 0 :

        i = string2.find(",")
        #If B is over A:
        if string2[i+1:] == "a)" :
            #If A is on table:
            if j1 == 0:
                i2 = i1
                j2 = j1 + 1
            #If A is not on table (A is over C):
            if j1 != 0 :
                i2 = string1.find(",")
                if string1[i2+1:] == "c)" :
                    j1 = 1
                    j2 = 2
                    j3 = 0
                    i1 = i2 = i3 = 2

        #If B is over C:
        if string2[i+1:] == "c)" :
            #If C is on table:
            if j3 == 0:
                i2 = i3
                j2 = j3 + 1
            #If C is not on table (C is over A):
            if j3 != 0:
                i3 = string3.find(",")
                if string3[i3+1:] == "a)" :
                    j1 = 0
                    j2 = 2
                    j3 = 1
                    i1 = i2 = i3 = 0

#----------------------------If C is not on table:--------------------------#

    if j3 != 0 :

        i = string3.find(",")
        #If C is over A:
        if string3[i+1:] == "a)" :
            #If A is on table:
            if j1 == 0:
                i3 = i1
                j3 = j1 + 1
            #If A is not on table (A is over B):
            if j1 != 0 :
                i2 = string1.find(",")
                if string1[i2+1:] == "b)" :
                    j1 = 1
                    j2 = 0
                    j3 = 2
                    i1 = i2 = i3 = 1

        #If C is over B:
        if string3[i+1:] == "b)" :
            #If B is on table:
            if j2 == 0:
                i3 = i2
                j3 = j2 + 1
            #If B is not on table (B is over A):
            if j2 != 0:
                i3 = string2.find(",")
                if string2[i3+1:] == "a)" :
                    j1 = 0
                    j2 = 1
                    j3 = 2
                    i1 = i2 = i3 = 0




    mcoord_list = [i1, j1, i2, j2, i3, j3]
    print(i1,j1,i2,j2,i3,j3)
    return mcoord_list
