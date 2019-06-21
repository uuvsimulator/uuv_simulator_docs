# uuv_thrusters

# uuv_thrusters.thruster_manager

## ThrusterManager
```python
ThrusterManager(self)
```

The thruster manager generates the thruster allocation matrix using the
TF information and publishes the thruster forces assuming the the thruster
topics are named in the following pattern

<thruster_topic_prefix>/<index>/<thruster_topic_suffix>

Thruster frames should also be named as follows

<thruster_frame_base>_<index>

### MAX_THRUSTERS
int(x=0) -> int or long
int(x, base=10) -> int or long

Convert a number or string to an integer, or return 0 if no arguments
are given.  If x is floating point, the conversion truncates towards zero.
If x is outside the integer range, the function returns a long instead.

If x is not a number or if base is given, then x must be a string or
Unicode object representing an integer literal in the given base.  The
literal can be preceded by '+' or '-' and be surrounded by whitespace.
The base defaults to 10.  Valid bases are 0 and 2-36.  Base 0 means to
interpret the base from the string as an integer literal.
>>> int('0b100', base=0)
4
### update_tam
```python
ThrusterManager.update_tam(self, recalculate=False)
```
Calculate the thruster allocation matrix, if one is not given.
### command_thrusters
```python
ThrusterManager.command_thrusters(self)
```
Publish the thruster input into their specific topic.
### compute_thruster_forces
```python
ThrusterManager.compute_thruster_forces(self, gen_forces)
```
Compute desired thruster forces using the inverse configuration
matrix.

# uuv_thrusters.models

# uuv_thrusters.models.thruster

## Thruster
```python
Thruster(self, index, topic, pos, orientation, axis=array([1, 0, 0, 0]))
```
Abstract function to all the thruster models avaialble. The instance
of a thruster model must use the factory method.
### LABEL
str(object='') -> string

Return a nice string representation of the object.
If the argument is a string, the return value is the same object.
### get_command_value
```python
Thruster.get_command_value(self, thrust)
```
Convert desired thrust force to input command according to this
function. Overwrite this method to implement custom models.
### get_thrust_value
```python
Thruster.get_thrust_value(self, command)
```
Computes the thrust force for the given command.
### get_curve
```python
Thruster.get_curve(self, min_value, max_value, n_points)
```
Sample the conversion curve and return the values.
# uuv_thrusters.models.thruster_custom

## ThrusterCustom
```python
ThrusterCustom(self, *args, **kwargs)
```
Class describing a custom conversion curve between the command input,
usually the angular velocity, and the correspondent output thrust force.
Here the inverse of the conversion function can be computed so that the
command for the desired thrust force is retrieved.
The input vector corresponds to sampled values for the command input, and
the output vector corresponds to the sampled values for the correspondent
thrust forces.
This information is usually available in the datasheet of the thruster's
manufacturer.

### LABEL
str(object='') -> string

Return a nice string representation of the object.
If the argument is a string, the return value is the same object.
### get_thrust_value
```python
ThrusterCustom.get_thrust_value(self, command)
```
Computes the thrust force for the given command.
# uuv_thrusters.models.thruster_proportional

## ThrusterProportional
```python
ThrusterProportional(self, *args, **kwargs)
```
This model corresponds to the linear relation between a function
abs(command)*command of the command input (usually the command angular
velocity) to the thrust force. A constant gain has to be provided.

### LABEL
str(object='') -> string

Return a nice string representation of the object.
If the argument is a string, the return value is the same object.
### get_thrust_value
```python
ThrusterProportional.get_thrust_value(self, command)
```
Computes the thrust force for the given command.
