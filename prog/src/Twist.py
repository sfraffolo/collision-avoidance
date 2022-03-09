#! /usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from random import *
from time import sleep

class creaTwist:
    def __init__(self):
        self.pub = rospy.Publisher('/vel_input', Twist, queue_size=10)
        self.move()
    
    def move(self):
        vel_msg = Twist()
        vel_msg.linear.x=0
        vel_msg.linear.y=0
        vel_msg.linear.z=0
        vel_msg.angular.x=0
        vel_msg.angular.y=0
        vel_msg.angular.z=0
        self.pub.publish(vel_msg)
        while not rospy.is_shutdown():
            vel_msg.linear.x = random()
            self.pub.publish(vel_msg)


def main():
    rospy.init_node('Twist', anonymous=True)
    twist = creaTwist()
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("Program stopped")

if __name__ == '__main__':
    main()
