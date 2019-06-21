# uuv_trajectory_generator
Trajectory generation package.
# uuv_trajectory_generator.trajectory_generator

## TrajectoryGenerator
```python
TrajectoryGenerator(self, full_dof=False, stamped_pose_only=False)
```
Trajectory generator based on waypoint and trajectory interpolation.

> *Input arguments*

* `full_dof` (*type:* `bool`, *default:* `False`): If `True`, generate
the trajectory in 6 DoFs, otherwise `roll` and `pitch` are set to zero.
* `stamped_pose_only` (*type:* `bool`, *default:* `False`): If `True`
the output trajectory will set velocity and acceleration references
as zero.

### points
List of `uuv_trajectory_generator.TrajectoryPoint`: List of trajectory points
### time
List of `float`: List of timestamps
### set_stamped_pose_only
```python
TrajectoryGenerator.set_stamped_pose_only(self, flag)
```
Set flag to enable or disable computation of trajectory
points

> *Input arguments*

* `flag` (*type:* `bool`): Parameter description

> *Returns*

Description of return values

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
Trajectory point data structure.

> *Input arguments*

* `t` (*type:* `float`, *value:* `0`): Timestamp
* `pos` (*type:* list of `float` or `numpy.array`, *default:* `[0, 0, 0]`):
3D position vector in meters
* `quat` (*type:* list of `float` or `numpy.array`, *default:* `[0, 0, 0, 1]`):
Quaternion in the form of `(x, y, z, w)`.
* `lin_vel` (*type:* list of `float` or `numpy.array`, *default:* `[0, 0, 0]`):
3D linear velocity vector in m/s
* `ang_vel` (*type:* list of `float` or `numpy.array`, *default:* `[0, 0, 0]`):
3D angular velocity vector as rad/s
* `lin_acc` (*type:* list of `float` or `numpy.array`, *default:* `[0, 0, 0]`):
3D linear acceleration vector as m/s$^2$
* `ang_acc` (*type:* list of `float` or `numpy.array`, *default:* `[0, 0, 0]`):
3D angular acceleration vector as rad/s$^2$

### a
`numpy.array`: Linear acceleration vector
### acc
`numpy.array`: Linear acceleration vector
### alpha
`numpy.array`: Angular acceleartion vector
### p
`numpy.array`: Position vector
### pos
`numpy.array`: Position vector
### q
`numpy.array`: Quaternion vector as `(x, y, z, w)`
### rot
`numpy.array`: `roll`, `pitch` and `yaw` angles
### rot_matrix
`numpy.array`: Rotation matrix
### rotq
`numpy.array`: Quaternion vector as `(x, y, z, w)`
### t
`float`: Time stamp
### v
`numpy.array`: Linear velocity vector
### vel
`numpy.array`: Linear velocity vector
### w
`numpy.array`: Angular velocity vector
### x
`float`: X coordinate of position vector
### y
`float`: Y coordinate of position vector
### z
`float`: Z coordinate of position vector
### to_message
```python
TrajectoryPoint.to_message(self)
```
Convert current data to a trajectory point message.

> *Returns*

Trajectory point message as `uuv_control_msgs/TrajectoryPoint`

### from_message
```python
TrajectoryPoint.from_message(self, msg)
```
Parse a trajectory point message of type `uuv_control_msgs/TrajectoryPoint`
into the `uuv_trajectory_generator/TrajectoryPoint`.

> *Input arguments*

* `msg` (*type:* `uuv_control_msgs/TrajectoryPoint`): Input trajectory message

### from_dict
```python
TrajectoryPoint.from_dict(self, data)
```
Initialize the trajectory point attributes from a `dict`.

> *Input arguments*

* `data` (*type:* `dict`): Trajectory point as a `dict`

### to_dict
```python
TrajectoryPoint.to_dict(self)
```
Convert trajectory point to `dict`.

> *Returns*

Trajectory points data as a `dict`

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

> *Input arguments*

* `full_dof` (*type:* `bool`, *default:* `False`): `True` to generate 6 DoF
trajectories
* `use_finite_diff` (*type:* `bool`, *default:* `True`): Use finite differentiation
if `True`, otherwise use the motion regression algorithm
* `interpolation_method` (*type:* `str`, *default:* `cubic`): Name of the interpolation
method, options are `cubic`, `dubins`, `lipb` or `linear`
* `stamped_pose_only` (*type:* `bool`, *default:* `False`): Generate only position
and quaternion vectors, velocities and accelerations are set to zero

### closest_waypoint
Return the closest waypoint to the current position on the path.
### closest_waypoint_idx
`int`: Index of the closest waypoint to the current position on the
path.

### interpolator
`str`: Name of the interpolation method
### interpolator_tags
List of `str`: List of all interpolation method
### stamped_pose_only
`bool`: Flag to enable computation of stamped poses
### started
`bool`: Flag set to true if the interpolation has started.
### use_finite_diff
`bool`: Use finite differentiation for computation of
trajectory points

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

Implementation of [Bezier curves](https://en.wikipedia.org/wiki/B%C3%A9zier_curve)
of orders 3, 4 and 5 based on [1].

> *Input arguments*

* `pnts` (*type:* `list`): List of 3D points as a vector (example: `[[0, 0, 0], [0, 1, 2]]`)
* `order` (*type:* `int`): Order of the Bezier curve, options are 3, 4 or 5
* `tangents` (*type:* `list`, *default:* `None`): Optional input of the tangent
vectors for each of the input points. In case only two points are provided,
the tangents have to be provided, too. Otherwise, the tangents will be calculated.
* `normals` (*type:* `list`, *default:* `None`): Optional input of the normal
vectors for each of the input points. In case only two points are provided,
the normals have to be provided, too. Otherwise, the normals will be calculated.

!!! note

    [1] Biagiotti, Luigi, and Claudio Melchiorri. Trajectory planning for
        automatic machines and robots. Springer Science & Business Media, 2008.

### distance
```python
BezierCurve.distance(p1, p2)
```
Compute the distance between two 3D points.

> *Input arguments*

* `p1` (*type:* list of `float` or `numpy.array`): Point 1
* `p2` (*type:* list of `float` or `numpy.array`): Point 2

> *Returns*

Distance between points as a `float`

### generate_cubic_curve
```python
BezierCurve.generate_cubic_curve(pnts)
```
Generate cubic Bezier curve segments from a list of points.

> *Input arguments*

* `pnts` (*type:* list of `float` or of `numpy.array`): List of points

> *Returns*

List of `BezierCurve` segments

### generate_quintic_curve
```python
BezierCurve.generate_quintic_curve(pnts)
```
Generate quintic Bezier curve segments from a list of points.

> *Input arguments*

* `pnts` (*type:* list of `float` or of `numpy.array`): List of points

> *Returns*

List of `BezierCurve` segments

### control_pnts
```python
BezierCurve.control_pnts(self)
```
Return the list of control points of the Bezier curve.

> *Returns*

List of 3D points as `list`

### interpolate
```python
BezierCurve.interpolate(self, u)
```
Interpolate the Bezier curve using the input parametric variable `u`.

> *Input arguments*

* `u` (*type:* `float`): Curve parametric input in the interval `[0, 1]`

> *Returns*

3D point from the Bezier curve as `numpy.array`

### get_derivative
```python
BezierCurve.get_derivative(self, u, order=1)
```
Compute the derivative of the Bezier curve using the input parametric
variable `u`.

> *Input arguments*

* `u` (*type:* `float`): Curve parametric input in the interval `[0, 1]`
* `order` (*type:* `int`, *default:* `1`): Order of the derivative

> *Returns*

`numpy.array`: 3D derivative value from the Bezier curve

### get_length
```python
BezierCurve.get_length(self)
```
Get length of the Bezier curve segment.

> *Returns*

`float`: Length of the curve

### compute_polynomial
```python
BezierCurve.compute_polynomial(self, n, i, u)
```
Compute the Bernstein polynomial

$$
    \mathbf{B} = {n\choose i} (1 - u)^{(n - i)} u^{i}
$$

> *Input arguments*

* `n` (*type:* `int`): Degree of the Bezier curve
* `i` (*type:* `int`): Index of the control point
* `u` (*type:* `float`): Parametric input of the curve in interval [0, 1]

> *Returns*

`float`: Bernstein polynomial result

# uuv_trajectory_generator.path_generator.cs_interpolator

## CSInterpolator
```python
CSInterpolator(self)
```
Interpolator that will generate [cubic Bezier curve](https://en.wikipedia.org/wiki/B%C3%A9zier_curve)
segments for a set of waypoints. The full algorithm can
be seen in `Biagiotti and Melchiorri, 2008`.

!!! note

    Biagiotti, Luigi, and Claudio Melchiorri. Trajectory planning for
    automatic machines and robots. Springer Science & Business Media, 2008.

### LABEL
str(object='') -> string

Return a nice string representation of the object.
If the argument is a string, the return value is the same object.
### init_interpolator
```python
CSInterpolator.init_interpolator(self)
```
Initialize the interpolator. To have the path segments generated,
`init_waypoints()` must be called beforehand by providing a set of
waypoints as `uuv_waypoints.WaypointSet` type.

> *Returns*

`True` if the path segments were successfully generated.

### set_parameters
```python
CSInterpolator.set_parameters(self, params)
```
Not implemented for this interpolator.
### get_samples
```python
CSInterpolator.get_samples(self, max_time, step=0.001)
```
Sample the full path for position and quaternion vectors.
`step` is represented in the path's parametric space.

> *Input arguments*

* `step` (*type:* `float`, *default:* `0.001`): Parameter description

> *Returns*

List of `uuv_trajectory_generator.TrajectoryPoint`.

### generate_pos
```python
CSInterpolator.generate_pos(self, s)
```
Generate a position vector for the path sampled point
interpolated on the position related to `s`, `s` being
represented in the curve's parametric space.

> *Input arguments*

* `s` (*type:* `float`): Curve's parametric input expressed in the
interval of [0, 1]

> *Returns*

3D position vector as a `numpy.array`.

### generate_pnt
```python
CSInterpolator.generate_pnt(self, s, t, *args)
```
Compute a point that belongs to the path on the
interpolated space related to `s`, `s` being represented
in the curve's parametric space.

> *Input arguments*

* `s` (*type:* `float`): Curve's parametric input expressed in the
interval of [0, 1]
* `t` (*type:* `float`): Trajectory point's timestamp

> *Returns*

`uuv_trajectory_generator.TrajectoryPoint` including position
and quaternion vectors.

### generate_quat
```python
CSInterpolator.generate_quat(self, s)
```
Compute the quaternion of the path reference for a interpolated
point related to `s`, `s` being represented in the curve's parametric
space.
The quaternion is computed assuming the heading follows the direction
of the path towards the target. Roll and pitch can also be computed
in case the `full_dof` is set to `True`.

> *Input arguments*

* `s` (*type:* `float`): Curve's parametric input expressed in the
interval of [0, 1]

> *Returns*

Rotation quaternion as a `numpy.array` as `(x, y, z, w)`

# uuv_trajectory_generator.path_generator.dubins_interpolator

## DubinsInterpolator
```python
DubinsInterpolator(self)
```
3D Dubins path interpolator implemented based on the sources
below.

!!! note

    Owen, Mark, Randal W. Beard, and Timothy W. McLain.
    "Implementing Dubins Airplane Paths on Fixed-Wing UAVs."
    Handbook of Unmanned Aerial Vehicles (2014): 1677-1701.

    Cai, Wenyu, Meiyan Zhang, and Yahong Zheng. "Task Assignment
    and Path Planning for Multiple Autonomous Underwater Vehicles
    Using 3D Dubins Curves." Sensors 17.7 (2017):1607.

    Hansen, Karl D., and Anders La Cour-Harbo. "Waypoint Planning
    with Dubins Curves Using Genetic Algorithms." 2016 European
    Control Conference (ECC) (2016).

    Lin, Yucong, and Srikanth Saripalli. "Path Planning Using
    3D Dubins Curve for Unmanned Aerial Vehicles." 2014
    International Conference on Unmanned Aircraft Systems (ICUAS)
    (2014).

### LABEL
str(object='') -> string

Return a nice string representation of the object.
If the argument is a string, the return value is the same object.
### init_interpolator
```python
DubinsInterpolator.init_interpolator(self)
```
Initialize the interpolator. To have the path segments generated,
`init_waypoints()` must be called beforehand by providing a set of
waypoints as `uuv_waypoints.WaypointSet` type.

> *Returns*

`bool`: `True` if the path segments were successfully generated.

### set_parameters
```python
DubinsInterpolator.set_parameters(self, params)
```
Set interpolator's parameters. All the options
for the `params` input can be seen below:

```python
params=dict(
    radius=0.0,
    max_pitch=0.0
    )
```

* `radius` (*type:* `float`): Turning radius
* `max_pitch` (*type:* `float`): Max. pitch angle allowed
between two waypoints. If the pitch exceeds `max_pitch`, a
helical path is computed to perform steep climbs or dives.

> *Input arguments*

* `params` (*type:* `dict`): `dict` containing interpolator's
configurable elements.

### get_samples
```python
DubinsInterpolator.get_samples(self, max_time, step=0.001)
```
Sample the full path for position and quaternion vectors.
`step` is represented in the path's parametric space.

> *Input arguments*

* `step` (*type:* `float`, *default:* `0.001`): Parameter description

> *Returns*

List of `uuv_trajectory_generator.TrajectoryPoint`.

### generate_pos
```python
DubinsInterpolator.generate_pos(self, s)
```
Generate a position vector for the path sampled point
interpolated on the position related to `s`, `s` being
represented in the curve's parametric space.

> *Input arguments*

* `s` (*type:* `float`): Curve's parametric input expressed in the
interval of [0, 1]

> *Returns*

3D position vector as a `numpy.array`.

### generate_pnt
```python
DubinsInterpolator.generate_pnt(self, s, t, *args)
```
Compute a point that belongs to the path on the
interpolated space related to `s`, `s` being represented
in the curve's parametric space.

> *Input arguments*

* `s` (*type:* `float`): Curve's parametric input expressed in the
interval of [0, 1]
* `t` (*type:* `float`): Trajectory point's timestamp

> *Returns*

`uuv_trajectory_generator.TrajectoryPoint` including position
and quaternion vectors.

### generate_quat
```python
DubinsInterpolator.generate_quat(self, s)
```
Compute the quaternion of the path reference for a interpolated
point related to `s`, `s` being represented in the curve's parametric
space.
The quaternion is computed assuming the heading follows the direction
of the path towards the target. Roll and pitch can also be computed
in case the `full_dof` is set to `True`.

> *Input arguments*

* `s` (*type:* `float`): Curve's parametric input expressed in the
interval of [0, 1]

> *Returns*

Rotation quaternion as a `numpy.array` as `(x, y, z, w)`

# uuv_trajectory_generator.path_generator.helical_segment

## HelicalSegment
```python
HelicalSegment(self, center, radius, n_turns, delta_z, angle_offset, is_clockwise=True)
```
Generator of helical segments.

> *Input arguments*

* `center` (*type:* `list`): Center of the helix in meters
* `radius` (*type:* `float`): Radius of the helix in meters
* `n_turns` (*type:* `int`): Number of turns
* `delta_z` (*type:* `float`): Length of the step in the Z direction between each turn of the helix in meters
* `angle_offset` (*type:* `float`): Angle offset to start the helix
* `is_clockwise` (*type:* `bool`, *default:* `True`): If `True`, the helix is generated clockwise.

> *Example*

```python
radius = 3
center = [2, 2, 2]
n_turns = 2
delta_z = 1
angle_offset = 0.0
is_clockwise = True

helix = HelicalSegment(center, radius, n_turns, delta_z, angle_offset, is_clockwise)

u = numpy.linspace(0, 1, 100)
pnts = numpy.array([helix.interpolate(i) for i in u])
```

### get_length
```python
HelicalSegment.get_length(self)
```
Return the length of the helix in meters
### get_pitch
```python
HelicalSegment.get_pitch(self)
```
Return the pitch angle of the helical path in radians
### interpolate
```python
HelicalSegment.interpolate(self, u)
```
Compute the 3D point on the helical path

> *Input arguments*

* `param` (*type:* `data_type`, *default:* `data`): Parameter description

> *Returns*

Description of return values

# uuv_trajectory_generator.path_generator.line_segment

## LineSegment
```python
LineSegment(self, p_init, p_target)
```
Line segment class.

> *Input arguments*

* `p_init` (*type:* `list` or `numpy.array`): Line's starting point
* `p_target` (*type:* `list` or `numpy.array`): Line's ending point

### interpolate
```python
LineSegment.interpolate(self, u)
```
Interpolate the Bezier curve using the input parametric variable `u`.

> *Input arguments*

* `u` (*type:* `float`): Curve parametric input in the interval `[0, 1]`

> *Returns*

`numpy.array`: 3D point from the Bezier curve

### get_derivative
```python
LineSegment.get_derivative(self, *args)
```
Compute the derivative of the line segment.

> *Returns*

`numpy.array`: 3D derivative value from the Bezier curve

### get_length
```python
LineSegment.get_length(self)
```
Get length of the Bezier curve segment.

> *Returns*

`float`: Length of the curve

### get_tangent
```python
LineSegment.get_tangent(self)
```
Compute tangent vector.

> *Returns*

`numpy.array`: Tangent vector

# uuv_trajectory_generator.path_generator.linear_interpolator

## LinearInterpolator
```python
LinearInterpolator(self)
```
Simple interpolator that generates a parametric
line connecting the input waypoints.

> *Example*

```python
from uuv_waypoints import Waypoint, WaypointSet
from uuv_trajectory_generator import LinearInterpolator

# Some sample 3D points
q_x = [0, 1, 2, 4, 5, 6]
q_y = [0, 2, 3, 3, 2, 0]
q_z = [0, 1, 0, 0, 2, 2]

q = np.vstack((q_x, q_y, q_z)).T

# Create waypoint set
waypoints = WaypointSet()
for i in range(q.shape[0]):
    waypoints.add_waypoint(Waypoint(q[i, 0], q[i, 1], q[i, 2], max_forward_speed=0.5))

interpolator = LinearInterpolator()
interpolator.init_waypoints(waypoints)
interpolator.init_interpolator()

# Use get_samples to retrieve points interpolated
# using a fixed step, step being represented in the line's
# parametric space
pnts = interpolator.get_samples(max_time=None, step=0.01)

# Or use the following to retrieve a position vector on the
# set of lines
pos = interpolator.generate_pos(s=0.2)
```

### LABEL
str(object='') -> string

Return a nice string representation of the object.
If the argument is a string, the return value is the same object.
### init_interpolator
```python
LinearInterpolator.init_interpolator(self)
```
Initialize the interpolator. To have the path segments generated,
`init_waypoints()` must be called beforehand by providing a set of
waypoints as `uuv_waypoints.WaypointSet` type.

> *Returns*

`True` if the path segments were successfully generated.

### set_parameters
```python
LinearInterpolator.set_parameters(self, params)
```
Not implemented for this interpolator.
### get_samples
```python
LinearInterpolator.get_samples(self, max_time, step=0.001)
```
Sample the full path for position and quaternion vectors.
`step` is represented in the path's parametric space.

> *Input arguments*

* `step` (*type:* `float`, *default:* `0.001`): Parameter description

> *Returns*

List of `uuv_trajectory_generator.TrajectoryPoint`.

### generate_pos
```python
LinearInterpolator.generate_pos(self, s)
```
Generate a position vector for the path sampled point
interpolated on the position related to `s`, `s` being
represented in the curve's parametric space.

> *Input arguments*

* `s` (*type:* `float`): Curve's parametric input expressed in the
interval of [0, 1]

> *Returns*

3D position vector as a `numpy.array`.

### generate_pnt
```python
LinearInterpolator.generate_pnt(self, s, t, *args)
```
Compute a point that belongs to the path on the
interpolated space related to `s`, `s` being represented
in the curve's parametric space.

> *Input arguments*

* `s` (*type:* `float`): Curve's parametric input expressed in the
interval of [0, 1]
* `t` (*type:* `float`): Trajectory point's timestamp

> *Returns*

`uuv_trajectory_generator.TrajectoryPoint` including position
and quaternion vectors.

### generate_quat
```python
LinearInterpolator.generate_quat(self, s)
```
Compute the quaternion of the path reference for a interpolated
point related to `s`, `s` being represented in the curve's parametric
space.
The quaternion is computed assuming the heading follows the direction
of the path towards the target. Roll and pitch can also be computed
in case the `full_dof` is set to `True`.

> *Input arguments*

* `s` (*type:* `float`): Curve's parametric input expressed in the
interval of [0, 1]

> *Returns*

Rotation quaternion as a `numpy.array` as `(x, y, z, w)`

# uuv_trajectory_generator.path_generator.lipb_interpolator

## LIPBInterpolator
```python
LIPBInterpolator(self)
```

Linear interpolator with polynomial blends.

!!! note

    Biagiotti, Luigi, and Claudio Melchiorri. Trajectory planning for
    automatic machines and robots. Springer Science & Business Media, 2008.

### LABEL
str(object='') -> string

Return a nice string representation of the object.
If the argument is a string, the return value is the same object.
### init_interpolator
```python
LIPBInterpolator.init_interpolator(self)
```
Initialize the interpolator. To have the path segments generated,
`init_waypoints()` must be called beforehand by providing a set of
waypoints as `uuv_waypoints.WaypointSet` type.

> *Returns*

`True` if the path segments were successfully generated.

### set_parameters
```python
LIPBInterpolator.set_parameters(self, params)
```
Set interpolator's parameters. All the options
for the `params` input can be seen below:

```python
params=dict(
    radius=0.0
    )
```

* `radius` (*type:* `float`): Radius of the corners modeled
as fifth-order Bezier curves.

> *Input arguments*

* `params` (*type:* `dict`): `dict` containing interpolator's
configurable elements.

### get_samples
```python
LIPBInterpolator.get_samples(self, max_time, step=0.001)
```
Sample the full path for position and quaternion vectors.
`step` is represented in the path's parametric space.

> *Input arguments*

* `step` (*type:* `float`, *default:* `0.001`): Parameter description

> *Returns*

List of `uuv_trajectory_generator.TrajectoryPoint`.

### generate_pos
```python
LIPBInterpolator.generate_pos(self, s, *args)
```
Generate a position vector for the path sampled point
interpolated on the position related to `s`, `s` being
represented in the curve's parametric space.

> *Input arguments*

* `s` (*type:* `float`): Curve's parametric input expressed in the
interval of [0, 1]

> *Returns*

3D position vector as a `numpy.array`.

### generate_pnt
```python
LIPBInterpolator.generate_pnt(self, s, t=0.0, *args)
```
Compute a point that belongs to the path on the
interpolated space related to `s`, `s` being represented
in the curve's parametric space.

> *Input arguments*

* `s` (*type:* `float`): Curve's parametric input expressed in the
interval of [0, 1]
* `t` (*type:* `float`): Trajectory point's timestamp

> *Returns*

`uuv_trajectory_generator.TrajectoryPoint` including position
and quaternion vectors.

### generate_quat
```python
LIPBInterpolator.generate_quat(self, s)
```
Compute the quaternion of the path reference for a interpolated
point related to `s`, `s` being represented in the curve's parametric
space.
The quaternion is computed assuming the heading follows the direction
of the path towards the target. Roll and pitch can also be computed
in case the `full_dof` is set to `True`.

> *Input arguments*

* `s` (*type:* `float`): Curve's parametric input expressed in the
interval of [0, 1]

> *Returns*

Rotation quaternion as a `numpy.array` as `(x, y, z, w)`

# uuv_trajectory_generator.path_generator.path_generator

