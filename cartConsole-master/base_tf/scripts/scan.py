#!/usr/bin/env python
#-*- coding: utf-8 -*-

import sys
import time

import PyKDL as kdl
# import scipy as np
import rospy
import tf


from nav_msgs.msg import Odometry
from geometry_msgs.msg import Point, Quaternion, Twist


if __name__ == '__main__':
	rospy.init_node('scan')

	gps_ekf_odom_pub = rospy.Publisher('/scan', Odometry, queue_size=5)
	frame_id = '/scan'
	child_frame_id = '/odom'
	odom_msg = Odometry()

	odom_msg.header.frame_id = frame_id
	odom_msg.child_frame_id = child_frame_id

	rate = rospy.Rate(10)
	while not rospy.is_shutdown():

		odom_msg.header.stamp = rospy.Time.now()
		odom_msg.pose.pose.position = Point(22, 21, 43)
		odom_msg.pose.pose.orientation = Quaternion(*(kdl.Rotation.RPY(1.8, 0.3, 1.2).GetQuaternion()))
		gps_ekf_odom_pub.publish(odom_msg)
		# print self.odom_msg.pose.pose.position 
		# print self.odom_msg.pose.pose.orientation
		rate.sleep()