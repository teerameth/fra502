import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.actions.execute_process import ExecuteProcess
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():

    use_sim_time = LaunchConfiguration('use_sim_time', default='true')
    
    pkg_fra502 = get_package_share_directory('fra502')

    world_file_name = 'test.world'
    print("world_file_name : {}".format(world_file_name))
    
    world = os.path.join(
        pkg_fra502,
        world_file_name)

    gz = ExecuteProcess(
        cmd=['gazebo', '--verbose', '-s', 'libgazebo_ros_factory.so', world],
        output='screen')
    
    cam = Node(
        package = 'image_view',
        node_executable = 'image_view',
        arguments = ['image:=/camera1/image_raw'],
        output = "screen")

    return LaunchDescription([
        gz,
        cam
    ])
