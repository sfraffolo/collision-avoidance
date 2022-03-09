#! /usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from prog.srv import Force, ForceResponse
import math
from random import random
from time import sleep

class controller:
    def __init__(self):
        self.pub = rospy.Subscriber('/vel_input', Twist, self.callback)
        self.pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

    def callback(self, msg):
        if msg.linear.x==0:
            self.pub.publish(msg)
            return
        rospy.wait_for_service('force_service')
        try:
            force_service = rospy.ServiceProxy('force_service', Force)
            force = force_service()
            vel_msg = Twist()
	    max_vel = msg.linear.x
            x_linear = msg.linear.x + force.intensity
	    if x_linear < max_vel :
                vel_msg.linear.x = x_linear  
 	    else:
		vel_msg.linear.x = max_vel
            vel_msg.angular.z = msg.angular.z + force.angle
            print(vel_msg)
            self.pub.publish(vel_msg)
        except rospy.ServiceException as exc:
            print('Service did not process request: ' +str(exc))


def main():
    rospy.init_node('controller', anonymous=True)
    vel = controller()
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("Program stopped")

if __name__ == '__main__':
    main()
