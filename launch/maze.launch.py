from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, SetEnvironmentVariable
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():

    # Tell simulation to use the burger model
    set_tb3 = SetEnvironmentVariable(
        name='TURTLEBOT3_MODEL',
        value='burger'
    )

    # Path to your custom world
    world_file = os.path.join(
        get_package_share_directory('tb3_maze_sim'),
        'worlds',
        'z.world'
    )

    # Package directories
    gazebo_ros = get_package_share_directory('gazebo_ros')
    tb3_gazebo = get_package_share_directory('turtlebot3_gazebo')

    # START SERVER WITH CUSTOM WORLD
    gzserver = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(gazebo_ros, 'launch', 'gzserver.launch.py')
        ),
        launch_arguments={'world': world_file}.items()
    )

    # GAZEBO CLIENT (GUI)
    gzclient = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(gazebo_ros, 'launch', 'gzclient.launch.py')
        )
    )

    # ROBOT STATE PUBLISHER
    robot_state_pub = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(tb3_gazebo, 'launch', 'robot_state_publisher.launch.py')
        ),
        launch_arguments={'use_sim_time': 'true'}.items()
    )

    # SPAWN TURTLEBOT3
    spawn_robot = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(tb3_gazebo, 'launch', 'spawn_turtlebot3.launch.py')
        ),
        launch_arguments={
            'x_pose': '7.0',
            'y_pose': '-9.1',
            'yaw': '3.14159'

        }.items()
    )

    return LaunchDescription([
        set_tb3,
        gzserver,
        gzclient,
        robot_state_pub,
        spawn_robot
    ])
