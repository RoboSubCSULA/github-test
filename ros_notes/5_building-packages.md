## building your own package
If you followed the instructions from the previous page (4), then everything in this tutorial will look similar. Or rather, it should...
Go back if you missed something or skipped a step. Well need everything.

Go into the catkin workspace and list its contents:
```
$ cd ~/catkin_ws/
$ ls src
```

You should see that there is a folder called 'beginner_tutorials' which you created with 'catkin_create_pkg' in the previous tutorial. We can now build that package using catkin_make: 
```
$ catkin_make
```

My terminal only produced this result:
```
####
#### Running command: "make cmake_check_build_system" in "/home/sisyphus/catkin_ws/build"
####
####
#### Running command: "make -j4 -l4" in "/home/sisyphus/catkin_ws/build"
####
```

But the tutorials expected much more:
```
Base path: /home/user/catkin_ws
Source space: /home/user/catkin_ws/src
Build space: /home/user/catkin_ws/build
Devel space: /home/user/catkin_ws/devel
Install space: /home/user/catkin_ws/install
####
#### Running command: "cmake /home/user/catkin_ws/src
-DCATKIN_DEVEL_PREFIX=/home/user/catkin_ws/devel
-DCMAKE_INSTALL_PREFIX=/home/user/catkin_ws/install" in "/home/user/catkin_ws/build"
####
-- The C compiler identification is GNU 4.2.1
-- The CXX compiler identification is Clang 4.0.0
-- Checking whether C compiler has -isysroot
-- Checking whether C compiler has -isysroot - yes
-- Checking whether C compiler supports OSX deployment target flag
-- Checking whether C compiler supports OSX deployment target flag - yes
-- Check for working C compiler: /usr/bin/gcc
-- Check for working C compiler: /usr/bin/gcc -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working CXX compiler: /usr/bin/c++
-- Check for working CXX compiler: /usr/bin/c++ -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Using CATKIN_DEVEL_PREFIX: /tmp/catkin_ws/devel
-- Using CMAKE_PREFIX_PATH: /opt/ros/kinetic
-- This workspace overlays: /opt/ros/kinetic
-- Found PythonInterp: /usr/bin/python (found version "2.7.1") 
-- Found PY_em: /usr/lib/python2.7/dist-packages/em.pyc
-- Found gtest: gtests will be built
-- catkin 0.5.51
-- BUILD_SHARED_LIBS is on
-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
-- ~~  traversing packages in topological order:
-- ~~  - beginner_tutorials
-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
-- +++ add_subdirectory(beginner_tutorials)
-- Configuring done
-- Generating done
-- Build files have been written to: /home/user/catkin_ws/build
####
#### Running command: "make -j4" in "/home/user/catkin_ws/build"
####
```
If this discrepancy still exist when you read it that means :
1. I ignored this difference and kept going
2. there wasn't anything wrong, after all


catkin_make should display what paths it is using for each of the 'spaces'. More importantly, notivce that several folders have been created in your catkin workspace. go to it and use ls.

- the build folder is the default location of the 'build space'
- it is also where 'cmake' and 'make' are called to build your packages
- 'devel' is where execuatables and libraries go before you install packages

The next step is [ROS Nodes](http://wiki.ros.org/ROS/Tutorials/UnderstandingNodes).
