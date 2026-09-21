# generated from rosidl_cmake/cmake/rosidl_cmake_aggregate_target-extras.cmake.in

# Create a convenience aggregate target path_manager_interfaces::path_manager_interfaces
# that links all generated interface targets, so downstream packages can use
# a single modern CMake target name instead of ${path_manager_interfaces_TARGETS}.
if(path_manager_interfaces_TARGETS AND NOT TARGET path_manager_interfaces::path_manager_interfaces)
  add_library(path_manager_interfaces::path_manager_interfaces INTERFACE IMPORTED)
  set_target_properties(path_manager_interfaces::path_manager_interfaces PROPERTIES
    INTERFACE_LINK_LIBRARIES "${path_manager_interfaces_TARGETS}")
endif()
