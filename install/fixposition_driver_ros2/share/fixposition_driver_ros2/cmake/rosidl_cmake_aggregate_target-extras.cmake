# generated from rosidl_cmake/cmake/rosidl_cmake_aggregate_target-extras.cmake.in

# Create a convenience aggregate target fixposition_driver_ros2::fixposition_driver_ros2
# that links all generated interface targets, so downstream packages can use
# a single modern CMake target name instead of ${fixposition_driver_ros2_TARGETS}.
if(fixposition_driver_ros2_TARGETS AND NOT TARGET fixposition_driver_ros2::fixposition_driver_ros2)
  add_library(fixposition_driver_ros2::fixposition_driver_ros2 INTERFACE IMPORTED)
  set_target_properties(fixposition_driver_ros2::fixposition_driver_ros2 PROPERTIES
    INTERFACE_LINK_LIBRARIES "${fixposition_driver_ros2_TARGETS}")
endif()
