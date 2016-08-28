#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import sys
import serial
import struct
import time
import threading
import scipy as np

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
		self.Com = SerialCtrl()
		self.Com.OpenSerial()
		self.threads = []
		self.ListenThread = threading.Thread(target = self.ReadData)
		self.PublicThread = threading.Thread(target = self.PublicMsgs)
		self.threads.append(self.ListenThread)
		self.threads.append(self.PublicThread)
		for self.rt in self.threads:
			self.rt.setDaemon(True)
			self.rt.start()
		self.rt.join() 		

	def ReadData(self):
		self.Com.ser.write('MS0128063901000\n\r99b\n\r')
		while True:
			# self.Com.ser.write('MS0128063901000\n\r99b\n\r')
		# 	self.serRead = self.Com.ReadLine()
		# 	if self.serRead.strip() == '':
		# 		pass
		# 	else:
		# 		self.info = tuple(eval(self.serRead))
		# 		# print self.info
		# 		if self.info[-1] == 1:
		# 			(self.X, self.Y,
		# 			self.A, self.T) = (self.info[0], self.info[1],
		# 								self.info[2], self.info[3])
		# 			print self.X, self.Y,self.A, self.T
			time.sleep(0.005)

	def PublicMsgs(self):
		while True:
			print 'continue'
			time.sleep(0.2)

if __name__ == '__main__':
	heilsCar = HeilsCar()

