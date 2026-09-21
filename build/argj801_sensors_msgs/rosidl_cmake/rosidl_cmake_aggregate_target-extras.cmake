# generated from rosidl_cmake/cmake/rosidl_cmake_aggregate_target-extras.cmake.in

# Create a convenience aggregate target argj801_sensors_msgs::argj801_sensors_msgs
# that links all generated interface targets, so downstream packages can use
# a single modern CMake target name instead of ${argj801_sensors_msgs_TARGETS}.
if(argj801_sensors_msgs_TARGETS AND NOT TARGET argj801_sensors_msgs::argj801_sensors_msgs)
  add_library(argj801_sensors_msgs::argj801_sensors_msgs INTERFACE IMPORTED)
  set_target_properties(argj801_sensors_msgs::argj801_sensors_msgs PROPERTIES
    INTERFACE_LINK_LIBRARIES "${argj801_sensors_msgs_TARGETS}")
endif()
