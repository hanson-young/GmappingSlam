#!/usr/bin/env python
#-*- coding: utf-8 -*-

import sys
import serial
import struct
import binascii
import time

import PyKDL as kdl

import rospy
import tf


from nav_msgs.msg import Odometry
from geometry_msgs.msg import Point, Quaternion, Twist

class SerialCtrl(object):

	def __init__(self, port = '/dev/ttyUSB0' , baud = 115200, timeout = 0,
						parity = 'N', bytesize = 8, stopbits=1):
		self.ser = None
		self.port = port
		self.baudrate = baud
		self.timeout = timeout
		self.parity = parity
		self.bytesize = bytesize
		self.stopbits = stopbits
		self.message = 0

	def OpenSerial(self):
		try:
			self.ser = serial.Serial(self.port, baudrate = self.baudrate, 
						timeout = self.timeout)
		except Exception:
			print 'Open com failed!Please check the port!'
			return False
		else:
			print 'Open com Successfully!'
			return True

	def CloseSerial(self):
		self.ser.close()

	def ReadLine(self):
		try:
			return self.ser.readline()
		except serial.SerialException:
			raise serial.SerialException
	def WriteCmd(self,string):
		string = eval(string)
		string = struct.pack('i', string)
		self.ser.write(string)

if __name__ == '__main__':

	rospy.init_node('serial_port',anonymous = False)
	Com = SerialCtrl()
	Com.OpenSerial()
	gps_ekf_odom_pub = rospy.Publisher('/odom', Odometry, queue_size=5)
	frame_id = '/odom'
	child_frame_id = '/map'
	odom_msg = Odometry()

	odom_msg.header.frame_id = frame_id
	odom_msg.child_frame_id = child_frame_id

	X = 0
	Y = 0
	Z = 0
	T = 0
	A = 0

	rate = rospy.Rate(200)
	while not rospy.is_shutdown():
		serRead = Com.ReadLine()
		if serRead.strip() == '':
			# print 'No Data'
			pass
		else:
			info = tuple(eval(serRead))
			# print self.info
			if info[-1] == 1:
				X, Y, A, T = info[0], info[1], info[2], info[3]

				odom_msg.header.stamp = rospy.Time.now()
				odom_msg.pose.pose.position = Point(float(X)/1000000, float(Y)/1000000, 0)
				odom_msg.pose.pose.orientation = Quaternion(*(kdl.Rotation.RPY(0, 0, float(A)/1000).GetQuaternion()))
				gps_ekf_odom_pub.publish(odom_msg)
		rate.sleep()
	Com.CloseSerial()