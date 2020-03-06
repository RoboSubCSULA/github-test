What you will need to start and begin the tutorials :
- [ ] I feel comfortable with the terminal
- [ ] I have Ubuntu 18.04 bionic (x86-64) installed
- [ ] I am comfortable with python

where you can go to learn : 
1. unix tutorial - http://www.ee.surrey.ac.uk/Teaching/Unix/
2. Ubuntu - http://wiki.ros.org/melodic/Installation
3. online tutorials, convert any programs you've built into .py files

## Install ROS Melodic Morenia (as of Spring 2020)
Once you have the above, go here :
`http://wiki.ros.org/ROS/Installation`

The following steps are taken from the link above. They are condensed, and simplified. If you want to know the reason why a step is required, feel free to explore the links above:

**Installation**
I didn't have to do this step but just in case :
    
- Configure your Ubuntu repositories to allow "restricted," "universe," and "multiverse." 
- You can follow `https://help.ubuntu.com/community/Repositories/Ubuntu` for instructions on doing this. 
    
Open your terminal, do the following :

a. accept software from packsages.ros.org

    `sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'`

b. set up your keys

    `sudo apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654`

c. make sure Ubuntu is up to date :

    `sudo apt update`

d. do a full installation : 

    `sudo apt install ros-melodic-desktop-full`

**Set up your environment**

a. set up your ros dependencies to run core components in ROS

    sudo rosdep init
    rosdep update
b. add ROS environment variables automatically to your bash session

    echo "source /opt/ros/melodic/setup.bash" >> ~/.bashrc
    source ~/.bashrc

    or you can change the enviroment of the current shell
    source /opt/ros/melodic/setup.bash
c. if you use zsh instead of bash (generated errors for me though) :
    
    ```
    echo "source /opt/ros/melodic/setup.zsh" >> ~/.zshrc
    source ~/.zshrc
    ```
d. make sure your environment is set up properly, run :

`$ printenv | grep ROS` and see the following output

    ROS_ETC_DIR=/opt/ros/melodic/etc/ros
    ROS_ROOT=/opt/ros/melodic/share/ros
    ROS_MASTER_URI=http://localhost:11311
    ROS_VERSION=1
    ROS_PYTHON_VERSION=2
    ROS_PACKAGE_PATH=/opt/ros/melodic/share
    ROSLISP_PACKAGE_DIRECTORIES=
    ROS_DISTRO=melodic

You can now proceed to [http://wiki.ros.org/ROS/Tutorials](http://wiki.ros.org/ROS/Tutorials)

note: 
- in the tutorials you will see rosbuild and catkin, use catkin
    + read more about it here http://wiki.ros.org/catkin_or_rosbuild
