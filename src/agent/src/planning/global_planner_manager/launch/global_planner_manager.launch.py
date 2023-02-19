# Copyright 2023 michael. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

import os
import launch
from ament_index_python.packages import get_package_share_directory
import launch_ros
from pathlib import Path
from launch_ros.actions import Node
from launch.conditions import IfCondition
from launch.substitutions import LaunchConfiguration
from launch.actions import DeclareLaunchArgument


def generate_launch_description():
    ld = launch.LaunchDescription()
    waypoint_file_path = DeclareLaunchArgument(
        "waypoint_file_path",
        default_value="./src/roar-indy-launches/config/carla_waypoints.txt",
    )
    lookahead_dist = DeclareLaunchArgument(
        "lookahead_dist",
        default_value="5.0",
    )
    odom_topic = DeclareLaunchArgument(
        "odom_topic",
        default_value="/carla/ego_vehicle/odometry",
    )

    waypoint_follower_server_loop_rate = DeclareLaunchArgument(
        "loop_rate",
        default_value="5.0",
    )
    global_planner_manager_node = Node(
        name="global_planner_manager",
        executable="global_planner_manager",
        package="global_planner_manager",
        parameters=[
            {
                "waypoint_file_path": LaunchConfiguration(
                    "waypoint_file_path",
                    default="./src/roar-indy-launches/config/carla_waypoints.txt",
                ),
                "debug": LaunchConfiguration("debug", default=False),
            }
        ],
    )
    waypoint_follower_server_node = Node(
        name="waypoint_follower_server_node",
        executable="waypoint_follower",
        package="global_planner_manager",
        parameters=[
            {
                "lookahead_dist": LaunchConfiguration("lookahead_dist"),
                "loop_rate": LaunchConfiguration("loop_rate"),
            }
        ],
        remappings=[
            (
                "odom",
                LaunchConfiguration("odom_topic", default="/carla/ego_vehicle/odom"),
            )
        ],
    )
    # args
    ld.add_action(waypoint_file_path)
    ld.add_action(lookahead_dist)
    ld.add_action(odom_topic)
    ld.add_action(waypoint_follower_server_loop_rate)

    # node
    ld.add_action(global_planner_manager_node)
    ld.add_action(waypoint_follower_server_node)

    return ld