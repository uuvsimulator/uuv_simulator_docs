# class `gazebo::MagnetometerROSPlugin` 

```
class gazebo::MagnetometerROSPlugin
  : public gazebo::ROSBaseModelPlugin
```  

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public  `[`MagnetometerROSPlugin`](#classgazebo_1_1_magnetometer_r_o_s_plugin_1a6eaa4d0461db8bc1dd03a6efb2046049)`()` | Class constructor.
`public virtual  `[`~MagnetometerROSPlugin`](#classgazebo_1_1_magnetometer_r_o_s_plugin_1a5c394ca9a12d4da9d15d91337194a282)`()` | Class destructor.
`public virtual void `[`Load`](#classgazebo_1_1_magnetometer_r_o_s_plugin_1aa8d9083af5fae036731f513b94a029a1)`(physics::ModelPtr _model,sdf::ElementPtr _sdf)` | Load the plugin.
`protected `[`MagnetometerParameters`](docs/packages/uuv_simulator/docs/api/gazebo::MagnetometerParameters.md#structgazebo_1_1_magnetometer_parameters)` `[`parameters`](#classgazebo_1_1_magnetometer_r_o_s_plugin_1a417aaca91431fb47e949ae947a3c595a) | Magnetometer configuration parameters:
`protected ignition::math::Vector3d `[`magneticFieldWorld`](#classgazebo_1_1_magnetometer_r_o_s_plugin_1a79e45d104255fac396dba8e868ae79df) | Reference magnetic field in world frame:
`protected ignition::math::Vector3d `[`turnOnBias`](#classgazebo_1_1_magnetometer_r_o_s_plugin_1ab4723d042e1d2b382e73cc0e2219e4e9) | Constant turn-on bias [muT].
`protected ignition::math::Vector3d `[`measMagneticField`](#classgazebo_1_1_magnetometer_r_o_s_plugin_1a7ead881188c3d53928ba95569672cba6) | Last measurement of magnetic field.
`protected sensor_msgs::MagneticField `[`rosMsg`](#classgazebo_1_1_magnetometer_r_o_s_plugin_1ad2c2f64e76ecc2f24afa4c6c6810821c) | ROS message.
`protected virtual bool `[`OnUpdate`](#classgazebo_1_1_magnetometer_r_o_s_plugin_1a1834c8718fa80c4e1b26c62a2e9a407f)`(const common::UpdateInfo & _info)` | Update sensor measurement.

## Members

#### `public  `[`MagnetometerROSPlugin`](#classgazebo_1_1_magnetometer_r_o_s_plugin_1a6eaa4d0461db8bc1dd03a6efb2046049)`()` 

Class constructor.

#### `public virtual  `[`~MagnetometerROSPlugin`](#classgazebo_1_1_magnetometer_r_o_s_plugin_1a5c394ca9a12d4da9d15d91337194a282)`()` 

Class destructor.

#### `public virtual void `[`Load`](#classgazebo_1_1_magnetometer_r_o_s_plugin_1aa8d9083af5fae036731f513b94a029a1)`(physics::ModelPtr _model,sdf::ElementPtr _sdf)` 

Load the plugin.

#### `protected `[`MagnetometerParameters`](docs/packages/uuv_simulator/docs/api/gazebo::MagnetometerParameters.md#structgazebo_1_1_magnetometer_parameters)` `[`parameters`](#classgazebo_1_1_magnetometer_r_o_s_plugin_1a417aaca91431fb47e949ae947a3c595a) 

Magnetometer configuration parameters:

#### `protected ignition::math::Vector3d `[`magneticFieldWorld`](#classgazebo_1_1_magnetometer_r_o_s_plugin_1a79e45d104255fac396dba8e868ae79df) 

Reference magnetic field in world frame:

#### `protected ignition::math::Vector3d `[`turnOnBias`](#classgazebo_1_1_magnetometer_r_o_s_plugin_1ab4723d042e1d2b382e73cc0e2219e4e9) 

Constant turn-on bias [muT].

#### `protected ignition::math::Vector3d `[`measMagneticField`](#classgazebo_1_1_magnetometer_r_o_s_plugin_1a7ead881188c3d53928ba95569672cba6) 

Last measurement of magnetic field.

#### `protected sensor_msgs::MagneticField `[`rosMsg`](#classgazebo_1_1_magnetometer_r_o_s_plugin_1ad2c2f64e76ecc2f24afa4c6c6810821c) 

ROS message.

#### `protected virtual bool `[`OnUpdate`](#classgazebo_1_1_magnetometer_r_o_s_plugin_1a1834c8718fa80c4e1b26c62a2e9a407f)`(const common::UpdateInfo & _info)` 

Update sensor measurement.

