#!/usr/bin/env python3
# robot_with_frames.launch.py

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.conditions import IfCondition
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration
import os
import xacro
import xml.etree.ElementTree as ET


def unity_owned_sensor_description(robot_urdf):
    root = ET.fromstring(robot_urdf)
    joints = [joint for joint in root.findall("joint")
              if joint.find("child") is not None
              and joint.find("child").get("link") == "Velodyne_link"]
    links = [link for link in root.findall("link") if link.get("name") == "Velodyne_link"]
    if len(joints) != 1 or len(links) != 1:
        raise RuntimeError("Expected exactly one URDF Velodyne link and joint")
    if any(joint.find("parent") is not None
           and joint.find("parent").get("link") == "Velodyne_link"
           for joint in root.findall("joint")):
        raise RuntimeError("Cannot remove Velodyne_link with dependent URDF joints")
    root.remove(joints[0])
    root.remove(links[0])
    return ET.tostring(root, encoding="unicode")

def generate_launch_description():
    # Unity uses the simulation model, whose sensor axes match the Unity scene.
    xacro_path = os.path.join(
        '/home/rhobtor/PHD/j8_control/J8_control/src/gazebo_sim_pkgs',
        'j8_xacro_model_sim',
        'j8_xacro_model',
        'urdf',
        'argo_j8.xacro'
    )

    # Procesar el xacro → robot_description (XML)
    robot_description_config = xacro.process_file(xacro_path)
    robot_urdf = unity_owned_sensor_description(robot_description_config.toxml())

    # ======= Parámetro opcional para el alias Velodyne_link -> lidar_link =======
    use_lidar_alias_arg = DeclareLaunchArgument(
        'use_lidar_alias',
        default_value='true',
        description='Crear alias TF Velodyne_link -> lidar_link (identidad)'
    )
    use_lidar_alias = LaunchConfiguration('use_lidar_alias')

    # ======= Compatibilidad con frame "mmap" (si RViz lo usa como Fixed Frame) =======
    publish_mmap_alias_arg = DeclareLaunchArgument(
        'publish_mmap_alias',
        default_value='true',
        description='Publicar TF estático identidad mmap -> map para conectar ambos árboles'
    )
    publish_mmap_alias = LaunchConfiguration('publish_mmap_alias')

    # ========== NODOS ==========
    # Robot State Publisher (publica TF del URDF)
    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        output='screen',
        parameters=[{'robot_description': robot_urdf}]
    )

    # Joint State Publisher (si no tienes otro publicador de joints, fija a 0)
    joint_state_publisher_node = Node(
        package='joint_state_publisher',
        executable='joint_state_publisher',
        name='joint_state_publisher',
        output='screen',
        parameters=[{
            'use_gui': False,
            'robot_description': robot_urdf,
        }]
    )

    # map -> odom (identidad provisional)
    map_odom_tf = Node(
        package='tf2_ros',
        executable='static_transform_publisher',
        name='static_map_to_odom',
        arguments=[
            '--frame-id', 'map',
            '--child-frame-id', 'odom',
            '--x', '0', '--y', '0', '--z', '0',
            '--roll', '0', '--pitch', '0', '--yaw', '0',
        ],
        output='screen'
    )


    # Physical Unity front_camera mount, including J8_top scale and vertical offset.
    base_camera_tf = Node(
        package='tf2_ros',
        executable='static_transform_publisher',
        name='static_base_to_camera',
        arguments=[
            '--frame-id', 'base_link',
            '--child-frame-id', 'camera_link',
            '--x', '0.90528685', '--y', '0.00281843', '--z', '1.01813796',
            '--roll', '0', '--pitch', '0', '--yaw', '0',
        ],
        output='screen'
    )

    # (Opcional) alias Velodyne_link -> lidar_link (identidad)
    velodyne_to_lidar_alias = Node(
        package='tf2_ros',
        executable='static_transform_publisher',
        name='velodyne_to_lidar_alias',
        arguments=[
            '--frame-id', 'Velodyne_link',
            '--child-frame-id', 'lidar_link',
            '--x', '0', '--y', '0', '--z', '0',
            '--roll', '0', '--pitch', '0', '--yaw', '0',
        ],
        output='screen',
        condition=IfCondition(use_lidar_alias)
    )

    return LaunchDescription([
        use_lidar_alias_arg,
        publish_mmap_alias_arg,
        robot_state_publisher_node,
        joint_state_publisher_node,
        map_odom_tf,
        base_camera_tf,
        velodyne_to_lidar_alias,
    ])
