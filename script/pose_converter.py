#!/usr/bin/env python
import rospy
import roslib
from time import sleep
from geometry_msgs.msg import PoseWithCovarianceStamped, Quaternion
from tf.transformations import euler_from_quaternion, quaternion_from_euler

class pose_converter():
    def __init__(self):
        rospy.init_node('pose_converter')
        self.pub = rospy.Publisher('slam_pose', PoseWithCovarianceStamped, queue_size=100)
        print('node started')

        rospy.Subscriber("amcl_pose", PoseWithCovarianceStamped, self.callback)
        rospy.spin()

    def callback(self, poseWithStamped):
        print('receive pose...')
        orientation = Quaternion()
        orientation = poseWithStamped.pose.pose.orientation
        q = [orientation.x, orientation.y, orientation.z, orientation.w]
        qx= self.convert(q)

        poseWithStamped.pose.pose.orientation.x = qx.x
        poseWithStamped.pose.pose.orientation.y = qx.y
        poseWithStamped.pose.pose.orientation.z = qx.z
        poseWithStamped.pose.pose.orientation.w = qx.w

        self.pub.publish(poseWithStamped)

    def convert(self, q):
        (roll, pitch, yaw) = euler_from_quaternion(q)

        yaw += 1.57

        qx = quaternion_from_euler (roll, pitch, yaw)
        return qx


if __name__ == '__main__':
    try:
        print('starting pose converter....')
        p = pose_converter()

    except rospy.ROSInterruptException:
        print('ROS error')
        pass