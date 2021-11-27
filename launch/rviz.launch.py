import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument

from launch.actions.execute_process import ExecuteProcess
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():

    use_sim_time = LaunchConfiguration('use_sim_time', default='false')

    pkg_fra502 = get_package_share_directory('fra502')

    rviz_file_name = 'tratsah.rviz'
    urdf_file_name = 'tratsah.urdf'

    print("rviz_file_name : {}".format(rviz_file_name))

    urdf = os.path.join(
        pkg_fra502,
        urdf_file_name)
    rviz_file_path = os.path.join(
        pkg_fra502,
        rviz_file_name)

    rviz = ExecuteProcess(
        cmd=['rviz2', '-d', rviz_file_path],
        output='screen')

    return LaunchDescription([
        DeclareLaunchArgument(
            'use_sim_time',
            default_value='true',
            description='Use simulation (Gazebo) clock if true'),

        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[{'use_sim_time': use_sim_time}],
            arguments=[urdf]),

        Node(
            package='joint_state_publisher',
            executable='joint_state_publisher',
            name='joint_state_publisher',
            output='screen',
            parameters=[{'use_sim_time': use_sim_time}],
            arguments=[urdf]),

            rviz,
    ])
