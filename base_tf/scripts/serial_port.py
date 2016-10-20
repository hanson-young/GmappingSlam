#!/usr/bin/env python
#-*- coding: utf-8 -*-

import sys
import serial
import struct
import binascii
import time
import threading

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


class HeilsCar(object):
	def __init__(self):

		self.X = 0
		self.Y = 0
		self.Z = 0
		self.T = 0
		self.A = 0
		rospy.init_node('serial_port',anonymous = False)
		self.Com = SerialCtrl()
		self.Com.OpenSerial()
		self.threads = []
		self.ListenThread = threading.Thread(target = self.ReadData)
		self.PublicThread = threading.Thread(target = self.PublicMsgs)
		self.SendThread = threading.Thread(target = self.SendMsgs)
		self.threads.append(self.ListenThread)
		self.threads.append(self.PublicThread)
		self.threads.append(self.SendThread)
		for self.rt in self.threads:
			self.rt.setDaemon(True)
			self.rt.start()
		self.rt.join() 		

	def ReadData(self):
		while not rospy.is_shutdown():
			self.serRead = self.Com.ReadLine()
			if self.serRead.strip() == '':
				pass
			else:
				self.info = tuple(eval(self.serRead))
				# print self.info
				if self.info[-1] == 1:
					self.X, self.Y,self.A, self.T = self.info[0], self.info[1],self.info[2], self.info[3]
					# print self.X, self.Y,self.A, self.T
			# self.X, self.Y,self.A, self.T = 10, 20, 0, 40
			# print self.X, self.Y,self.A
			time.sleep(0.003)

	def PublicMsgs(self):

		self.gps_ekf_odom_pub = rospy.Publisher('/odom', Odometry, queue_size=5)
		self.frame_id = '/odom'
		self.child_frame_id = '/map'
		self.odom_msg = Odometry()

		self.odom_msg.header.frame_id = self.frame_id
		self.odom_msg.child_frame_id = self.child_frame_id

		rate = rospy.Rate(10)
		while not rospy.is_shutdown():
			self.odom_msg.header.stamp = rospy.Time.now()
			self.odom_msg.pose.pose.position = Point(self.X, self.Y, 0)
			self.odom_msg.pose.pose.orientation = Quaternion(*(kdl.Rotation.RPY(0, 0, self.A).GetQuaternion()))

			self.gps_ekf_odom_pub.publish(self.odom_msg)
			# print self.odom_msg.pose.pose.position 
			# print self.odom_msg.pose.pose.orientation
			rate.sleep()
	def SendMsgs(self):
		rospy.Subscriber('cmd_vel', Twist, self.CallBack)
		rospy.spin()
	def CallBack(self, twist):
		# print twist
		print("publihsed: vx: {0}, wy: {1}, rot: {2}".format(twist.linear.x, twist.linear.y, twist.angular.z))
		head = struct.pack('BB',0x0D, 0x0A)
		bytes = struct.pack('fff',twist.linear.x, twist.linear.y, twist.angular.z)
		tail = struct.pack('BB',0x0A, 0x0D)
		# bytes = struct.pack('BBBB',0x0D, 0x0A, 0x0A, 0x0D)
		# print binascii.hexlify(head + bytes + tail)
		self.Com.ser.write(head + bytes + tail)

if __name__ == '__main__':
	# rospy.init_node('serial_port',anonymous = False)
	heilsCar = HeilsCar()

