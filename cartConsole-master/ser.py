#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.gridspec as gridspec
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT
import serial
import os.path
import platform
import struct
import time
import matplotlib
import threading

class COMThread(threading.Thread):
    def __init__(self, name = 'COMThread'):  #初始化线程        
        threading.Thread.__init__(self, name = name)
        self._stopevent = threading.Event()
        self._sleepperiod = 1.0
        #将串口定义为”com1，比特率为19200，超时0.4秒“
        #edited by LIHF 090831, 参数10表示COM11
        self.ser = serial.Serial( "/dev/ttyUSB0", 9600, timeout = 0.4)        
        
        if self.ser is None:
            print '无法打开串口'
        else:
        	print "OK"
        self.parser = None        

    def run(self):        
        global flag_zhuan
        m = 0
        print "%s starts" % (self.getName())
        while not self._stopevent.isSet():
            try:
            	self.ser.write("123456")
            	print "send"
                #x = self.ser.read(6)
            except serial.SerialException:
                print 'serial.SerialException ERROR'
                print traceback.format_exc()
                continue
            if len(x) > 0:
                print x
            #接收到数据
        self.ser.close()  #串口关闭
        print "%s ends" % (self.getName())

    #关闭串口线程
    def join(self, timeout = None):
        """ Stop the thread. """
        self._stopevent.set()
        print "COMThread.join()"
        threading.Thread.join(self, timeout)

if __name__ == '__main__':
    com = COMThread()
    com1 = 'com123'
	#print 'Open'+,com1,+'failed!Please check the port!'
    com.run()