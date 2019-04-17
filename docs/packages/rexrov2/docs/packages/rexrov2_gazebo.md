![Version](https://img.shields.io/badge/version-0.1.3-brightgreen.svg)

> Link to the `rexrov2` repository [here](https://github.com/uuvsimulator/rexrov2)

# Launch files

## [`start_demo_pd_grav_compensation_controller.launch`](https://github.com/uuvsimulator/rexrov2/tree/master/rexrov2_gazebo/launch/start_demo_pd_grav_compensation_controller.launch)

> **Arguments**

* **record** (*default:* `false`): Set this flag to true to call record.launch
* **bag_filename** (*default:* `recording.bag`): Name of the output ROS bag file in case record is set to true
* **use_ned_frame** (*default:* `false`): If true, uses the NED (North-East-Down) frame conversion. If false, ENU (East-North-Up) will be used per default.
* **x** (*default:* `0`): X coordinate of the vehicle's initial position (in ENU)
* **y** (*default:* `0`): Y coordinate of the vehicle's initial position (in ENU)
* **z** (*default:* `-25`): Z coordinate of the vehicle's initial position (in ENU)
* **yaw** (*default:* `0`): Yaw angle of the vehicle's initial orientation
* **teleop_on** (*default:* `false`): If true, the teleop node will be started
* **joy_id** (*default:* `0`): Joystick ID

## [`start_demo_nmb_sm_controller.launch`](https://github.com/uuvsimulator/rexrov2/tree/master/rexrov2_gazebo/launch/start_demo_nmb_sm_controller.launch)

> **Arguments**

* **record** (*default:* `false`): Set this flag to true to call record.launch
* **bag_filename** (*default:* `recording.bag`): Name of the output ROS bag file in case record is set to true
* **use_ned_frame** (*default:* `false`): If true, uses the NED (North-East-Down) frame conversion. If false, ENU (East-North-Up) will be used per default.
* **x** (*default:* `0`): X coordinate of the vehicle's initial position (in ENU)
* **y** (*default:* `0`): Y coordinate of the vehicle's initial position (in ENU)
* **z** (*default:* `-25`): Z coordinate of the vehicle's initial position (in ENU)
* **yaw** (*default:* `0`): Yaw angle of the vehicle's initial orientation
* **teleop_on** (*default:* `false`): If true, the teleop node will be started
* **joy_id** (*default:* `0`): Joystick ID

## [`start_demo_pid_controller.launch`](https://github.com/uuvsimulator/rexrov2/tree/master/rexrov2_gazebo/launch/start_demo_pid_controller.launch)

> **Arguments**

* **record** (*default:* `false`): Set this flag to true to call record.launch
* **bag_filename** (*default:* `recording.bag`): Name of the output ROS bag file in case record is set to true
* **use_ned_frame** (*default:* `false`): If true, uses the NED (North-East-Down) frame conversion. If false, ENU (East-North-Up) will be used per default.
* **x** (*default:* `0`): X coordinate of the vehicle's initial position (in ENU)
* **y** (*default:* `0`): Y coordinate of the vehicle's initial position (in ENU)
* **z** (*default:* `-25`): Z coordinate of the vehicle's initial position (in ENU)
* **yaw** (*default:* `0`): Yaw angle of the vehicle's initial orientation
* **teleop_on** (*default:* `false`): If true, the teleop node will be started
* **joy_id** (*default:* `0`): Joystick ID

## [`start_demo_sf_controller.launch`](https://github.com/uuvsimulator/rexrov2/tree/master/rexrov2_gazebo/launch/start_demo_sf_controller.launch)

> **Arguments**

* **record** (*default:* `false`): Set this flag to true to call record.launch
* **bag_filename** (*default:* `recording.bag`): Name of the output ROS bag file in case record is set to true
* **use_ned_frame** (*default:* `false`): If true, uses the NED (North-East-Down) frame conversion. If false, ENU (East-North-Up) will be used per default.
* **x** (*default:* `0`): X coordinate of the vehicle's initial position (in ENU)
* **y** (*default:* `0`): Y coordinate of the vehicle's initial position (in ENU)
* **z** (*default:* `-25`): Z coordinate of the vehicle's initial position (in ENU)
* **yaw** (*default:* `0`): Yaw angle of the vehicle's initial orientation
* **teleop_on** (*default:* `false`): If true, the teleop node will be started
* **joy_id** (*default:* `0`): Joystick ID

## [`start_demo_mb_fl_controller.launch`](https://github.com/uuvsimulator/rexrov2/tree/master/rexrov2_gazebo/launch/start_demo_mb_fl_controller.launch)

> **Arguments**

* **record** (*default:* `false`): Set this flag to true to call record.launch
* **bag_filename** (*default:* `recording.bag`): Name of the output ROS bag file in case record is set to true
* **use_ned_frame** (*default:* `false`): If true, uses the NED (North-East-Down) frame conversion. If false, ENU (East-North-Up) will be used per default.
* **x** (*default:* `0`): X coordinate of the vehicle's initial position (in ENU)
* **y** (*default:* `0`): Y coordinate of the vehicle's initial position (in ENU)
* **z** (*default:* `-5`): Z coordinate of the vehicle's initial position (in ENU)
* **yaw** (*default:* `0`): Yaw angle of the vehicle's initial orientation
* **teleop_on** (*default:* `false`): If true, the teleop node will be started
* **joy_id** (*default:* `0`): Joystick ID

## [`record.launch`](https://github.com/uuvsimulator/rexrov2/tree/master/rexrov2_gazebo/launch/record.launch)

> **Arguments**

* **record** (*default:* `false`): If true, the rosbag record node will be called
* **bag_filename** (*default:* `recording.bag`): Name of the recording bag
* **uuv_name** (*default:* `rexrov2`): Namespace of the vehicle

