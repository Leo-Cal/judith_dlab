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
    pub1 = rospy.Publisher('Xcoord',Float32, queue_size = 5)
    pub2 = rospy.Publisher('Ycoord',Float32, queue_size = 5)
    pub3 = rospy.Publisher('Zcoord',Float32, queue_size = 5)
    #pub4 = rospy.Publisher('status',String, queue_size = 5)

    rate = rospy.Rate(0.5)

    while not rospy.is_shutdown() :

        global matrix

        matrix = callback1(data)
        x = matrix[1][0][0]
        y = matrix[1][0][1]
        z = matrix[1][0][2]

        #print(matrix[0])
        


        rospy.loginfo(x)
        rospy.loginfo(y)
        rospy.loginfo(z)

        pub1.publish(x)
        pub2.publish(y)
        pub3.publish(z)
        #pub4.publish()
        rate.sleep()

   #Callbacks
def callback1(data) :

    action = data.data
    rospy.loginfo(rospy.get_caller_id() + 'Fetched action %s',data.data)

    #initialize matricial coordinates from list imported from state_process
    i1 = mcoord_list[0]
    j1 = mcoord_list[1]
    i2 = mcoord_list[2]
    j2 = mcoord_list[3]
    i3 = mcoord_list[4]
    j3 = mcoord_list[5]

    global matrix

    #use matricial coordinates and action received from topic and process action
    matrix = action_process(i1,j1,i2,j2,i3,j3,action)  #matrix[1][0] is the position to grab or let go the block

    return matrix

def callback2(data) :

    status = data.data
    rospy.loginfo(rospy.get_caller_id() + 'Fetched status : %s',data.data)

    global mcoord_list

    mcoord_list = state_process(status)

if __name__ == '__main__':
    try:
        interpreter()
    except rospy.ROSInterruptException:
        pass
