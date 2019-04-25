# class `gazebo::IMUROSPlugin` 

```
class gazebo::IMUROSPlugin
  : public gazebo::ROSBaseModelPlugin
```  

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public  `[`IMUROSPlugin`](#classgazebo_1_1_i_m_u_r_o_s_plugin_1a5c7035a09686f2688c235b17a3d8a7db)`()` | Class constructor.
`public virtual  `[`~IMUROSPlugin`](#classgazebo_1_1_i_m_u_r_o_s_plugin_1ab19c7cfef17c9a660f495841e494edd6)`()` | Class destructor.
`public virtual void `[`Load`](#classgazebo_1_1_i_m_u_r_o_s_plugin_1a91f9dd3cb212d8b2207e4b51bd06bc79)`(physics::ModelPtr _model,sdf::ElementPtr _sdf)` | Load the plugin.
`protected ignition::math::Vector3d `[`measLinearAcc`](#classgazebo_1_1_i_m_u_r_o_s_plugin_1ae376a7d63023a8fe4246251a59fe3636) | Last measurement of linear acceleration..
`protected ignition::math::Vector3d `[`measAngularVel`](#classgazebo_1_1_i_m_u_r_o_s_plugin_1aa8b6ebdfdd7c36570214121a479185ae) | Last measurement of angular velocity.
`protected ignition::math::Quaterniond `[`measOrientation`](#classgazebo_1_1_i_m_u_r_o_s_plugin_1a237f775ebb67751d4c0a3dd5b806b1b5) | (Simulation) time when the last sensor measurement was generated.
`protected ignition::math::Vector3d `[`gravityWorld`](#classgazebo_1_1_i_m_u_r_o_s_plugin_1ac5c80e66a5029f008a776dd3ca5c7585) | Gravity vector wrt. reference frame.
`protected ignition::math::Vector3d `[`gyroscopeBias`](#classgazebo_1_1_i_m_u_r_o_s_plugin_1a78de6a1ae264ea41a4297b6789120cc9) | Current (drifting) gyroscope bias.
`protected ignition::math::Vector3d `[`accelerometerBias`](#classgazebo_1_1_i_m_u_r_o_s_plugin_1aedcd0a802dc7598c88347bdad2e952e4) | Current (drifting) accelerometer bias.
`protected ignition::math::Vector3d `[`gyroscopeTurnOnBias`](#classgazebo_1_1_i_m_u_r_o_s_plugin_1a5f49ef5082c887fe00818b1153ad8d43) | Constant turn-on gyroscope bias.
`protected ignition::math::Vector3d `[`accelerometerTurnOnBias`](#classgazebo_1_1_i_m_u_r_o_s_plugin_1a21b7f5a23e79eeb076bc89182890e5a3) | Constant turn-on accelerometer bias.
`protected `[`IMUParameters`](docs/packages/uuv_simulator/docs/api/gazebo::IMUParameters.md#structgazebo_1_1_i_m_u_parameters)` `[`imuParameters`](#classgazebo_1_1_i_m_u_r_o_s_plugin_1a9c4660a48d5365bd6c1465e8e2e33f57) | IMU model parameters.
`protected sensor_msgs::Imu `[`imuROSMessage`](#classgazebo_1_1_i_m_u_r_o_s_plugin_1a9270c9a643245555dffac3768f380fc4) | ROS IMU message.
`protected virtual bool `[`OnUpdate`](#classgazebo_1_1_i_m_u_r_o_s_plugin_1aa15397b1f75e506ddb42841966306392)`(const common::UpdateInfo & _info)` | Update sensor measurement.
`protected void `[`AddNoise`](#classgazebo_1_1_i_m_u_r_o_s_plugin_1af354ab1547a4509481807e08c959655f)`(ignition::math::Vector3d & _linAcc,ignition::math::Vector3d & _angVel,ignition::math::Quaterniond & _orientation,double _dt)` | Apply and add nosie model to ideal measurements.

## Members

#### `public  `[`IMUROSPlugin`](#classgazebo_1_1_i_m_u_r_o_s_plugin_1a5c7035a09686f2688c235b17a3d8a7db)`()` 

Class constructor.

#### `public virtual  `[`~IMUROSPlugin`](#classgazebo_1_1_i_m_u_r_o_s_plugin_1ab19c7cfef17c9a660f495841e494edd6)`()` 

Class destructor.

#### `public virtual void `[`Load`](#classgazebo_1_1_i_m_u_r_o_s_plugin_1a91f9dd3cb212d8b2207e4b51bd06bc79)`(physics::ModelPtr _model,sdf::ElementPtr _sdf)` 

Load the plugin.

#### `protected ignition::math::Vector3d `[`measLinearAcc`](#classgazebo_1_1_i_m_u_r_o_s_plugin_1ae376a7d63023a8fe4246251a59fe3636) 

Last measurement of linear acceleration..

#### `protected ignition::math::Vector3d `[`measAngularVel`](#classgazebo_1_1_i_m_u_r_o_s_plugin_1aa8b6ebdfdd7c36570214121a479185ae) 

Last measurement of angular velocity.

#### `protected ignition::math::Quaterniond `[`measOrientation`](#classgazebo_1_1_i_m_u_r_o_s_plugin_1a237f775ebb67751d4c0a3dd5b806b1b5) 

(Simulation) time when the last sensor measurement was generated.

#### `protected ignition::math::Vector3d `[`gravityWorld`](#classgazebo_1_1_i_m_u_r_o_s_plugin_1ac5c80e66a5029f008a776dd3ca5c7585) 

Gravity vector wrt. reference frame.

#### `protected ignition::math::Vector3d `[`gyroscopeBias`](#classgazebo_1_1_i_m_u_r_o_s_plugin_1a78de6a1ae264ea41a4297b6789120cc9) 

Current (drifting) gyroscope bias.

#### `protected ignition::math::Vector3d `[`accelerometerBias`](#classgazebo_1_1_i_m_u_r_o_s_plugin_1aedcd0a802dc7598c88347bdad2e952e4) 

Current (drifting) accelerometer bias.

#### `protected ignition::math::Vector3d `[`gyroscopeTurnOnBias`](#classgazebo_1_1_i_m_u_r_o_s_plugin_1a5f49ef5082c887fe00818b1153ad8d43) 

Constant turn-on gyroscope bias.

#### `protected ignition::math::Vector3d `[`accelerometerTurnOnBias`](#classgazebo_1_1_i_m_u_r_o_s_plugin_1a21b7f5a23e79eeb076bc89182890e5a3) 

Constant turn-on accelerometer bias.

#### `protected `[`IMUParameters`](docs/packages/uuv_simulator/docs/api/gazebo::IMUParameters.md#structgazebo_1_1_i_m_u_parameters)` `[`imuParameters`](#classgazebo_1_1_i_m_u_r_o_s_plugin_1a9c4660a48d5365bd6c1465e8e2e33f57) 

IMU model parameters.

#### `protected sensor_msgs::Imu `[`imuROSMessage`](#classgazebo_1_1_i_m_u_r_o_s_plugin_1a9270c9a643245555dffac3768f380fc4) 

ROS IMU message.

#### `protected virtual bool `[`OnUpdate`](#classgazebo_1_1_i_m_u_r_o_s_plugin_1aa15397b1f75e506ddb42841966306392)`(const common::UpdateInfo & _info)` 

Update sensor measurement.

#### `protected void `[`AddNoise`](#classgazebo_1_1_i_m_u_r_o_s_plugin_1af354ab1547a4509481807e08c959655f)`(ignition::math::Vector3d & _linAcc,ignition::math::Vector3d & _angVel,ignition::math::Quaterniond & _orientation,double _dt)` 

Apply and add nosie model to ideal measurements.

