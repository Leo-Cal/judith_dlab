import rospy
from std_msgs.msg import String
from std_msgs.msg import Float32
from state_processor import state_process
from state_processor import processor
from action_processor import action_process
from state_actualizer import state_actualize

global action
global initial_state



def test() :

    initial_state = "on(a,table);on(b,table);on(c,table)"
    lista_action = ["pickup(a)","putdown(a,b)","pickup(c)","putdown(c,a)"]

    i = 0

    while i < len(lista_action):

        if i == 0 :
            state_inter = initial_state
        if i != 0 :
            state_inter = state


        m_state = state_process(state_inter)


        state = state_actualize(state_inter,lista_action[i])

        m_state = state_process(state)

        print(state_inter)
        print(lista_action[i])
        print(state)
        print(m_state)
        print("----------------")
        i = i + 1

test()
