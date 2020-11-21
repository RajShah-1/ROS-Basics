#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist


def talker():
  pub = rospy.Publisher('chatter', String, queue_size=10)
  rospy.init_node('talker', anonymous=True)
  rate = rospy.Rate(2)  # 10hz
  index = 0
  while not rospy.is_shutdown():
    hello_str = "hello world " + str(index)
    rospy.loginfo(hello_str)
    pub.publish(hello_str)
    index += 1
    rate.sleep()


def turtleController():
  velocity_publisher = rospy.Publisher(
      'turtle1/cmd_vel',
      Twist,
      queue_size=10,
  )
  rospy.init_node('talker', anonymous=True)
  rate = rospy.Rate(2)  # 10hz
  velocity_msg = Twist()
  velocity_msg.angular.z = 2
  velocity_msg.linear.x = 2
  while not rospy.is_shutdown():
    velocity_publisher.publish(velocity_msg)
    rate.sleep()


if __name__ == '__main__':
  try:
    talker()
    # turtleController()
  except rospy.ROSInterruptException:
    pass
