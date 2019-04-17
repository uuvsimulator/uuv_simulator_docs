![Version](https://img.shields.io/badge/version-0.1.3-brightgreen.svg)

> Link to the `rexrov2` repository [here](https://github.com/uuvsimulator/rexrov2)

# Description

The robot description files for the RexROV 2 underwater vehicle and launch files to spawn the model in different configurations.

# Launch files

## [`upload_rexrov2_oberon4.launch`](https://github.com/uuvsimulator/rexrov2/tree/master/rexrov2_description/launch/upload_rexrov2_oberon4.launch)

> **Arguments**

* **debug** (*default:* `0`)
* **x** (*default:* `0`)
* **y** (*default:* `0`)
* **z** (*default:* `-20`)
* **roll** (*default:* `0.0`)
* **pitch** (*default:* `0.0`)
* **yaw** (*default:* `0.0`)
* **use_geodetic** (*default:* `false`)
* **latitude** (*default:* `0`)
* **longitude** (*default:* `0`)
* **depth** (*default:* `0`)
* **latitude_ref** (*default:* `0`)
* **longitude_ref** (*default:* `0`)
* **altitude_ref** (*default:* `0`)
* **namespace** (*default:* `rexrov2`)
* **use_simplified_mesh** (*default:* `false`)
* **world_frame** (*default:* `world`)

## [`upload_rexrov2_oberon7.launch`](https://github.com/uuvsimulator/rexrov2/tree/master/rexrov2_description/launch/upload_rexrov2_oberon7.launch)

> **Arguments**

* **debug** (*default:* `0`)
* **x** (*default:* `0`)
* **y** (*default:* `0`)
* **z** (*default:* `-20`)
* **roll** (*default:* `0.0`)
* **pitch** (*default:* `0.0`)
* **yaw** (*default:* `0.0`)
* **use_geodetic** (*default:* `false`)
* **latitude** (*default:* `0`)
* **longitude** (*default:* `0`)
* **depth** (*default:* `0`)
* **latitude_ref** (*default:* `0`)
* **longitude_ref** (*default:* `0`)
* **altitude_ref** (*default:* `0`)
* **namespace** (*default:* `rexrov2`)
* **use_simplified_mesh** (*default:* `false`)
* **world_frame** (*default:* `world`)

## [`upload_rexrov2_oberon_arms.launch`](https://github.com/uuvsimulator/rexrov2/tree/master/rexrov2_description/launch/upload_rexrov2_oberon_arms.launch)

> **Arguments**

* **debug** (*default:* `0`)
* **x** (*default:* `0`)
* **y** (*default:* `0`)
* **z** (*default:* `-20`)
* **roll** (*default:* `0.0`)
* **pitch** (*default:* `0.0`)
* **yaw** (*default:* `0.0`)
* **use_geodetic** (*default:* `false`)
* **latitude** (*default:* `0`)
* **longitude** (*default:* `0`)
* **depth** (*default:* `0`)
* **latitude_ref** (*default:* `0`)
* **longitude_ref** (*default:* `0`)
* **altitude_ref** (*default:* `0`)
* **namespace** (*default:* `rexrov2`)
* **use_simplified_mesh** (*default:* `false`)
* **world_frame** (*default:* `world`)

## [`upload_rexrov2.launch`](https://github.com/uuvsimulator/rexrov2/tree/master/rexrov2_description/launch/upload_rexrov2.launch)

> **Description**

Spawns the RexROV 2 vehicle in the simulation 


> **Arguments**

* **debug** (*default:* `0`): Starts the Gazebo plugins in debug mode for more verbose output
* **x** (*default:* `0`): X coordinate of the vehicle's initial position (in ENU)
* **y** (*default:* `0`): Y coordinate of the vehicle's initial position (in ENU)
* **z** (*default:* `-20`): Z coordinate of the vehicle's initial position (in ENU)
* **roll** (*default:* `0.0`): Roll angle of the vehicle's initial orientation
* **pitch** (*default:* `0.0`): Pitch angle of the vehicle's initial orientation
* **yaw** (*default:* `0.0`): Yaw angle of the vehicle's initial orientation
* **use_geodetic** (*default:* `false`): Spawn the vehicle using geodetic instead of Cartesian coordinates
* **latitude** (*default:* `0`): Latitude for the vehicle's initial position in degrees
* **longitude** (*default:* `0`): Longitude for the vehicle's initial position in degrees
* **depth** (*default:* `0`): Depth of the vehicle's initial position with respect to the water surface in meters
* **latitude_ref** (*default:* `0`): Latitude of the origin in degrees
* **longitude_ref** (*default:* `0`): Longitude of the origin in degrees
* **altitude_ref** (*default:* `0`): Altitude of the origin in meters
* **mode** (*default:* `default`): Vehicle's build configuration mode
* **namespace** (*default:* `rexrov2`): Namespace to spawn the vehicle
* **use_simplified_mesh** (*default:* `false`): Use simplified geometries instead of the mesh
* **use_ned_frame** (*default:* `false`): Set the inertial reference to NED (North-East-Down) convention instead of Gazebo's default ENU (East-North-Up)

