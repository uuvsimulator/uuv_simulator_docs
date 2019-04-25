# class `gazebo::CustomBatteryConsumerROSPlugin` 

```
class gazebo::CustomBatteryConsumerROSPlugin
  : public ModelPlugin
```  

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public  `[`CustomBatteryConsumerROSPlugin`](#classgazebo_1_1_custom_battery_consumer_r_o_s_plugin_1a1dfc5cbec8fb4bb7c398b5f92ebfe025)`()` | Constructor.
`public virtual  `[`~CustomBatteryConsumerROSPlugin`](#classgazebo_1_1_custom_battery_consumer_r_o_s_plugin_1ad874654e87502adee138a375c59096a5)`()` | Destructor.
`public void `[`Load`](#classgazebo_1_1_custom_battery_consumer_r_o_s_plugin_1a092657cb2832d56f4f4f9037e29de22f)`(physics::ModelPtr _parent,sdf::ElementPtr _sdf)` | Load module and read parameters from SDF.
`protected boost::scoped_ptr< ros::NodeHandle > `[`rosNode`](#classgazebo_1_1_custom_battery_consumer_r_o_s_plugin_1a849c350038fc65f0b6618daa9bff2d5a) | Pointer to this ROS node's handle.
`protected ros::Subscriber `[`deviceStateSub`](#classgazebo_1_1_custom_battery_consumer_r_o_s_plugin_1a5f4ab26681042a3704d0854c80179ccb) | Subscriber to the device state flag.
`protected common::BatteryPtr `[`battery`](#classgazebo_1_1_custom_battery_consumer_r_o_s_plugin_1aab63a2fd9601f9ed588cd310a31d166d) | Pointer to battery.
`protected bool `[`isDeviceOn`](#classgazebo_1_1_custom_battery_consumer_r_o_s_plugin_1adb9208bcb12e204be32cdafbd4dedece) | Flag to signal whether a specific device is running.
`protected double `[`powerLoad`](#classgazebo_1_1_custom_battery_consumer_r_o_s_plugin_1a2a77576499d0d9a4121df0ab26263999) | Power load in W.
`protected int `[`consumerID`](#classgazebo_1_1_custom_battery_consumer_r_o_s_plugin_1afa8963cf588440f8a65a40709ee87f1b) | Battery consumer ID.
`protected std::string `[`linkName`](#classgazebo_1_1_custom_battery_consumer_r_o_s_plugin_1aab7c22693c5544d155fe5e3a193d9848) | Link name.
`protected std::string `[`batteryName`](#classgazebo_1_1_custom_battery_consumer_r_o_s_plugin_1aabf460331c052e75d5bdfd801832e67c) | Battery model name.
`protected event::ConnectionPtr `[`rosPublishConnection`](#classgazebo_1_1_custom_battery_consumer_r_o_s_plugin_1ac88de3b1d146e46df3352b5769a86b81) | Connection for callbacks on update world.
`protected void `[`UpdateDeviceState`](#classgazebo_1_1_custom_battery_consumer_r_o_s_plugin_1a884a9bccf2a5f4a5a935b67a133a18a2)`(const std_msgs::Bool::ConstPtr & _msg)` | Callback for the device state topic subscriber.
`protected void `[`UpdatePowerLoad`](#classgazebo_1_1_custom_battery_consumer_r_o_s_plugin_1aa0f068f722eb00582d21cd0c69379a2f)`(double _powerLoad)` | Update power load.

## Members

#### `public  `[`CustomBatteryConsumerROSPlugin`](#classgazebo_1_1_custom_battery_consumer_r_o_s_plugin_1a1dfc5cbec8fb4bb7c398b5f92ebfe025)`()` 

Constructor.

#### `public virtual  `[`~CustomBatteryConsumerROSPlugin`](#classgazebo_1_1_custom_battery_consumer_r_o_s_plugin_1ad874654e87502adee138a375c59096a5)`()` 

Destructor.

#### `public void `[`Load`](#classgazebo_1_1_custom_battery_consumer_r_o_s_plugin_1a092657cb2832d56f4f4f9037e29de22f)`(physics::ModelPtr _parent,sdf::ElementPtr _sdf)` 

Load module and read parameters from SDF.

#### `protected boost::scoped_ptr< ros::NodeHandle > `[`rosNode`](#classgazebo_1_1_custom_battery_consumer_r_o_s_plugin_1a849c350038fc65f0b6618daa9bff2d5a) 

Pointer to this ROS node's handle.

#### `protected ros::Subscriber `[`deviceStateSub`](#classgazebo_1_1_custom_battery_consumer_r_o_s_plugin_1a5f4ab26681042a3704d0854c80179ccb) 

Subscriber to the device state flag.

#### `protected common::BatteryPtr `[`battery`](#classgazebo_1_1_custom_battery_consumer_r_o_s_plugin_1aab63a2fd9601f9ed588cd310a31d166d) 

Pointer to battery.

#### `protected bool `[`isDeviceOn`](#classgazebo_1_1_custom_battery_consumer_r_o_s_plugin_1adb9208bcb12e204be32cdafbd4dedece) 

Flag to signal whether a specific device is running.

#### `protected double `[`powerLoad`](#classgazebo_1_1_custom_battery_consumer_r_o_s_plugin_1a2a77576499d0d9a4121df0ab26263999) 

Power load in W.

#### `protected int `[`consumerID`](#classgazebo_1_1_custom_battery_consumer_r_o_s_plugin_1afa8963cf588440f8a65a40709ee87f1b) 

Battery consumer ID.

#### `protected std::string `[`linkName`](#classgazebo_1_1_custom_battery_consumer_r_o_s_plugin_1aab7c22693c5544d155fe5e3a193d9848) 

Link name.

#### `protected std::string `[`batteryName`](#classgazebo_1_1_custom_battery_consumer_r_o_s_plugin_1aabf460331c052e75d5bdfd801832e67c) 

Battery model name.

#### `protected event::ConnectionPtr `[`rosPublishConnection`](#classgazebo_1_1_custom_battery_consumer_r_o_s_plugin_1ac88de3b1d146e46df3352b5769a86b81) 

Connection for callbacks on update world.

#### `protected void `[`UpdateDeviceState`](#classgazebo_1_1_custom_battery_consumer_r_o_s_plugin_1a884a9bccf2a5f4a5a935b67a133a18a2)`(const std_msgs::Bool::ConstPtr & _msg)` 

Callback for the device state topic subscriber.

#### `protected void `[`UpdatePowerLoad`](#classgazebo_1_1_custom_battery_consumer_r_o_s_plugin_1aa0f068f722eb00582d21cd0c69379a2f)`(double _powerLoad)` 

Update power load.

