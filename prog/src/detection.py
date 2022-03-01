#! /usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan
from prog.srv import force, forceResponse
import math

class Detection:
    def __init__(self):
    self.sub = rospy.Subscriber('/base_scan', LaserScan, self.callback)
    self.service = rospy.Service('force_service', force, self.force_service)
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

    def set_force(self, force)
	x_r = self.force.intensity * math.cos(self.force.angle)
	y_r = self.force.intensity * math.sin(self.force.angle)
	x_o = force.intensity * math.cos(force.angle)
	y_o = force.intensity * math.sin(force.angle)
	x_total = x_r + x_o
	y_total = y_r + y_o
	total_intensity = math.sqrt(x_total ** 2 + y_total ** 2)
	total_angle = math.atan2(y_total, x_total)
	self.force = forceResponse(total_intensity, total_angle)
	
def main():
    rospy.init_node('detection', anonymous=True)
    det = detection()
    try:
	rospy.spin()

if __name__ == 'main':
    main()

	











