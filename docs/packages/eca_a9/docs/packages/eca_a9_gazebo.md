![Version](https://img.shields.io/badge/version-0.1.5-brightgreen.svg)

> Link to the `eca_a9` repository [here](https://github.com/uuvsimulator/eca_a9)

# Description

Package with launch files for demonstrations with the ECA A9 AUV

# Launch files

## [`start_demo_nmb_sm.launch`](https://github.com/uuvsimulator/eca_a9/tree/master/eca_a9_gazebo/launch/start_demo_nmb_sm.launch)

> **Arguments**

* **uuv_name** (*default:* `eca_a9`)
* **x** (*default:* `0`)
* **y** (*default:* `0`)
* **z** (*default:* `-20`)
* **yaw** (*default:* `0`)
* **gui_on** (*default:* `true`)
* **record** (*default:* `false`)
* **bag_filename** (*default:* `recording.bag`)
* **use_ned_frame** (*default:* `false`)
* **joy_id** (*default:* `0`)

## [`record_demo.launch`](https://github.com/uuvsimulator/eca_a9/tree/master/eca_a9_gazebo/launch/record_demo.launch)

> **Arguments**

* **record** (*default:* `false`)
* **bag_filename** (*default:* `recording.bag`)
* **use_ned_frame** (*default:* `false`)

## [`start_demo_teleop.launch`](https://github.com/uuvsimulator/eca_a9/tree/master/eca_a9_gazebo/launch/start_demo_teleop.launch)

> **Arguments**

* **x** (*default:* `0`)
* **y** (*default:* `0`)
* **z** (*default:* `-5`)
* **yaw** (*default:* `0`)
* **record** (*default:* `false`)
* **bag_filename** (*default:* `recording.bag`)
* **use_ned_frame** (*default:* `false`)
* **joy_id** (*default:* `0`)

## [`start_waypoint_set.launch`](https://github.com/uuvsimulator/eca_a9/tree/master/eca_a9_gazebo/launch/start_waypoint_set.launch)

> **Arguments**

* **interpolator** (*default:* `cubic`)

## [`start_demo_auv_control.launch`](https://github.com/uuvsimulator/eca_a9/tree/master/eca_a9_gazebo/launch/start_demo_auv_control.launch)

> **Arguments**

* **x** (*default:* `0`)
* **y** (*default:* `0`)
* **z** (*default:* `-5`)
* **yaw** (*default:* `0`)
* **record** (*default:* `false`)
* **bag_filename** (*default:* `recording.bag`)
* **use_ned_frame** (*default:* `false`)

