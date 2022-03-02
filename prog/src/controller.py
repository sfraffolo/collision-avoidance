#! /usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from prog.srv import Force, ForceResponse
import math
from random import random

class controller:
    def __init__(self):
	self.pub = rospy.Subscriber('/vel_input', Twist, self.callback)
	self.pub = rospy.Publisher('/controller', Twist, queue_size=10)
	
    def callback(self, msg):
	if msg.linear.x==0:
	    self.pub.publisher(msg)
	    return
	rospy.wait_for_service('force_service')
	try:
	    force_service = rospy.ServiceProxy('force_service', force)
	    force = force_service()
	    vel_msg = Twist()
	    vel_msg.linear.x = vel_msg.linear.x - force.intensity
	    vel_msg.angular.z = vel_msg.angular.z + force.angle
	    print(vel_msg)
	    self.pub.publish(vel_msg)
	except rospy.ServiceException as ecx:
	    print('Service did not process request: ' +str(exc))
	    

def main():
    rospy.init_node('controller', anonymous='True')
    vel = controller()
    try:
	rospy.spin()
    except KeyboardInterrupt:
        print("Program stopped")

if __name__ == '__main__':
    main()
