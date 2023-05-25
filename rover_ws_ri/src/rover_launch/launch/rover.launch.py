import os

from ament_index_python import get_package_share_directory

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.actions import IncludeLaunchDescription
from launch.actions import GroupAction
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch.substitutions import TextSubstitution
from launch_ros.actions import Node
from launch_ros.actions import PushRosNamespace

from launch_ros.substitutions import FindPackageShare



def generate_launch_description():
    ld = LaunchDescription()
    
    # Nodes
    state_ctrl = Node(
        package="locomotion_core",
        executable="rover_state_controller",
    )

    drive_core = Node(
        package="locomotion_core",
        executable="movebase_kinematics",
    )

    # du_enable = Node(
    #     package="locomotion_core",
    #     executable="rover_enable",
    # )
    
    cmd_roboteq1 = Node(
        package="locomotion_core",
        executable="cmd_roboteq",
    )

    cmd_roboteq2 = Node(
        package="locomotion_core",
        executable="cmd_roboteq2",
    )

    en_srv = Node(
        package="locomation_core",
        executable="enable_srv"
    )

    # include another launch file
    launch_joy = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                get_package_share_directory('teleop_twist_joy'),
                'launch/teleop-launch.py'))
    )

    

    ld.add_action(launch_joy)
    ld.add_action(drive_core)
    # ld.add_action(du_enable)
    ld.add_action(cmd_roboteq1)
    ld.add_action(cmd_roboteq2)
    ld.add_action(state_ctrl)

    return ld


