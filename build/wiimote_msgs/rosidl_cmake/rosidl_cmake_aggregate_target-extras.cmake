# generated from rosidl_cmake/cmake/rosidl_cmake_aggregate_target-extras.cmake.in

# Create a convenience aggregate target wiimote_msgs::wiimote_msgs
# that links all generated interface targets, so downstream packages can use
# a single modern CMake target name instead of ${wiimote_msgs_TARGETS}.
if(wiimote_msgs_TARGETS AND NOT TARGET wiimote_msgs::wiimote_msgs)
  add_library(wiimote_msgs::wiimote_msgs INTERFACE IMPORTED)
  set_target_properties(wiimote_msgs::wiimote_msgs PROPERTIES
    INTERFACE_LINK_LIBRARIES "${wiimote_msgs_TARGETS}")
endif()
