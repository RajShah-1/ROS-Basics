Create pkg_pub_sub
```
cd ~/catkin_ws/src
catkin_create_pkg pkg_pub_sub rospy std_msgs

cd ~/catkin_ws
catkin build
source ~/catkin_ws/devel/setup.bash
```
Create pkg_pub_sub/scripts/pub_node.py <br/>
Create pkg_pub_sub/scripts/sub_node.py <br/>
Code! <br/>

Make the script executable <br/>
```
cd ~/catkin_ws/src/pkg_pub_sub/scripts
sudo chmod +x pub_node.py
sudo chmod +x sub_node.py
```

Run ROS Master  
```
roscore
```

Run the ROS Node hello_world
```
rosrun pkg_pub_sub pub_node.py
rosrun pkg_pub_sub sub_node.py
```