Create pkg_hello_world
```
cd ~/catkin_ws/src
catkin_create_pkg pkg_hello_world rospy std_msgs

cd ~/catkin_ws
catkin build
source ~/catkin_ws/devel/setup.bash
```
Create pkg_hello_world/scripts/hello_world.py <br/>
Code! <br/>

Make the script executable <br/>
```
cd ~/catkin_ws/src/pkg_hello_world/scripts
sudo chmod +x hello_world.py
```

Run ROS Master  
```
roscore
```

Run the ROS Node hello_world
```
rosrun pkg_hello_world hello_world.py
```
