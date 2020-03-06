 ## catkin workspaces
 A catkin workspace is a folder where you modify, build, and install catkin packages. A catkin workspace can contain up to four different spaces which each serve a different role in the software development process.

Build a catkin workspace :

    $ mkdir -p ~/catkin_ws/src
    $ cd ~/catkin_ws/
    $ catkin_make

**Source Space**
- source space contains the source code of catkin packages
- extract/checkout/clone source code for the packakes you want to build
- each folder within the source space contains one or more catkin packages
- *do not* change\edit\install anything in the source space
- the root of the space contains a link to CMakeLists.txt, invoked by cmake
- it can be created by calling catkin_init_workspace

**Build Space**
- build space is where `cmake` is invoked to build catkin
- `cmake` and `catkin` keep their cache information here
- it is recommened that build space be contained within the workspace

**Development Space**
- this is where build targets are placed prior to being installed
- provides a useful testing and development environment which does not require invoking the installation step
- - it is recommened to set the devel space directory to be a peer of the `build space` directory

**Install Space**
- once targets are built, they can be installed by invoking the install space, usually with `make install`

**Result Space**
- when referring to a folder which can either be development or install space the generic term result space is used.