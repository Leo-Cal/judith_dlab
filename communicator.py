#!/usr/bin/env python


import rospy
from std_msgs.msg import String
from std_msgs.msg import Float32
from state_processor import state_process
from state_processor import processor
from action_processor import action_process
from state_actualizer import state_actualize

global action
global initial_state

def communicator() :

    #Initializing node
    rospy.init_node('communicator')

    #Subscribers

    rospy.Subscriber('action',String,callback1)
    rospy.Subscriber('initial_state',String,callback2)

    #Publishers

    pub1 = rospy.Publisher('x_coord',Float32,queue_size=5)
    pub2 = rospy.Publisher('y_coord',Float32,queue_size=5)
    pub3 = rospy.Publisher('z_coord',Float32,queue_size=5)

    rate = rospy.Rate(0.5)
    rospy.spin()

    i = 0 #interaction counter
    while not rospy.is_shutdown() :

        #Getting matricial coordinates from state and refreshing state
        if i == 0 :

            m_state = state_process(initial_state)

        else:

            initial_state = state

            state = state_actualize(initial_state,action)

            m_state = state_process(state)


        movement_matrix = action_process(m_state,action) #i.e. : [20,30,10]

        x_coord = movement_matrix[0]
        y_coord = movement_matrix[1]
        z_coord = movement_matrix[2]

        rospy.loginfo(x_coord)
        rospy.loginfo(y_coord)
        rospy.loginfo(z_coord)

        pub1.publish(x_coord)
        pub2.publish(y_coord)
        pub3.publish(z_coord)

        i = i + 1

        rate.sleep()


def callback1(data) :
    global action
    action = data.data


def callback2(data) :
    global initial_state
    initial_state = data.data



if __name__ == '__main__':
    try:
        communicator()
    except rospy.ROSInterruptException:
        pass
