#!/usr/bin/env python


import rospy
from std_msgs.msg import String
from std_msgs.msg import Float32
from state_processor import state_process
from state_processor import processor
from action_processor import action_process


def communicator() :

    #Initializing node
    rospy.init_node('communicator')

    #Subscribers
    #rospy.Subscriber('Xcoord',Float32,callback1)
    #rospy.Subscriber('Ycoord',Float32,callback2)
    #rospy.Subscriber('Zcoord',Float32,callback3)


    #Publishers
    pub1 = rospy.Publisher('status',String,queue_size=5)

    rate = rospy.Rate(0.5)
    #rospy.spin()

    while not rospy.is_shutdown() :

        #PRECISO FAZER FUNCAO PARA DESCREVER NOVO ESTADO(recebe estado e açao e retorna outro estado)
        status = "held(a),on(b,table),on(c,table)"
        rospy.loginfo(status)
        pub1.publish(status)
        rate.sleep()


if __name__ == '__main__':
    try:
        communicator()
    except rospy.ROSInterruptException:
        pass
