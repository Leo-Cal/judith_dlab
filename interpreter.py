#!/usr/bin/env python


import rospy
from std_msgs.msg import String
from std_msgs.msg import Float32
from state_processor import state_process
from state_processor import processor
from action_processor import action_process

mcoord_list = []
matrix = []

def interpreter () :

   #Initializing node
    rospy.init_node('interpreter')

   #Subscribers
    rospy.Subscriber('status',String,callback2)
    rospy.Subscriber('action',String,callback1)

   #Publishers
    pub1 = rospy.Publisher('Xcoord',float32, queue_size = 5)
    pub2 = rospy.Publisher('Ycoord',float32, queue_size = 5)
    pub3 = rospy.Publisher('Zcoord',float32, queue_size = 5)
    #pub4 = rospy.Publisher('status',String, queue_size = 5)

    rate = rospy.rate(1)

    while not rospy.is_shutdown() :
        pub1.publish()
        pub2.publish()
        pub3.publish()
        #pub4.publish()
        rate.sleep()

   #Callbacks
def callback1(data) :

    action = data.data
    rospy.loginfo(rospy.get_caller_id() + 'Fetched action %s',data.data)

    i1 = mcoord_list[0]
    j1 = mcoord_list[1]
    i2 = mcoord_list[2]
    j2 = mcoord_list[3]
    i3 = mcoord_list[4]
    j3 = mcoord_list[5]

    global matrix

    matrix = action_process(i1,j1,i2,j2,i3,j3,action)


def callback2(data) :

    status = data.data
    rospy.loginfo(rospy.get_caller_id() + 'Fetched status : %s',data.data)

    global mcoord_list

    mcoord_list = state_process(status)





"""
class Workspace :

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
