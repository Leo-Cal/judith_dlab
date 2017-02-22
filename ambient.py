#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from std_msgs.msg import Float32
from state_processor import state_process
from state_processor import processor
from action_processor import action_process


def ambient() :

    #Initializing node
    rospy.init_node('ambient')

    pub = rospy.Publisher('status',String,queue_size = 5)

    rate = rospy.Rate(0.5)

    while not rospy.is_shutdown() :

        string = "on(a,table);on(b,table);on(c,table)"
        rospy.loginfo(string)
        pub.publish(string)
        rate.sleep()


if __name__ == '__main__':
    try:
        ambient()
    except rospy.ROSInterruptException:
        pass
