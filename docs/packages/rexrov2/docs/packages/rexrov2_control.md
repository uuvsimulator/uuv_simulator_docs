![Version](https://img.shields.io/badge/version-0.1.3-brightgreen.svg)

> Link to the `rexrov2` repository [here](https://github.com/uuvsimulator/rexrov2)

# Description

Launch and configuration files to start controllers nodes from the [`uuv_trajectory_control`](https://github.com/uuvsimulator/uuv_simulator/tree/master/uuv_control/uuv_trajectory_control) package for the RexROV 2 vehicle.

# Launch files

## [`start_sf_controller.launch`](https://github.com/uuvsimulator/rexrov2/tree/master/rexrov2_control/launch/start_sf_controller.launch)

> **Description**


Starts the [singulary-tree tracking controller](https://github.com/uuvsimulator/uuv_simulator/blob/master/uuv_control/uuv_trajectory_control/scripts/rov_sf_controller.py) 
node with the configurations for the RexROV 2 vehicle.

> **Example**

```
roslaunch uuv_gazebo_worlds ocean_waves.launch
```

```
roslaunch rexrov2_description upload_rexrov2.launch
```

```
roslaunch rexrov2_control start_sf_controller.launch
```



> **Arguments**

* **uuv_name** (*default:* `rexrov2`): Namespace of the vehicle to be controller
* **record** (*default:* `false`): Record ROS bag
* **gui_on** (*default:* `true`)
* **use_ned_frame** (*default:* `true`)
* **Kd** (*default:* `1000.0,1000.0,1000.0,100.0,100.0,100.0`)
* **lambda** (*default:* `100.0`)
* **c** (*default:* `100.0`)
* **teleop_on** (*default:* `false`)
* **joy_id** (*default:* `0`)
* **axis_yaw** (*default:* `0`)
* **axis_x** (*default:* `4`)
* **axis_y** (*default:* `3`)
* **axis_z** (*default:* `1`)
* **model_params_file** (*default:* `$(find rexrov2_control)/config/model_params.yaml`)
* **thruster_manager_output_dir** (*default:* `$(find rexrov2_control)/config`)
* **thruster_manager_config_file** (*default:* `$(find rexrov2_control)/config/thruster_manager.yaml`)
* **tam_file** (*default:* `$(find rexrov2_control)/config/TAM.yaml`)

## [`start_velocity_control.launch`](https://github.com/uuvsimulator/rexrov2/tree/master/rexrov2_control/launch/start_velocity_control.launch)

> **Arguments**

* **model_name** (*default:* `rexrov2`)
* **uuv_name** (*default:* `$(arg model_name)`)
* **joy_id** (*default:* `0`)

## [`start_pd_grav_compensation_controller.launch`](https://github.com/uuvsimulator/rexrov2/tree/master/rexrov2_control/launch/start_pd_grav_compensation_controller.launch)

> **Description**


Starts the [PD controller with compensation of restoring forces](https://github.com/uuvsimulator/uuv_simulator/blob/master/uuv_control/uuv_trajectory_control/scripts/rov_pd_grav_compensation_controller.py) 
node with the configurations for the RexROV 2 vehicle.

> **Example**

```
roslaunch uuv_gazebo_worlds ocean_waves.launch
```

```
roslaunch rexrov2_description upload_rexrov2.launch
```

```
roslaunch rexrov2_control start_pd_grav_compensation_controller.launch
```



> **Arguments**

* **uuv_name** (*default:* `rexrov2`): Namespace of the vehicle to be controller
* **record** (*default:* `false`): Record ROS bag
* **gui_on** (*default:* `true`): Start Gazebo client and RViz
* **use_ned_frame** (*default:* `false`): If true, the reference frame is set to be NED (North-East-Down) instead of Gazebo's default ENU (East-North-Up)
* **Kp** (*default:* `1000,1000,1000,1000,1000,1000`): Coefficients for the $K_p$ diagonal matrix
* **Kd** (*default:* `100,100,100,100,100,100`): Coefficients for the $K_d$ diagonal matrix
* **teleop_on** (*default:* `false`): Start joystick teleop node
* **joy_id** (*default:* `0`): ID of the joystick device
* **axis_yaw** (*default:* `0`): Joystick mapping for yaw angle input
* **axis_x** (*default:* `4`): Joystick mapping for X component of velocity reference input
* **axis_y** (*default:* `3`): Joystick mapping for Y component of velocity reference input
* **axis_z** (*default:* `1`): Joystick mapping for Z component of velocity reference input
* **thruster_manager_output_dir** (*default:* `$(find rexrov2_control)/config`): Output directory for the generated thruster manager
* **thruster_manager_config_file** (*default:* `$(find rexrov2_control)/config/thruster_manager.yaml`): File storing the configuration of the thruster manager
* **tam_file** (*default:* `$(find rexrov2_control)/config/TAM.yaml`): File storing the thruster allocation matrix
* **model_params_file** (*default:* `$(find rexrov2_control)/config/model_params.yaml`): File storing the vehicle model parameters loaded by the controller

## [`start_mb_fl_controller.launch`](https://github.com/uuvsimulator/rexrov2/tree/master/rexrov2_control/launch/start_mb_fl_controller.launch)

> **Description**


Starts the [model-based feedback linearization controller](https://github.com/uuvsimulator/uuv_simulator/blob/master/uuv_control/uuv_trajectory_control/scripts/rov_mb_fl_controller.py) 
node with the configurations for the RexROV 2 vehicle.
The controller's default parameters `Kp`, `Kd` and `Ki`  
were optimized using [SMAC](https://github.com/automl/SMAC3).

> **Example**

```
roslaunch uuv_gazebo_worlds ocean_waves.launch
```

```
roslaunch rexrov2_description upload_rexrov2.launch
```

```
roslaunch rexrov2_control start_mb_fl_controller.launch
```



> **Arguments**

* **uuv_name** (*default:* `rexrov2`)
* **record** (*default:* `false`): Record ROS bag
* **gui_on** (*default:* `true`)
* **use_ned_frame** (*default:* `false`)
* **Kp** (*default:* `7750.307,7750.307,7750.307,7430.825,7430.825,7430.825`)
* **Kd** (*default:* `8953.924,8953.924,8953.924,8267.137,8267.137,8267.137`)
* **Ki** (*default:* `9144.575,9144.575,9144.575,2095.077,2095.077,2095.077`)
* **teleop_on** (*default:* `false`)
* **joy_id** (*default:* `0`)
* **axis_yaw** (*default:* `0`)
* **axis_x** (*default:* `4`)
* **axis_y** (*default:* `3`)
* **axis_z** (*default:* `1`)
* **model_params_file** (*default:* `$(find rexrov2_control)/config/model_params.yaml`)
* **thruster_manager_output_dir** (*default:* `$(find rexrov2_control)/config`)
* **thruster_manager_config_file** (*default:* `$(find rexrov2_control)/config/thruster_manager.yaml`)
* **tam_file** (*default:* `$(find rexrov2_control)/config/TAM.yaml`)

## [`start_nmb_sm_controller.launch`](https://github.com/uuvsimulator/rexrov2/tree/master/rexrov2_control/launch/start_nmb_sm_controller.launch)

> **Description**


Starts the [non-model-based sliding mode controller](https://github.com/uuvsimulator/uuv_simulator/blob/master/uuv_control/uuv_trajectory_control/scripts/rov_nmb_sm_controller.py) 
node with the configurations for the RexROV 2 vehicle.
The controller's default parameters `K`, `Kd`, `Ki` and `slope` 
were optimized using [SMAC](https://github.com/automl/SMAC3).

> **Example**

```
roslaunch uuv_gazebo_worlds ocean_waves.launch
```

```
roslaunch rexrov2_description upload_rexrov2.launch
```

```
roslaunch rexrov2_control start_pd_grav_compensation_controller.launch
```



> **Arguments**

* **uuv_name** (*default:* `rexrov2`): Namespace of the vehicle to be controller
* **record** (*default:* `false`): Record ROS bag
* **gui_on** (*default:* `true`): Start Gazebo client and RViz
* **use_ned_frame** (*default:* `false`): If true, the reference frame is set to be NED (North-East-Down) instead of Gazebo's default ENU (East-North-Up)
* **K** (*default:* `5,5,5,5,5,5`): Coefficients for the $K$ diagonal matrix
* **Kd** (*default:* `4490.0,4490.0,4490.0,19541.395,19541.395,19541.395`): Coefficients for the $K_d$ diagonal matrix
* **Ki** (*default:* `0.1,0.1,0.1,0.476,0.476,0.476`): Coefficients for the $K_i$ diagonal matrix
* **slope** (*default:* `3.83,3.83,3.83,0.508,0.508,0.508`): Coefficients for the $\alpha$ diagonal matrix
* **teleop_on** (*default:* `false`): Start joystick teleop node
* **joy_id** (*default:* `0`): ID of the joystick device
* **axis_yaw** (*default:* `0`): Joystick mapping for yaw angle input
* **axis_x** (*default:* `4`): Joystick mapping for X component of velocity reference input
* **axis_y** (*default:* `3`): Joystick mapping for Y component of velocity reference input
* **axis_z** (*default:* `1`): Joystick mapping for Z component of velocity reference input
* **max_forward_speed** (*default:* `0.5`): Maximum forward speed in m/s
* **thruster_manager_output_dir** (*default:* `$(find rexrov2_control)/config`): Output directory for the generated thruster manager
* **thruster_manager_config_file** (*default:* `$(find rexrov2_control)/config/thruster_manager.yaml`): File storing the configuration of the thruster manager
* **tam_file** (*default:* `$(find rexrov2_control)/config/TAM.yaml`): File storing the thruster allocation matrix

## [`start_thruster_manager.launch`](https://github.com/uuvsimulator/rexrov2/tree/master/rexrov2_control/launch/start_thruster_manager.launch)

> **Description**


Starts the [thruster allocator node](https://github.com/uuvsimulator/uuv_simulator/blob/master/uuv_control/uuv_thruster_manager/scripts/thruster_allocator.py) 
with the configuration for the RexROV 2 vehicle.

The thruster allocator uses the [thruster allocation matrix](https://github.com/uuvsimulator/rexrov2/blob/master/rexrov2_control/config/TAM.yaml)
to convert the [geometry_msgs/Wrench message](https://docs.ros.org/lunar/api/geometry_msgs/html/msg/Wrench.html) from the `/<uuv_name>/thruster_manager/input` topic
into reference input for each thruster unit.

> **Create or reset the thruster allocation matrix**

In case the [thruster allocation matrix](https://github.com/uuvsimulator/rexrov2/blob/master/rexrov2_control/config/TAM.yaml)
has to be created or recalculated, start the simulation as follows

```
roslaunch uuv_gazebo_worlds ocean_waves.launch
```

```
roslaunch rexrov2_description upload_rexrov2.launch
```

and then start the thruster manager with the `reset_tam` set to true. The file will be stored 
under the filename provided with the path under the input `tam_file` as follows

```
roslaunch rexrov2_control start_thruster_manager.launch reset_tam:=true
```

> **Example**

Start the simulation, spawn the RexROV 2 vehicle and then start the thruster allocation node as follows

```
roslaunch uuv_gazebo_worlds ocean_waves.launch
```

```
roslaunch rexrov2_description upload_rexrov2.launch
```

```
roslaunch rexrov2_control start_thruster_manager.launch 
```

!!! note
    
    A controller node or similar must publish the geometry_msgs/Wrench message in the 
    `/<uuv_name>/thruster_manager/input` topic for the vehicle to move.



> **Arguments**

* **model_name** (*default:* `rexrov2`): Name of the model of the vehicle
* **uuv_name** (*default:* `$(arg model_name)`): Namespace for the vehicle instance
* **base_link** (*default:* `base_link`): Name of the base link frame
* **timeout** (*default:* `-1`)
* **reset_tam** (*default:* `false`)
* **output_dir** (*default:* `$(find rexrov2_control)/config`)
* **config_file** (*default:* `$(find rexrov2_control)/config/thruster_manager.yaml`)
* **tam_file** (*default:* `$(find rexrov2_control)/config/TAM.yaml`)

## [`record_demo.launch`](https://github.com/uuvsimulator/rexrov2/tree/master/rexrov2_control/launch/record_demo.launch)

> **Description**


Starts the `rosbag record` node and records a set of topics for the RexROV 2.



> **Arguments**

* **record** (*default:* `false`): Starts the recording node if set to true
* **bag_filename** (*default:* `recording.bag`): Filename for the recording ROS bag
* **use_ned_frame** (*default:* `false`): If set to true, stores the odometry with respect to NED frame
* **uuv_name** (*default:* `rexrov2`): Namespace of the vehicle

## [`start_pid_controller.launch`](https://github.com/uuvsimulator/rexrov2/tree/master/rexrov2_control/launch/start_pid_controller.launch)

> **Description**


Starts the [6-DoF PID controller](https://github.com/uuvsimulator/uuv_simulator/blob/master/uuv_control/uuv_trajectory_control/scripts/rov_pid_controller.py) 
node with the configurations for the RexROV 2 vehicle.
The controller's default parameters `Kp`, `Kd` and `Ki`
were optimized using [SMAC](https://github.com/automl/SMAC3).

> **Example**

```
roslaunch uuv_gazebo_worlds ocean_waves.launch
```

```
roslaunch rexrov2_description upload_rexrov2.launch
```

```
roslaunch rexrov2_control start_pid_controller.launch
```



> **Arguments**

* **uuv_name** (*default:* `rexrov2`): Namespace of the vehicle to be controller
* **record** (*default:* `false`): Record ROS bag
* **gui_on** (*default:* `true`): Start Gazebo client and RViz
* **use_ned_frame** (*default:* `false`): If true, the reference frame is set to be NED (North-East-Down) instead of Gazebo's default ENU (East-North-Up)
* **Kp** (*default:* `11993.888,11993.888,11993.888,19460.069,19460.069,19460.069`): Coefficients for the $K_p$ diagonal matrix
* **Kd** (*default:* `9077.459,9077.459,9077.459,18880.925,18880.925,18880.925`): Coefficients for the $K_d$ diagonal matrix
* **Ki** (*default:* `321.417,321.417,321.417,2096.951,2096.951,2096.951`): Coefficients for the $K_i$ diagonal matrix
* **teleop_on** (*default:* `false`): Start joystick teleop node
* **joy_id** (*default:* `0`): ID of the joystick device
* **axis_yaw** (*default:* `0`): Joystick mapping for yaw angle input
* **axis_x** (*default:* `4`): Joystick mapping for X component of velocity reference input
* **axis_y** (*default:* `3`): Joystick mapping for Y component of velocity reference input
* **axis_z** (*default:* `1`): Joystick mapping for Z component of velocity reference input
* **thruster_manager_output_dir** (*default:* `$(find rexrov2_control)/config`): Output directory for the generated thruster manager
* **thruster_manager_config_file** (*default:* `$(find rexrov2_control)/config/thruster_manager.yaml`): File storing the configuration of the thruster manager
* **tam_file** (*default:* `$(find rexrov2_control)/config/TAM.yaml`): File storing the thruster allocation matrix

