# generated from rosidl_cmake/cmake/rosidl_cmake_aggregate_target-extras.cmake.in

# Create a convenience aggregate target hector_gazebo_plugins::hector_gazebo_plugins
# that links all generated interface targets, so downstream packages can use
# a single modern CMake target name instead of ${hector_gazebo_plugins_TARGETS}.
if(hector_gazebo_plugins_TARGETS AND NOT TARGET hector_gazebo_plugins::hector_gazebo_plugins)
  add_library(hector_gazebo_plugins::hector_gazebo_plugins INTERFACE IMPORTED)
  set_target_properties(hector_gazebo_plugins::hector_gazebo_plugins PROPERTIES
    INTERFACE_LINK_LIBRARIES "${hector_gazebo_plugins_TARGETS}")
endif()
