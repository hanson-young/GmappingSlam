#!/usr/bin/env python3
#-*- coding: utf-8 -*-
# import math
import rospy
from nav_msgs.msg import Odometry
from geometry_msgs.msg import *

def Position(odom_data):
    curr_time = odom_data.header.stamp
    pose = odom_data.pose.pose #  the x,y,z pose and quaternion orientation
    print pose

def begin():
    while not rospy.is_shutdown():
        rospy.init_node('listener', anonymous=False) #make node 
        rospy.Subscriber('/odom',Odometry,Position)
        rospy.spin()


if __name__ == "__main__":
    begin()
    