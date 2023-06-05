import os
import sys
import xacro
from ament_index_python import get_package_share_directory
from launch import LaunchDescription, LaunchService
from launch.actions import DeclareLaunchArgument
from launch.conditions import IfCondition, UnlessCondition
from launch.substitutions import Command, LaunchConfiguration
from launch_ros.actions import Node
from launch_ros.substitutions import Parameter

def xacro_urdf_launcher(robot_name):
    urdf_xacro_path = os.path.abspath("src/robot/" + robot_name + "/urdf/" + robot_name + ".urdf.xacro")
    if os.path.exists(urdf_xacro_path):
        print("[URDF Viewer] All good in the hood, the robot URDF exists")
    else:
        print("[URDF Viewer] URDF file does not exist, suffer")
    # most of this code is borrowed from online, hopefully it works
    gui = LaunchConfiguration("gui")
    urdf_model = LaunchConfiguration("urdf_model")
    use_robot_state_pub = LaunchConfiguration("use_robot_state_pub")
    use_rviz = LaunchConfiguration("use_rviz")

    xacro_urdf = xacro.parse(open(urdf_xacro_path))
    xacro.process_doc(xacro_urdf)
    urdf = xacro_urdf.toxml()
    
    declare_use_joint_state_publisher_cmd = DeclareLaunchArgument(
        name="gui",
        default_value="True"
    )
    declare_use_robot_state_publisher_cmd = DeclareLaunchArgument(
        name="use_robot_state_pub",
        default_value="True"
    )
    declare_use_rvis_cmd = DeclareLaunchArgument(
        name="use_rviz",
        default_value="True"
    )

    start_joint_state_publisher_cmd = Node(
        condition=UnlessCondition(gui),
        package="joint_state_publisher",
        executable="joint_state_publisher",
        name="joint_state_publisher"
    )
    start_joint_state_publisher_gui_node = Node(
        condition=IfCondition(gui),
        package="joint_state_publisher_gui",
        executable="joint_state_publisher_gui",
        name="joint_state_publisher_gui"
    )
    start_robot_state_publisher_cmd = Node(
        condition=IfCondition(use_robot_state_pub),
        package="robot_state_publisher",
        executable="robot_state_publisher",
        parameters=[{"robot_description": urdf}]
    )

    start_rviz_cmd = Node(
        condition=IfCondition(use_rviz),
        package="rviz2",
        executable="rviz2",
        name="rviz2",
        output="screen"
    )
    tf_node = Node(
        package="tf2_ros",
        executable="static_transform_publisher",
        arguments=["0", "0", "0", "0", "0", "0", "map", "base_link"]
    )


    ld = LaunchDescription()
    
    ld.add_action(declare_use_joint_state_publisher_cmd)
    ld.add_action(declare_use_robot_state_publisher_cmd)
    ld.add_action(declare_use_rvis_cmd)

    ld.add_action(start_joint_state_publisher_cmd)
    ld.add_action(start_joint_state_publisher_gui_node)
    ld.add_action(start_robot_state_publisher_cmd)
    ld.add_action(start_rviz_cmd)
    ld.add_action(tf_node)

    return ld
    

def main():
    print("[SSL ROS2 Robot Control Software Challenge] \nWelcome to the RVIS robot viewer! please enter a robot from the list:")
    robots = os.listdir("../ssl_robot_challenge/src/robot")
    for names in robots:
        if names != "tools":
            print("-" + names)
    print("\nWaiting for input...")
    input_name = input()
    if input_name not in robots:
        print("[Xacro Viewer] You fucking clutz, thats not a robot in the list!")
    else:
        ld = xacro_urdf_launcher(input_name)
        ls = LaunchService(argv=sys.argv[1:])
        ls.include_launch_description(ld)
        ls.run()
    sys.exit(0)
    
    
    


if __name__ == "__main__":
    main()