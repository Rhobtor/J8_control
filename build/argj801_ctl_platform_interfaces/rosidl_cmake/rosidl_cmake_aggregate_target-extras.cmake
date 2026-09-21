# generated from rosidl_cmake/cmake/rosidl_cmake_aggregate_target-extras.cmake.in

# Create a convenience aggregate target argj801_ctl_platform_interfaces::argj801_ctl_platform_interfaces
# that links all generated interface targets, so downstream packages can use
# a single modern CMake target name instead of ${argj801_ctl_platform_interfaces_TARGETS}.
if(argj801_ctl_platform_interfaces_TARGETS AND NOT TARGET argj801_ctl_platform_interfaces::argj801_ctl_platform_interfaces)
  add_library(argj801_ctl_platform_interfaces::argj801_ctl_platform_interfaces INTERFACE IMPORTED)
  set_target_properties(argj801_ctl_platform_interfaces::argj801_ctl_platform_interfaces PROPERTIES
    INTERFACE_LINK_LIBRARIES "${argj801_ctl_platform_interfaces_TARGETS}")
endif()
