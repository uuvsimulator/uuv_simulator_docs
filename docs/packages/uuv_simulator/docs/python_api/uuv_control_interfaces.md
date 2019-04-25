# uuv_control_interfaces

# uuv_control_interfaces.dp_controller_base

## DPControllerBase
```python
DPControllerBase(self, is_model_based=False, list_odometry_callbacks=[], planner_full_dof=False)
```
General abstract class for DP controllers for underwater vehicles.
This is an abstract class, must be inherited by a controller module that
overrides the update_controller method. If the controller is set to be
model based (is_model_based=True), than the vehicle parameters are going
to be read from the ROS parameter server.

### error_orientation_rpy
Return orientation error in Euler angles.
### error_pose_euler
Pose error with orientation represented in Euler angles.
### get_controller
```python
DPControllerBase.get_controller(name, *args)
```
Create instance of a specific DP controller.
### get_list_of_controllers
```python
DPControllerBase.get_list_of_controllers()
```
Return list of DP controllers using this interface.
# uuv_control_interfaces.dp_controller_local_planner

## DPControllerLocalPlanner
```python
DPControllerLocalPlanner(self, full_dof=False, stamped_pose_only=False, thrusters_only=True)
```

Local planner for the dynamic positioning controllers to interpolate
trajectories and generate trajectories from interpolated waypoint paths.

### set_station_keeping
```python
DPControllerLocalPlanner.set_station_keeping(self, is_on=True)
```
Set station keeping mode flag.
### set_automatic_mode
```python
DPControllerLocalPlanner.set_automatic_mode(self, is_on=True)
```
Set automatic mode flag.
### set_trajectory_running
```python
DPControllerLocalPlanner.set_trajectory_running(self, is_on=True)
```
Set trajectory tracking flag.
### has_started
```python
DPControllerLocalPlanner.has_started(self)
```

Return if the trajectory interpolator has started generating reference
points.

### hold_vehicle
```python
DPControllerLocalPlanner.hold_vehicle(self, request)
```

Service callback function to hold the vehicle's current position.

### start_waypoint_list
```python
DPControllerLocalPlanner.start_waypoint_list(self, request)
```

Service callback function to follow a set of waypoints
Args:
    request (InitWaypointSet)

### go_to_incremental
```python
DPControllerLocalPlanner.go_to_incremental(self, request)
```

Service callback to set the command to the vehicle to move to a
relative position in the world.

### interpolate
```python
DPControllerLocalPlanner.interpolate(self, t)
```

Function interface to the controller. Calls the interpolator to
calculate the current trajectory sample or returns a fixed position
based on the past odometry measurements for station keeping.

# uuv_control_interfaces.dp_pid_controller_base

## DPPIDControllerBase
```python
DPPIDControllerBase(self, *args)
```

This is an abstract class for PID-based controllers. The base class method
update_controller must be overridden in other for a controller to work.

# uuv_control_interfaces.sym_vehicle

# uuv_control_interfaces.vehicle

## cross_product_operator
```python
cross_product_operator(x)
```
Return a cross product operator for the given vector.
## Vehicle
```python
Vehicle(self, inertial_frame_id='world')
```
Vehicle interface to be used by model-based controllers. It receives the
parameters necessary to compute the vehicle's motion according to Fossen's.

### acc
Return linear and angular acceleration vector.
### depth
Return depth of the vehicle.
### euler
Return orientation in Euler angles as described in Fossen, 2011.
### euler_dot
Return time derivative of the Euler angles.
### heading
Return the heading of the vehicle.
### namespace
Return robot namespace.
### pos
Return the position of the vehicle.
### pose_euler
Return pose as a vector, orientation in Euler angles.
### pose_quat
Return pose as a vector, orientation as quaternion.
### quat
Return orientation quaternion.
### quat_dot
Return the time derivative of the quaternion vector.
### restoring_forces
Return the restoring force vector.
### rotBtoI
Return rotation from BODY to INERTIAL frame using the zyx convention
to retrieve Euler angles from the quaternion vector (Fossen, 2011).

### rotItoB
Return rotation from INERTIAL to BODY frame
### TBtoIquat

Return matrix for transformation of BODY-fixed angular velocities in the
BODY frame in relation to the INERTIAL frame into quaternion rate.

### vel
Return linear and angular velocity vector.
### print_info
```python
Vehicle.print_info(self)
```
Print the vehicle's parameters.
### set_added_mass
```python
Vehicle.set_added_mass(self, Ma)
```
Set added-mass matrix coefficients.
### set_damping_coef
```python
Vehicle.set_damping_coef(self, linear_damping, quad_damping)
```
Set linear and quadratic damping coefficients.
### compute_force
```python
Vehicle.compute_force(self, acc=None, vel=None, with_restoring=True, use_sname=True)
```
Return the sum of forces acting on the vehicle.

Given acceleration and velocity vectors, this function returns the
sum of forces given the rigid-body and hydrodynamic models for the
marine vessel.

### compute_acc
```python
Vehicle.compute_acc(self, gen_forces=None, use_sname=True)
```
Calculate inverse dynamics to obtain the acceleration vector.
### get_jacobian
```python
Vehicle.get_jacobian(self)
```

Return the Jacobian for the current orientation using transformations
from BODY to INERTIAL frame.

### update_odometry
```python
Vehicle.update_odometry(self, msg)
```
Odometry topic subscriber callback function.
