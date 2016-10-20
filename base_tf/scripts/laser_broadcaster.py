#!/usr/bin/env python
#-*- coding: utf-8 -*-
import roslib
roslib.load_manifest('base_tf')
import rospy
import tf
from nav_msgs.msg import Odometry

if __name__ == '__main__':
    rospy.init_node('laser_broadcaster')
    parent_frame_id = rospy.get_param('~parent_frame_id')
    child_frame_id = rospy.get_param('~child_frame_id')

    rate = rospy.Rate(10.0)
    while not rospy.is_shutdown():
        br = tf.TransformBroadcaster()
        br.sendTransform((0,0,0),
                         tf.transformations.quaternion_from_euler(0, 0, 0),
                         rospy.Time.now(),
                         parent_frame_id,
                         child_frame_id)
        rate.sleep()
