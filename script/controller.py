#!/usr/bin/env python
import rospy
import roslib
from time import sleep
from geometry_msgs.msg import PoseWithCovarianceStamped, Quaternion, Twist
from std_msgs.msg import Bool

class pose_converter():
    def __init__(self):
        rospy.init_node('hushus_controller')
        self.pub = rospy.Publisher('husky_velocity_controller/cmd_vel', Twist, queue_size=1)
        self.goal = False

        print('node started')

        rospy.Subscriber("twitch", Twist, self.callback)
        rospy.Subscriber("if_goal", Bool, self.is_goal)
        rospy.spin()

    def callback(self, t):
        print('receive t...')
        if self.goal is  False:
            self.pub.publish(t)
        else:
            print('nonono')

    def is_goal(self, data):
        if data.data == True:
            t = self.create_zero_twist()
            self.pub.publish(t)
            print('achieve')
            ans = raw_input("if next goal:")
            if ans == 'y' or ans =='yes' or ans == 'Y':
                self.goal = False
            else:
                exit(0)
    
    def create_zero_twist(self):
        t = Twist()
        t.linear.x = 0.0
        t.linear.y = 0.0
        t.linear.z = 0.0

        t.angular.x = 0.0
        t.angular.y = 0.0
        t.angular.z = 0.0

        return t




if __name__ == '__main__':
    try:
        print('starting pose converter....')
        p = pose_converter()

    except rospy.ROSInterruptException:
        print('ROS error')
        pass
