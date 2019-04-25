# C++ API

List of all classes categorized by package and file.

## `uuv_simulator`

### `uuv_gazebo_plugins`

> `BuoyantObject`

* [`BuoyantObject`](packages/uuv_simulator/docs/api/gazebo::BuoyantObject.md)  

> `Dynamics`

* [`Dynamics`](packages/uuv_simulator/docs/api/gazebo::Dynamics.md)
* [`DynamicsFactory`](packages/uuv_simulator/docs/api/gazebo::DynamicsFactory.md)
* [`DynamicsFirstOrder`](packages/uuv_simulator/docs/api/gazebo::DynamicsFirstOrder.md)
* [`DynamicsZeroOrder`](packages/uuv_simulator/docs/api/gazebo::DynamicsZeroOrder.md)
* [`ThrusterDynamicsBessa`](packages/uuv_simulator/docs/api/gazebo::ThrusterDynamicsBessa.md)
* [`ThrusterDynamicsYoerger`](packages/uuv_simulator/docs/api/gazebo::ThrusterDynamicsYoerger.md)

> `FinPlugin`

* [`FinPlugin`](packages/uuv_simulator/docs/api/gazebo::FinPlugin.md)

> `HydrodynamicModel`

* [`HydrodynamicModel`](packages/uuv_simulator/docs/api/gazebo::HydrodynamicModel.md)
* [`HydrodynamicModelFactory`](packages/uuv_simulator/docs/api/gazebo::HydrodynamicModelFactory.md)
* [`HMBox`](packages/uuv_simulator/docs/api/gazebo::HMBox.md)
* [`HMCylinder`](packages/uuv_simulator/docs/api/gazebo::HMCylinder.md)
* [`HMFossen`](packages/uuv_simulator/docs/api/gazebo::HMFossen.md)
* [`HMSphere`](packages/uuv_simulator/docs/api/gazebo::HMSphere.md)
* [`HMSpheroid`](packages/uuv_simulator/docs/api/gazebo::HMSpheroid.md)

> `LiftDragModel`

* [`LiftDrag`](packages/uuv_simulator/docs/api/gazebo::LiftDrag.md)
* [`LiftDragFactory`](packages/uuv_simulator/docs/api/gazebo::LiftDragFactory.md)
* [`LiftDragQuadratic`](packages/uuv_simulator/docs/api/gazebo::LiftDragQuadratic.md)
* [`LiftDragTwoLines`](packages/uuv_simulator/docs/api/gazebo::LiftDragTwoLines.md)
  
> `ThrusterConversionFcn`

* [`ConversionFunction`](packages/uuv_simulator/docs/api/gazebo::ConversionFunction.md)
* [`ConversionFunctionFactory`](packages/uuv_simulator/docs/api/gazebo::ConversionFunctionFactory.md)
* [`ConversionFunctionBasic`](packages/uuv_simulator/docs/api/gazebo::ConversionFunctionBasic.md)
* [`ConversionFunctionBessa`](packages/uuv_simulator/docs/api/gazebo::ConversionFunctionBessa.md)
* [`ConversionFunctionLinearInterp`](packages/uuv_simulator/docs/api/gazebo::ConversionFunctionLinearInterp.md)

> `ThrusterPlugin`

* [`ThrusterPlugin`](packages/uuv_simulator/docs/api/gazebo::ThrusterPlugin.md)

> `UnderwaterObjectPlugin`

* [`UnderwaterObjectPlugin`](packages/uuv_simulator/docs/api/gazebo::UnderwaterObjectPlugin.md)

### `uuv_gazebo_ros_plugins`

### `uuv_sensor_ros_plugins`

### `uuv_world_plugins`

### `uuv_world_ros_plugins`

# Python API

## `uuv_simulator`

### `uuv_auv_control_allocator`

> [`uuv_auv_actuator_interface`](packages/uuv_simulator/docs/python_api/uuv_auv_actuator_interface.md)

### `uuv_control_cascaded_pids`

> [`PID`](packages/uuv_simulator/docs/python_api/PID.md)

### `uuv_thruster_manager`

> [`uuv_thrusters`](packages/uuv_simulator/docs/python_api/uuv_thrusters.md)

### `uuv_trajectory_control`

> [`uuv_control_interfaces`](packages/uuv_simulator/docs/python_api/uuv_control_interfaces.md)

> [`uuv_trajectory_generator`](packages/uuv_simulator/docs/python_api/uuv_trajectory_generator.md)

> [`uuv_waypoints`](packages/uuv_simulator/docs/python_api/uuv_waypoints.md)


## `uuv_plume_simulator`

### `uuv_plume_simulator`

> [`uuv_gm_process`](packages/uuv_plume_simulator/docs/python_api/uuv_gm_process.md)

Python module that described a Gauss*Markov process of first*order and is used to compute 2D and 3D current velocity models.

> [`uuv_plume_model`](packages/uuv_plume_simulator/docs/python_api/uuv_plume_model.md)

Python module to generate plume particles and compute their dynamic model based on the turbulent diffusion coefficients, current velocity and buoyancy.