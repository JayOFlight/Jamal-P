cmake_minimum_required(VERSION 2.8.3)
project(joyrobotics)

## Compile as C++11, supported in ROS Kinetic and newer
# add_compile_options(-std=c++11)

## Find catkin macros and libraries
## if COMPONENTS list like find_package(catkin REQUIRED COMPONENTS xyz)
## is used, also find other catkin packages
find_package(catkin REQUIRED COMPONENTS
  joy
  std_msgs
  sensor_msgs
)
include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)
catkin_package()
catkin_install_python(PROGRAMS
  nodes/roboteq_joy.py
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)
