#!/usr/bin/env python
import rospy
import roslib
import keyboard  # using module keyboard
from time import sleep
from geometry_msgs.msg import PoseWithCovarianceStamped, Quaternion

STEP_DISTANCE = 1.0
x = 0.0
y = 0.0
z = 0.0

def create_pose(dx,dy,dz):
    global x, y, z
    pose_stamped = PoseWithCovarianceStamped()
    pose_stamped.header.frame_id = 'map'
    pose_stamped.header.stamp = rospy.Time.now() 

    x = x + dx
    y = y + dy
    z = z + dz

    pose_stamped.pose.pose.position.x = x
    pose_stamped.pose.pose.position.y = y
    pose_stamped.pose.pose.position.z = z

    pose_stamped.pose.pose.orientation.y = 0.0
    pose_stamped.pose.pose.orientation.x = 0.0
    pose_stamped.pose.pose.orientation.z = 0.0
    pose_stamped.pose.pose.orientation.w = 0.0

    for i in range(36):
        pose_stamped.pose.covariance[i] = 0.0

    return pose_stamped 

def fake_amcl_pose_publish():
    rospy.init_node('fake_amcl_pose')
    pub = rospy.Publisher('amcl_pose', PoseWithCovarianceStamped, queue_size=100)
    print('ros node started')
    while True:
        try:
            if keyboard.is_pressed('up'):
                print('up')
                pose = create_pose(0, STEP_DISTANCE, 0)
                pub.publish(pose)
                sleep(0.1)
            elif keyboard.is_pressed('down'):
                print('down')
                pose = create_pose(0, -STEP_DISTANCE, 0)
                pub.publish(pose)
            elif keyboard.is_pressed('right'):
                print('right')
                pose = create_pose(STEP_DISTANCE, 0, 0)
                pub.publish(pose)
            elif keyboard.is_pressed('left'):
                print('left')
                pose = create_pose(-STEP_DISTANCE, 0, 0)
                pub.publish(pose)
            elif keyboard.is_pressed('esc'):
                print('finished')
                break
        except:
            print('keyboard error')
            break


if __name__ == '__main__':
    try:
        print('start fake amcl pose publisher')
        fake_amcl_pose_publish()

    except rospy.ROSInterruptException:
        print('ROS error')
        pass
