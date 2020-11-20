#!/usr/bin/env python 
# Shebang -> Tells OS to execute it with a Python interpreter

import rospy

def main():
  # Initialize the node
  """ 
  Node names must be unique in ROS
  anonymous=True
    If we want to run many instances of the node and don't care about the name
  """
  rospy.init_node('hello_world', anonymous=True)

  # Log on the console
  rospy.loginfo("Hello World!")
  rospy.logwarn("Hello World")
  rospy.logerr("Hello World")
  print("Hello World!")

  # Keep the node alive until it is killed by the user
  # rospy.spin()


if __name__ == '__main__':
  try:
    main()
  except rospy.ROSInterruptException:
    pass
