![Version](https://img.shields.io/badge/version-0.6.12-brightgreen.svg)

> Link to the `uuv_simulator` repository [here](https://github.com/uuvsimulator/uuv_simulator)

# Description

Tools and utilities to monitor and analyze the simulation

# Launch files

## [`publish_footprints.launch`](https://github.com/uuvsimulator/uuv_simulator/tree/master/uuv_assistants/launch/publish_footprints.launch)

## [`message_to_tf.launch`](https://github.com/uuvsimulator/uuv_simulator/tree/master/uuv_assistants/launch/message_to_tf.launch)

> **Arguments**

* **namespace** (*default:* `rexrov`)
* **world_frame** (*default:* `world`)
* **child_frame_id** (*default:* `/$(arg namespace)/base_link`)
* **odometry_topic** (*default:* `/$(arg namespace)/pose_gt`)

## [`publish_vehicle_footprint.launch`](https://github.com/uuvsimulator/uuv_simulator/tree/master/uuv_assistants/launch/publish_vehicle_footprint.launch)

> **Arguments**

* **uuv_name**
* **scale_footprint** (*default:* `10`)
* **scale_label** (*default:* `10`)
* **label_x_offset** (*default:* `60`)
* **odom_topic** (*default:* `pose_gt`)

## [`publish_world_ned_frame.launch`](https://github.com/uuvsimulator/uuv_simulator/tree/master/uuv_assistants/launch/publish_world_ned_frame.launch)

## [`set_simulation_timer.launch`](https://github.com/uuvsimulator/uuv_simulator/tree/master/uuv_assistants/launch/set_simulation_timer.launch)

> **Arguments**

* **timeout**

## [`unpause_simulation.launch`](https://github.com/uuvsimulator/uuv_simulator/tree/master/uuv_assistants/launch/unpause_simulation.launch)

> **Arguments**

* **timeout** (*default:* `0`)

## [`publish_body_sname.launch`](https://github.com/uuvsimulator/uuv_simulator/tree/master/uuv_assistants/launch/publish_body_sname.launch)

> **Arguments**

* **uuv_name**

# Scripts

## `publish_world_models.py`

> **Script type:** `python`

## `generate_urdf`

## `publish_footprints.py`

> **Script type:** `python`

## `publish_vehicle_footprint.py`

> **Script type:** `python`

## `create_new_robot_model`

> **Script type:** `python`

## `unpause_simulation.py`

> **Script type:** `python`

## `create_thruster_manager_configuration`

> **Script type:** `python`

## `set_simulation_timer.py`

> **Script type:** `python`

