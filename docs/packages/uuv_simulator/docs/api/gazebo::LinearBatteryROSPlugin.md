# class `gazebo::LinearBatteryROSPlugin` 

```
class gazebo::LinearBatteryROSPlugin
  : public LinearBatteryPlugin
```  

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public  `[`LinearBatteryROSPlugin`](#classgazebo_1_1_linear_battery_r_o_s_plugin_1aabebb4f5b17d524e9c3d74dd0cb1acdd)`()` | Constructor.
`public virtual  `[`~LinearBatteryROSPlugin`](#classgazebo_1_1_linear_battery_r_o_s_plugin_1a46c86524f2df0f027533d1806c32a47e)`()` | Destructor.
`public void `[`Load`](#classgazebo_1_1_linear_battery_r_o_s_plugin_1a224ee323f756ae606c9836493f1ff494)`(physics::ModelPtr _parent,sdf::ElementPtr _sdf)` | Load module and read parameters from SDF.
`public virtual void `[`Init`](#classgazebo_1_1_linear_battery_r_o_s_plugin_1aedd9b7053962837e687826e7e06ac249)`()` | Initialize Module.
`public virtual void `[`Reset`](#classgazebo_1_1_linear_battery_r_o_s_plugin_1a869ec61ac6792894bff98f7fc3b7fae0)`()` | Reset Module.
`protected boost::scoped_ptr< ros::NodeHandle > `[`rosNode`](#classgazebo_1_1_linear_battery_r_o_s_plugin_1ac079f1d2cb6edb06f4432c69f165a0a4) | Pointer to this ROS node's handle.
`protected std::string `[`robotNamespace`](#classgazebo_1_1_linear_battery_r_o_s_plugin_1ae9469d16486e6a1730d6ba881caef006) | Namespace for this ROS node.
`protected sensor_msgs::BatteryState `[`batteryStateMsg`](#classgazebo_1_1_linear_battery_r_o_s_plugin_1a44c22f944534c81519677c63c78c7701) | Battery state ROS message.
`protected ros::Timer `[`updateTimer`](#classgazebo_1_1_linear_battery_r_o_s_plugin_1ac1ba8a2811bbcf5f5700a2505f7a63d9) | Connection for callbacks on update world.
`protected void `[`PublishBatteryState`](#classgazebo_1_1_linear_battery_r_o_s_plugin_1af7dd1d4bd4f0b220d8c815bdb8e38679)`()` | Publish battery states.

## Members

#### `public  `[`LinearBatteryROSPlugin`](#classgazebo_1_1_linear_battery_r_o_s_plugin_1aabebb4f5b17d524e9c3d74dd0cb1acdd)`()` 

Constructor.

#### `public virtual  `[`~LinearBatteryROSPlugin`](#classgazebo_1_1_linear_battery_r_o_s_plugin_1a46c86524f2df0f027533d1806c32a47e)`()` 

Destructor.

#### `public void `[`Load`](#classgazebo_1_1_linear_battery_r_o_s_plugin_1a224ee323f756ae606c9836493f1ff494)`(physics::ModelPtr _parent,sdf::ElementPtr _sdf)` 

Load module and read parameters from SDF.

#### `public virtual void `[`Init`](#classgazebo_1_1_linear_battery_r_o_s_plugin_1aedd9b7053962837e687826e7e06ac249)`()` 

Initialize Module.

#### `public virtual void `[`Reset`](#classgazebo_1_1_linear_battery_r_o_s_plugin_1a869ec61ac6792894bff98f7fc3b7fae0)`()` 

Reset Module.

#### `protected boost::scoped_ptr< ros::NodeHandle > `[`rosNode`](#classgazebo_1_1_linear_battery_r_o_s_plugin_1ac079f1d2cb6edb06f4432c69f165a0a4) 

Pointer to this ROS node's handle.

#### `protected std::string `[`robotNamespace`](#classgazebo_1_1_linear_battery_r_o_s_plugin_1ae9469d16486e6a1730d6ba881caef006) 

Namespace for this ROS node.

#### `protected sensor_msgs::BatteryState `[`batteryStateMsg`](#classgazebo_1_1_linear_battery_r_o_s_plugin_1a44c22f944534c81519677c63c78c7701) 

Battery state ROS message.

#### `protected ros::Timer `[`updateTimer`](#classgazebo_1_1_linear_battery_r_o_s_plugin_1ac1ba8a2811bbcf5f5700a2505f7a63d9) 

Connection for callbacks on update world.

#### `protected void `[`PublishBatteryState`](#classgazebo_1_1_linear_battery_r_o_s_plugin_1af7dd1d4bd4f0b220d8c815bdb8e38679)`()` 

Publish battery states.

