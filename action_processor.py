#!/usr/bin/env python]
from __future__ import print_function


def action_process(i1,j1,i2,j2,i3,j3,string) :
    #i1,j1,i2,j2,i3,j3,string
    """Receives the 6 matricial coordinates of the blocks and a string
    representing the action. Returns a string with numbers representing the gripper action numbered as follows :
        1 - GOTO
        2 - OPEN_GRIPPER
        3 - CLOSE_GRIPPER
    and the (x,y,z) coordinates do move the gripper. If coords are null, don't move gripper
    return(string,string) """
# uncomment lines below for testing purposes
    """i1 = 0
    j1 = 0
    i2 = 1
    j2 = 0
    i3 = 2
    j3 = 0
    string = "putdown(a,b)"
"""
#Block sizes. Adjust as necessary

    block_l = 50
    block_h = 50

#Gripper initial position. Adjust to referential

    x_gripper = 0
    y_gripper = 0
    z_gripper = 0

#Block initial positions. Adjust to referential and coordinate system

    x_a = (block_l/2) + (block_l + 30)*i1
    y_a = (block_h/2) + (block_h)*j1
    z_a = 10

    x_b = (block_l/2) + (block_l + 30)*i2
    y_b = (block_h/2) + (block_h)*j2
    z_b = 10

    x_c = (block_l/2) + (block_l + 30)*i3
    y_c = (block_h/2) + (block_h)*j3
    z_c = 10

#string manipulation


    i = string.find("(")

    action_string = string[:i]
    object_string = string[i+1:]



 #Processing action_string

    acts = [] #list with the numbers of actions


    if action_string == "pickup" :

        acts.append(1)
        acts.append(3)
        acts.append(1)  #GOTO(block), CLOSE_GRIPPER, GOTO(rest position)

    if action_string == "putdown" or action_string == "put_on_table" :

        acts.append(1)
        acts.append(2) #GOTO(place), OPEN_GRIPPER, GOTO(rest position)
        acts.append(1)

#Processing object_string


    element = [] #list with the coords to GOTO

    if object_string.count(",") == 1 :

        i = object_string.find(",")
        object_string = object_string[i+1:]

    if object_string == 'a)' :

        element.append(x_a)
        element.append(y_a)
        element.append(z_a)


    if object_string == 'b)' :

        element.append(x_b)
        element.append(y_b)
        element.append(z_b)


    if object_string == 'c)' :

        element.append(x_c)
        element.append(y_c)
        element.append(z_c)


#VERIFICAR COMO ta put_on_table NO PROLOG!!!!!!
    if object_string == 'table)' :

        element.append(x_table)
        element.append(y_table)
        element.append(z_table)


#Construction of Action/Position matrix


    line = [] #second line  of matrix
    line.append(element) #fist element of line, another list
    line.append('.') #second element of line, a dot, since it is a non-coordinate action

    rest_list = [] #list to coordinate to rest Position

    rest_list.append(0)
    rest_list.append(0)  # ADJUST IF REST POSITION IS NOT (0,0,0)
    rest_list.append(0)

    line.append(rest_list) #third element of line, another list, representing coordinates to rest position


    matrix = []

    matrix.append(acts)
    matrix.append(line)

#uncomment lines below for testing purposes
    return matrix

    """for i in range(2) :
        if i> 0 :
            print(" ")
        for j in range(3) :
            print(matrix[i][j], end = '')
    print(matrix[1][0][0])

    return matrix

action_process()
"""
