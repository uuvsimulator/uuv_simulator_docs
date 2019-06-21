# uuv_waypoints
Waypoint description for construction of 3D paths and trajectories.
# uuv_waypoints.waypoint

## Waypoint
```python
Waypoint(self, x=0, y=0, z=0, max_forward_speed=0, heading_offset=0, use_fixed_heading=False, inertial_frame_id='world', radius_acceptance=0.0)
```
Waypoint data structure

> *Attributes*

* `FINAL_WAYPOINT_COLOR` (*type:* list of `float`, *value:* `[1.0, 0.5737, 0.0]`): RGB color for marker of the final waypoint in RViz
* `OK_WAYPOINT` (*type:* list of `float`, *value:* `[0.1216, 0.4157, 0.8863]`): RGB color for marker of a successful waypoint in RViz
* `FAILED_WAYPOINT` (*type:* list of `float`, *value:* `[1.0, 0.0, 0.0]`): RGB color for marker of a failed waypoint in RViz

> *Input arguments*

* `x` (*type:* `float`, *default:* `0`): X coordinate in meters
* `y` (*type:* `float`, *default:* `0`): Y coordinate in meters
* `z` (*type:* `float`, *default:* `0`): Z coordinate in meters
* `max_forward_speed` (*type:* `float`, *default:* `0`): Reference maximum forward speed in m/s
* `heading_offset` (*type:* `float`, *default:* `0`): Heading offset to be added to the computed heading reference in radians
* `use_fixed_heading` (*type:* `float`, *default:* `False`): Use the heading offset as a fixed heading reference in radians
* `inertial_frame_id` (*type:* `str`, *default:* `'world'`): Name of the inertial reference frame, options are `world` or `world_ned`
* `radius_acceptance` (*type:* `float`, *default:* `0`): Radius around the waypoint where the vehicle can be considered to have reached the waypoint


### FAILED_WAYPOINT
list() -> new empty list
list(iterable) -> new list initialized from iterable's items
### FINAL_WAYPOINT_COLOR
list() -> new empty list
list(iterable) -> new list initialized from iterable's items
### heading
`float`: Heading reference stored for this waypoint in radians
### heading_offset
`float`: Heading offset in radians
### inertial_frame_id
`str`: Name of the inertial reference frame
### max_forward_speed
`float`: Maximum reference forward speed
### OK_WAYPOINT
list() -> new empty list
list(iterable) -> new list initialized from iterable's items
### pos
`numpy.ndarray`: Position 3D vector
### radius_of_acceptance
`float`: Radius of acceptance in meters
### using_heading_offset
`float`: Flag to use the heading offset
### violates_constraint
`bool`: Flag on constraint violation for this waypoint
### x
`float`: X coordinate of the waypoint in meters
### y
`float`: Y coordinate of the waypoint in meters
### z
`float`: Z coordinate of the waypoint in meters
### get_color
```python
Waypoint.get_color(self)
```
Return the waypoint marker's color

> *Returns*

RGB color as a `list`

### get_final_color
```python
Waypoint.get_final_color(self)
```
Return the RGB color for the final waypoint

> *Returns*

RGB color as a `list`

### from_message
```python
Waypoint.from_message(self, msg)
```
Set waypoint parameters from `uuv_control_msgs/Waypoint`
message

> *Input arguments*

* `msg` (*type:* `uuv_control_msgs/Waypoint`): Waypoint message

### to_message
```python
Waypoint.to_message(self)
```
Convert waypoint to `uuv_control_msgs/Waypoint` message

> *Returns*

`uuv_control_msgs/Waypoint` message

### dist
```python
Waypoint.dist(self, pos)
```
Compute distance of waypoint to a point

> *Input arguments*

* `pos` (*type:* list of `float`): 3D position vector

> *Returns*

Distance to point in meters

### calculate_heading
```python
Waypoint.calculate_heading(self, target)
```
Compute heading to target waypoint

> *Input arguments*

* `target` (*type:* `uuv_waypoints/Waypoint`): Target waypoint

> *Returns*

Heading angle in radians

# uuv_waypoints.waypoint_set

## WaypointSet
```python
WaypointSet(self, scale=0.1, inertial_frame_id='world', max_surge_speed=None)
```
Set of waypoints.

> *Attributes*

* `FINAL_WAYPOINT_COLOR` (*type:* list of `float`, *value:* `[1.0, 0.5737, 0.0]`): RGB color for marker of the final waypoint in RViz
* `OK_WAYPOINT` (*type:* list of `float`, *value:* `[0.1216, 0.4157, 0.8863]`): RGB color for marker of a successful waypoint in RViz
* `FAILED_WAYPOINT` (*type:* list of `float`, *value:* `[1.0, 0.0, 0.0]`): RGB color for marker of a failed waypoint in RViz

> *Input arguments*

* `scale` (*type:* `float`, *default:* `0.1`): Scale of the spherical marker for waypoints
* `inertial_frame_id` (*type:* `str`, *default:* `'world'`): Name of the inertial reference frame, options are `world` and `world_ned` for `ENU` and `NED` inertial reference frames, respectively
* `max_surge_speed` (*type:* `float`, *default:* `None`): Max. surge speed in m/s associated with each waypoint


### FAILED_WAYPOINT
list() -> new empty list
list(iterable) -> new list initialized from iterable's items
### FINAL_WAYPOINT_COLOR
list() -> new empty list
list(iterable) -> new list initialized from iterable's items
### inertial_frame_id
`str`: Name of inertial reference frame
### is_empty
`bool`: True if the list of waypoints is empty
### num_waypoints
`int`: Number of waypoints
### OK_WAYPOINT
list() -> new empty list
list(iterable) -> new list initialized from iterable's items
### x
`list`: List of the X-coordinates of all waypoints
### y
`list`: List of the Y-coordinates of all waypoints
### z
`list`: List of the Z-coordinates of all waypoints
### clear_waypoints
```python
WaypointSet.clear_waypoints(self)
```
Clear the list of waypoints
### set_constraint_status
```python
WaypointSet.set_constraint_status(self, index, flag)
```
Set the flag violates_constraint to a waypoint

> *Input arguments*

* `index` (*type:* `int`): Index of the waypoints
* `flag` (*type:* `bool`): True, if waypoint violates a constraint

> *Returns*

`True` if successful, and `False` if the waypoint `index` is outsite of the list's range.

### get_waypoint
```python
WaypointSet.get_waypoint(self, index)
```
Return a waypoint

> *Input arguments*

* `index` (*type:* `int`): Index of the waypoint

> *Returns*

Return a waypoint as `uuv_waypoints.Waypoint` or `None` if `index` is outside of range.

### add_waypoint
```python
WaypointSet.add_waypoint(self, waypoint, add_to_beginning=False)
```
Add a waypoint to the set

> *Input arguments*

* `waypoint` (*type:* `uuv_waypoints.Waypoint`): Waypoint object
* `add_to_beginning` (*type:* `bool`, *default:* `False`): If `True`, add the waypoint to the beginning of the list.

> *Returns*

`True` if waypoint was added to the set. `False` if a repeated waypoint is already found in the set.

### add_waypoint_from_msg
```python
WaypointSet.add_waypoint_from_msg(self, msg)
```
Add waypoint from ROS `uuv_control_msgs/Waypoint` message

> *Input arguments*

* `msg` (*type:* `uuv_control_msgs/Waypoint`): Waypoint message

> *Returns*

`True`, if waypoint could be added to set, `False`, otherwise.

### get_start_waypoint
```python
WaypointSet.get_start_waypoint(self)
```
Return the starting waypoint

> *Returns*

A `uuv_waypoints.Waypoint` object or None, if the list of waypoints is empty.

### get_last_waypoint
```python
WaypointSet.get_last_waypoint(self)
```
Return the final waypoint

> *Returns*

A `uuv_waypoints.Waypoint` object or None, if the list of waypoints is empty.

### remove_waypoint
```python
WaypointSet.remove_waypoint(self, waypoint)
```
Remove waypoint from set.

> *Input arguments*

* `waypoint` (*type:* `uuv_waypoints.Waypoint`): Waypoint object

### read_from_file
```python
WaypointSet.read_from_file(self, filename)
```
Read waypoint set from a YAML file.

> *Input arguments*

* `filename` (*type:* `str`): Filename of the waypoint set

> *Returns*

`True` if waypoint set file could be parsed, `False`, otherwise.

### export_to_file
```python
WaypointSet.export_to_file(self, path, filename)
```
Export waypoint set to YAML file.

> *Input arguments*

* `path` (*type:* `str`): Path to the folder containing the file
* `filename` (*type:* `str`): Name of the YAML file.

> *Returns*

`True` is waypoints could be exported to file. `False`, otherwise.

### to_message
```python
WaypointSet.to_message(self)
```
Convert waypoints set to message `uuv_control_msgs/WaypointSet`

> *Returns*

`uuv_control_msgs/WaypointSet` message object

### from_message
```python
WaypointSet.from_message(self, msg)
```
Convert `uuv_control_msgs/WaypointSet` message into `uuv_waypoints.WaypointSet`

> *Input arguments*

* `msg` (*type:* `uuv_control_msgs/WaypointSet` object): Waypoint set message

### dist_to_waypoint
```python
WaypointSet.dist_to_waypoint(self, pos, index=0)
```
Compute the distance of a waypoint in the set to point

> *Input arguments*

* `pos` (*type:* list of `float`): 3D point as a list of coordinates
* `index` (*type:* `int`, *default:* `0`): Waypoint index in set

> *Returns*

Distance between `pos` and the waypoint in `index`. `None` if waypoint set is empty.

### set_radius_of_acceptance
```python
WaypointSet.set_radius_of_acceptance(self, index, radius)
```
Set the radius of acceptance around each waypoint
inside which a vehicle is considered to have reached
a waypoint.

> *Input arguments*

* `index` (*type:* `int`): Index of the waypoint
* `radius` (*type:* `float`): Radius of the sphere representing the volume of acceptance

### get_radius_of_acceptance
```python
WaypointSet.get_radius_of_acceptance(self, index)
```
Return the radius of acceptance for a waypoint

> *Input arguments*

* `index` (*type:* `int`): Index of the waypoint

> *Returns*

Radius of acceptance for the waypoint in position
given by `index` as a `float`. `None` if waypoint
set is empty.

### to_path_marker
```python
WaypointSet.to_path_marker(self, clear=False)
```
Return a `nav_msgs/Path` message with all waypoints in the set

> *Input arguments*

* `clear` (*type:* `bool`, *default:* `False`): Return an empty `nav_msgs/Path` message.

> *Returns*

`nav_msgs/Path` message

### to_marker_list
```python
WaypointSet.to_marker_list(self, clear=False)
```
Return waypoint set as a markers list message of type `visualization_msgs/MarkerArray`

> *Input arguments*

* `clear` (*type:* `bool`, *default:* `False`): Return an empty marker array message

> *Returns*

`visualization_msgs/MarkerArray` message

### generate_circle
```python
WaypointSet.generate_circle(self, radius, center, num_points, max_forward_speed, theta_offset=0.0, heading_offset=0.0, append=False)
```
Generate a set of waypoints describing a circle

> *Input arguments*

* `radius` (*type:* `float`): Radius of the circle in meters
* `num_points` (*type:* `int`): Number of waypoints to be generated
* `max_forward_speed` (*type:* `float`): Max. forward speed set to each waypoint in m/s
* `theta_offset` (*type:* `float`, *default:* `0`): Angle offset to start generating the waypoints in radians
* `heading_offset` (*type:* `float`, *default:* `0`): Heading offset set to the reference heading of the vehicle in radians
* `append` (*type:* `bool`, *default:* `False`): If `True`, append the generated waypoints to the existent waypoints in the set

> *Returns*

`True` if the circle was successfully generated, `False`, otherwise

### generate_helix
```python
WaypointSet.generate_helix(self, radius, center, num_points, max_forward_speed, delta_z, num_turns, theta_offset=0.0, heading_offset=0.0, append=False)
```
Generate a set of waypoints describing a helix

> *Input arguments*

* `radius` (*type:* `float`): Radius of the circle in meters
* `num_points` (*type:* `int`): Number of waypoints to be generated
* `max_forward_speed` (*type:* `float`): Max. forward speed set to each waypoint in m/s
* `delta_z` (*type:* `float`): Step in the Z direction for each lap of the helix in meters
* `theta_offset` (*type:* `float`, *default:* `0`): Angle offset to start generating the waypoints in radians
* `heading_offset` (*type:* `float`, *default:* `0`): Heading offset set to the reference heading of the vehicle in radians
* `append` (*type:* `bool`, *default:* `False`): If `True`, append the generated waypoints to the existent waypoints in the set

> *Returns*

`True` if the circle was successfully generated, `False`, otherwise

