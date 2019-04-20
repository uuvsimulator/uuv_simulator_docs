![Version](https://img.shields.io/badge/version-0.3.2-brightgreen.svg)

> Link to the `desistek_saga` repository [here](https://github.com/uuvsimulator/desistek_saga)

# Description

Configuration and launch files to control the Desistek SAGA ROV

# Launch files

## [`start_pdc_control.launch`](https://github.com/uuvsimulator/desistek_saga/tree/master/desistek_saga_control/launch/start_pdc_control.launch)

> **Arguments**

* **uuv_name** (*default:* `desistek_saga`)
* **record** (*default:* `false`)
* **gui_on** (*default:* `true`)
* **use_ned_frame** (*default:* `false`)
* **Kp** (*default:* `1,1,1,0,0,1`)
* **Kd** (*default:* `0,0,0,0,0,0`)
* **teleop_on** (*default:* `false`)
* **joy_id** (*default:* `0`)
* **axis_yaw** (*default:* `0`)
* **axis_x** (*default:* `4`)
* **axis_y** (*default:* `3`)
* **axis_z** (*default:* `1`)
* **thruster_manager_output_dir** (*default:* `$(find desistek_saga_control)/config`)
* **thruster_manager_config_file** (*default:* `$(find desistek_saga_control)/config/thruster_manager.yaml`)
* **tam_file** (*default:* `$(find desistek_saga_control)/config/TAM.yaml`)
* **model_params_file** (*default:* `$(find desistek_saga_control)/config/model_params.yaml`)

## [`start_thruster_manager.launch`](https://github.com/uuvsimulator/desistek_saga/tree/master/desistek_saga_control/launch/start_thruster_manager.launch)

> **Arguments**

* **uuv_name** (*default:* `desistek_saga`)

## [`record_demo.launch`](https://github.com/uuvsimulator/desistek_saga/tree/master/desistek_saga_control/launch/record_demo.launch)

> **Arguments**

* **record** (*default:* `false`)
* **bag_filename** (*default:* `recording.bag`)

## [`start_nmb_sm_control.launch`](https://github.com/uuvsimulator/desistek_saga/tree/master/desistek_saga_control/launch/start_nmb_sm_control.launch)

> **Arguments**

* **uuv_name** (*default:* `desistek_saga`)
* **record** (*default:* `false`)
* **gui_on** (*default:* `true`)
* **use_ned_frame** (*default:* `false`)
* **K** (*default:* `5.0,5.0,5.0,0.0,0.0,5.0`)
* **Kd** (*default:* `10.0,13.73,2.44,0.0,0.0,3.55`)
* **Ki** (*default:* `0.05,0.62,0.05,0.0,0.0,0.05`)
* **slope** (*default:* `2.0,0.89,2.0,0.0,0.0,0.8`)
* **teleop_on** (*default:* `false`)
* **joy_id** (*default:* `0`)
* **axis_yaw** (*default:* `0`)
* **axis_x** (*default:* `4`)
* **axis_y** (*default:* `3`)
* **axis_z** (*default:* `1`)
* **thruster_manager_output_dir** (*default:* `$(find desistek_saga_control)/config`)
* **thruster_manager_config_file** (*default:* `$(find desistek_saga_control)/config/thruster_manager.yaml`)
* **tam_file** (*default:* `$(find desistek_saga_control)/config/TAM.yaml`)

## [`start_sf_control.launch`](https://github.com/uuvsimulator/desistek_saga/tree/master/desistek_saga_control/launch/start_sf_control.launch)

> **Arguments**

* **uuv_name** (*default:* `desistek_saga`)
* **record** (*default:* `false`)
* **gui_on** (*default:* `true`)
* **use_ned_frame** (*default:* `false`)
* **Kd** (*default:* `1.0,1.0,1.0,0.0,0.0,1.0`)
* **lambda** (*default:* `1.0`)
* **c** (*default:* `1.0`)
* **teleop_on** (*default:* `false`)
* **joy_id** (*default:* `0`)
* **axis_yaw** (*default:* `0`)
* **axis_x** (*default:* `4`)
* **axis_y** (*default:* `3`)
* **axis_z** (*default:* `1`)
* **thruster_manager_output_dir** (*default:* `$(find desistek_saga_control)/config`)
* **thruster_manager_config_file** (*default:* `$(find desistek_saga_control)/config/thruster_manager.yaml`)
* **tam_file** (*default:* `$(find desistek_saga_control)/config/TAM.yaml`)
* **model_params_file** (*default:* `$(find desistek_saga_control)/config/model_params.yaml`)

## [`start_pid_control.launch`](https://github.com/uuvsimulator/desistek_saga/tree/master/desistek_saga_control/launch/start_pid_control.launch)

> **Arguments**

* **uuv_name** (*default:* `desistek_saga`)
* **record** (*default:* `false`)
* **gui_on** (*default:* `true`)
* **use_ned_frame** (*default:* `false`)
* **Kp** (*default:* `1,1,1,0,0,1`)
* **Kd** (*default:* `0,0,0,0,0,0`)
* **Ki** (*default:* `0,0,0,0,0,0`)
* **teleop_on** (*default:* `false`)
* **joy_id** (*default:* `0`)
* **axis_yaw** (*default:* `0`)
* **axis_x** (*default:* `4`)
* **axis_y** (*default:* `3`)
* **axis_z** (*default:* `1`)
* **thruster_manager_output_dir** (*default:* `$(find desistek_saga_control)/config`)
* **thruster_manager_config_file** (*default:* `$(find desistek_saga_control)/config/thruster_manager.yaml`)
* **tam_file** (*default:* `$(find desistek_saga_control)/config/TAM.yaml`)

## [`start_cascaded_pid_with_teleop.launch`](https://github.com/uuvsimulator/desistek_saga/tree/master/desistek_saga_control/launch/start_cascaded_pid_with_teleop.launch)

> **Arguments**

* **namespace** (*default:* `desistek_saga`)
* **joy_id** (*default:* `0`)
* **axis_x** (*default:* `4`)
* **axis_y** (*default:* `3`)
* **axis_z** (*default:* `1`)
* **axis_yaw** (*default:* `0`)
* **gui_on** (*default:* `true`)

## [`start_position_hold.launch`](https://github.com/uuvsimulator/desistek_saga/tree/master/desistek_saga_control/launch/start_position_hold.launch)

> **Arguments**

* **namespace** (*default:* `desistek_saga`)

## [`start_geometric_tracking_control.launch`](https://github.com/uuvsimulator/desistek_saga/tree/master/desistek_saga_control/launch/start_geometric_tracking_control.launch)

> **Arguments**

* **uuv_name** (*default:* `desistek_saga`)
* **record** (*default:* `false`)
* **gui_on** (*default:* `true`)
* **Kp** (*default:* `2.0,2.0,2.0,0.8`)
* **Kd** (*default:* `0.1,0.1,0.1,0.1`)
* **Ki** (*default:* `0.05,0.05,0.05,0.05`)
* **teleop_on** (*default:* `false`)
* **joy_id** (*default:* `0`)
* **axis_yaw** (*default:* `0`)
* **axis_x** (*default:* `4`)
* **axis_y** (*default:* `3`)
* **axis_z** (*default:* `1`)
* **thruster_manager_output_dir** (*default:* `$(find desistek_saga_control)/config`)
* **thruster_manager_config_file** (*default:* `$(find desistek_saga_control)/config/thruster_manager.yaml`)
* **tam_file** (*default:* `$(find desistek_saga_control)/config/TAM.yaml`)

