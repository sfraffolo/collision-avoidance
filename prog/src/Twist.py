import rospy
from geometry_msgs.msg import Twist

class Twist:
    def __init__(self):
	self.move();

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

