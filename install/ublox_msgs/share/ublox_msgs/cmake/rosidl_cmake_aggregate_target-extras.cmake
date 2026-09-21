# generated from rosidl_cmake/cmake/rosidl_cmake_aggregate_target-extras.cmake.in

# Create a convenience aggregate target ublox_msgs::ublox_msgs
# that links all generated interface targets, so downstream packages can use
# a single modern CMake target name instead of ${ublox_msgs_TARGETS}.
if(ublox_msgs_TARGETS AND NOT TARGET ublox_msgs::ublox_msgs)
  add_library(ublox_msgs::ublox_msgs INTERFACE IMPORTED)
  set_target_properties(ublox_msgs::ublox_msgs PROPERTIES
    INTERFACE_LINK_LIBRARIES "${ublox_msgs_TARGETS}")
endif()
