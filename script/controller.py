#!/usr/bin/env python
import rospy
import roslib
from time import sleep
from geometry_msgs.msg import PoseWithCovarianceStamped, Quaternion, Twist
from std_msgs.msg import Bool
from communication import sender

class controller():
    def __init__(self):
        rospy.init_node('controller')
        self.goal = False
        self.sendman = sender()

        print('node started')

        rospy.Subscriber("twitch", Twist, self.callback)
        rospy.Subscriber("if_goal", Bool, self.is_goal)
        rospy.spin()

    def callback(self, t):
        print('receive t...')
        if (self.goal is False):
            j = self.msgs2json(t)
            self.sendman.send(j)

    def is_goal(self, data):
        if data.data == True:
            j = self.create_zero_twist()
            self.sendman.send(j)
            self.goal = True
            print('achieve')

            # continue
            ans = raw_input("if next goal exists:")
            if ans == 'y' or ans =='yes' or ans == 'Y':
                self.goal = False
            else:
                exit(0)
    
    def create_zero_twist(self):
        j = {
            'linear_x' : 0.0,
            'linear_y' : 0.0,
            'linear_z' : 0.0,
            'angular_x': 0.0,
            'angular_y': 0.0,
            'angular_z': 0.0,
        }

        return j
    
    def msgs2json(self, t):
        j = {
            'linear_x' : t.linear.x,
            'linear_y' : t.linear.y,
            'linear_z' : t.linear.z,
            'angular_x': t.angular.x,
            'angular_y': t.angular.y,
            'angular_z': t.achieve.z
        }
        return j




if __name__ == '__main__':
    try:
        print('starting controll husky....')
        c = controller()

    except rospy.ROSInterruptException:
        print('ROS error')
        pass