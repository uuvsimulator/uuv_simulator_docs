![Version](https://img.shields.io/badge/version-0.3.3-brightgreen.svg)

> Link to the `uuv_plume_simulator` repository [here](https://github.com/uuvsimulator/uuv_plume_simulator)

# Description

Plume simulator package

# Launch files

## [`start_demo_turbulent_plume.launch`](https://github.com/uuvsimulator/uuv_plume_simulator/tree/master/uuv_plume_simulator/launch/start_demo_turbulent_plume.launch)

> **Arguments**

* **use_gazebo** (*default:* `false`)

## [`start_plume_example.launch`](https://github.com/uuvsimulator/uuv_plume_simulator/tree/master/uuv_plume_simulator/launch/start_plume_example.launch)

> **Arguments**

* **use_gazebo** (*default:* `false`)

## [`start_current_velocity_server.launch`](https://github.com/uuvsimulator/uuv_plume_simulator/tree/master/uuv_plume_simulator/launch/start_current_velocity_server.launch)

> **Arguments**

* **current_velocity_topic** (*default:* `current_velocity`)
* **update_rate** (*default:* `10`)

## [`start_turbulent_plume.launch`](https://github.com/uuvsimulator/uuv_plume_simulator/tree/master/uuv_plume_simulator/launch/start_turbulent_plume.launch)

> **Arguments**

* **diffusion_coef_x** (*default:* `0.4`)
* **diffusion_coef_y** (*default:* `0.4`)
* **diffusion_coef_z** (*default:* `0.1`)
* **source_x** (*default:* `-180.0`)
* **source_y** (*default:* `0.0`)
* **source_z** (*default:* `-30.0`)
* **buoyancy_flux** (*default:* `0.1`)
* **stability_param** (*default:* `0.001`)
* **n_points** (*default:* `150000`)
* **x_min** (*default:* `-200`)
* **x_max** (*default:* `200.0`)
* **y_min** (*default:* `-75`)
* **y_max** (*default:* `75`)
* **z_min** (*default:* `-60`)
* **z_max** (*default:* `0.0`)
* **max_particules_per_iter** (*default:* `80`)
* **max_life_time** (*default:* `-1`)

## [`start_plume_server.launch`](https://github.com/uuvsimulator/uuv_plume_simulator/tree/master/uuv_plume_simulator/launch/start_plume_server.launch)

> **Arguments**

* **current_velocity_topic** (*default:* `/hydrodynamics/current_velocity`)
* **update_rate** (*default:* `5.0`)

# Scripts

## `set_demo_turbulent_plume`

> **Script type:** `shell`

## `plume_server`

> **Script type:** `python`

**Description**

Passive turbulent plume server node.

!!! note "See also"

    [Description of the turbulent plume model](../user_guide/introduction.md)

**Input ROS parameters**

* `update_rate` (*default:* `5`, *type:* `int` or `float`):  Update rate for the plume particle point cloud update

**Launch file snippet**

```xml
<group ns="plume">
    <node name="plume_simulation_server"
          pkg="uuv_plume_simulator"
          type="plume_server"
          output="screen">
      <remap from="current_vel" to="/hydrodynamics/current_velocity"/>
      <rosparam subst_value="true">
            update_rate: 5
      </rosparam>
    </node>
</group>
```

**ROS services**

> **`create_spheroid_plume`**

*Service description file*

[`uuv_plume_msgs/CreateSpheroidPlume`](uuv_plume_msgs.md#createspheroidplume)

*Service call*

```bash
rosservice call /<plume_namespace>/create_spheroid_plume "source: {x: 0.0, y: 0.0, z: 0.0}
orientation: {x: 0.0, y: 0.0, z: 0.0, w: 0.0}
n_points: 0
a: 0.0
c: 0.0
x_min: 0.0
x_max: 0.0
y_min: 0.0
y_max: 0.0
z_min: 0.0
z_max: 0.0"
```

Create a static plume in the shape of a spheroid.

* `source`: Plume source position wrt ENU frame
* `orientation`: Spheroid orientation in quaternion
* `n_points`: Number of plume particles
* `a` and `c`: Spheroid's semi-axis length
* `x_min`, `x_max`, `y_min`, `y_max`, `z_min`, `z_max`: Limits of the bounding box where the plume particles are allowed to exist

> **`create_passive_scalar_turbulent_plume`**

*Service description file*

[`uuv_plume_msgs/CreatePassiveScalarTurbulentPlume`](uuv_plume_msgs.md#createpassivescalarturbulentplume)

*Service call*

```bash
rosservice call /<plume_namespace>/create_passive_scalar_turbulent_plume "turbulent_diffusion_coefficients: {x: 0.0, y: 0.0, z: 0.0}
source: {x: 0.0, y: 0.0, z: 0.0}
buoyancy_flux: 0.0
stability_param: 0.0
n_points: 0
max_particles_per_iter: 0
x_min: 0.0
x_max: 0.0
y_min: 0.0
y_max: 0.0
z_min: 0.0
z_max: 0.0
max_life_time: 0.0" 
```

Create a passive turbulent plume.

* `turbulent_diffusion_coefficients`: Coefficients ruling the diffusion of the particles for each degree of freedom of the particle.
* `source`: Position of the plume source wrt ENU frame
* `buoyancy_flux` and `stability_param`: Parameters controlling the plume rise
* `n_points`: Maximum number of plume particles to be generated
* `max_particles_per_iter`: Maximum number of particles generated at the source position at each iteration
* `x_min`, `x_max`, `y_min`, `y_max`, `z_min`, `z_max`: Limits of the bounding box where the plume particles are allowed to exist
* `max_life_time`: Maximum life time of each particle in seconds

> **`set_plume_limits`**

*Service description file*

[`uuv_plume_msgs/SetPlumeLimits`](uuv_plume_msgs.md#setplumelimits)

*Service call*

```bash
rosservice call /<plume_namespace>/set_plume_limits "{x_min: 0.0, x_max: 0.0, y_min: 0.0, y_max: 0.0, z_min: 0.0, z_max: 0.0}"
```

Sets the bounds of the box where the plume particles are allowed to exist.

* `x_min`, `x_max`, `y_min`, `y_max`, `z_min`, `z_max`: Limits of the bounding box where the plume particles are allowed to exist

> **`set_plume_config`**

*Service description file*

[`uuv_plume_msgs/SetPlumeConfiguration`](uuv_plume_msgs.md#setplumeconfiguration)

*Service call*

```bash
rosservice call /<plume_namespace>/set_plume_config "n_points: 0
max_particles_per_iter: 0"
```

Configure the plume's particle generation parameters.

* `n_points`: Maximum number of plume particles to be generated
* `max_particles_per_iter`: Maximum number of particles generated at the source position at each iteration

> **`get_plume_config`**

*Service description file*

[`uuv_plume_msgs/GetPlumeConfiguration`](uuv_plume_msgs.md#getplumeconfiguration)

*Service call*

```bash
rosservice call /<plume_namespace>/get_plume_config
```

Return the plume's generation configuration parameters, including maximum number of particles,
maximum number of particles per iteration, source position and limits of the bounding box.

> **`delete_plume`**

*Service description file*

[`uuv_plume_msgs/DeletePlume`](uuv_plume_msgs.md#deleteplume)

*Service call*

```bash
rosservice call /<plume_namespace>/delete_plume
```

Delete the source and the particles.

> **`set_plume_source_position`**

*Service description file*

[`uuv_plume_msgs/SetPlumeSourcePosition`](uuv_plume_msgs.md#setplumesourceposition)

*Service call*

```bash
rosservice call /<plume_namespace>/set_plume_source_position "source:
  x: 0.0
  y: 0.0
  z: 0.0"
```

Set plume source position wrt ENU frame

* `source`: New plume source position wrt ENU frame

> **`get_plume_source_position`**

*Service description file*

[`uuv_plume_msgs/GetPlumeSourcePosition`](uuv_plume_msgs.md#getplumesourceposition)

*Service call*

```bash
rosservice call /<plume_namespace>/get_plume_source_position
```

Return the plume source position coordinates.

> **`get_num_particles`**

*Service description file*

[`uuv_plume_msgs/GetNumParticles`](uuv_plume_msgs.md#getnumparticles)

*Service call*

```bash
rosservice call /<plume_namespace>/get_num_particles
```

Return current number of plume particles.

> **`store_plume_state`**

*Service description file*

[`uuv_plume_msgs/StorePlumeState`](uuv_plume_msgs.md#storeplumestate)

*Service call*

```bash
rosservice call /<plume_namespace>/store_plume_state "output_dir: ''
filename: ''"
```

Store the position and time of creation for of each particle in a file as an YAML file.

* `output_dir`: Path to output directory
* `filename`: Output YAML file

> **`load_plume_particles`**

*Service description file*

[`uuv_plume_msgs/LoadPlumeParticles`](uuv_plume_msgs.md#loadplumeparticles)

*Service call*

```bash
rosservice call /<plume_namespace>/load_plume_particles "plume_file: ''" 
```

Load an YAML file with the plume particles' list positions and time of creation.

* `plume_file`: Plume YAML file



## `current_velocity_server`

> **Script type:** `python`

**Description**

Current velocity server node.
In case no Gazebo simulation is providing the current velocity 
topic to steer the plume, this node generates a 2D current
velocity topic. Both the current's velocity magnitude and horizontal 
angle are modeled using a Gaussian-Markov process of first order, as 
shown in [Fossen's lecture notes](http://www.fossen.biz/wiley/Ch8.pdf).
The velocity magnitude is described by

$$
    \dot{v_c}(t) + \mu_c v_c(t) = w_c
$$

and the horizontal angle $\phi$ is modeled similarly as

$$
    \dot{\phi}(t) + \mu_a \phi(t) = w_a
$$

where $\mu$ is the inverse of the time constant of the process and
$w$ is a random variable described by a normal distribution.

The final current velocity vector is then written as

$$
    v(t) = ( v_c \cos \phi, v_c \sin \phi, 0 )
$$

and published as a `geometry_msgs/TwistStamped` message.

**Input ROS parameters**

* `current_velocity_topic` (*default:* `current_velocity`, *type:* `string`): Name of the output current velocity topic
* `update_rate` (*default:* `10`, *type:* `int` or `float`): Update rate of the output current velocity topic

**Launch file snippet**

```xml
<node name="current_velocity_server"
    pkg="uuv_plume_simulator"
    type="current_velocity_server"
    output="screen">
    <rosparam subst_value="true">
        current_velocity_topic: /current_velocity
        update_rate: 10
    </rosparam>
</node>
```

**Running from the launch file**

```bash
roslaunch uuv_plume_simulator start_current_velocity_server.launch current_velocity_topic:=current_velocity update_rate:=10
```

!!! warning
    Do **NOT** run the current velocity server with a Gazebo 
    simulation that generates the same topic, it can cause unexpected 
    behaviours to the plume's steering.

**ROS services**

> **`get_current_velocity_model`**

*Service description file*

[`uuv_plume_msgs/GetCurrentModel`](uuv_plume_msgs.md#getcurrentmodel)

*Service call*

```bash
rosservice call /<namespace>/get_current_velocity_model
```

Return the parameters for the Gauss-Markov process describing the current velocity magnitude $v_c$.

> **`get_angle_model`**

*Service description file*

[`uuv_plume_msgs/GetCurrentModel`](uuv_plume_msgs.md#getcurrentmodel)

*Service call*

```bash
rosservice call /<namespace>/get_angle_model 
```

Return the parameters for the Gauss-Markov process describing the current's horizontal angle $\phi$.

> **`set_current_velocity_model`**

*Service description file*

[`uuv_plume_msgs/SetCurrentModel`](uuv_plume_msgs.md#setcurrentmodel)

*Service call*

```bash
rosservice call /<namespace>/set_current_velocity_model "{mean: 0.0, min: 0.0, max: 0.0, noise: 0.0, mu: 0.0}" 
```

Set the parameters for the Gauss-Markov process describing the current velocity magnitude $v_c$.

* `mean`: Mean value in m/s
* `min` and `max`: Bounds of the output velocity magnitude in m/s
* `noise`: Amplitude of the random noise value in m/s
* `mu`: Inverse of the process' time constant

> **`set_angle_model`**

*Service description file*

[`uuv_plume_msgs/SetCurrentModel`](uuv_plume_msgs.md#setcurrentmodel)

*Service call*

```bash
rosservice call /<namespace>/set_angle_model "{mean: 0.0, min: 0.0, max: 0.0, noise: 0.0, mu: 0.0}" 
```

Set the parameters for the Gauss-Markov process describing the current's horizontal angle $\phi$.

* `mean`: Mean value in radians
* `min` and `max`: Bounds of the output angle in radians
* `noise`: Amplitude of the random noise value in radians
* `mu`: Inverse of the process' time constant

> **`set_current_velocity`**

*Service description file*

[`uuv_plume_msgs/SetCurrentVelocity`](uuv_plume_msgs.md#setcurrentvelocity)

*Service call*

```bash
rosservice call /<namespace>/set_current_velocity "velocity: 0.0
horizontal_angle: 0.0" 
```

Set a default model for current velocity magnitude $v_c$ and horizontal angle $\phi$.

* `velocity`: Mean current velocity magnitude in m/s
* `horizontal_angle: Mean horizonal angle in degrees



## `set_demo_current_vel_gazebo`

> **Script type:** `shell`

## `set_demo_spheroid_plume`

> **Script type:** `shell`

## `load_plume_particles`

> **Script type:** `python`

**Description**

Node to call the ROS service from the plume server to load
the plume particles from an YAML file.

**Input ROS parameters**

* `filename` (*type:* `string`): Input YAML file where the plume particles' coordinates and time of creation are stored

**ROS launch snippet**

```xml
<node name="load_plume_particles"
      pkg="uuv_plume_simulator"
      type="load_plume_particles"
      output="screen">
    <rosparam>
        filename: /<path>/file.yaml
    </rosparam>
</node>
```



## `set_demo_current_vel`

> **Script type:** `shell`

## `set_turbulent_plume`

> **Script type:** `python`

**Description**

Node to call the ROS service from the plume server to create a 
passive turbulent plume.

!!! note "See als

    [Description of the turbulent plume model](../user_guide/introduction.md)

**Input ROS parameters**

* `turbulent_diffusion_coefficients` (*type:* `dict`): Dictionary with keys `x`, `y` and `z`

**ROS launch snippet**

**Running from the launch file**

```bash
roslaunch uuv_plume_simulator start_turbulent_plume.launch
```



