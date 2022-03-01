#! /usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from collision_avoidance.srv import Force, ForceResponse
import math



class controller:
    def __init__(self):
	self.pub = rospy.Subscriber('vel_input', Twist, self.callback)
	
    def callback(self, msg):
	if msg.linear.x==0:
	    return
	rospy.wait_for_service('force_service')
	try:
	    force_service = rospy.ServiceProxy('force_service', force)
	    force = force_service()
	    vel_msg = Twist()
	    vel_msg.linear.x = vel_msg.linear.x - force.intensity
	    vel_msg.angular.z = vel_msg.angular.z + force.angle
	    print(vel_msg)
	    

def main():
    rospy.init_node('controller', anonymous='True')
    vel = controller()
    try:
	rospy.spin()

if __name__ == '__main__':
    main()
