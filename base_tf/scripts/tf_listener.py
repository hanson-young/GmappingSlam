#!/usr/bin/env python
#-*- coding: utf-8 -*-

import roslib
roslib.load_manifest('base_tf')
import rospy
import math
import tf
import geometry_msgs.msg

if __name__ == '__main__':
    rospy.init_node('listener')

    listener = tf.TransformListener()

    rate = rospy.Rate(10.0)
    
    while not rospy.is_shutdown():
        try:
            (trans,rot) = listener.lookupTransform('/base_footprint', '/scan', rospy.Time(0))
        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            continue
        print trans,rot

        rate.sleep()
