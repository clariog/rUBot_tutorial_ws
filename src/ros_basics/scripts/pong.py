#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def callback_number(data):
	if data.data == 'ping':
	    pub.publish('pong')
	    rospy.loginfo('pong')
	else:
	    pub.publish('Failed you jackass')
	    rospy.loginfo('Failed you jackass')

rospy.init_node('pong_node', anonymous = True)
pub = rospy.Publisher('pong', String, queue_size=10)
sub = rospy.Subscriber('ping', String, callback)
rospy.spin()
