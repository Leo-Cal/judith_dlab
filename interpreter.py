#!/usr/bin/env python


"""import rospy
from std_msgs.msg import String
from std_msgs import float32

def interpreter () :

   #Initializing node
    rospy.init_node('interpreter')

   #Subscribers
    rospy.Subscriber('action',String,callback1)
    rospy.Subscriber('status',String,callback2)

   #Publishers
    pub1 = rospy.Publisher('Xcoord',float32, queue_size = 5)
    pub2 = rospy.Publisher('Ycoord',float32, queue_size = 5)
    pub3 = rospy.Publisher('Zcoord',float32, queue_size = 5)
    pub4 = rospy.Publisher('status',String, queue_size = 5)

    rate = rospy.rate(1)

    while not rospy.is_shutdown() :
        pub1.publish()
        pub2.publish()
        pub3.publish()
        pub4.publish()
        rate.sleep()

   #Callbacks
def callback1(data) :

    action = data.data
    rospy.loginfo(rospy.get_caller_id() + 'Fetched action %s',data.data)

def callback2(data) :

    status = data.data
    rospy.loginfo(rospy.get_caller_id() + 'Fetched status : %s',data.data)

"""
def main():
    #MUDAR PROLOG PRA FICAR COM ; ENTRE OS "ON"

    string = "on(a,b);on(b,table);on(c,table)"


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
    process(string1,string2,string3)

    return 0


def process(string1,string2,string3) :
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





    print(i1,j1,i2,j2,i3,j3)
    return 0





main()



"""class Workspace :

     def __init__(self) :

         matriz = []
         for i in range (3) :
             for j in range (3):
                 matriz[i][j] = '.'

         self.matrix = matriz


     def __str__(self) :
         matrix = self.matrix
         string = ""
         for i in range (len(matrix)):
                 if i > 0:
                     string = string + "\n"
                     for j in range (len(self.matrix[1])):
                         string = string + matrix[i][j]
                         string = string + " "

                 return string

class Block :

     def __init__(self,block_name,i,j,workspace) :
         self.block_name = block_name
         self.block_l = 50
         self.block_h = 50
         self.space = workspace
         self.coordx = (self.block_l/2) + 80*i
         self.coordy = (self.block_h/2) + 50*j

    def __str__(self,i,j) :

        matrix = self.space.matrix
        matrix[i][j] = self.block_name
        string = ""
        for k in range (len(matrix)):
                 if k > 0:
                     string = string + "\n"
                     for p in range (len(self.matrix[1])):
                         string = string + matrix[i][j]
                         string = string + " "

                 return string
"""
