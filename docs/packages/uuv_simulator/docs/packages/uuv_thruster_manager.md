![Version](https://img.shields.io/badge/version-0.6.11-brightgreen.svg)

> Link to the `uuv_simulator` repository [here](https://github.com/uuvsimulator/uuv_simulator)

# Description

The thruster manager package

# Launch files

## [`thruster_manager.launch`](https://github.com/uuvsimulator/uuv_simulator/tree/master/uuv_thruster_manager/launch/thruster_manager.launch)

> **Arguments**

* **model_name**
* **uuv_name** (*default:* `$(arg model_name)`)
* **base_link** (*default:* `base_link`)
* **timeout** (*default:* `-1`)
* **reset_tam** (*default:* `false`)
* **output_dir** (*default:* `$(find uuv_thruster_manager)/config/$(arg model_name)`)
* **config_file** (*default:* `$(find uuv_thruster_manager)/config/$(arg model_name)/thruster_manager.yaml`)
* **tam_file** (*default:* `$(find uuv_thruster_manager)/config/$(arg model_name)/TAM.yaml`)

# ROS Services

## `GetThrusterManagerConfig`

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

---
string tf_prefix
string base_link
string thruster_frame_base
string thruster_topic_prefix
string thruster_topic_suffix
float64 timeout
float64 max_thrust
int32 n_thrusters
float64[] allocation_matrix

```

## `SetThrusterManagerConfig`

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

# Definitions
string DEFAULT_BASE_LINK            = /base_link
string DEFAULT_THRUSTER_FRAME_BASE  = /thruster_
string DEFAULT_PREFIX               = thrusters/
string DEFAULT_SUFFIX               = /input
# Service definition
string base_link
string thruster_frame_base
string thruster_topic_prefix
string thruster_topic_suffix
float64 timeout
float64 max_thrust
---
bool success

```

## `ThrusterManagerInfo`

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

---
int32 n_thrusters
float64[] allocation_matrix
string reference_frame

```

## `GetThrusterCurve`

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

float64 min
float64 max
int32 n_points
---
float64[] input
float64[] thrust

```

# Scripts

## `thruster_allocator.py`

> **Script type:** `python`

