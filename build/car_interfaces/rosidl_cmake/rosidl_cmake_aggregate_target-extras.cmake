# generated from rosidl_cmake/cmake/rosidl_cmake_aggregate_target-extras.cmake.in

# Create a convenience aggregate target car_interfaces::car_interfaces
# that links all generated interface targets, so downstream packages can use
# a single modern CMake target name instead of ${car_interfaces_TARGETS}.
if(car_interfaces_TARGETS AND NOT TARGET car_interfaces::car_interfaces)
  add_library(car_interfaces::car_interfaces INTERFACE IMPORTED)
  set_target_properties(car_interfaces::car_interfaces PROPERTIES
    INTERFACE_LINK_LIBRARIES "${car_interfaces_TARGETS}")
endif()
