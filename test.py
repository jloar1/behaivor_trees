#!/usr/bin/env python

import behavior as bt
import rospy
import time
from std_msgs.msg import Float64

position = 5.0

root = bt.Root("root")

action = bt.Action("Message1")
action2 = bt.Action("Message2")
condition = bt.Condition("condition")

root.nodes.append(condition)
root.nodes.append(action2)

condition.nodes.append(action)

bt.display_tree(root)

# while True:
#     print("------------------")
#     root.activate()
#     time.sleep(3)

def publisher(pos):
    pub = rospy.Publisher('cusub_common/motor_controlls/pid/drive/setpoint', Float64, queue_size=1)
    rospy.init_node('state_machine')
    rate = rospy.Rate(0.5)
    while not rospy.is_shutdown():
        pos += 1.0
        pub.publish(pos)
        rate.sleep()

try:
    publisher(position)
except rospy.ROSInterruptException:
    pass