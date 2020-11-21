#!/usr/bin/env python
import rospy
from std_msgs.msg import String


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


if __name__ == '__main__':
  try:
    talker()
  except rospy.ROSInterruptException:
    pass
