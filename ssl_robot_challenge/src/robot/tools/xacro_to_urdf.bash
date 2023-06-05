#!/bin/bash
echo -e "Input deired robot to convert \nIF robot doesnt exist, expect error"
read name_input
cd ~/ssl_robot_challenge/src/robot
cd ${name_input}
cd urdf
ros2 run xacro xacro -o ${name_input}.urdf ${name_input}.urdf.xacro