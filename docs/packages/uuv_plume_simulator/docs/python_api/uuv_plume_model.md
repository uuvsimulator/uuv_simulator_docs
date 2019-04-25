# uuv_plume_model

# uuv_plume_model.plume

## Plume
```python
Plume(self, source_pos, n_points, start_time)
```

Base class for plume model classes. Plume models should inherit this class
and implement the update function to maintain a standard interface with the
plume server. Each new inherited plume model must have an unique *LABEL*
tag, since it will be used by the factory method to create plume models
without the need to import all the plume model class files.

### LABEL
str(object='') -> string

Return a nice string representation of the object.
If the argument is a string, the return value is the same object.
### n_points
Return the maximum number of points to be created by the plume model.

### num_particles
Return the current number of particles.
### points
Return list of `[N x 3]` position vectors for particles created.

### source_pos
Return the position vector with the Cartesian coordinates
for the plume source

### time_of_creation
Return the time of creation vector.
### x
Return only the X coordinates for the particle positions.

### x_lim
Return the lower and upper limit for the bounding box on the X axis.

### y
Return only the Y coordinates for the particle positions.

### y_lim
Return the lower and upper limit for the bounding box on the Y axis.

### z
Return only the Z coordinates for the particle positions.

### z_lim
Return the lower and upper limit for the bounding box on the Z axis.

### create_plume_model
```python
Plume.create_plume_model(tag, *args)
```
Factory function to create the plume model using the LABEL
attribute as identifier.

> **Parameters**

* `tag` (*type:* `str`): label of the plume model to be created
* `args`: list of input arguments for the specific plume model to be created

### set_n_points
```python
Plume.set_n_points(self, n_points)
```
Set the maximum number of points to be created by the plume model.

> **Parameters**

* n_points (*type: `int`): number maximum of particles (must be greater
than zero).

### update_current_vel
```python
Plume.update_current_vel(self, vel)
```
Update the current velocity vector.

> **Parameters**

* `vel` (*type:* `list` or `numpy.array`): current velocity vector
containing three elements $(u, v, w)$.

### set_x_lim
```python
Plume.set_x_lim(self, min_value, max_value)
```
Set the X limits for the plume bounding box. The bounding box is
defined with respect to the ENU inertial frame.

> **Parameters**

* `min_value` (*type:* `float`): lower limit for the bounding box over the X axis.
* `max_value` (*type:* `float`): upper limit for the bounding box over the X axis.

> **Returns**

`True` if limits are valid.

### set_y_lim
```python
Plume.set_y_lim(self, min_value, max_value)
```
Set the Y limits for the plume bounding box. The bounding box is
defined with respect to the ENU inertial frame.

> **Parameters**

* `min_value` (*type:* `float`): lower limit for the bounding box over the Y axis.
* `max_value` (*type:* `float`): upper limit for the bounding box over the Y axis.

> **Returns**

`True` if limits are valid.

### set_z_lim
```python
Plume.set_z_lim(self, min_value, max_value)
```
Set the Z limits for the plume bounding box. The bounding box is
defined with respect to the ENU inertial frame.

> **Parameters**

* `min_value` (*type:* `float`): lower limit for the bounding box over the Z axis.
* `max_value` (*type:* `float`): upper limit for the bounding box over the Z axis.

> **Returns**

`True` if limits are valid.

### reset_plume
```python
Plume.reset_plume(self)
```
Reset point cloud and time of creating vectors.
### get_contraints_filter
```python
Plume.get_contraints_filter(self)
```
Return a binary vector of $N$ elements, $N$ being current number of
particles created. The $i$-th element is set to False if the $i$-th
particle finds itself outside of the bounding box limits.

> **Returns**

Logical vector with elements set to *True* if they fulfill the constraints.

### apply_constraints
```python
Plume.apply_constraints(self)
```
Truncate the position of the particle to the closest bounding box limit
if the particle is positioned outside of the limits.

### set_plume_particles
```python
Plume.set_plume_particles(self, t, x, y, z, time_creation)
```
Set the plume particles with the input coordinates wrt ENU frame
and time of creation vector in seconds.

> **Parameters**

* `t` (*type:* `float`): Current time stamp in seconds
* `x` (*type:* `list`): List of X coordinates for the plume particles' positions
* `y` (*type:* `list`): List of Y coordinates for the plume particles' positions
* `z` (*type:* `list`): List of Z coordinates for the plume particles' positions
* `time_creation`(*type:* `list`): List of the relative time of creation for
each particle in seconds

### get_point_cloud_as_msg
```python
Plume.get_point_cloud_as_msg(self)
```
Return a ROS point cloud sensor message with the points representing
the plume's particles and one channel containing the time of creation
for each particle.

> **Returns**

The plume particles as a `sensor_msgs/PointCloud` message or `None`
if no particles are found.

### get_markers
```python
Plume.get_markers(self)
```
Return a ROS marker array message structure with an sphere marker to
represent the plume source, the bounding box and an arrow marker to
show the direction of the current velocity if it's norm is greater
than zero.

> **Returns**

`visualizaton_msgs/MarkerArray` message with markers for the current
velocity arrow and source position or `None` if no plume particles are
found.

### update
```python
Plume.update(self, t=0.0)
```
Plume dynamics update function. It must be implemented by the child
class and will be used by the plume server to update the position of
the plume particles at each iteration.

# uuv_plume_model.passive_scalar_turbulence

## PlumePassiveScalarTurbulence
```python
PlumePassiveScalarTurbulence(self, turbulent_diffusion_coefficients, buoyancy_flux, stability_param, source_pos, n_points, start_time, max_particles_per_iter=10, max_life_time=-1)
```

Plume model implementation based on [1]. The chemical plume is described
here by discretized particles generated that are generated on the Cartesian
position given as the source of the plume. The plume is treated as a
passive scalar turbulence, meaning that it will not affect the
environmental fluid flow.

To model the dynamics of the plume particles, the Lagrangian particle
random walk approach [2] is used. The particles are generated from the
source position in batches at each iteration to ensure a steady flow and
each particle has its position $(x_k, y_k, z_k)$ at the instant
$t_k$ computed as

$$
    x_k = x_{k - 1} + (u_a + u_i) \Delta t
$$

$$
    y_k = y_{k - 1} + (v_a + v_i) \Delta t
$$

$$
    z_k = z_{k - 1} + (w_a + w_b + w_i) \Delta t
$$

where $(u_a, v_a, w_a)$ are the particle's velocities due to the
current velocity, $(u_t, v_t, w_t)$ are the particle's velocities
due to turbulent diffusion, and $w_b$ is the vertical buoyant
velocity.

!!! note "[1] `Tian and Zhang, 2010`"
    Yu Tian and Aiqun Zhang, "Simulation environment and guidance system
    for AUV tracing chemical plume in 3-dimensions," 2010 2nd International
    Asia Conference on Informatics in Control, Automation and Robotics
    (CAR 2010), Mar. 2010.

!!! note "[2] `Mestres et al., 2003`"
    M. Mestres et al., "Modelling of the Ebro River plume. Validation with
    field observations," Scientia Marina, vol. 67, no. 4, pp. 379-391,
    Dec. 2003.

### LABEL
str(object='') -> string

Return a nice string representation of the object.
If the argument is a string, the return value is the same object.
### max_particles_per_iter

Return the maximum number of particles to be generated per iteration
from the source of the plume.

### set_max_particles_per_iter
```python
PlumePassiveScalarTurbulence.set_max_particles_per_iter(self, n_particles)
```

Set the maximum number of particles to be generated per iteration from
the source of the plume.

> **Parameters**

* `n_particles` (*type:* `int`): number of particles

> **Returns**

`True` if the new maximum number of particles could be set.
`False` if the input is equal or smaller than zero.

### create_particles
```python
PlumePassiveScalarTurbulence.create_particles(self, t)
```

Create random number of particles for one iteration up to the given
maximum limit and remove all particles that have left the plume's
bounding box limits.

> **Parameters**

* `t` (*type:* `float`): time stamp in seconds

### set_plume_particles
```python
PlumePassiveScalarTurbulence.set_plume_particles(self, t, x, y, z, time_creation)
```

Load the plume particles' position vectors and time of creation.

> **Parameters**

* `t` (*type:* `float`): Current time stamp in seconds
* `x` (*type:* `list`): List of X coordinates
* `y` (*type:* `list`): List of Y coordinates
* `z` (*type:* `list`): List of Z coordinates
* `time_creation` (*type:* `list`): List of time stamps of creation
    of each particle

### compute_plume_rise
```python
PlumePassiveScalarTurbulence.compute_plume_rise(self, t)
```

The plume rise equation is used to compute the vertical buoyant
velocity. It is based on the experimental results presented in [1]
and can be written as

$H(u, s, t) = 2.6 ( F t^2 / u )^{1/3} (t^2 s + 4.3)^{-1/3}$

where $F$ is the buoyancy flux parameter and $s$ the
stability parameters, and both can be tuned by the user. $u$ is
the magnitude of the current velocity on the horizontal plane. The
resulting vertical buoyant velocity will be computed as follows

$w_b = H(u, s, t + \Delta t) - H(u, s, t) / \Delta t$

!!! note "[1] `Domenico, 1985`"
    Anfossi, Domenico. "Analysis of plume rise data from five TVA steam
    plants." Journal of climate and applied meteorology 24.11 (1985):
    1225-1236.

> **Parameters**

* `t` (*type:* `float`): current time stamp in seconds

> **Returns**

Plume rise velocity components vector.

### update
```python
PlumePassiveScalarTurbulence.update(self, t=0.0)
```
Update the position of all particles and create/remove particles from
the plume according to the bounding box limit constraints and the
maximum number of particles allowed.

> **Parameters**

* `t` (*type:* `float`): current time stamp in seconds

> **Returns**

`True` if update was succesful, `False` if computed time step is invalid.

# uuv_plume_model.spheroid

## PlumeSpheroid
```python
PlumeSpheroid(self, a, c, orientation, source_pos, n_points, start_time)
```
Plume model to generate a static plume with spheroid form.

### LABEL
str(object='') -> string

Return a nice string representation of the object.
If the argument is a string, the return value is the same object.
### update
```python
PlumeSpheroid.update(self, t=0.0)
```
Update the position of all particles and create/remove particles from
the plume according to the bounding box limit constraints and the
maximum number of particles allowed.

> **Parameters**

* `t` (*type: `float`): current time stamp in seconds

> **Returns**

`True` if update was succesful, `False` if computed time step is invalid.

