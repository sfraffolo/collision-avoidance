#! /usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan
import time
import math
from prog.srv import Force, ForceResponse


class detection:
    def __init__(self):
        self.srv = rospy.Service('force_service', Force, self.force_service)
	self.sub = rospy.Subscriber('/base_scan', LaserScan, self.callback)
        self.force = ForceResponse(0, 0)
	
    def callback(self, msg):
        self.force = ForceResponse(0, 0)
	i_min=0
	min_val=msg.ranges[0]
        for i, val in enumerate(msg.ranges, start=0):
	    if val >= 0.6:
	        continue
	    if val < min_val:
	    	min_val = val
		i_min = i
	intensity = 1/min_val
	col_angle = msg.angle_min + (i_min * msg.angle_increment)
	x = intensity * math.cos(col_angle)
	y = intensity * math.sin(col_angle)
	angle = math.atan2(-y, -x)
	force = ForceResponse(intensity, angle)
	self.set_force(force)
        
    def set_force(self, force):
        x_r = self.force.intensity * math.cos(self.force.angle)
        y_r = self.force.intensity * math.sin(self.force.angle)
        x_o = force.intensity * math.cos(force.angle)
        y_o = force.intensity * math.sin(force.angle)
        x_tot = x_r + x_o
        y_tot = y_r + y_o
        tot_intensity = math.sqrt(x_tot ** 2 +  y_tot ** 2)
        tot_angle = math.atan2(y_tot, x_tot)
        self.force = ForceResponse(tot_intensity, tot_angle)
 

    def force_service(self, request):
        return self.force

def main():
    rospy.init_node('detection', anonymous=True)
    det = detection()
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("Program stopped")

if __name__ == '__main__':
    main()
