![Version](https://img.shields.io/badge/version-0.6.11-brightgreen.svg)

> Link to the `uuv_simulator` repository [here](https://github.com/uuvsimulator/uuv_simulator)

# Launch files

## [`uuv_teleop.launch`](https://github.com/uuvsimulator/uuv_simulator/tree/master/uuv_teleop/launch/uuv_teleop.launch)

> **Arguments**

* **uuv_name**
* **joy_id** (*default:* `0`)
* **deadman_button** (*default:* `-1`)
* **exclusion_buttons** (*default:* `4,5`)
* **axis_roll** (*default:* `-1`)
* **axis_pitch** (*default:* `-1`)
* **axis_yaw** (*default:* `0`)
* **axis_x** (*default:* `4`)
* **axis_y** (*default:* `3`)
* **axis_z** (*default:* `1`)
* **gain_roll** (*default:* `0.0`)
* **gain_pitch** (*default:* `0.0`)
* **gain_yaw** (*default:* `0.2`)
* **gain_x** (*default:* `0.3`)
* **gain_y** (*default:* `0.3`)
* **gain_z** (*default:* `0.3`)
* **output_topic** (*default:* `cmd_vel`)
* **message_type** (*default:* `twist`)

## [`finned_uuv_teleop.launch`](https://github.com/uuvsimulator/uuv_simulator/tree/master/uuv_teleop/launch/finned_uuv_teleop.launch)

> **Arguments**

* **uuv_name**
* **joy_id** (*default:* `0`)
* **use_param_file** (*default:* `0`)
* **filename** (*default:* `.`)
* **axis_thruster** (*default:* `1`)
* **axis_roll** (*default:* `0`)
* **axis_pitch** (*default:* `4`)
* **axis_yaw** (*default:* `3`)
* **thruster_rotor_gain** (*default:* `0.0009`)
* **max_thrust** (*default:* `200`)
* **thruster_topic** (*default:* `thrusters/0/input`)
* **fin_topic_prefix** (*default:* `fins/`)
* **fin_topic_suffix** (*default:* `/input`)
* **thruster_joy_gain** (*default:* `1.0`)
* **n_fins** (*default:* `4`)
* **gain_roll** (*default:* `1,1,1,1`)
* **gain_pitch** (*default:* `1,1,-1,-1`)
* **gain_yaw** (*default:* `-1,1,1,-1`)

# Scripts

## `finned_uuv_teleop.py`

> **Script type:** `python`

## `vehicle_teleop.py`

> **Script type:** `python`

