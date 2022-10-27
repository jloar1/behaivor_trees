#!/usr/bin/env python

import behavior as bt
import rospy
import time
from std_msgs.msg import Float64
from std_msgs.msg import String


class Test:   
    def __init__(self):
        # constants
        self.rate = 2
        #self.delta = 1.0 / self.rate
        #self.speed = 0.8

        # variables
        #self.position = 0.0


    # create nodes for behaivor tree
    root = bt.Root("root")

    move1 = bt.Move("move forward")
    move2 = bt.Move("move backward")
    condition = bt.Condition("condition", False)


    # arrange nodes
    #root.nodes.append(condition)
    root.nodes.append(move1)
    root.nodes.append(move2)


    # display behaivor tree
    bt.display_tree(root)


    # while True:
    #     print("------------------")
    #     root.activate()
    #     time.sleep(3)


    # set up publisher
    def publisher(self):
        # create node and publisher
        rospy.init_node('state_machine')
        pub = rospy.Publisher('/leviathan/cusub_common/motor_controllers/pid/drive/setpoint', Float64, queue_size=1)
        rospy.Subscriber("/leviathan/cusub_common/motor_controllers/pid/drive/state", Float64, self.callback)

        self.move1.publisher = pub
        self.move2.publisher = pub

        self.move1.destination = 3.0
        self.move2.destination = -3.0
        
        # set rate
        rate = rospy.Rate(self.rate)
        
        # main loop
        while not rospy.is_shutdown():

            self.root.activate()
            # wait
            rate.sleep()

    def callback(self, data):
        self.move1.position = round(data.data, 1)
        self.move2.position = round(data.data, 1)



test = Test()
test.publisher()
