#! /usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

class Twist:
    def __init__(self):
	self.move();
	self.publisher = rospy.Publisher('vel_input', Twist, queue_size = 10)

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
	    self.publisher.publish(vel_msg)

def main():
    rospy.init_node('Twist', anonymous=True)
    twist = Twist()
    rospy.spin()

if __name__ == '__main__':
    main()
