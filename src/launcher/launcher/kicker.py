import os, pathlib, xacro

# Messages and Services
from bitchin_n_moanin.srv import AddRobit

# ROS stuff
import rclpy
from rclpy.node import Node

# ROS launch stuff
from ament_index_python import get_package_share_directory
from launch import LaunchDescription, LaunchService
from launch.actions import DeclareLaunchArgument
from launch.conditions import IfCondition, UnlessCondition
from launch.substitutions import Command, LaunchConfiguration
from launch_ros.actions import Node as NODE
from launch_ros.substitutions import Parameter

class KoreKicker(Node):

    def __init__(self):
        super().__init__("kore_kicker")
        self.srv = self.create_service(AddRobit, "add_robit", self.add_robit_callback)

    def add_robit_callback(self, request, response):
        if (request.add_robit == True):
            self.get_logger().info("Attempting to add robot: %s" % request.robot_name)
            response.robit_added = True
        if (response.robit_added == True):
            self.get_logger().info("Robit added! Robot: %s" % request.robot_name)
        
        return response


def main(args=None):
    rclpy.init(args=args)
    kore_kicker = KoreKicker()
    rclpy.spin(kore_kicker)

    rclpy.shutdown()

if __name__ == "__main__":
    main()