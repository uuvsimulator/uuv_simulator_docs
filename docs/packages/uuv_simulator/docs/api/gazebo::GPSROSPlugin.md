# class `gazebo::GPSROSPlugin` 

```
class gazebo::GPSROSPlugin
  : public gazebo::ROSBaseSensorPlugin
```  

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public  `[`GPSROSPlugin`](#classgazebo_1_1_g_p_s_r_o_s_plugin_1ab969180b479e77d98f8cb29e8c94b269)`()` | Class constructor.
`public virtual  `[`~GPSROSPlugin`](#classgazebo_1_1_g_p_s_r_o_s_plugin_1ae4a602032a43f1a3cc904fa4ff938fc3)`()` | Class destructor.
`public virtual void `[`Load`](#classgazebo_1_1_g_p_s_r_o_s_plugin_1ac59efd08373c7f691308609836a2a03d)`(sensors::SensorPtr _parent,sdf::ElementPtr _sdf)` | Load module and read parameters from SDF.
`public bool `[`OnUpdateGPS`](#classgazebo_1_1_g_p_s_r_o_s_plugin_1a255822b5790c6202d5ab5f3bca0eca8b)`()` | Update GPS ROS message.
`protected sensors::GpsSensorPtr `[`gazeboGPSSensor`](#classgazebo_1_1_g_p_s_r_o_s_plugin_1aaa97f3a5236f6c5d9914d042848f97d6) | Pointer to the parent sensor.
`protected sensor_msgs::NavSatFix `[`gpsMessage`](#classgazebo_1_1_g_p_s_r_o_s_plugin_1aa365281835351f7720482bd36611733d) | Output GPS ROS message.

## Members

#### `public  `[`GPSROSPlugin`](#classgazebo_1_1_g_p_s_r_o_s_plugin_1ab969180b479e77d98f8cb29e8c94b269)`()` 

Class constructor.

#### `public virtual  `[`~GPSROSPlugin`](#classgazebo_1_1_g_p_s_r_o_s_plugin_1ae4a602032a43f1a3cc904fa4ff938fc3)`()` 

Class destructor.

#### `public virtual void `[`Load`](#classgazebo_1_1_g_p_s_r_o_s_plugin_1ac59efd08373c7f691308609836a2a03d)`(sensors::SensorPtr _parent,sdf::ElementPtr _sdf)` 

Load module and read parameters from SDF.

#### `public bool `[`OnUpdateGPS`](#classgazebo_1_1_g_p_s_r_o_s_plugin_1a255822b5790c6202d5ab5f3bca0eca8b)`()` 

Update GPS ROS message.

#### `protected sensors::GpsSensorPtr `[`gazeboGPSSensor`](#classgazebo_1_1_g_p_s_r_o_s_plugin_1aaa97f3a5236f6c5d9914d042848f97d6) 

Pointer to the parent sensor.

#### `protected sensor_msgs::NavSatFix `[`gpsMessage`](#classgazebo_1_1_g_p_s_r_o_s_plugin_1aa365281835351f7720482bd36611733d) 

Output GPS ROS message.

