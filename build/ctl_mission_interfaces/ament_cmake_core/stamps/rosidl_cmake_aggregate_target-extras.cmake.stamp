# generated from rosidl_cmake/cmake/rosidl_cmake_aggregate_target-extras.cmake.in

# Create a convenience aggregate target ctl_mission_interfaces::ctl_mission_interfaces
# that links all generated interface targets, so downstream packages can use
# a single modern CMake target name instead of ${ctl_mission_interfaces_TARGETS}.
if(ctl_mission_interfaces_TARGETS AND NOT TARGET ctl_mission_interfaces::ctl_mission_interfaces)
  add_library(ctl_mission_interfaces::ctl_mission_interfaces INTERFACE IMPORTED)
  set_target_properties(ctl_mission_interfaces::ctl_mission_interfaces PROPERTIES
    INTERFACE_LINK_LIBRARIES "${ctl_mission_interfaces_TARGETS}")
endif()
