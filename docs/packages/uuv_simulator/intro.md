[![Build Status](https://travis-ci.org/uuvsimulator/uuv_simulator.svg?branch=dev%2Ftravis_integration)](https://travis-ci.org/uuvsimulator/uuv_simulator)
[![GitHub issues](https://img.shields.io/github/issues/uuvsimulator/uuv_simulator.svg)](https://github.com/uuvsimulator/uuv_simulator/issues)
[![License](https://img.shields.io/badge/license-Apache%202-blue.svg)](https://github.com/uuvsimulator/uuv_simulator/blob/master/LICENSE)

> Link to the `uuv_simulator` repository [here](https://github.com/uuvsimulator/uuv_simulator)

> Link to the [documentation page](https://uuvsimulator.github.io/) 

The **Unmanned Underwater Vehicle Simulator** is a set of packages that include plugins and ROS applications that allow simulation of underwater vehicles in [Gazebo](http://gazebosim.org/). 

# Features

> **Gazebo/ROS plugins**
  
- Implementation of Fossen's equations of motion for underwater vehicles
- Thruster modules with implementations for thruster's angular velocity to output thrust force based on [`Yoerger el al., 1990`](http://dx.doi.org/10.1109/48.107145) and [`Bessa et al., 2006`](http://www.abcm.org.br/symposium-series/SSM_Vol2/Section_IX_Submarine_Robotics/SSM2_IX_01.pdf)
- Lift and drag plugin for simulation of fins
- Simulation of 3D current velocity models (constant or based on first-order Gauss-Markov processes)
- Sensor plugins

> **Controllers**

- For AUVs
    - [`casadi`](https://web.casadi.org/)-based effort allocation algorithm 
    - Geometric tracking PD controller
- For ROVs
    - Thruster manager with computation of the thruster allocation matrix based on the thruster frames available in `/tf`
    - Model-based feedback linearization controller
    - Nonlinear PID controller
    - Non-model-based sliding mode controller
    - PD controller with restoration forces compensation 
    - 6-DOF PID controller
    - Singularity-free tracking controller
- Teleoperation nodes for AUVs and ROVs

> **Gazebo world models**

- Ocean wave shaders for wave animation
- Scenarios from the SWARMs project demonstration locations (e.g. Mangalia, Romania and Trondheim, Norway)
- Subsea BOP panel for manipulation tasks

> **Vehicle models**

- Work-class ROV `rexrov` based on the model presetend in [`Berg, 2012`](https://brage.bibsys.no/xmlui/handle/11250/238170?locale-attribute=no)
- [`eca_a9`](https://github.com/uuvsimulator/eca_a9)
- [`lauv_gazebo`](https://github.com/uuvsimulator/lauv_gazebo)
- [`desistek_saga`](https://github.com/uuvsimulator/desistek_saga)
- [`rexrov2`](https://github.com/uuvsimulator/rexrov2)
  
# Installation

This packages has been released for the following ROS distributions

- `kinetic` (See [installation instructions for ROS Kinetic](https://wiki.ros.org/kinetic/Installation/Ubuntu))
- `lunar` (See [installation instructions for ROS Kinetic](https://wiki.ros.org/lunar/Installation/Ubuntu))
- `melodic` (See [installation instructions for ROS Kinetic](https://wiki.ros.org/melodic/Installation/Ubuntu))

Once the `ros-<distro>-desktop-full` package for the desired distribution is installed, the uuv_simulator can be installed as

```bash tab="kinetic"
sudo apt install ros-kinetic-uuv-simulator
```

```bash tab="lunar"
sudo apt install ros-lunar-uuv-simulator
```

```bash tab="melodic"
sudo apt install ros-melodic-uuv-simulator
```

# Purpose of the project

This software is a research prototype, originally developed for the EU ECSEL
Project 662107 [SWARMs](http://swarms.eu/).

The software is not ready for production use. However, the license conditions of the
applicable Open Source licenses allow you to adapt the software to your needs.
Before using it in a safety relevant setting, make sure that the software
fulfills your requirements and adjust it according to any applicable safety
standards (e.g. ISO 26262).

# License

UUV Simulator is open-sourced under the Apache-2.0 license. See the
[LICENSE](https://github.com/uuvsimulator/uuv_simulator/blob/master/LICENSE) file for details.

For a list of other open source components included in UUV Simulator, see the
file [3rd-party-licenses.txt](https://github.com/uuvsimulator/uuv_simulator/blob/master/3rd-party-licenses.txt).

# Releases

[![ROS Kinetic](https://img.shields.io/badge/ROS%20Distro-kinetic-brightgreen.svg)](http://repositories.ros.org/status_page/ros_kinetic_default.html?q=uuv_simulator)
[![ROS Lunar](https://img.shields.io/badge/ROS%20Distro-lunar-brightgreen.svg)](http://repositories.ros.org/status_page/ros_lunar_default.html?q=uuv_simulator)
[![ROS Melodic](https://img.shields.io/badge/ROS%20Distro-melodic-brightgreen.svg)](http://repositories.ros.org/status_page/ros_melodic_default.html?q=uuv_simulator)