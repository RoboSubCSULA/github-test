[Publishers and Subscribers](http://wiki.ros.org/ROS/Tutorials/WritingPublisherSubscriber%28python%29)
*On the link itself, you can skip steps 1-2 if you followed the previous steps. For step 3, we created the workspace already, but you need to read that part.*

## Writing the Publisher Node
'Node' is the ROS term for an executable on the network. Publishers "talk" so we  will create a publisher which continually broadcast a message. 

-[] demonstate how to use the `catkin_create_pkg`
-[] what you can do with it, after creation

- change to the source space directory of the catkin workspace you created `cd ~/catkin_ws/src`
- use 'catkin_create_pkg' to create a new folder called 'beginner_tutorials' `catkin_create_pkg beginner_tutorials std_msgs rospy roscpp`
- std_msgs, rospy, roscpp are dependencies

## build a catkin workspace\source the setup file
- build packages in the catkin workspace
```
$ cd ~/catkin_ws
$ catkin_make

the output :
####
#### Running command: "cmake /home/sisyphus/catkin_ws/src -DCATKIN_DEVEL_PREFIX=/home/sisyphus/catkin_ws/devel -DCMAKE_INSTALL_PREFIX=/home/sisyphus/catkin_ws/install -G Unix Makefiles" in "/home/sisyphus/catkin_ws/build"
####
-- Using CATKIN_DEVEL_PREFIX: /home/sisyphus/catkin_ws/devel
-- Using CMAKE_PREFIX_PATH: /opt/ros/melodic
-- This workspace overlays: /opt/ros/melodic
-- Found PythonInterp: /usr/bin/python2 (found suitable version "2.7.17", minimum required is "2") 
-- Using PYTHON_EXECUTABLE: /usr/bin/python2
-- Using Debian Python package layout
-- Using empy: /usr/bin/empy
-- Using CATKIN_ENABLE_TESTING: ON
-- Call enable_testing()
-- Using CATKIN_TEST_RESULTS_DIR: /home/sisyphus/catkin_ws/build/test_results
-- Found gtest sources under '/usr/src/googletest': gtests will be built
-- Found gmock sources under '/usr/src/googletest': gmock will be built
-- Found PythonInterp: /usr/bin/python2 (found version "2.7.17") 
-- Using Python nosetests: /usr/bin/nosetests-2.7
-- catkin 0.7.20
-- BUILD_SHARED_LIBS is on
-- BUILD_SHARED_LIBS is on
-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
-- ~~  traversing 1 packages in topological order:
-- ~~  - beginner_tutorials
-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
-- +++ processing catkin package: 'beginner_tutorials'
-- ==> add_subdirectory(beginner_tutorials)
-- Configuring done
-- Generating done
-- Build files have been written to: /home/sisyphus/catkin_ws/build
####
#### Running command: "make -j4 -l4" in "/home/sisyphus/catkin_ws/build"
####
```

- ROS creates a structure in the `devel` subfolder
- add the workspacce to your ROS environment
`$ . ~/catkin_ws/devel/setup.bash`
- don't miss that period, you are SOURCING the bash, not making executable

## package dependencies
#### first-order dependecies
The `rospack` tool : first-order dependencies can be review
```
$ rospack depends1 beginner_tutorials
----results you should see
roscpp
rospy
std_msgs
```

The same dependencies we used as arguments when running `catkin_create_pkg` are the same ones you see listed. These dependencies are stored in `package.xml`. Lets go take a look :
```
$ roscd beginner_tutorials
$ cat package.xml
```

#### indirect dependencies
"yo dawg, I heard you like dependencies so i put dependencies in your dependencies!"
- only if your curious about this part, else skip.
`$ rospack depends1 rospy`
- all the dependencies that 'rospy' would depend on

**recursively determine all nested dependencies**
`$ rospack depends1 <package>`

## customizing your package (#10 on ros tutorials)
This part is huge, but the part of the work we need to do is minimal. Still, we need to look at the 'package.xml' file line-by-line so that we can customize our package.

#### description tag
- line 5:   <description>The beginner_tutorials package</description>
    - the description should state what it is in a single sentence

#### maintainer tag
- lines 7-10: lets others know who to contact
- you can have as many as you want, but you need at least 1
- name of the maintainer\user goes into the body, but the email is filled inside the tag.
```
   7   <!-- One maintainer tag required, multiple allowed, one person per tag --> 
   8   <!-- Example:  -->
   9   <!-- <maintainer email="jane.doe@example.com">Jane Doe</maintainer> -->
  10   <maintainer email="user@todo.todo"> user </maintainer>
```

#### license tag
- also required
- ROS componenets use certain licenses, so they're already included
```
  12   <!-- One license tag required, multiple allowed, one license per tag -->
  13   <!-- Commonly used license strings: -->
  14   <!--   BSD, MIT, Boost Software License, GPLv2, GPLv3, LGPLv2.1, LGPLv3 -->
  15   <license>TODO</license>\
```

#### dependencies tag
[Catkin Dependencies](http://wiki.ros.org/catkin/package.xml#Build.2C_Run.2C_and_Test_Dependencies) are split into : `build_depend, buildtool_depend   , exec_depend, test_depend`. See the link for more info.

Since we passed `std_msgs, roscpp, rospy`, our dependencies will look like this:
```
  27   <!-- The *_depend tags are used to specify dependencies -->
  28   <!-- Dependencies can be catkin packages or system dependencies -->
  29   <!-- Examples: -->
  30   <!-- Use build_depend for packages you need at compile time: -->
  31   <!--   <build_depend>genmsg</build_depend> -->
  32   <!-- Use buildtool_depend for build tool packages: -->
  33   <!--   <buildtool_depend>catkin</buildtool_depend> -->
  34   <!-- Use exec_depend for packages you need at runtime: -->
  35   <!--   <exec_depend>python-yaml</exec_depend> -->
  36   <!-- Use test_depend for packages you need only for testing: -->
  37   <!--   <test_depend>gtest</test_depend> -->
  38   <buildtool_depend>catkin</buildtool_depend>
  39   <build_depend>roscpp</build_depend>
  40   <build_depend>rospy</build_depend>
```

We still want all of our specified dependencies to be available at build and run time, so we need a `exec_depend` tag for each of them as well :
```
  12   <buildtool_depend>catkin</buildtool_depend>
  13 
  14   <build_depend>roscpp</build_depend>
  15   <build_depend>rospy</build_depend>
  16   <build_depend>std_msgs</build_depend>
  17 
  18   <exec_depend>roscpp</exec_depend>
  19   <exec_depend>rospy</exec_depend>
  20   <exec_depend>std_msgs</exec_depend>
```

#### admire my package
- once you have the tags filled out, you can remove any comments or unused tags
- the result is much more concise
```
   1 <?xml version="1.0"?>
   2 <package format="2">
   3   <name>beginner_tutorials</name>
   4   <version>0.1.0</version>
   5   <description>The beginner_tutorials package</description>
   6 
   7   <maintainer email="you@yourdomain.tld">Your Name</maintainer>
   8   <license>BSD</license>
   9   <url type="website">http://wiki.ros.org/beginner_tutorials</url>
  10   <author email="you@yourdomain.tld">Jane Doe</author>
  11 
  12   <buildtool_depend>catkin</buildtool_depend>
  13 
  14   <build_depend>roscpp</build_depend>
  15   <build_depend>rospy</build_depend>
  16   <build_depend>std_msgs</build_depend>
  17 
  18   <exec_depend>roscpp</exec_depend>
  19   <exec_depend>rospy</exec_depend>
  20   <exec_depend>std_msgs</exec_depend>
  21 
  22 </package>
```

Your 'package.xml' contains meta information tailored to your package. You can now move on and build a [ROS package](http://wiki.ros.org/ROS/Tutorials/BuildingPackages).

*there is still the "Customizing the CMakeLists.txt" but that is covered in a later tutorial.*