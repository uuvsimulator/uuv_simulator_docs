![Version](https://img.shields.io/badge/version-0.1.3-brightgreen.svg)

> Link to the `rexrov2` repository [here](https://github.com/uuvsimulator/rexrov2)

# Launch files

## [`start_sf_controller.launch`](https://github.com/uuvsimulator/rexrov2/tree/master/rexrov2_control/launch/start_sf_controller.launch)

> **Arguments**

* **uuv_name** (*default:* `rexrov2`)
* **record** (*default:* `false`)
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


Starts a Gazebo simulation with the RexROV 2 vehicle and the 
[PD controller with compensation of restoring forces](https://github.com/uuvsimulator/uuv_simulator/blob/master/uuv_control/uuv_trajectory_control/scripts/rov_pd_grav_compensation_controller.py) 
node. 



> **Arguments**

* **uuv_name** (*default:* `rexrov2`)
* **record** (*default:* `false`)
* **gui_on** (*default:* `true`)
* **use_ned_frame** (*default:* `false`)
* **Kp** (*default:* `1000,1000,1000,1000,1000,1000`)
* **Kd** (*default:* `100,100,100,100,100,100`)
* **teleop_on** (*default:* `false`)
* **joy_id** (*default:* `0`)
* **axis_yaw** (*default:* `0`)
* **axis_x** (*default:* `4`)
* **axis_y** (*default:* `3`)
* **axis_z** (*default:* `1`)
* **thruster_manager_output_dir** (*default:* `$(find rexrov2_control)/config`)
* **thruster_manager_config_file** (*default:* `$(find rexrov2_control)/config/thruster_manager.yaml`)
* **tam_file** (*default:* `$(find rexrov2_control)/config/TAM.yaml`)
* **model_params_file** (*default:* `$(find rexrov2_control)/config/model_params.yaml`)

## [`start_mb_fl_controller.launch`](https://github.com/uuvsimulator/rexrov2/tree/master/rexrov2_control/launch/start_mb_fl_controller.launch)

> **Description**

MB 


> **Arguments**

* **uuv_name** (*default:* `rexrov2`)
* **record** (*default:* `false`)
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

> **Arguments**

* **uuv_name** (*default:* `rexrov2`)
* **gui_on** (*default:* `true`)
* **use_ned_frame** (*default:* `false`)
* **K** (*default:* `5,5,5,5,5,5`)
* **Kd** (*default:* `4490.0,4490.0,4490.0,19541.395,19541.395,19541.395`)
* **Ki** (*default:* `0.1,0.1,0.1,0.476,0.476,0.476`)
* **slope** (*default:* `3.83,3.83,3.83,0.508,0.508,0.508`)
* **teleop_on** (*default:* `false`)
* **joy_id** (*default:* `0`)
* **axis_yaw** (*default:* `0`)
* **axis_x** (*default:* `4`)
* **axis_y** (*default:* `3`)
* **axis_z** (*default:* `1`)
* **max_forward_speed** (*default:* `0.5`)
* **thruster_manager_output_dir** (*default:* `$(find rexrov2_control)/config`)
* **thruster_manager_config_file** (*default:* `$(find rexrov2_control)/config/thruster_manager.yaml`)
* **tam_file** (*default:* `$(find rexrov2_control)/config/TAM.yaml`)

## [`start_thruster_manager.launch`](https://github.com/uuvsimulator/rexrov2/tree/master/rexrov2_control/launch/start_thruster_manager.launch)

> **Arguments**

* **model_name** (*default:* `rexrov2`)
* **uuv_name** (*default:* `$(arg model_name)`)
* **base_link** (*default:* `base_link`)
* **timeout** (*default:* `-1`)
* **reset_tam** (*default:* `false`)
* **output_dir** (*default:* `$(find rexrov2_control)/config`)
* **config_file** (*default:* `$(find rexrov2_control)/config/thruster_manager.yaml`)
* **tam_file** (*default:* `$(find rexrov2_control)/config/TAM.yaml`)

## [`record_demo.launch`](https://github.com/uuvsimulator/rexrov2/tree/master/rexrov2_control/launch/record_demo.launch)

> **Arguments**

* **record** (*default:* `false`)
* **bag_filename** (*default:* `recording.bag`)
* **use_ned_frame** (*default:* `false`)

## [`start_pid_controller.launch`](https://github.com/uuvsimulator/rexrov2/tree/master/rexrov2_control/launch/start_pid_controller.launch)

> **Arguments**

* **uuv_name** (*default:* `rexrov2`)
* **record** (*default:* `false`)
* **gui_on** (*default:* `true`)
* **use_ned_frame** (*default:* `false`)
* **Kp** (*default:* `11993.888,11993.888,11993.888,19460.069,19460.069,19460.069`)
* **Kd** (*default:* `9077.459,9077.459,9077.459,18880.925,18880.925,18880.925`)
* **Ki** (*default:* `321.417,321.417,321.417,2096.951,2096.951,2096.951`)
* **teleop_on** (*default:* `false`)
* **joy_id** (*default:* `0`)
* **axis_yaw** (*default:* `0`)
* **axis_x** (*default:* `4`)
* **axis_y** (*default:* `3`)
* **axis_z** (*default:* `1`)
* **thruster_manager_output_dir** (*default:* `$(find rexrov2_control)/config`)
* **thruster_manager_config_file** (*default:* `$(find rexrov2_control)/config/thruster_manager.yaml`)
* **tam_file** (*default:* `$(find rexrov2_control)/config/TAM.yaml`)

