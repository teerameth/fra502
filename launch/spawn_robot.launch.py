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

    # xacro_file = os.path.join(get_package_share_directory('fra502'), 'tratsah.xacro')
    # assert os.path.exists(xacro_file), "tratsah.urdf doesnt exist in "+str(xacro_file)

    # robot_description_config = xacro.process_file(xacro_file)
    # robot_desc = robot_description_config.toxml()
    # print(robot_desc)

    # urdf_file_name = 'tratsah.urdf'
    urdf_file_name = 'omni_tratsah.urdf'

    print("urdf_file_name : {}".format(urdf_file_name))
    
    urdf = os.path.join(
        pkg_fra502,
        urdf_file_name)

    spawn_entity = Node(
        package = 'gazebo_ros',
        node_executable = 'spawn_entity.py',
        arguments = ['-entity', 'tratsah', '-file', urdf, "-x -1.0", "-y -1.0", "-z 0.0"],
        output = "screen")

    return LaunchDescription([
        spawn_entity
    ])
