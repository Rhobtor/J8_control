# generated from rosidl_cmake/cmake/rosidl_cmake_aggregate_target-extras.cmake.in

# Create a convenience aggregate target security_check_interfaces::security_check_interfaces
# that links all generated interface targets, so downstream packages can use
# a single modern CMake target name instead of ${security_check_interfaces_TARGETS}.
if(security_check_interfaces_TARGETS AND NOT TARGET security_check_interfaces::security_check_interfaces)
  add_library(security_check_interfaces::security_check_interfaces INTERFACE IMPORTED)
  set_target_properties(security_check_interfaces::security_check_interfaces PROPERTIES
    INTERFACE_LINK_LIBRARIES "${security_check_interfaces_TARGETS}")
endif()
