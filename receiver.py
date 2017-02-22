#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from std_msgs.msg import Float32
from state_processor import state_process
from state_processor import processor
from action_processor import action_process


def receiver() :

    rospy.init_node('receiver')
    pub = rospy.Publisher('action',String,queue_size = 5)
    rate = rospy.Rate(0.5)

    while not rospy.is_shutdown() :

        action = "pickup(a)"
        rospy.loginfo(action)
        pub.publish(action)
        rate.sleep()


if __name__ == '__main__':
    try:
        receiver()
    except rospy.ROSInterruptException:
        pass
