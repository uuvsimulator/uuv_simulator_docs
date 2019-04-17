We assume you are using at least Ubuntu 14.04.4 LTS and ROS Indigo, even though the simulator package should also work with later versions (minor adjustments may be required). Please refer to the installation instructions for

- [`indigo`](http://wiki.ros.org/indigo/Installation/Ubuntu)
- [`kinetic`](http://wiki.ros.org/kinetic/Installation/Ubuntu)
- [`melodic`](http://wiki.ros.org/melodic/Installation/Ubuntu)

The `uuv_simulator` package has currently been released for `kinetic`, `lunar` and `melodic`. To install all the packages, run 

```bash
sudo apt install ros-kinetic-uuv-simulator
```

or 

```bash
sudo apt install ros-lunar-uuv-simulator
```

or 

```bash
sudo apt install ros-melodic-uuv-simulator
```

# Installation from source

## Dependencies

Checkout below the needed dependencies for ROS `indigo`, `kinetic` and `melodic`. 
Choose the ones you need according to the ROS version you are using. 
It is recommended to also install [`catkin_tools`](https://catkin-tools.readthedocs.io/en/latest/installing.html).

### Using `uuv_simulator` with `indigo` and Gazebo 7

* To install ROS Indigo, first follow the installation instructions in this [wiki page](http://wiki.ros.org/indigo/Installation/Ubuntu) and choose the installation of the `ros-indigo-desktop-full` package.

* Follow the instructions from the [Gazebo 7 installation tutorial](http://gazebosim.org/tutorials?cat=install&tut=install_ubuntu&ver=7.0)

* Install the necessary ROS packages for Gazebo 7 

```bash
sudo apt-get install ros-indigo-gazebo7-*
```

* Some extra packages that might also be needed

```
sudo apt-get install protobuf-compiler protobuf-c-compiler
```

!!! info

    To use the vehicles with robotic manipulators using `indigo`, it might also be necessary to use a different version of the `ros-control` modules (listed below). In that case, clone the following repositories in the `src` folder 

    ```
    git clone https://github.com/ros-controls/control_msgs.git
    cd control_msgs
    git checkout c0b322b
    cd ..

    git clone https://github.com/ros-controls/control_toolbox.git
    cd control_toolbox
    git checkout 5ccdc6d
    cd ..

    git clone https://github.com/ros-simulation/gazebo_ros_pkgs.git
    cd gazebo_ros_pkgs
    git checkout 231b76d
    cd ..

    git clone https://github.com/ros-controls/realtime_tools.git
    cd realtime_tools
    git checkout bf55298
    cd ..

    git clone https://github.com/ros-controls/ros_controllers.git
    cd ros_controllers
    git checkout b4dc152
    cd ..
    ```

### Using `uuv_simulator` with `kinetic` and Gazebo 7

* If you installed `ros-kinetic-desktop-full` after following the [installation instructions for ROS Kinetic](http://wiki.ros.org/kinetic/Installation/Ubuntu), Gazebo 7.0 should already be installed.

* In case you want to update Gazebo 7, follow the [instructions to add the mirror from OSRF](http://gazebosim.org/tutorials?cat=install&tut=install_ubuntu&ver=7.0) and then upgrade `gazebo7` and `libgazebo7-dev`

```bash
sudo apt-get install --only-upgrade gazebo7 libgazebo7-dev
```

### Using `uuv_simulator` with `kinetic` and Gazebo 9

* Install the package `ros-kinetic-desktop-full` following these [installation instructions](http://wiki.ros.org/kinetic/Installation/Ubuntu). 

* Follow the [installation instructions for Gazebo 9 in this wiki page](http://gazebosim.org/tutorials?cat=install&tut=install_ubuntu&ver=9.0).

* Install the additional packages necessary to work with `kinetic` and Gazebo 9

```bash
sudo apt-get install ros-kinetic-gazebo9-*
```

### Using `uuv_simulator` with `melodic` and Gazebo 9

## Creating and configuring a workspace

If you don't have the ROS workspace yet, you should run the following and then clone the `uuv_simulator` package in the `~/catkin_ws/src` folder

```bash
mkdir -p ~/catkin_ws/src
cd ~/catkin_ws/src
```

Be sure to install `catkin tools` package by following the installation instructions on the [catkin tools documentation page](https://catkin-tools.readthedocs.io/en/latest/installing.html). After the installation, initialize the catkin workspace

```bash
cd ~/catkin_ws
catkin init
```

You can then clone the UUV simulator into your `src` folder

```bash
cd ~/catkin_ws/src
git clone https://github.com/uuvsimulator/uuv_simulator.git
```

Configure the environment variables by adding the following lines in `~/.bashrc` (replace `kinetic` with the ROS version you are using).

!!! info

    If you install a version of Gazebo newer than 7.X, you might need to adjust `gazebo-7` below (e.g. `gazebo-9`).
    You can find out which version you are using by typing
    
    ```
    gazebo --version
    ```

    in your terminal.

```bash
source /usr/share/gazebo-7/setup.sh
source /opt/ros/kinetic/setup.bash
source $HOME/catkin_ws/devel/setup.bash
```

After saving these changes, remember to source the `.bashrc` by either typing

```bash
source ~/.bashrc
```

## Installation

To install the simulator's dependencies, you can run one of the following commands (see which of the ROS/Gazebo combinations from dependencies you have on your machine):

* For `indigo` + Gazebo 7

```bash
cd ~/catkin_ws
rosdep install --from-paths src --ignore-src --rosdistro=indigo -y --skip-keys "gazebo gazebo_msgs gazebo_plugins gazebo_ros gazebo_ros_control gazebo_ros_pkgs"
```

* For `kinetic` + Gazebo 7 

```bash
cd ~/catkin_ws
rosdep install --from-paths src --ignore-src --rosdistro=kinetic -y
```

* For `kinetic` + Gazebo 9 

```bash
cd ~/catkin_ws
rosdep install --from-paths src --ignore-src --rosdistro=kinetic -y --skip-keys "gazebo gazebo_msgs gazebo_plugins gazebo_ros gazebo_ros_control gazebo_ros_pkgs"
```

!!! info

    In case you are using `lunar`, you might need to clone the following repositories directly to your `~/catkin_ws/src` folder and build them with the rest of the packages
    ```bash
    cd ~/catkin/src
    git clone https://github.com/tu-darmstadt-ros-pkg/hector_localization 
    git clone https://github.com/ros-teleop/teleop_tools
    ```

Finally, build your workspace using 

```bash
cd ~/catkin_ws
catkin_make install
```

or 

```bash
cd ~/catkin_ws
catkin build
```

in case you are using `catkin_tools`.

!!! tip

    If after compiling your catkin workspace using `catkin build` ROS seems to not update the paths to the packages even after you run
    
    ```bash
    cd ~/catkin_ws
    source devel/setup.bash
    ```
    
    you can try disabling the option to source the `install` folder of your catkin workspace by running
    ```bash
    cd ~/catkin_ws
    catkin config --no-install
    catkin clean --all
    ```

    Then rebuild your workspace 
    ```bash
    catkin build
    source devel/setup.bash
    ```