#! /usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan
from prog.srv import force, forceResponse
import math

class detection:
    def __init__(self):
        self.srv = rospy.Service('force_service', force, self.force_service)
        self.force = forceResponse(0,0)

    def force_service(self, request):
	return self.force

    def callback(self, msg):
	for i, val in enumerate(msg.ranges, start=0):
	    if val >= 2:
	     	continue
	    intensity= 1/val
	    col_angle= msg.angle_min + (i * msg.angle_increment)
	    x = intensity * math.cos(col_angle)
	    y = intensity * math.sin(col_angle)
	    angle = math.atan2(y, x)
	    force = forceResponse(intensity, angle)
	    self.set_force(force)

    def set_force(self, force):
	x_r = self.force.intensity * math.cos(self.force.angle)
	y_r = self.force.intensity * math.sin(self.force.angle)
	x_o = force.intensity * math.cos(force.angle)
	y_o = force.intensity * math.sin(force.angle)
	x_tot = x_r + x_o
	y_tot = y_r + y_o
	tot_intensity = math.sqrt(x_tot ** 2 + y_tot ** 2)
	tot_angle = math.atan2(y_tot, x_tot)
	self.force = forceResponse(tot_intensity, tot_angle)
	
def main():
    rospy.init_node('detection', anonymous=True)
    det = detection()
    try:
	rospy.spin()
    except KeyboardInterrupt:
        print("Program stopped")


if __name__ == '__main__':
    main()
	


