#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import rospy
from nav_msgs.msg import Odometry
from geometry_msgs.msg import *

counter = 0

def Position(odom_data):

    global counter
    rospy.sleep(1)
    curr_time = odom_data.header.stamp
    pose = odom_data.pose.pose #  the x,y,z pose and quaternion orientation
    counter= counter+1
    print counter, curr_time
    print
    print pose


def transformation(tf_data):
    global counter
    rospy.sleep(1)
    transform = tf_data.transform
    print transform


def begin():
    while not rospy.is_shutdown():
        rospy.init_node('listener', anonymous=False) #make node 
        rospy.Subscriber('/odom',Odometry,Position)


if __name__ == "__main__":
    begin()
    rospy.spin() # not really necessary because we have while not rospy.is_shutdown()