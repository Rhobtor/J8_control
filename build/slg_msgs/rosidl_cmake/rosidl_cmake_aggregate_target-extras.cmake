# generated from rosidl_cmake/cmake/rosidl_cmake_aggregate_target-extras.cmake.in

# Create a convenience aggregate target slg_msgs::slg_msgs
# that links all generated interface targets, so downstream packages can use
# a single modern CMake target name instead of ${slg_msgs_TARGETS}.
if(slg_msgs_TARGETS AND NOT TARGET slg_msgs::slg_msgs)
  add_library(slg_msgs::slg_msgs INTERFACE IMPORTED)
  set_target_properties(slg_msgs::slg_msgs PROPERTIES
    INTERFACE_LINK_LIBRARIES "${slg_msgs_TARGETS}")
endif()
