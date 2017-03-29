#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from std_msgs.msg import Float32
from state_processor import state_process
from state_processor import processor
from action_processor import action_process


def receiver() :

    rospy.init_node('receiver')
    pub1 = rospy.Publisher('action',String,queue_size = 5)
    #pub2 = rospy.Publisher('initial_state',String,queue_size=5)
    rate = rospy.Rate(0.5)

    while not rospy.is_shutdown() :

        action = "pickup(a)" #action tem que ser recebido do PROLOG
        #initial_state = "on(a,table);on(b,table);on(c,table)"
        rospy.loginfo(action)
        #rospy.loginfo(initial_state)
        pub1.publish(action)
        #pub2.publish(initial_state)
        rate.sleep()


if __name__ == '__main__':
    try:
        receiver()
    except rospy.ROSInterruptException:
        pass
