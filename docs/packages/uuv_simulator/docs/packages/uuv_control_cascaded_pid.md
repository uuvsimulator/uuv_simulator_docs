![Version](https://img.shields.io/badge/version-0.6.11-brightgreen.svg)

> Link to the `uuv_simulator` repository [here](https://github.com/uuvsimulator/uuv_simulator)

# Launch files

## [`joy_velocity.launch`](https://github.com/uuvsimulator/uuv_simulator/tree/master/uuv_control_cascaded_pid/launch/joy_velocity.launch)

> **Arguments**

* **model_name**
* **uuv_name** (*default:* `$(arg model_name)`)
* **joy_id** (*default:* `0`)

## [`joy_accel.launch`](https://github.com/uuvsimulator/uuv_simulator/tree/master/uuv_control_cascaded_pid/launch/joy_accel.launch)

> **Arguments**

* **model_name**
* **uuv_name** (*default:* `$(arg model_name)`)
* **joy_id** (*default:* `0`)

## [`position_hold.launch`](https://github.com/uuvsimulator/uuv_simulator/tree/master/uuv_control_cascaded_pid/launch/position_hold.launch)

> **Arguments**

* **model_name**
* **uuv_name** (*default:* `$(arg model_name)`)

# Scripts

## `AccelerationControl.py`

> **Script type:** `python`

## `PositionControl.py`

> **Script type:** `python`

## `PositionControlUnderactuated.py`

> **Script type:** `python`

## `VelocityControl.py`

> **Script type:** `python`

