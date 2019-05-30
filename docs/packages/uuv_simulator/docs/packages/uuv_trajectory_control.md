![Version](https://img.shields.io/badge/version-0.6.12-brightgreen.svg)

> Link to the `uuv_simulator` repository [here](https://github.com/uuvsimulator/uuv_simulator)

# Description

The uuv_trajectory_control package

# Launch files

## [`rov_pid_controller.launch`](https://github.com/uuvsimulator/uuv_simulator/tree/master/uuv_trajectory_control/launch/rov_pid_controller.launch)

> **Arguments**

* **uuv_name**
* **model_name** (*default:* `$(arg uuv_name)`)
* **saturation** (*default:* `1200`)
* **gui_on** (*default:* `true`)
* **use_params_file** (*default:* `false`)
* **use_ned_frame** (*default:* `false`)
* **Kp** (*default:* `11993.888,11993.888,11993.888,19460.069,19460.069,19460.069`)
* **Kd** (*default:* `9077.459,9077.459,9077.459,18880.925,18880.925,18880.925`)
* **Ki** (*default:* `321.417,321.417,321.417,2096.951,2096.951,2096.951`)
* **controller_config_file** (*default:* `$(find uuv_trajectory_control)/config/controllers/pid/$(arg model_name)/params.yaml`)
* **thruster_manager_output_dir** (*default:* `$(find uuv_thruster_manager)/config/$(arg model_name)`)
* **thruster_manager_config_file** (*default:* `$(find uuv_thruster_manager)/config/$(arg model_name)/thruster_manager.yaml`)
* **tam_file** (*default:* `$(find uuv_thruster_manager)/config/$(arg model_name)/TAM.yaml`)

## [`rov_mb_sm_controller.launch`](https://github.com/uuvsimulator/uuv_simulator/tree/master/uuv_trajectory_control/launch/rov_mb_sm_controller.launch)

> **Arguments**

* **uuv_name**
* **model_name** (*default:* `$(arg uuv_name)`)
* **saturation** (*default:* `1200`)
* **gui_on** (*default:* `true`)
* **use_params_file** (*default:* `false`)
* **use_ned_frame** (*default:* `false`)
* **lambda** (*default:* `10,10,10,10,10,10`)
* **rho_constant** (*default:* `10000,10000,10000,10000,10000,10000`)
* **k** (*default:* `500,500,500,500,500,500`)
* **c** (*default:* `50,50,50,1,1,1`)
* **adapt_slope** (*default:* `100,10,10`)
* **rho_0** (*default:* `3000,3000,8000,1500,1500,8000`)
* **drift_prevent** (*default:* `0.03`)
* **controller_config_file** (*default:* `$(find uuv_trajectory_control)/config/controllers/mb_sm/$(arg model_name)/params.yaml`)
* **model_params_file** (*default:* `$(find uuv_trajectory_control)/config/models/$(arg model_name)/params.yaml`)
* **thruster_manager_output_dir** (*default:* `$(find uuv_thruster_manager)/config/$(arg model_name)`)
* **thruster_manager_config_file** (*default:* `$(find uuv_thruster_manager)/config/$(arg model_name)/thruster_manager.yaml`)
* **tam_file** (*default:* `$(find uuv_thruster_manager)/config/$(arg model_name)/TAM.yaml`)

## [`auv_geometric_tracking_controller.launch`](https://github.com/uuvsimulator/uuv_simulator/tree/master/uuv_trajectory_control/launch/auv_geometric_tracking_controller.launch)

> **Arguments**

* **uuv_name**
* **use_params_file** (*default:* `false`)
* **gui_on** (*default:* `true`)
* **use_ned_frame** (*default:* `false`)
* **max_forward_speed** (*default:* `2`)
* **dubins_radius** (*default:* `10`)
* **dubins_max_pitch** (*default:* `0.09`)
* **min_thrust** (*default:* `70`)
* **max_thrust** (*default:* `200`)
* **thruster_topic** (*default:* `thrusters/0/input`)
* **thrust_p_gain** (*default:* `1`)
* **thrust_d_gain** (*default:* `1`)
* **gain_roll** (*default:* `1`)
* **gain_pitch** (*default:* `1`)
* **gain_yaw** (*default:* `1`)
* **n_fins** (*default:* `4`)
* **map_roll** (*default:* `0,0,0,0`)
* **map_pitch** (*default:* `0,0,0,0`)
* **map_yaw** (*default:* `0,0,0,0`)
* **max_fin_angle** (*default:* `0.0`)
* **fin_topic_prefix** (*default:* `fins`)
* **fin_topic_suffix** (*default:* `input`)
* **idle_radius** (*default:* `10.0`)
* **look_ahead_delay** (*default:* `5.0`)
* **desired_pitch_limit** (*default:* `0.26`)
* **yaw_error_limit** (*default:* `1.0`)
* **thruster_topic_prefix** (*default:* `thrusters`)
* **thruster_topic_suffix** (*default:* `input`)
* **thruster_frame_base** (*default:* `thruster_`)
* **thruster_conversion_fcn** (*default:* `proportional`)
* **thruster_gain** (*default:* `0.0`)
* **thruster_input** (*default:* `0,1,2,3`)
* **thruster_output** (*default:* `0,1,2,3`)

## [`rov_mb_fl_controller.launch`](https://github.com/uuvsimulator/uuv_simulator/tree/master/uuv_trajectory_control/launch/rov_mb_fl_controller.launch)

> **Arguments**

* **uuv_name**
* **model_name** (*default:* `$(arg uuv_name)`)
* **saturation** (*default:* `1200`)
* **gui_on** (*default:* `true`)
* **use_params_file** (*default:* `false`)
* **use_ned_frame** (*default:* `false`)
* **Kp** (*default:* `19987.218,19987.218,19987.218,19460.293,19460.293,19460.293`)
* **Kd** (*default:* `11458.051,11458.051,11458.051,17068.778,17068.778,17068.778`)
* **Ki** (*default:* `1689.976,1689.976,1689.976,186.198,186.198,186.198`)
* **controller_config_file** (*default:* `$(find uuv_trajectory_control)/config/controllers/pid/$(arg model_name)/params.yaml`)
* **model_params_file** (*default:* `$(find uuv_trajectory_control)/config/models/$(arg model_name)/params.yaml`)
* **thruster_manager_output_dir** (*default:* `$(find uuv_thruster_manager)/config/$(arg model_name)`)
* **thruster_manager_config_file** (*default:* `$(find uuv_thruster_manager)/config/$(arg model_name)/thruster_manager.yaml`)
* **tam_file** (*default:* `$(find uuv_thruster_manager)/config/$(arg model_name)/TAM.yaml`)

## [`rov_nmb_sm_controller.launch`](https://github.com/uuvsimulator/uuv_simulator/tree/master/uuv_trajectory_control/launch/rov_nmb_sm_controller.launch)

> **Arguments**

* **uuv_name**
* **model_name** (*default:* `$(arg uuv_name)`)
* **saturation** (*default:* `1200`)
* **gui_on** (*default:* `true`)
* **use_params_file** (*default:* `false`)
* **use_ned_frame** (*default:* `false`)
* **max_forward_speed** (*default:* `0.5`)
* **K** (*default:* `5,5,5,5,5,5`)
* **Kd** (*default:* `4118.98,4118.98,4118.98,8000.0,8000.0,8000.0`)
* **Ki** (*default:* `0.06144,0.06144,0.06144,0.078,0.078,0.078`)
* **slope** (*default:* `0.182,0.182,0.182,3.348,3.348,3.348`)
* **controller_config_file** (*default:* `$(find uuv_trajectory_control)/config/controllers/nmb_sm/$(arg model_name)/params.yaml`)
* **thruster_manager_output_dir** (*default:* `$(find uuv_thruster_manager)/config/$(arg model_name)`)
* **thruster_manager_config_file** (*default:* `$(find uuv_thruster_manager)/config/$(arg model_name)/thruster_manager.yaml`)
* **tam_file** (*default:* `$(find uuv_thruster_manager)/config/$(arg model_name)/TAM.yaml`)

## [`rov_nl_pid_controller.launch`](https://github.com/uuvsimulator/uuv_simulator/tree/master/uuv_trajectory_control/launch/rov_nl_pid_controller.launch)

> **Arguments**

* **uuv_name**
* **model_name**
* **saturation** (*default:* `6000`)
* **gui_on** (*default:* `true`)
* **use_params_file** (*default:* `false`)
* **use_ned_frame** (*default:* `false`)
* **Kp** (*default:* `6017.059667616178,6017.059667616178,6017.059667616178,9731.391095849109,9731.391095849109,9731.391095849109`)
* **Kd** (*default:* `2682.9509286089447,2682.9509286089447,2682.9509286089447,9440.462338720527,9440.462338720527,9440.462338720527`)
* **Ki** (*default:* `0,0,0,0,0,0`)
* **Hm** (*default:* `1657.655912647713,1657.655912647713,1657.655912647713,4193.901741127024,4193.901741127024,4193.901741127024`)
* **controller_config_file** (*default:* `$(find uuv_trajectory_control)/config/controllers/nl_pid/$(arg model_name)/params.yaml`)
* **model_params_file** (*default:* `$(find uuv_trajectory_control)/config/models/$(arg model_name)/params.yaml`)
* **thruster_manager_output_dir** (*default:* `$(find uuv_thruster_manager)/config/$(arg model_name)`)
* **thruster_manager_config_file** (*default:* `$(find uuv_thruster_manager)/config/$(arg model_name)/thruster_manager.yaml`)
* **tam_file** (*default:* `$(find uuv_thruster_manager)/config/$(arg model_name)/TAM.yaml`)

## [`rov_sf_controller.launch`](https://github.com/uuvsimulator/uuv_simulator/tree/master/uuv_trajectory_control/launch/rov_sf_controller.launch)

> **Arguments**

* **uuv_name**
* **model_name** (*default:* `$(arg uuv_name)`)
* **saturation** (*default:* `5000`)
* **gui_on** (*default:* `true`)
* **use_params_file** (*default:* `false`)
* **use_ned_frame** (*default:* `false`)
* **Kd** (*default:* `100.0,100.0,100.0,100.0,100.0,100.0`)
* **lambda** (*default:* `1.0`)
* **c** (*default:* `1.0`)
* **controller_config_file** (*default:* `$(find uuv_trajectory_control)/config/controllers/pid/$(arg model_name)/params.yaml`)
* **model_params_file** (*default:* `$(find uuv_trajectory_control)/config/models/$(arg model_name)/params.yaml`)
* **thruster_manager_output_dir** (*default:* `$(find uuv_thruster_manager)/config/$(arg model_name)`)
* **thruster_manager_config_file** (*default:* `$(find uuv_thruster_manager)/config/$(arg model_name)/thruster_manager.yaml`)
* **tam_file** (*default:* `$(find uuv_thruster_manager)/config/$(arg model_name)/TAM.yaml`)

## [`rov_pd_grav_compensation_controller.launch`](https://github.com/uuvsimulator/uuv_simulator/tree/master/uuv_trajectory_control/launch/rov_pd_grav_compensation_controller.launch)

> **Arguments**

* **uuv_name**
* **model_name** (*default:* `$(arg uuv_name)`)
* **saturation** (*default:* `1200`)
* **gui_on** (*default:* `true`)
* **use_params_file** (*default:* `false`)
* **use_ned_frame** (*default:* `false`)
* **Kp** (*default:* `11993.888,11993.888,11993.888,19460.069,19460.069,19460.069`)
* **Kd** (*default:* `9077.459,9077.459,9077.459,18880.925,18880.925,18880.925`)
* **controller_config_file** (*default:* `$(find uuv_trajectory_control)/config/controllers/pid/$(arg model_name)/params.yaml`)
* **model_params_file** (*default:* `$(find uuv_trajectory_control)/config/models/$(arg model_name)/params.yaml`)
* **thruster_manager_output_dir** (*default:* `$(find uuv_thruster_manager)/config/$(arg model_name)`)
* **thruster_manager_config_file** (*default:* `$(find uuv_thruster_manager)/config/$(arg model_name)/thruster_manager.yaml`)
* **tam_file** (*default:* `$(find uuv_thruster_manager)/config/$(arg model_name)/TAM.yaml`)

## [`rov_ua_pid_controller.launch`](https://github.com/uuvsimulator/uuv_simulator/tree/master/uuv_trajectory_control/launch/rov_ua_pid_controller.launch)

> **Arguments**

* **uuv_name**
* **model_name** (*default:* `$(arg uuv_name)`)
* **saturation** (*default:* `1200`)
* **use_params_file** (*default:* `false`)
* **gui_on** (*default:* `true`)
* **Kp** (*default:* `10.0,10.0,10.0,10.0`)
* **Kd** (*default:* `1.0,1.0,1.0,1.0`)
* **Ki** (*default:* `0.5,0.5,0.5,0.5`)
* **controller_config_file** (*default:* `$(find uuv_trajectory_control)/config/controllers/ua_pid/$(arg model_name)/params.yaml`)
* **thruster_manager_output_dir** (*default:* `$(find uuv_thruster_manager)/config/$(arg model_name)`)
* **thruster_manager_config_file** (*default:* `$(find uuv_thruster_manager)/config/$(arg model_name)/thruster_manager.yaml`)
* **tam_file** (*default:* `$(find uuv_thruster_manager)/config/$(arg model_name)/TAM.yaml`)

# Scripts

## `rov_mb_fl_controller.py`

> **Script type:** `python`

## `rov_pd_grav_compensation_controller.py`

> **Script type:** `python`

## `rov_mb_sm_controller.py`

> **Script type:** `python`

## `rov_sf_controller.py`

> **Script type:** `python`

## `rov_nmb_sm_controller.py`

> **Script type:** `python`

## `rov_ua_pid_controller.py`

> **Script type:** `python`

## `rov_pid_controller.py`

> **Script type:** `python`

## `rov_nl_pid_controller.py`

> **Script type:** `python`

## `auv_geometric_tracking_controller.py`

> **Script type:** `python`

## `demo_wp_trajectory_generator.py`

> **Script type:** `python`

