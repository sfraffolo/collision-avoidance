#! /usr/bin/env python

import rospy
from random import random 
from geometry_msgs.msg import Twist
from time import sleep

class Twist:
    def __init__(self):
	self.move();
	self.pub = rospy.Publisher('/vel_input', Twist, queue_size = 10)

    def move(self):
	vel_msg = Twist()
	vel_msg.linear.x=0;
	vel_msg.linear.y=0;
	vel_msg.linear.z=0;
	vel_msg.angular.x=0;
	vel_msg.angular.y=0;
	vel_msg.angular.z=0;
	while not rospy.is_shoutdown():
	    vel_msg.linear.x=random()*100
	    self.pub.publish(vel_msg)

def main():
    rospy.init_node('Twist', anonymous=True)
    twist = Twist()
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("Program stopped")

if __name__ == '__main__':
    main()
