# uuv_trajectory_generator

# uuv_trajectory_generator.trajectory_generator

## TrajectoryGenerator
```python
TrajectoryGenerator(self, full_dof=False, stamped_pose_only=False)
```

### get_trajectory_as_message
```python
TrajectoryGenerator.get_trajectory_as_message(self)
```

Return the trajectory points as a Trajectory type message. If waypoints
are currently in use, then sample the interpolated path and return the
poses only.

### is_using_waypoints
```python
TrajectoryGenerator.is_using_waypoints(self)
```
Return true if the waypoint interpolation is being used.
### set_waypoints
```python
TrajectoryGenerator.set_waypoints(self, waypoints, init_rot=(0, 0, 0, 1))
```
Initializes the waypoint interpolator with a set of waypoints.
### get_waypoints
```python
TrajectoryGenerator.get_waypoints(self)
```

Return the waypoints used by the waypoint interpolator,
if any exist.

### add_waypoint
```python
TrajectoryGenerator.add_waypoint(self, waypoint, add_to_beginning=False)
```

Add waypoint to the current waypoint set, if one has been initialized.

### add_trajectory_point
```python
TrajectoryGenerator.add_trajectory_point(self, pnt)
```

If a trajectory set is currently being used in the interpolation
process, add a trajectory point to the set.

# uuv_trajectory_generator.trajectory_point

## TrajectoryPoint
```python
TrajectoryPoint(self, t=0.0, pos=[0, 0, 0], quat=[0, 0, 0, 1], lin_vel=[0, 0, 0], ang_vel=[0, 0, 0], lin_acc=[0, 0, 0], ang_acc=[0, 0, 0])
```

### a
Return linear acceleration vector.
### alpha
Return angular acceleration vector.
### p
Return position vector.
### q
Return rotation quaterinon.
### t
Return time stamp in seconds.
### v
Return linear velocity vector.
### w
Return angular velocity vector.
### x
Return X coordinate from the position vector.
### y
Return Y coordinate from the position vector.
### z
Return Z coordinate from the position vector.
### to_message
```python
TrajectoryPoint.to_message(self)
```
Convert current data to a trajectory point message.
### from_message
```python
TrajectoryPoint.from_message(self, msg)
```
Read trajectory point message and initialize internal attributes.
# uuv_trajectory_generator.wp_trajectory_generator

## WPTrajectoryGenerator
```python
WPTrajectoryGenerator(self, full_dof=False, use_finite_diff=True, interpolation_method='cubic', stamped_pose_only=False)
```

Class that generates a trajectory from the interpolated path generated
from a set of waypoints. It uses the information given for the waypoint's
maximum forward speed to estimate the velocity between waypoint and
parametrize the interpolated curve.
The velocity and acceleration profiles are the generated through finite
discretization. These profiles are not optimized, this class is a
simple solution for quick trajectory generation for waypoint navigation.

### closest_waypoint
Return the closest waypoint to the current position on the path.
### closest_waypoint_idx

Return the index of the closest waypoint to the current position on the
path.

### started
Return true if the interpolation has started.
### is_full_dof
```python
WPTrajectoryGenerator.is_full_dof(self)
```
Return true if the trajectory is generated for all 6 degrees of
freedom.

### get_max_time
```python
WPTrajectoryGenerator.get_max_time(self)
```
Return maximum trajectory time.
### set_duration
```python
WPTrajectoryGenerator.set_duration(self, t)
```
Set a new maximum trajectory time.
### is_finished
```python
WPTrajectoryGenerator.is_finished(self)
```
Return true if the trajectory has finished.
### reset
```python
WPTrajectoryGenerator.reset(self)
```
Reset all class attributes to allow a new trajectory to be
computed.

### init_waypoints
```python
WPTrajectoryGenerator.init_waypoints(self, waypoint_set, init_rot=(0, 0, 0, 1))
```
Initialize the waypoint set.
### add_waypoint
```python
WPTrajectoryGenerator.add_waypoint(self, waypoint, add_to_beginning=False)
```
Add waypoint to the existing waypoint set. If no waypoint set has
been initialized, create new waypoint set structure and add the given
waypoint.
### get_waypoints
```python
WPTrajectoryGenerator.get_waypoints(self)
```
Return waypoint set.
### update_dt
```python
WPTrajectoryGenerator.update_dt(self, t)
```
Update the time stamp.
### get_samples
```python
WPTrajectoryGenerator.get_samples(self, step=0.005)
```
Return pose samples from the interpolated path.
### set_start_time
```python
WPTrajectoryGenerator.set_start_time(self, t)
```
Set a custom starting time to the interpolated trajectory.
### generate_pnt
```python
WPTrajectoryGenerator.generate_pnt(self, t, pos, rot)
```
Return trajectory sample for the current parameter s.
# uuv_trajectory_generator.path_generator.bezier_curve

## BezierCurve
```python
BezierCurve(self, pnts, order, tangents=None, normals=None)
```

Implementation of Bezier curves of orders 3, 4 and 5 based on [1].

[1] Biagiotti, Luigi, and Claudio Melchiorri. Trajectory planning for
    automatic machines and robots. Springer Science & Business Media, 2008.

# uuv_trajectory_generator.path_generator.cs_interpolator

## CSInterpolator
```python
CSInterpolator(self)
```

Interpolator that will generate cubic Bezier curve segments for a set of waypoints.

### LABEL
str(object='') -> string

Return a nice string representation of the object.
If the argument is a string, the return value is the same object.
### set_parameters
```python
CSInterpolator.set_parameters(self, params)
```
Not implemented for this interpolator.
# uuv_trajectory_generator.path_generator.dubins_interpolator

## DubinsInterpolator
```python
DubinsInterpolator(self)
```

3D Dubins path interpolator

### LABEL
str(object='') -> string

Return a nice string representation of the object.
If the argument is a string, the return value is the same object.
# uuv_trajectory_generator.path_generator.helical_segment

# uuv_trajectory_generator.path_generator.line_segment

# uuv_trajectory_generator.path_generator.linear_interpolator

## LinearInterpolator
```python
LinearInterpolator(self)
```

Simple linear interpolator

### LABEL
str(object='') -> string

Return a nice string representation of the object.
If the argument is a string, the return value is the same object.
### set_parameters
```python
LinearInterpolator.set_parameters(self, params)
```
Not implemented for this interpolator.
# uuv_trajectory_generator.path_generator.lipb_interpolator

## LIPBInterpolator
```python
LIPBInterpolator(self)
```

Linear interpolator with polynomial blends.

[1] Biagiotti, Luigi, and Claudio Melchiorri. Trajectory planning for
    automatic machines and robots. Springer Science & Business Media, 2008.

### LABEL
str(object='') -> string

Return a nice string representation of the object.
If the argument is a string, the return value is the same object.
# uuv_trajectory_generator.path_generator.path_generator

