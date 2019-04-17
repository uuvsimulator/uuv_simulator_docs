![Version](https://img.shields.io/badge/version-0.3.1-brightgreen.svg)

> Link to the `uuv_plume_simulator` repository [here](https://github.com/uuvsimulator/uuv_plume_simulator)

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

**Passive turbulent plume server node**

**Input ROS parameters**

* `update_rate` (*default:* `5`, *type:* `int` or `float`):  Update rate for the plume particle point cloud update

**ROS services**

> **`create_spheroid_plume`**

> **`create_passive_scalar_turbulent_plume`**

> **`set_plume_limits`**

> **`set_plume_config`**

> **`get_plume_config`**

> **`delete_plume`**

> **`set_plume_source_position`**

> **`get_plume_source_position`**

> **`get_num_particles`**

> **`store_plume_state`**

> **`load_plume_particles`**


## `current_velocity_server`

> **Script type:** `python`

**Current velocity server node**

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

**ROS services**

> **`get_current_velocity_model`**

ROS service description: [`GetCurrentModel`](uuv_plume_msgs.md)

Returns the parameters for the current velocity magnitude $v_c$.

> **`get_angle_model`**

ROS service description: [`GetCurrentModel`](uuv_plume_msgs.md)

> **`set_current_velocity_model`**

ROS service description: [`SetCurrentModel`](uuv_plume_msgs.md)

> **`set_angle_model`**

ROS service description: [`SetCurrentModel`](uuv_plume_msgs.md)

> **`set_current_velocity`**

ROS service description: [`SetCurrentVelocity`](uuv_plume_msgs.md)

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
>> roslaunch uuv_plume_simulator start_current_velocity_server.launch current_velocity_topic:=current_velocity update_rate:=10
```

!!! warning
    Do **NOT** run the current velocity server with a Gazebo 
    simulation that generates the same topic, it can cause unexpected 
    behaviours to the plume's steering.


## `set_demo_current_vel_gazebo`

> **Script type:** `shell`

## `set_demo_spheroid_plume`

> **Script type:** `shell`

## `load_plume_particles`

> **Script type:** `python`

## `set_demo_current_vel`

> **Script type:** `shell`

## `set_turbulent_plume`

> **Script type:** `python`

