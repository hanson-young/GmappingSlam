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
		while True:
			print 1
			try:
				print 1
				self.serRead = self.Com.ReadLine()
			except serial.SerialException:
				raise serial.SerialException
			if self.serRead == b'':
				(self.X, self.Y, self.A) = (None, None, None)
				yield (self.X, self.Y, self.A,self.Speed_X, self.Speed_Y, self.Speed)
			else:
				try:
					self.info = tuple(eval(self.serRead))
					print self.info
					if self.info[-1] == 2:
						self.timeNode.append(self.info[0])
						print(self.timeNode)
						raise Exception
					elif self.info[-1] != 1 and self.info[-1] != 2:
						raise Exception
				except Exception:
					self.type = 'bad_datatype'
					print(self.type, self.info)
				else:
					self.X, self.Y,
					self.A, self.T = (self.info[0], self.info[1],
					self.info[2], self.info[-2])

					yield (self.X, self.Y, self.A)
			time.sleep(0.001)


	def PublicMsgs(self):
		while True:
			print 'continue'
			time.sleep(0.002)

if __name__ == '__main__':
	heilsCar = HeilsCar()


