![Version](https://img.shields.io/badge/version-0.1.5-brightgreen.svg)

> Link to the `eca_a9` repository [here](https://github.com/uuvsimulator/eca_a9)

# Launch files

## [`start_control_allocator.launch`](https://github.com/uuvsimulator/eca_a9/tree/master/eca_a9_control/launch/start_control_allocator.launch)

## [`start_nmb_sm_control.launch`](https://github.com/uuvsimulator/eca_a9/tree/master/eca_a9_control/launch/start_nmb_sm_control.launch)

> **Arguments**

* **uuv_name** (*default:* `eca_a9`)
* **gui_on** (*default:* `true`)
* **use_ned_frame** (*default:* `false`)
* **teleop_on** (*default:* `false`)
* **joy_id** (*default:* `0`)
* **axis_yaw** (*default:* `0`)
* **axis_x** (*default:* `4`)
* **axis_y** (*default:* `3`)
* **axis_z** (*default:* `1`)
* **Kd** (*default:* `24.328999405818507,95.16574836816616,25.943377407248825,0,6.388371356010936,79.2844976871164`)
* **Ki** (*default:* `0.0010232768152540483,0.0010232768152540483,0.0010232768152540483,0,0.11901644069756079,0.11901644069756079`)
* **slope** (*default:* `0.9903858668992097,0.9903858668992097,0.9903858668992097,0,0.20796465986893387,0.20796465986893387`)
* **look_ahead_delay** (*default:* `2.0`)
* **min_thrust** (*default:* `40`)

## [`start_auv_teleop.launch`](https://github.com/uuvsimulator/eca_a9/tree/master/eca_a9_control/launch/start_auv_teleop.launch)

> **Arguments**

* **uuv_name** (*default:* `eca_a9`)
* **joy_id** (*default:* `0`)

## [`start_geometric_tracking_control.launch`](https://github.com/uuvsimulator/eca_a9/tree/master/eca_a9_control/launch/start_geometric_tracking_control.launch)

> **Arguments**

* **uuv_name** (*default:* `eca_a9`)
* **gui_on** (*default:* `true`)
* **max_forward_speed** (*default:* `2`)
* **dubins_radius** (*default:* `10`)
* **min_thrust** (*default:* `0`)
* **max_thrust** (*default:* `120`)
* **thrust_p_gain** (*default:* `5.0`)
* **thrust_d_gain** (*default:* `0.01`)
* **p_roll** (*default:* `0.2`)
* **p_pitch** (*default:* `0.8`)
* **d_pitch** (*default:* `0.0`)
* **p_yaw** (*default:* `0.8`)
* **d_yaw** (*default:* `0.0`)
* **n_fins** (*default:* `4`)
* **map_roll**
* **map_pitch**
* **map_yaw**
* **max_fin_angle** (*default:* `1.396263402`)
* **idle_radius** (*default:* `30`)
* **look_ahead_delay** (*default:* `0.0`)
* **dubins_max_pitch** (*default:* `0.26`)
* **desired_pitch_limit** (*default:* `0.26`)
* **yaw_error_limit** (*default:* `1.57`)
* **use_ned_frame** (*default:* `false`)
* **stamped_pose_only** (*default:* `false`)
* **timeout_idle_mode** (*default:* `5`)
* **thruster_topic** (*default:* `thrusters/0/input`)
* **thruster_topic_prefix** (*default:* `thrusters`)
* **thruster_topic_suffix** (*default:* `input`)
* **thruster_frame_base** (*default:* `thruster_`)
* **thruster_conversion_fcn** (*default:* `proportional`)
* **thruster_gain** (*default:* `0.000049`)
* **fin_topic_prefix** (*default:* `fins`)
* **fin_topic_suffix** (*default:* `input`)

