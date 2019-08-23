#!/usr/bin/env python
import rospy
import roslib
import keyboard  # using module keyboard
from time import sleep
from geometry_msgs.msg import PoseWithCovarianceStamped, Pose

STEP_DISTANCE = 0.01
SLEEP_TIME = 0.1
x = 0.0
y = 0.0
z = 0.0
ox = 0.0
oy = 0.0
oz = -1.0

def create_pose(dx,dy,dz,dox, doy, doz):
    global x, y, z, ox, oy, oz
    pose_stamped = PoseWithCovarianceStamped()
    pose_stamped.header.frame_id = 'map'
    pose_stamped.header.stamp = rospy.Time.now() 

    x = x + dx
    y = y + dy
    z = z + dz

    ox = ox + dox
    oy = oy + doy
    oz = oz + doz

    pose_stamped.pose.pose.position.x = x
    pose_stamped.pose.pose.position.y = y
    pose_stamped.pose.pose.position.z = z

    pose_stamped.pose.pose.orientation.x = ox
    pose_stamped.pose.pose.orientation.y = oy
    pose_stamped.pose.pose.orientation.z = oz
    pose_stamped.pose.pose.orientation.w = -1.0

    for i in range(36):
        pose_stamped.pose.covariance[i] = 0.0

    return pose_stamped 

pose = None

def fake_amcl_pose_publish():
    global pose
    rospy.init_node('fake_amcl_pose')
    pub = rospy.Publisher('slam_pose', PoseWithCovarianceStamped, queue_size=100)
    print('ros node started')
    pose = create_pose(0,0,0,0,0,0)
    while True:
        try:
            if keyboard.is_pressed('up'):
                print('up')
                pose = create_pose(0, STEP_DISTANCE, 0, 0, 0, 0)
                pub.publish(pose)
                sleep(SLEEP_TIME)
            elif keyboard.is_pressed('down'):
                print('down')
                pose = create_pose(0, -STEP_DISTANCE, 0, 0, 0, 0)
                pub.publish(pose)
                sleep(SLEEP_TIME)
            elif keyboard.is_pressed('right'):
                print('right')
                pose = create_pose(STEP_DISTANCE, 0, 0, 0, 0, 0)
                pub.publish(pose)
                sleep(SLEEP_TIME)
            elif keyboard.is_pressed('left'):
                print('left')
                pose = create_pose(-STEP_DISTANCE, 0, 0, 0, 0, 0)
                pub.publish(pose)
                sleep(SLEEP_TIME)
            elif keyboard.is_pressed('a'):
                print('rotate left')
                pose = create_pose(0, 0, 0, 0, 0, -STEP_DISTANCE)
                pub.publish(pose)
                sleep(SLEEP_TIME)
            elif keyboard.is_pressed('d'):
                print('rotate right')
                pose = create_pose(0, 0, 0, 0, 0, STEP_DISTANCE)
                pub.publish(pose)
                sleep(SLEEP_TIME)
            elif keyboard.is_pressed('esc'):
                print('finished')
                break
            else:
                pub.publish(pose)
                sleep(SLEEP_TIME)
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
