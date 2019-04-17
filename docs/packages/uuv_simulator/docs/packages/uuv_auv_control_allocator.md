![Version](https://img.shields.io/badge/version-0.6.11-brightgreen.svg)

> Link to the `uuv_simulator` repository [here](https://github.com/uuvsimulator/uuv_simulator)

# Description

Optimal allocation of forces and torques to thruster and fins of AUVs

# Launch files

## [`start_control_allocator.launch`](https://github.com/uuvsimulator/uuv_simulator/tree/master/uuv_auv_control_allocator/launch/start_control_allocator.launch)

> **Arguments**

* **uuv_name**
* **base_link** (*default:* `base_link`)
* **output_dir**
* **input_topic** (*default:* `control_allocation/control_input`)
* **thruster_topic_prefix** (*default:* `thrusters`)
* **thruster_topic_suffix** (*default:* `input`)
* **thruster_frame_base** (*default:* `thruster_`)
* **max_thrust** (*default:* `120`)
* **thruster_conversion_fcn** (*default:* `proportional`)
* **thruster_gain** (*default:* `0.0`)
* **thruster_input** (*default:* `0,1,2,3`)
* **thruster_output** (*default:* `0,1,2,3`)
* **fin_frame_base** (*default:* `fin`)
* **fluid_density** (*default:* `1028.0`)
* **lift_coefficient** (*default:* `0.0`)
* **fin_area** (*default:* `0.0`)
* **fin_topic_prefix** (*default:* `fins`)
* **fin_topic_suffix** (*default:* `input`)
* **fin_lower_joint_limit** (*default:* `-1.57`)
* **fin_upper_joint_limit** (*default:* `1.57`)
* **timeout** (*default:* `-1`)
* **update_rate** (*default:* `10`)

# ROS Messages

## `AUVCommand`

```
# Copyright (c) 2016 The UUV Simulator Authors.
# All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

std_msgs/Header header
float64 surge_speed
geometry_msgs/Wrench command
```

# Scripts

## `control_allocator`

> **Script type:** `python`

