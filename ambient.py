#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from std_msgs.msg import Float32
from state_processor import state_process
from state_processor import processor
from action_processor import action_process

global string

def ambient() :

    #Initializing node
    rospy.init_node('ambient')

    #Subscribers
    rospy.Subscriber('status',String,callback1)


    #Publishers
    pub = rospy.Publisher('status',String,queue_size = 5)

    rate = rospy.Rate(0.5)
    rospy.spin()



    while not rospy.is_shutdown() :
        global string
        rospy.loginfo(string)
        pub.publish(string)
        rate.sleep()

def callback1(data) :

    global string
    string = data.data
    rospy.loginfo(rospy.get_caller_id() + 'Fetched status : %s',data.data)


if __name__ == '__main__':
    try:
        ambient()
    except rospy.ROSInterruptException:
        pass
