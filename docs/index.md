[![License](https://img.shields.io/badge/license-Apache%202-blue.svg)](about/license.md)

The UUV Simulator is a package containing the implementation of Gazebo plugins and ROS nodes necessary for the simulation of unmanned underwater vehicles, such as ROVs (remotely operated vehicles) and AUVs (autonomous underwater vehicles).

To send questions and/or issues, please refer to the [repository’s issues page](https://github.com/uuvsimulator/uuv_simulator/issues).

# Purpose of the project

This software is a research prototype, originally developed for the EU ECSEL
Project 662107 [SWARMs](http://swarms.eu/).

The software is not ready for production use. However, the license conditions of the applicable Open Source licenses allow you to adapt the software to your needs.
Before using it in a safety relevant setting, make sure that the software
fulfills your requirements and adjust it according to any applicable safety
standards (e.g. ISO 26262).

# Reference

If you wish to use the UUV Simulator in a research project, please cite our paper 

```
@inproceedings{Manhaes_2016,
    doi = {10.1109/oceans.2016.7761080},
    url = {https://doi.org/10.1109%2Foceans.2016.7761080},
    year = 2016,
    month = {sep},
    publisher = {{IEEE}},
    author = {Musa Morena Marcusso Manh{\~{a}}es and Sebastian A. Scherer and Martin Voss and Luiz Ricardo Douat and Thomas Rauschenbach},
    title = {{UUV} Simulator: A Gazebo-based package for underwater intervention and multi-robot simulation},
    booktitle = {{OCEANS} 2016 {MTS}/{IEEE} Monterey}
}
```

# List of repositories

Name | Documentation | Releases | CI | Issues 
---|---|---|---|---
[`uuv_simulator`](https://github.com/uuvsimulator/uuv_simulator) | [![Documentation](https://img.shields.io/badge/read-the%20docs-blue.svg)](packages/uuv_simulator/intro.md) | [![ROS Kinetic](https://img.shields.io/badge/ROS-kinetic-brightgreen.svg)](http://repositories.ros.org/status_page/ros_kinetic_default.html?q=uuv_simulator) [![ROS Lunar](https://img.shields.io/badge/ROS-lunar-brightgreen.svg)](http://repositories.ros.org/status_page/ros_lunar_default.html?q=uuv_simulator) [![ROS Melodic](https://img.shields.io/badge/ROS-melodic-brightgreen.svg)](http://repositories.ros.org/status_page/ros_melodic_default.html?q=uuv_simulator) | [![Build Status](https://travis-ci.org/uuvsimulator/uuv_simulator.svg?branch=dev%2Ftravis_integration)](https://travis-ci.org/uuvsimulator/uuv_simulator) | [![GitHub issues](https://img.shields.io/github/issues/uuvsimulator/uuv_simulator.svg)](https://github.com/uuvsimulator/uuv_simulator/issues)
[`uuv_plume_simulator`](https://github.com/uuvsimulator/uuv_plume_simulator) | [![Documentation](https://img.shields.io/badge/read-the%20docs-blue.svg)](packages/uuv_plume_simulator/intro.md) | | [![Build Status](https://travis-ci.org/uuvsimulator/uuv_plume_simulator.svg?branch=master)](https://travis-ci.org/uuvsimulator/uuv_plume_simulator) | [![GitHub issues](https://img.shields.io/github/issues/uuvsimulator/uuv_plume_simulator.svg)](https://github.com/uuvsimulator/uuv_plume_simulator/issues)
[`rexrov2`](https://github.com/uuvsimulator/rexrov2) | [![Documentation](https://img.shields.io/badge/read-the%20docs-blue.svg)](packages/rexrov2/intro.md) | [![ROS Kinetic](https://img.shields.io/badge/ROS-kinetic-brightgreen.svg)](http://repositories.ros.org/status_page/ros_kinetic_default.html?q=rexrov2) [![ROS Melodic](https://img.shields.io/badge/ROS-melodic-brightgreen.svg)](http://repositories.ros.org/status_page/ros_melodic_default.html?q=rexrov2) | [![Build Status](https://travis-ci.org/uuvsimulator/rexrov2.svg?branch=master)](https://travis-ci.org/uuvsimulator/rexrov2) | [![GitHub issues](https://img.shields.io/github/issues/uuvsimulator/rexrov2.svg)](https://github.com/uuvsimulator/rexrov2/issues)
[`eca_a9`](https://github.com/uuvsimulator/eca_a9) | [![Documentation](https://img.shields.io/badge/read-the%20docs-blue.svg)](packages/eca_a9/intro.md) | | [![Build Status](https://travis-ci.org/uuvsimulator/eca_a9.svg?branch=master)](https://travis-ci.org/uuvsimulator/eca_a9) | [![GitHub issues](https://img.shields.io/github/issues/uuvsimulator/eca_a9.svg)](https://github.com/uuvsimulator/eca_a9/issues)
[`desistek_saga`](https://github.com/uuvsimulator/desistek_saga) | [![Documentation](https://img.shields.io/badge/read-the%20docs-blue.svg)](packages/desistek_saga/intro.md) | | [![Build Status](https://travis-ci.org/uuvsimulator/desistek_saga.svg?branch=master)](https://travis-ci.org/uuvsimulator/desistek_saga) | [![GitHub issues](https://img.shields.io/github/issues/uuvsimulator/desistek_saga.svg)](https://github.com/uuvsimulator/desistek_saga/issues)
[`lauv_gazebo`](https://github.com/uuvsimulator/lauv_gazebo) | [![Documentation](https://img.shields.io/badge/read-the%20docs-blue.svg)](packages/lauv_gazebo/intro.md) | | [![Build Status](https://travis-ci.org/uuvsimulator/lauv_gazebo.svg?branch=master)](https://travis-ci.org/uuvsimulator/lauv_gazebo) | [![GitHub issues](https://img.shields.io/github/issues/uuvsimulator/lauv_gazebo.svg)](https://github.com/uuvsimulator/lauv_gazebo/issues)

# Videos

## ROSCon 2018

<iframe src="https://player.vimeo.com/video/292691843" width="640" height="360" frameborder="0" allow="autoplay; fullscreen" allowfullscreen></iframe>
<p><a href="https://vimeo.com/292691843">ROSCon 2018 Madrid: Unmanned Underwater Vehicle Simulator: Enabling Simulation of Multi-Robot Underwater Missions with Gazebo</a> from <a href="https://vimeo.com/osrfoundation">OSRF</a> on <a href="https://vimeo.com">Vimeo</a>.</p>

## EU-Project SWARMs

<iframe width="640" height="360" src="https://www.youtube.com/embed/vKMR8-7WRF4" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

<iframe width="640" height="360" src="https://www.youtube.com/embed/6V_TR9i0k1Q" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

<iframe width="640" height="360" src="https://www.youtube.com/embed/PB9OD7rsLG4" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Maritime Robot X Forum 2017

<iframe width="640" height="360" src="https://www.youtube.com/embed/eoq-Ro2Hnao" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

<iframe width="640" height="360" src="https://www.youtube.com/embed/CXZtw-LeQsY" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>



