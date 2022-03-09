#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

rospy.init_node('ping_node', anonymous=True)
pub = rospy.Publisher('ping', String, queue_size=10)
rate = rospy.Rate(1)

while not rospy.is_shutdown():
	ping_str = 'ping'
	pub.publish(ping_str)
	rate.sleep()
