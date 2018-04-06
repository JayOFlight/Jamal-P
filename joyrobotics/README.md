# Usage
```
$ cd
$ mkdir -p rmc_ws/src
$ cd rmc_wc/src
$ git clone https://github.com/YorkAstrobotics/joyrobocode-1.git
$ cd ..
$ catkin build
$ source devel/setup.bash
$ roscore &
$ rosrun joy joy_node &
$ rosrun joyrobotics roboteq_joy.py
```
