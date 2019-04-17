![Version](https://img.shields.io/badge/version-0.6.11-brightgreen.svg)

> Link to the `uuv_simulator` repository [here](https://github.com/uuvsimulator/uuv_simulator)

# Description

The uuv_control_utils package

# Launch files

## [`send_waypoints_file.launch`](https://github.com/uuvsimulator/uuv_simulator/tree/master/uuv_control_utils/launch/send_waypoints_file.launch)

> **Arguments**

* **uuv_name**
* **filename** (*default:* `$(find uuv_control_utils)/config/example_waypoints.yaml`)
* **start_time** (*default:* `-1`)
* **interpolator** (*default:* `lipb`)

## [`set_timed_current_perturbation.launch`](https://github.com/uuvsimulator/uuv_simulator/tree/master/uuv_control_utils/launch/set_timed_current_perturbation.launch)

> **Arguments**

* **starting_time** (*default:* `0.0`)
* **end_time** (*default:* `-1`)
* **current_vel** (*default:* `1`)
* **horizontal_angle** (*default:* `0.0`)
* **vertical_angle** (*default:* `0.0`)

## [`start_disturbance_manager.launch`](https://github.com/uuvsimulator/uuv_simulator/tree/master/uuv_control_utils/launch/start_disturbance_manager.launch)

> **Arguments**

* **uuv_name**
* **use_file** (*default:* `false`)
* **disturbance_file**
* **current_starting_time** (*default:* `20.0`)
* **current_vel** (*default:* `1`)
* **current_horz_angle** (*default:* `0.0`)
* **current_vert_angle** (*default:* `0.0`)
* **current_duration** (*default:* `10`)
* **force_x** (*default:* `0`)
* **force_y** (*default:* `2000`)
* **force_z** (*default:* `0`)
* **torque_x** (*default:* `0`)
* **torque_y** (*default:* `0`)
* **torque_z** (*default:* `0`)
* **wrench_starting_time** (*default:* `30`)
* **wrench_duration** (*default:* `20`)

## [`apply_body_wrench.launch`](https://github.com/uuvsimulator/uuv_simulator/tree/master/uuv_control_utils/launch/apply_body_wrench.launch)

> **Arguments**

* **uuv_name**
* **force_x** (*default:* `0`)
* **force_y** (*default:* `0`)
* **force_z** (*default:* `0`)
* **torque_x** (*default:* `0`)
* **torque_y** (*default:* `0`)
* **torque_z** (*default:* `0`)
* **starting_time** (*default:* `0`)
* **duration** (*default:* `1`)

## [`start_circular_trajectory.launch`](https://github.com/uuvsimulator/uuv_simulator/tree/master/uuv_control_utils/launch/start_circular_trajectory.launch)

> **Arguments**

* **uuv_name**
* **start_time** (*default:* `-1`)
* **radius** (*default:* `8`)
* **center_x** (*default:* `4`)
* **center_y** (*default:* `2`)
* **center_z** (*default:* `-22`)
* **n_points** (*default:* `50`)
* **heading_offset** (*default:* `0`)
* **duration** (*default:* `0`)
* **max_forward_speed** (*default:* `0.3`)

## [`set_gm_current_perturbation.launch`](https://github.com/uuvsimulator/uuv_simulator/tree/master/uuv_control_utils/launch/set_gm_current_perturbation.launch)

> **Arguments**

* **component**
* **mean** (*default:* `0.0`)
* **min** (*default:* `0.0`)
* **max** (*default:* `0.0`)
* **noise** (*default:* `0.0`)
* **mu** (*default:* `0.0`)

## [`set_scalar_parameter.launch`](https://github.com/uuvsimulator/uuv_simulator/tree/master/uuv_control_utils/launch/set_scalar_parameter.launch)

> **Arguments**

* **uuv_name**
* **service_name**
* **data**

## [`set_thruster_output_efficiency.launch`](https://github.com/uuvsimulator/uuv_simulator/tree/master/uuv_control_utils/launch/set_thruster_output_efficiency.launch)

> **Arguments**

* **uuv_name**
* **starting_time** (*default:* `0.0`)
* **thruster_id** (*default:* `0`)
* **efficiency** (*default:* `1.0`)
* **duration** (*default:* `-1`)

## [`set_thruster_state.launch`](https://github.com/uuvsimulator/uuv_simulator/tree/master/uuv_control_utils/launch/set_thruster_state.launch)

> **Arguments**

* **uuv_name**
* **starting_time** (*default:* `0.0`)
* **thruster_id** (*default:* `0`)
* **is_on** (*default:* `0`)
* **duration** (*default:* `-1`)

## [`start_helical_trajectory.launch`](https://github.com/uuvsimulator/uuv_simulator/tree/master/uuv_control_utils/launch/start_helical_trajectory.launch)

> **Arguments**

* **uuv_name**
* **start_time** (*default:* `-1`)
* **radius** (*default:* `8`)
* **center_x** (*default:* `0`)
* **center_y** (*default:* `0`)
* **center_z** (*default:* `-30`)
* **n_points** (*default:* `50`)
* **n_turns** (*default:* `1`)
* **delta_z** (*default:* `5.0`)
* **heading_offset** (*default:* `0`)
* **duration** (*default:* `150`)
* **max_forward_speed** (*default:* `0.3`)

# Scripts

## `set_timed_current_perturbation.py`

> **Script type:** `python`

## `apply_body_wrench.py`

> **Script type:** `python`

## `trajectory_marker_publisher.py`

> **Script type:** `python`

## `set_scalar_parameter.py`

> **Script type:** `python`

## `set_thruster_output_efficiency.py`

> **Script type:** `python`

## `start_helical_trajectory.py`

> **Script type:** `python`

## `disturbance_manager.py`

> **Script type:** `python`

## `send_waypoint_file.py`

> **Script type:** `python`

## `start_circular_trajectory.py`

> **Script type:** `python`

## `set_thruster_state.py`

> **Script type:** `python`

## `set_gm_current_perturbation.py`

> **Script type:** `python`

