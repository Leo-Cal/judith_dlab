#!/usr/bin/env python

class Action :
    ##string = "pickup(a)" , "putdown(a,b)" , "put_on_table(a)"
    '''
    3 characteristics:
            self.description -> action description
            self.object -> block that is moved by the action
            self.destination -> destination of the moved block (if ther is one)
    '''

    def __init__(self,string) :

        i = string.find("(")
        act_description = string[:i]
        self.description = act_description

        string = string[i+1:]

        act_object = string[0]
        self.object = act_object

        i = string.find(",")

        if i == -1 :

            self.destination = 0

        else :

            string = string[i+1:]
            act_destination = string[0]
            self.destination = act_destination

class State:
    #string = "on(a,table);on(b,c);on(c,table)" [PRECISO MUDAR PRA ; NO PROLOG!]
    '''
    3 characteristics:
        self.a , self.b , self.c, each representing state
        of block a, b and c respectively
    '''

    def __init__(self,string):

        i = string.find(";")
        string1 = string[:i]


        string = string[i+1:]

        i = string.find(";")
        string2 = string[:i]


        string3 = string[i+1:]

        self.a = string1
        self.b = string2
        self.c = string3



def state_actualize(state_string,action_string) :
    '''Function receives a state and an action(STRINGS!) and returns
    the state after the action'''

    #Initializing as class objects
    state = State(state_string)
    action = Action(action_string)

#------------------------Pickups---------------------------#

    if action.description == "pickup" :

        if action.object == "a" :

            state.a = "held(a)"

        if action.object == "b" :

            state.b = "held(b)"

        if action.object == "c" :

            state.c = "held(c)"

#-----------------------Putdowns-------------------------------#

    if action.description == "putdown" :

        if action.object == "a":

            if action.destination == "b":

                state.a = "on(a,b)"

            if action.destination == "c":

                state.a = "on(a,c)"



        if action.object == "b":

            if action.destination == "a":

                state.a = "on(b,a)"

            if action.destination == "c":

                state.a = "on(b,c)"



        if action.object == "c":

            if action.destination == "a":

                state.a = "on(c,a)"

            if action.destination == "b":

                state.a = "on(c,b)"


#------------------------Put_on_tables----------------------#


    if action.description == "put_on_table":


        if action.object == "a":

            state.a = "on(a,table)"

        if action.object == "b" :

            state.b = "on(b,table)"

        if action.object == "c":

            state.c = "on(c,table)"



    state_string = "%s;%s;%s"%(state.a,state.b,state.c)
    return(state_string)
