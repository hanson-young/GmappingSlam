#!/usr/bin/env python
#-*- coding: utf-8 -*-

import sys
import time

import PyKDL as kdl

import rospy
import tf


from nav_msgs.msg import Odometry
from geometry_msgs.msg import Point, Quaternion, Twist


if __name__ == '__main__':
	rospy.init_node('odomtery')
	gps_ekf_odom_pub = rospy.Publisher('/odom', Odometry, queue_size=5)
	frame_id = '/odom'
	child_frame_id = '/base_footprint'
	odom_msg = Odometry()

	odom_msg.header.frame_id = frame_id
	odom_msg.child_frame_id = child_frame_id

	rate = rospy.Rate(10)
	while not rospy.is_shutdown():
		odom_msg.header.stamp = rospy.Time.now()
		odom_msg.pose.pose.position = Point(1, 56, 24)
		odom_msg.pose.pose.orientation = Quaternion(*(kdl.Rotation.RPY(0, 0, 0).GetQuaternion()))
		gps_ekf_odom_pub.publish(odom_msg)
		# print self.odom_msg.pose.pose.position 
		# print self.odom_msg.pose.pose.orientation
		rate.sleep()
