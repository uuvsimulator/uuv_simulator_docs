# Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`namespace `[`gazebo`](#namespacegazebo) | 
`namespace `[`uuv_simulator_ros`](#namespaceuuv__simulator__ros) | 

# namespace `gazebo` 

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public geometry_msgs::Accel `[`accelFromEigen`](#_accelerations_test_plugin_8cc_1a5463c8c5b3e3efe4238a6ab8d7a7488c)`(const Eigen::Vector6d & acc)`            | 
`public Eigen::Matrix3d `[`Matrix3ToEigen`](#_accelerations_test_plugin_8cc_1ac2ca911914770b251917b341cab3341c)`(const ignition::math::Matrix3d & m)`            | 
`class `[`gazebo::AccelerationsTestPlugin`](#classgazebo_1_1_accelerations_test_plugin) | Gazebo model plugin class for underwater objects.
`class `[`gazebo::CustomBatteryConsumerROSPlugin`](#classgazebo_1_1_custom_battery_consumer_r_o_s_plugin) | 
`class `[`gazebo::LinearBatteryROSPlugin`](#classgazebo_1_1_linear_battery_r_o_s_plugin) | 

## Members

#### `public geometry_msgs::Accel `[`accelFromEigen`](#_accelerations_test_plugin_8cc_1a5463c8c5b3e3efe4238a6ab8d7a7488c)`(const Eigen::Vector6d & acc)` 

#### `public Eigen::Matrix3d `[`Matrix3ToEigen`](#_accelerations_test_plugin_8cc_1ac2ca911914770b251917b341cab3341c)`(const ignition::math::Matrix3d & m)` 

# class `gazebo::AccelerationsTestPlugin` 

```
class gazebo::AccelerationsTestPlugin
  : public ModelPlugin
```  

Gazebo model plugin class for underwater objects.

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public  `[`AccelerationsTestPlugin`](#classgazebo_1_1_accelerations_test_plugin_1a55aab0da39c4400e84646b11caa72507)`()` | Constructor.
`public virtual  `[`~AccelerationsTestPlugin`](#classgazebo_1_1_accelerations_test_plugin_1a6e91ba8c0d0817eea3f16480f5b5137b)`()` | Destructor.
`public virtual void `[`Load`](#classgazebo_1_1_accelerations_test_plugin_1a8122bf6caafdee89d84f6a17059f1864)`(gazebo::physics::ModelPtr _model,sdf::ElementPtr _sdf)` | 
`public virtual void `[`Init`](#classgazebo_1_1_accelerations_test_plugin_1a44dd56d9db03bd76aae7dee71d186a56)`()` | 
`public void `[`Update`](#classgazebo_1_1_accelerations_test_plugin_1affd8910814c560e28e926827fa70e70c)`(const gazebo::common::UpdateInfo & _info)` | Update the simulation state.
`protected gazebo::event::ConnectionPtr `[`updateConnection`](#classgazebo_1_1_accelerations_test_plugin_1a0ca115f72985faf7538a4af8761ace97) | Update event.
`protected gazebo::physics::WorldPtr `[`world`](#classgazebo_1_1_accelerations_test_plugin_1ae3fb62216782f354834b5000ffb290fc) | Pointer to the world plugin.
`protected gazebo::physics::ModelPtr `[`model`](#classgazebo_1_1_accelerations_test_plugin_1affe319c6bc7669cadac84a248a0113ad) | Pointer to the model structure.
`protected gazebo::transport::NodePtr `[`node`](#classgazebo_1_1_accelerations_test_plugin_1a78096f01be7e0804b178f565862315bf) | Gazebo node.
`protected physics::LinkPtr `[`link`](#classgazebo_1_1_accelerations_test_plugin_1af0c72cd442cedea70084db09fef483ad) | Link of test object.
`protected ros::Publisher `[`pub_accel_b_gazebo`](#classgazebo_1_1_accelerations_test_plugin_1a491b199de59266f1e559ab0667cdc602) | 
`protected ros::Publisher `[`pub_accel_b_numeric`](#classgazebo_1_1_accelerations_test_plugin_1af15a43ec01edd5d0d0d5c00ecc93bbfe) | 
`protected ros::Publisher `[`pub_accel_w_gazebo`](#classgazebo_1_1_accelerations_test_plugin_1a51d748b8442b3856eeff4de3d8fbc83a) | 
`protected ros::Publisher `[`pub_accel_w_numeric`](#classgazebo_1_1_accelerations_test_plugin_1aa2bf1016615f64d5cb4d29592af494f7) | 
`protected Eigen::Vector6d `[`last_w_v_w_b`](#classgazebo_1_1_accelerations_test_plugin_1a0829056785ddad0daad41f40b61b1421) | Velocity of link with respect to world frame in previous time step.
`protected common::Time `[`lastTime`](#classgazebo_1_1_accelerations_test_plugin_1afedb74b4ade15db6baf2cc9fdcef5e7c) | Time stamp of previous time step.
`protected virtual void `[`Connect`](#classgazebo_1_1_accelerations_test_plugin_1afbfdb6e1ed425f0f4194f32fd69e36d0)`()` | Connects the update event callback.

## Members

#### `public  `[`AccelerationsTestPlugin`](#classgazebo_1_1_accelerations_test_plugin_1a55aab0da39c4400e84646b11caa72507)`()` 

Constructor.

#### `public virtual  `[`~AccelerationsTestPlugin`](#classgazebo_1_1_accelerations_test_plugin_1a6e91ba8c0d0817eea3f16480f5b5137b)`()` 

Destructor.

#### `public virtual void `[`Load`](#classgazebo_1_1_accelerations_test_plugin_1a8122bf6caafdee89d84f6a17059f1864)`(gazebo::physics::ModelPtr _model,sdf::ElementPtr _sdf)` 

#### `public virtual void `[`Init`](#classgazebo_1_1_accelerations_test_plugin_1a44dd56d9db03bd76aae7dee71d186a56)`()` 

#### `public void `[`Update`](#classgazebo_1_1_accelerations_test_plugin_1affd8910814c560e28e926827fa70e70c)`(const gazebo::common::UpdateInfo & _info)` 

Update the simulation state.

#### Parameters
* `_info` Information used in the update event.

#### `protected gazebo::event::ConnectionPtr `[`updateConnection`](#classgazebo_1_1_accelerations_test_plugin_1a0ca115f72985faf7538a4af8761ace97) 

Update event.

#### `protected gazebo::physics::WorldPtr `[`world`](#classgazebo_1_1_accelerations_test_plugin_1ae3fb62216782f354834b5000ffb290fc) 

Pointer to the world plugin.

#### `protected gazebo::physics::ModelPtr `[`model`](#classgazebo_1_1_accelerations_test_plugin_1affe319c6bc7669cadac84a248a0113ad) 

Pointer to the model structure.

#### `protected gazebo::transport::NodePtr `[`node`](#classgazebo_1_1_accelerations_test_plugin_1a78096f01be7e0804b178f565862315bf) 

Gazebo node.

#### `protected physics::LinkPtr `[`link`](#classgazebo_1_1_accelerations_test_plugin_1af0c72cd442cedea70084db09fef483ad) 

Link of test object.

#### `protected ros::Publisher `[`pub_accel_b_gazebo`](#classgazebo_1_1_accelerations_test_plugin_1a491b199de59266f1e559ab0667cdc602) 

#### `protected ros::Publisher `[`pub_accel_b_numeric`](#classgazebo_1_1_accelerations_test_plugin_1af15a43ec01edd5d0d0d5c00ecc93bbfe) 

#### `protected ros::Publisher `[`pub_accel_w_gazebo`](#classgazebo_1_1_accelerations_test_plugin_1a51d748b8442b3856eeff4de3d8fbc83a) 

#### `protected ros::Publisher `[`pub_accel_w_numeric`](#classgazebo_1_1_accelerations_test_plugin_1aa2bf1016615f64d5cb4d29592af494f7) 

#### `protected Eigen::Vector6d `[`last_w_v_w_b`](#classgazebo_1_1_accelerations_test_plugin_1a0829056785ddad0daad41f40b61b1421) 

Velocity of link with respect to world frame in previous time step.

#### `protected common::Time `[`lastTime`](#classgazebo_1_1_accelerations_test_plugin_1afedb74b4ade15db6baf2cc9fdcef5e7c) 

Time stamp of previous time step.

#### `protected virtual void `[`Connect`](#classgazebo_1_1_accelerations_test_plugin_1afbfdb6e1ed425f0f4194f32fd69e36d0)`()` 

Connects the update event callback.

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

# namespace `uuv_simulator_ros` 

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`class `[`uuv_simulator_ros::FinROSPlugin`](#classuuv__simulator__ros_1_1_fin_r_o_s_plugin) | 
`class `[`uuv_simulator_ros::JointStatePublisher`](#classuuv__simulator__ros_1_1_joint_state_publisher) | 
`class `[`uuv_simulator_ros::ThrusterROSPlugin`](#classuuv__simulator__ros_1_1_thruster_r_o_s_plugin) | 
`class `[`uuv_simulator_ros::UnderwaterObjectROSPlugin`](#classuuv__simulator__ros_1_1_underwater_object_r_o_s_plugin) | 

# class `uuv_simulator_ros::FinROSPlugin` 

```
class uuv_simulator_ros::FinROSPlugin
  : public FinPlugin
```  

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public  `[`FinROSPlugin`](#classuuv__simulator__ros_1_1_fin_r_o_s_plugin_1ab36ec9a6e6cf420763695f9e91cc155b)`()` | Constrcutor.
`public  `[`~FinROSPlugin`](#classuuv__simulator__ros_1_1_fin_r_o_s_plugin_1a424574c4b915a5af56a5c8daec47e626)`()` | Destructor.
`public void `[`Load`](#classuuv__simulator__ros_1_1_fin_r_o_s_plugin_1a0f70780cf0a115dc47cd4a21f6a62f60)`(gazebo::physics::ModelPtr _parent,sdf::ElementPtr _sdf)` | Load module and read parameters from SDF.
`public void `[`RosPublishStates`](#classuuv__simulator__ros_1_1_fin_r_o_s_plugin_1a2aa520188b885575965a7675f62d78c8)`()` | Publish state via ROS.
`public void `[`SetReference`](#classuuv__simulator__ros_1_1_fin_r_o_s_plugin_1a09703d436ca89cd2c7c75d110cdc5b7a)`(const uuv_gazebo_ros_plugins_msgs::FloatStamped::ConstPtr & _msg)` | Set new set point.
`public bool `[`GetLiftDragParams`](#classuuv__simulator__ros_1_1_fin_r_o_s_plugin_1ac5c561a272971295a1a0a2a79928732c)`(uuv_gazebo_ros_plugins_msgs::GetListParam::Request & _req,uuv_gazebo_ros_plugins_msgs::GetListParam::Response & _res)` | Return the list of paramaters of the lift and drag model.
`public gazebo::common::Time `[`GetRosPublishPeriod`](#classuuv__simulator__ros_1_1_fin_r_o_s_plugin_1aba957637565587cf7fc8114e951024a8)`()` | Return the ROS publish period.
`public void `[`SetRosPublishRate`](#classuuv__simulator__ros_1_1_fin_r_o_s_plugin_1a2ad58a55300e951a3a3f4b2d7dd61133)`(double _hz)` | Set the ROS publish frequency (Hz).
`public virtual void `[`Init`](#classuuv__simulator__ros_1_1_fin_r_o_s_plugin_1a3984861d97812ec447b20fd6edb90d26)`()` | Initialize Module.
`public virtual void `[`Reset`](#classuuv__simulator__ros_1_1_fin_r_o_s_plugin_1a423e0b46d5d38b327c6122ecd99665b4)`()` | Reset Module.

## Members

#### `public  `[`FinROSPlugin`](#classuuv__simulator__ros_1_1_fin_r_o_s_plugin_1ab36ec9a6e6cf420763695f9e91cc155b)`()` 

Constrcutor.

#### `public  `[`~FinROSPlugin`](#classuuv__simulator__ros_1_1_fin_r_o_s_plugin_1a424574c4b915a5af56a5c8daec47e626)`()` 

Destructor.

#### `public void `[`Load`](#classuuv__simulator__ros_1_1_fin_r_o_s_plugin_1a0f70780cf0a115dc47cd4a21f6a62f60)`(gazebo::physics::ModelPtr _parent,sdf::ElementPtr _sdf)` 

Load module and read parameters from SDF.

#### `public void `[`RosPublishStates`](#classuuv__simulator__ros_1_1_fin_r_o_s_plugin_1a2aa520188b885575965a7675f62d78c8)`()` 

Publish state via ROS.

#### `public void `[`SetReference`](#classuuv__simulator__ros_1_1_fin_r_o_s_plugin_1a09703d436ca89cd2c7c75d110cdc5b7a)`(const uuv_gazebo_ros_plugins_msgs::FloatStamped::ConstPtr & _msg)` 

Set new set point.

#### `public bool `[`GetLiftDragParams`](#classuuv__simulator__ros_1_1_fin_r_o_s_plugin_1ac5c561a272971295a1a0a2a79928732c)`(uuv_gazebo_ros_plugins_msgs::GetListParam::Request & _req,uuv_gazebo_ros_plugins_msgs::GetListParam::Response & _res)` 

Return the list of paramaters of the lift and drag model.

#### `public gazebo::common::Time `[`GetRosPublishPeriod`](#classuuv__simulator__ros_1_1_fin_r_o_s_plugin_1aba957637565587cf7fc8114e951024a8)`()` 

Return the ROS publish period.

#### `public void `[`SetRosPublishRate`](#classuuv__simulator__ros_1_1_fin_r_o_s_plugin_1a2ad58a55300e951a3a3f4b2d7dd61133)`(double _hz)` 

Set the ROS publish frequency (Hz).

#### `public virtual void `[`Init`](#classuuv__simulator__ros_1_1_fin_r_o_s_plugin_1a3984861d97812ec447b20fd6edb90d26)`()` 

Initialize Module.

#### `public virtual void `[`Reset`](#classuuv__simulator__ros_1_1_fin_r_o_s_plugin_1a423e0b46d5d38b327c6122ecd99665b4)`()` 

Reset Module.

# class `uuv_simulator_ros::JointStatePublisher` 

```
class uuv_simulator_ros::JointStatePublisher
  : public ModelPlugin
```  

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public  `[`JointStatePublisher`](#classuuv__simulator__ros_1_1_joint_state_publisher_1a8845851dbc4b8416f8d6e142ad4361c3)`()` | 
`public  `[`~JointStatePublisher`](#classuuv__simulator__ros_1_1_joint_state_publisher_1a795abdb7e09dda4ff9e7aa404c1e642f)`()` | 
`public void `[`Load`](#classuuv__simulator__ros_1_1_joint_state_publisher_1a68a2588c08f13a8286e7d9bb5cc2546e)`(gazebo::physics::ModelPtr _parent,sdf::ElementPtr _sdf)` | 
`public void `[`OnUpdate`](#classuuv__simulator__ros_1_1_joint_state_publisher_1af075fe8b44c6ee07f5a578b1bee99800)`(const gazebo::common::UpdateInfo & _info)` | 
`public void `[`PublishJointStates`](#classuuv__simulator__ros_1_1_joint_state_publisher_1a3c00e22e725df8df3b3f314edd87cce6)`()` | 

## Members

#### `public  `[`JointStatePublisher`](#classuuv__simulator__ros_1_1_joint_state_publisher_1a8845851dbc4b8416f8d6e142ad4361c3)`()` 

#### `public  `[`~JointStatePublisher`](#classuuv__simulator__ros_1_1_joint_state_publisher_1a795abdb7e09dda4ff9e7aa404c1e642f)`()` 

#### `public void `[`Load`](#classuuv__simulator__ros_1_1_joint_state_publisher_1a68a2588c08f13a8286e7d9bb5cc2546e)`(gazebo::physics::ModelPtr _parent,sdf::ElementPtr _sdf)` 

#### `public void `[`OnUpdate`](#classuuv__simulator__ros_1_1_joint_state_publisher_1af075fe8b44c6ee07f5a578b1bee99800)`(const gazebo::common::UpdateInfo & _info)` 

#### `public void `[`PublishJointStates`](#classuuv__simulator__ros_1_1_joint_state_publisher_1a3c00e22e725df8df3b3f314edd87cce6)`()` 

# class `uuv_simulator_ros::ThrusterROSPlugin` 

```
class uuv_simulator_ros::ThrusterROSPlugin
  : public ThrusterPlugin
```  

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public  `[`ThrusterROSPlugin`](#classuuv__simulator__ros_1_1_thruster_r_o_s_plugin_1a96d5b46e81d42adc6f1bedc129b56a92)`()` | Constrcutor.
`public  `[`~ThrusterROSPlugin`](#classuuv__simulator__ros_1_1_thruster_r_o_s_plugin_1a25fab91375decd55eec8a8ee3bd4079e)`()` | Destructor.
`public void `[`Load`](#classuuv__simulator__ros_1_1_thruster_r_o_s_plugin_1ab1b70d05c87212176d1237817bf9ddf5)`(gazebo::physics::ModelPtr _parent,sdf::ElementPtr _sdf)` | Load module and read parameters from SDF.
`public void `[`RosPublishStates`](#classuuv__simulator__ros_1_1_thruster_r_o_s_plugin_1ab3d7f21cabcbb88d9551860182e50096)`()` | Publish thruster state via ROS.
`public void `[`SetThrustReference`](#classuuv__simulator__ros_1_1_thruster_r_o_s_plugin_1ac3f8c621ead1c6fe22809c3abf284a68)`(const uuv_gazebo_ros_plugins_msgs::FloatStamped::ConstPtr & _msg)` | Set new set point (desired thrust [N]) for thruster.
`public gazebo::common::Time `[`GetRosPublishPeriod`](#classuuv__simulator__ros_1_1_thruster_r_o_s_plugin_1a61b52a4fbc5871061f3b8f4639596e32)`()` | Return the ROS publish period.
`public void `[`SetRosPublishRate`](#classuuv__simulator__ros_1_1_thruster_r_o_s_plugin_1adb8206d74cba2e15a209db4284198db8)`(double _hz)` | Set the ROS publish frequency (Hz).
`public virtual void `[`Init`](#classuuv__simulator__ros_1_1_thruster_r_o_s_plugin_1a670f0befa3efac82bcff5d187fe6cbb3)`()` | Initialize Module.
`public virtual void `[`Reset`](#classuuv__simulator__ros_1_1_thruster_r_o_s_plugin_1a525a9a8ea9be37c4542137640c4a2fbc)`()` | Reset Module.
`public bool `[`SetThrustForceEfficiency`](#classuuv__simulator__ros_1_1_thruster_r_o_s_plugin_1a9d65e6dda76939e59df4b18226f893b0)`(uuv_gazebo_ros_plugins_msgs::SetThrusterEfficiency::Request & _req,uuv_gazebo_ros_plugins_msgs::SetThrusterEfficiency::Response & _res)` | Set the thrust efficiency factor.
`public bool `[`GetThrustForceEfficiency`](#classuuv__simulator__ros_1_1_thruster_r_o_s_plugin_1a4a73039a9b93090462da51189a83b85b)`(uuv_gazebo_ros_plugins_msgs::GetThrusterEfficiency::Request & _req,uuv_gazebo_ros_plugins_msgs::GetThrusterEfficiency::Response & _res)` | Get the thrust efficiency factor.
`public bool `[`SetDynamicStateEfficiency`](#classuuv__simulator__ros_1_1_thruster_r_o_s_plugin_1a10f86f23ba017986e816a83dbd217a5a)`(uuv_gazebo_ros_plugins_msgs::SetThrusterEfficiency::Request & _req,uuv_gazebo_ros_plugins_msgs::SetThrusterEfficiency::Response & _res)` | Set the dynamic state efficiency factor.
`public bool `[`GetDynamicStateEfficiency`](#classuuv__simulator__ros_1_1_thruster_r_o_s_plugin_1a585e5327b2d1fd93d8bacce6e95e623c)`(uuv_gazebo_ros_plugins_msgs::GetThrusterEfficiency::Request & _req,uuv_gazebo_ros_plugins_msgs::GetThrusterEfficiency::Response & _res)` | Get the dynamic state efficiency factor.
`public bool `[`SetThrusterState`](#classuuv__simulator__ros_1_1_thruster_r_o_s_plugin_1ad8b0158748c2ae0950851e257d811988)`(uuv_gazebo_ros_plugins_msgs::SetThrusterState::Request & _req,uuv_gazebo_ros_plugins_msgs::SetThrusterState::Response & _res)` | Turn thruster on/off.
`public bool `[`GetThrusterState`](#classuuv__simulator__ros_1_1_thruster_r_o_s_plugin_1a03f9489a29bf669efb23ecc9df28f95b)`(uuv_gazebo_ros_plugins_msgs::GetThrusterState::Request & _req,uuv_gazebo_ros_plugins_msgs::GetThrusterState::Response & _res)` | Get thruster state.
`public bool `[`GetThrusterConversionFcn`](#classuuv__simulator__ros_1_1_thruster_r_o_s_plugin_1af012be49e3598405ceb764190838789c)`(uuv_gazebo_ros_plugins_msgs::GetThrusterConversionFcn::Request & _req,uuv_gazebo_ros_plugins_msgs::GetThrusterConversionFcn::Response & _res)` | Get thruster conversion function parameters.

## Members

#### `public  `[`ThrusterROSPlugin`](#classuuv__simulator__ros_1_1_thruster_r_o_s_plugin_1a96d5b46e81d42adc6f1bedc129b56a92)`()` 

Constrcutor.

#### `public  `[`~ThrusterROSPlugin`](#classuuv__simulator__ros_1_1_thruster_r_o_s_plugin_1a25fab91375decd55eec8a8ee3bd4079e)`()` 

Destructor.

#### `public void `[`Load`](#classuuv__simulator__ros_1_1_thruster_r_o_s_plugin_1ab1b70d05c87212176d1237817bf9ddf5)`(gazebo::physics::ModelPtr _parent,sdf::ElementPtr _sdf)` 

Load module and read parameters from SDF.

#### `public void `[`RosPublishStates`](#classuuv__simulator__ros_1_1_thruster_r_o_s_plugin_1ab3d7f21cabcbb88d9551860182e50096)`()` 

Publish thruster state via ROS.

#### `public void `[`SetThrustReference`](#classuuv__simulator__ros_1_1_thruster_r_o_s_plugin_1ac3f8c621ead1c6fe22809c3abf284a68)`(const uuv_gazebo_ros_plugins_msgs::FloatStamped::ConstPtr & _msg)` 

Set new set point (desired thrust [N]) for thruster.

#### `public gazebo::common::Time `[`GetRosPublishPeriod`](#classuuv__simulator__ros_1_1_thruster_r_o_s_plugin_1a61b52a4fbc5871061f3b8f4639596e32)`()` 

Return the ROS publish period.

#### `public void `[`SetRosPublishRate`](#classuuv__simulator__ros_1_1_thruster_r_o_s_plugin_1adb8206d74cba2e15a209db4284198db8)`(double _hz)` 

Set the ROS publish frequency (Hz).

#### `public virtual void `[`Init`](#classuuv__simulator__ros_1_1_thruster_r_o_s_plugin_1a670f0befa3efac82bcff5d187fe6cbb3)`()` 

Initialize Module.

#### `public virtual void `[`Reset`](#classuuv__simulator__ros_1_1_thruster_r_o_s_plugin_1a525a9a8ea9be37c4542137640c4a2fbc)`()` 

Reset Module.

#### `public bool `[`SetThrustForceEfficiency`](#classuuv__simulator__ros_1_1_thruster_r_o_s_plugin_1a9d65e6dda76939e59df4b18226f893b0)`(uuv_gazebo_ros_plugins_msgs::SetThrusterEfficiency::Request & _req,uuv_gazebo_ros_plugins_msgs::SetThrusterEfficiency::Response & _res)` 

Set the thrust efficiency factor.

#### `public bool `[`GetThrustForceEfficiency`](#classuuv__simulator__ros_1_1_thruster_r_o_s_plugin_1a4a73039a9b93090462da51189a83b85b)`(uuv_gazebo_ros_plugins_msgs::GetThrusterEfficiency::Request & _req,uuv_gazebo_ros_plugins_msgs::GetThrusterEfficiency::Response & _res)` 

Get the thrust efficiency factor.

#### `public bool `[`SetDynamicStateEfficiency`](#classuuv__simulator__ros_1_1_thruster_r_o_s_plugin_1a10f86f23ba017986e816a83dbd217a5a)`(uuv_gazebo_ros_plugins_msgs::SetThrusterEfficiency::Request & _req,uuv_gazebo_ros_plugins_msgs::SetThrusterEfficiency::Response & _res)` 

Set the dynamic state efficiency factor.

#### `public bool `[`GetDynamicStateEfficiency`](#classuuv__simulator__ros_1_1_thruster_r_o_s_plugin_1a585e5327b2d1fd93d8bacce6e95e623c)`(uuv_gazebo_ros_plugins_msgs::GetThrusterEfficiency::Request & _req,uuv_gazebo_ros_plugins_msgs::GetThrusterEfficiency::Response & _res)` 

Get the dynamic state efficiency factor.

#### `public bool `[`SetThrusterState`](#classuuv__simulator__ros_1_1_thruster_r_o_s_plugin_1ad8b0158748c2ae0950851e257d811988)`(uuv_gazebo_ros_plugins_msgs::SetThrusterState::Request & _req,uuv_gazebo_ros_plugins_msgs::SetThrusterState::Response & _res)` 

Turn thruster on/off.

#### `public bool `[`GetThrusterState`](#classuuv__simulator__ros_1_1_thruster_r_o_s_plugin_1a03f9489a29bf669efb23ecc9df28f95b)`(uuv_gazebo_ros_plugins_msgs::GetThrusterState::Request & _req,uuv_gazebo_ros_plugins_msgs::GetThrusterState::Response & _res)` 

Get thruster state.

#### `public bool `[`GetThrusterConversionFcn`](#classuuv__simulator__ros_1_1_thruster_r_o_s_plugin_1af012be49e3598405ceb764190838789c)`(uuv_gazebo_ros_plugins_msgs::GetThrusterConversionFcn::Request & _req,uuv_gazebo_ros_plugins_msgs::GetThrusterConversionFcn::Response & _res)` 

Get thruster conversion function parameters.

# class `uuv_simulator_ros::UnderwaterObjectROSPlugin` 

```
class uuv_simulator_ros::UnderwaterObjectROSPlugin
  : public UnderwaterObjectPlugin
```  

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public  `[`UnderwaterObjectROSPlugin`](#classuuv__simulator__ros_1_1_underwater_object_r_o_s_plugin_1a6d26a8a5c08e79c0a149a07cf61209e0)`()` | Constructor.
`public virtual  `[`~UnderwaterObjectROSPlugin`](#classuuv__simulator__ros_1_1_underwater_object_r_o_s_plugin_1ae1eb17f91cb1383400138b6ef241a06f)`()` | Destructor.
`public void `[`Load`](#classuuv__simulator__ros_1_1_underwater_object_r_o_s_plugin_1a86c5be6309611c623757fca4565051c9)`(gazebo::physics::ModelPtr _parent,sdf::ElementPtr _sdf)` | Load module and read parameters from SDF.
`public virtual void `[`Init`](#classuuv__simulator__ros_1_1_underwater_object_r_o_s_plugin_1a3401922bc6e94cfcb5db27a99d2e4f0a)`()` | Initialize Module.
`public virtual void `[`Reset`](#classuuv__simulator__ros_1_1_underwater_object_r_o_s_plugin_1ae0316192f5b26fa321f3e64dd46287b7)`()` | Reset Module.
`public virtual void `[`Update`](#classuuv__simulator__ros_1_1_underwater_object_r_o_s_plugin_1a8f81a22f771bc1203365de1438452e7a)`(const gazebo::common::UpdateInfo & _info)` | Update the simulation state.
`public void `[`UpdateLocalCurrentVelocity`](#classuuv__simulator__ros_1_1_underwater_object_r_o_s_plugin_1a8796c2736835dc203cb7f9c7e84a923e)`(const geometry_msgs::Vector3::ConstPtr & _msg)` | Update the local current velocity, this data will be used only if the useGlobalCurrent flag is set to false.
`public bool `[`SetUseGlobalCurrentVel`](#classuuv__simulator__ros_1_1_underwater_object_r_o_s_plugin_1a038402f422a3940e426eec798f6a0d39)`(uuv_gazebo_ros_plugins_msgs::SetUseGlobalCurrentVel::Request & _req,uuv_gazebo_ros_plugins_msgs::SetUseGlobalCurrentVel::Response & _res)` | Set flag to use the global current velocity topic input.
`public bool `[`GetModelProperties`](#classuuv__simulator__ros_1_1_underwater_object_r_o_s_plugin_1a36c121c67de5ba30cd0770fc9b60ea26)`(uuv_gazebo_ros_plugins_msgs::GetModelProperties::Request & _req,uuv_gazebo_ros_plugins_msgs::GetModelProperties::Response & _res)` | Return the model properties, along with parameters from the hydrodynamic and hydrostatic models.
`public bool `[`SetScalingAddedMass`](#classuuv__simulator__ros_1_1_underwater_object_r_o_s_plugin_1a5d6cd010fa2f18ae91147c03ee9d1408)`(uuv_gazebo_ros_plugins_msgs::SetFloat::Request & _req,uuv_gazebo_ros_plugins_msgs::SetFloat::Response & _res)` | Set the scaling factor for the added-mass matrix.
`public bool `[`GetScalingAddedMass`](#classuuv__simulator__ros_1_1_underwater_object_r_o_s_plugin_1ad8ee29496336a958fa59c6fc35026729)`(uuv_gazebo_ros_plugins_msgs::GetFloat::Request & _req,uuv_gazebo_ros_plugins_msgs::GetFloat::Response & _res)` | Return current scaling factor for the added-mass matrix.
`public bool `[`SetScalingDamping`](#classuuv__simulator__ros_1_1_underwater_object_r_o_s_plugin_1a67861c1e99ee10a9c64f96d6401b221d)`(uuv_gazebo_ros_plugins_msgs::SetFloat::Request & _req,uuv_gazebo_ros_plugins_msgs::SetFloat::Response & _res)` | Set a scaling factor for the overall damping matrix.
`public bool `[`GetScalingDamping`](#classuuv__simulator__ros_1_1_underwater_object_r_o_s_plugin_1adc480b2b52d0da8a9c1d1b700d7bacd6)`(uuv_gazebo_ros_plugins_msgs::GetFloat::Request & _req,uuv_gazebo_ros_plugins_msgs::GetFloat::Response & _res)` | Return the scaling factor for the overall damping matrix.
`public bool `[`SetScalingVolume`](#classuuv__simulator__ros_1_1_underwater_object_r_o_s_plugin_1a2569924791d708d8d879c0fec853b5f4)`(uuv_gazebo_ros_plugins_msgs::SetFloat::Request & _req,uuv_gazebo_ros_plugins_msgs::SetFloat::Response & _res)` | Set scaling factor for the model's volume used for buoyancy force computation.
`public bool `[`GetScalingVolume`](#classuuv__simulator__ros_1_1_underwater_object_r_o_s_plugin_1a9eb2881a288725f83c9924b7be498c81)`(uuv_gazebo_ros_plugins_msgs::GetFloat::Request & _req,uuv_gazebo_ros_plugins_msgs::GetFloat::Response & _res)` | Get scaling factor for the model's volume used for buoyancy force computation.
`public bool `[`SetFluidDensity`](#classuuv__simulator__ros_1_1_underwater_object_r_o_s_plugin_1ac254edcbd59acb26fd70b70acad679c9)`(uuv_gazebo_ros_plugins_msgs::SetFloat::Request & _req,uuv_gazebo_ros_plugins_msgs::SetFloat::Response & _res)` | Set new fluid density (this will alter the value for the buoyancy force)
`public bool `[`GetFluidDensity`](#classuuv__simulator__ros_1_1_underwater_object_r_o_s_plugin_1a92c568850087edd355359e967f42d966)`(uuv_gazebo_ros_plugins_msgs::GetFloat::Request & _req,uuv_gazebo_ros_plugins_msgs::GetFloat::Response & _res)` | Get current value for the fluid density.
`public bool `[`SetOffsetVolume`](#classuuv__simulator__ros_1_1_underwater_object_r_o_s_plugin_1a473e7dae4ba36e061389cf4d193ce80d)`(uuv_gazebo_ros_plugins_msgs::SetFloat::Request & _req,uuv_gazebo_ros_plugins_msgs::SetFloat::Response & _res)` | Set offset factor for the model's volume (this will alter the value for the buoyancy force)
`public bool `[`GetOffsetVolume`](#classuuv__simulator__ros_1_1_underwater_object_r_o_s_plugin_1a70d64b6da3a18257bb1b4b1edc9afb3b)`(uuv_gazebo_ros_plugins_msgs::GetFloat::Request & _req,uuv_gazebo_ros_plugins_msgs::GetFloat::Response & _res)` | Return the offset factor for the model's volume.
`public bool `[`SetOffsetAddedMass`](#classuuv__simulator__ros_1_1_underwater_object_r_o_s_plugin_1ae062c4867e24ba3daf56032728fb3e9a)`(uuv_gazebo_ros_plugins_msgs::SetFloat::Request & _req,uuv_gazebo_ros_plugins_msgs::SetFloat::Response & _res)` | Set the offset factor for the added-mass matrix.
`public bool `[`GetOffsetAddedMass`](#classuuv__simulator__ros_1_1_underwater_object_r_o_s_plugin_1a317123306ae032c3cfb408553ed0706c)`(uuv_gazebo_ros_plugins_msgs::GetFloat::Request & _req,uuv_gazebo_ros_plugins_msgs::GetFloat::Response & _res)` | Return the offset factor for the added-mass matrix.
`public bool `[`SetOffsetLinearDamping`](#classuuv__simulator__ros_1_1_underwater_object_r_o_s_plugin_1a9b3127ae45a4972927bd7becc61a4cf4)`(uuv_gazebo_ros_plugins_msgs::SetFloat::Request & _req,uuv_gazebo_ros_plugins_msgs::SetFloat::Response & _res)` | Set the offset factor for the linear damping matrix.
`public bool `[`GetOffsetLinearDamping`](#classuuv__simulator__ros_1_1_underwater_object_r_o_s_plugin_1a979a847fb03c318d23809ef7e516f980)`(uuv_gazebo_ros_plugins_msgs::GetFloat::Request & _req,uuv_gazebo_ros_plugins_msgs::GetFloat::Response & _res)` | Return the offset factor for the linear damping matrix.
`public bool `[`SetOffsetLinearForwardSpeedDamping`](#classuuv__simulator__ros_1_1_underwater_object_r_o_s_plugin_1a85a1221c40202088731e56f1d7736bf1)`(uuv_gazebo_ros_plugins_msgs::SetFloat::Request & _req,uuv_gazebo_ros_plugins_msgs::SetFloat::Response & _res)` | Set the offset factor for the linear forward speed damping matrix.
`public bool `[`GetOffsetLinearForwardSpeedDamping`](#classuuv__simulator__ros_1_1_underwater_object_r_o_s_plugin_1a8c63d709fc992f899ffbe1eced7b6cd8)`(uuv_gazebo_ros_plugins_msgs::GetFloat::Request & _req,uuv_gazebo_ros_plugins_msgs::GetFloat::Response & _res)` | Return the offset factor for the linear forward speed damping matrix.
`public bool `[`SetOffsetNonLinearDamping`](#classuuv__simulator__ros_1_1_underwater_object_r_o_s_plugin_1a972ab56e380c00dcc489c0d9e9a4d0de)`(uuv_gazebo_ros_plugins_msgs::SetFloat::Request & _req,uuv_gazebo_ros_plugins_msgs::SetFloat::Response & _res)` | Set the offset factor for the nonlinear damping matrix.
`public bool `[`GetOffsetNonLinearDamping`](#classuuv__simulator__ros_1_1_underwater_object_r_o_s_plugin_1abc734c754de497bf62b13de980649f70)`(uuv_gazebo_ros_plugins_msgs::GetFloat::Request & _req,uuv_gazebo_ros_plugins_msgs::GetFloat::Response & _res)` | Return the offset factor for the nonlinear damping matrix.
`protected virtual void `[`PublishRestoringForce`](#classuuv__simulator__ros_1_1_underwater_object_r_o_s_plugin_1adf2dd5f72380c281f9176bd0e4e98f59)`(gazebo::physics::LinkPtr _link)` | Publish restoring force.
`protected virtual void `[`PublishHydrodynamicWrenches`](#classuuv__simulator__ros_1_1_underwater_object_r_o_s_plugin_1a22cd26dfdc7d64c8fa3b0a8d5ac40682)`(gazebo::physics::LinkPtr _link)` | Publish hydrodynamic wrenches.
`protected virtual void `[`GenWrenchMsg`](#classuuv__simulator__ros_1_1_underwater_object_r_o_s_plugin_1a62b50fa4ff5d5b36b78a2160bad1d500)`(ignition::math::Vector3d _force,ignition::math::Vector3d _torque,geometry_msgs::WrenchStamped & _output)` | Returns the wrench message for debugging topics.
`protected virtual void `[`InitDebug`](#classuuv__simulator__ros_1_1_underwater_object_r_o_s_plugin_1a5dbdc863b0902d14f77a3f31b585d0f8)`(gazebo::physics::LinkPtr _link,gazebo::HydrodynamicModelPtr _hydro)` | Sets the topics used for publishing the intermediate data during the simulation.
`protected virtual void `[`PublishCurrentVelocityMarker`](#classuuv__simulator__ros_1_1_underwater_object_r_o_s_plugin_1ae2defd15b338fe56edbbc87bfe364b6c)`()` | Publishes the current velocity marker.
`protected virtual void `[`PublishIsSubmerged`](#classuuv__simulator__ros_1_1_underwater_object_r_o_s_plugin_1afa9d2c09358d243270ee454905dcdb23)`()` | Publishes the state of the vehicle (is submerged)

## Members

#### `public  `[`UnderwaterObjectROSPlugin`](#classuuv__simulator__ros_1_1_underwater_object_r_o_s_plugin_1a6d26a8a5c08e79c0a149a07cf61209e0)`()` 

Constructor.

#### `public virtual  `[`~UnderwaterObjectROSPlugin`](#classuuv__simulator__ros_1_1_underwater_object_r_o_s_plugin_1ae1eb17f91cb1383400138b6ef241a06f)`()` 

Destructor.

#### `public void `[`Load`](#classuuv__simulator__ros_1_1_underwater_object_r_o_s_plugin_1a86c5be6309611c623757fca4565051c9)`(gazebo::physics::ModelPtr _parent,sdf::ElementPtr _sdf)` 

Load module and read parameters from SDF.

#### `public virtual void `[`Init`](#classuuv__simulator__ros_1_1_underwater_object_r_o_s_plugin_1a3401922bc6e94cfcb5db27a99d2e4f0a)`()` 

Initialize Module.

#### `public virtual void `[`Reset`](#classuuv__simulator__ros_1_1_underwater_object_r_o_s_plugin_1ae0316192f5b26fa321f3e64dd46287b7)`()` 

Reset Module.

#### `public virtual void `[`Update`](#classuuv__simulator__ros_1_1_underwater_object_r_o_s_plugin_1a8f81a22f771bc1203365de1438452e7a)`(const gazebo::common::UpdateInfo & _info)` 

Update the simulation state.

#### Parameters
* `_info` Information used in the update event.

#### `public void `[`UpdateLocalCurrentVelocity`](#classuuv__simulator__ros_1_1_underwater_object_r_o_s_plugin_1a8796c2736835dc203cb7f9c7e84a923e)`(const geometry_msgs::Vector3::ConstPtr & _msg)` 

Update the local current velocity, this data will be used only if the useGlobalCurrent flag is set to false.

#### `public bool `[`SetUseGlobalCurrentVel`](#classuuv__simulator__ros_1_1_underwater_object_r_o_s_plugin_1a038402f422a3940e426eec798f6a0d39)`(uuv_gazebo_ros_plugins_msgs::SetUseGlobalCurrentVel::Request & _req,uuv_gazebo_ros_plugins_msgs::SetUseGlobalCurrentVel::Response & _res)` 

Set flag to use the global current velocity topic input.

#### `public bool `[`GetModelProperties`](#classuuv__simulator__ros_1_1_underwater_object_r_o_s_plugin_1a36c121c67de5ba30cd0770fc9b60ea26)`(uuv_gazebo_ros_plugins_msgs::GetModelProperties::Request & _req,uuv_gazebo_ros_plugins_msgs::GetModelProperties::Response & _res)` 

Return the model properties, along with parameters from the hydrodynamic and hydrostatic models.

#### `public bool `[`SetScalingAddedMass`](#classuuv__simulator__ros_1_1_underwater_object_r_o_s_plugin_1a5d6cd010fa2f18ae91147c03ee9d1408)`(uuv_gazebo_ros_plugins_msgs::SetFloat::Request & _req,uuv_gazebo_ros_plugins_msgs::SetFloat::Response & _res)` 

Set the scaling factor for the added-mass matrix.

#### `public bool `[`GetScalingAddedMass`](#classuuv__simulator__ros_1_1_underwater_object_r_o_s_plugin_1ad8ee29496336a958fa59c6fc35026729)`(uuv_gazebo_ros_plugins_msgs::GetFloat::Request & _req,uuv_gazebo_ros_plugins_msgs::GetFloat::Response & _res)` 

Return current scaling factor for the added-mass matrix.

#### `public bool `[`SetScalingDamping`](#classuuv__simulator__ros_1_1_underwater_object_r_o_s_plugin_1a67861c1e99ee10a9c64f96d6401b221d)`(uuv_gazebo_ros_plugins_msgs::SetFloat::Request & _req,uuv_gazebo_ros_plugins_msgs::SetFloat::Response & _res)` 

Set a scaling factor for the overall damping matrix.

#### `public bool `[`GetScalingDamping`](#classuuv__simulator__ros_1_1_underwater_object_r_o_s_plugin_1adc480b2b52d0da8a9c1d1b700d7bacd6)`(uuv_gazebo_ros_plugins_msgs::GetFloat::Request & _req,uuv_gazebo_ros_plugins_msgs::GetFloat::Response & _res)` 

Return the scaling factor for the overall damping matrix.

#### `public bool `[`SetScalingVolume`](#classuuv__simulator__ros_1_1_underwater_object_r_o_s_plugin_1a2569924791d708d8d879c0fec853b5f4)`(uuv_gazebo_ros_plugins_msgs::SetFloat::Request & _req,uuv_gazebo_ros_plugins_msgs::SetFloat::Response & _res)` 

Set scaling factor for the model's volume used for buoyancy force computation.

#### `public bool `[`GetScalingVolume`](#classuuv__simulator__ros_1_1_underwater_object_r_o_s_plugin_1a9eb2881a288725f83c9924b7be498c81)`(uuv_gazebo_ros_plugins_msgs::GetFloat::Request & _req,uuv_gazebo_ros_plugins_msgs::GetFloat::Response & _res)` 

Get scaling factor for the model's volume used for buoyancy force computation.

#### `public bool `[`SetFluidDensity`](#classuuv__simulator__ros_1_1_underwater_object_r_o_s_plugin_1ac254edcbd59acb26fd70b70acad679c9)`(uuv_gazebo_ros_plugins_msgs::SetFloat::Request & _req,uuv_gazebo_ros_plugins_msgs::SetFloat::Response & _res)` 

Set new fluid density (this will alter the value for the buoyancy force)

#### `public bool `[`GetFluidDensity`](#classuuv__simulator__ros_1_1_underwater_object_r_o_s_plugin_1a92c568850087edd355359e967f42d966)`(uuv_gazebo_ros_plugins_msgs::GetFloat::Request & _req,uuv_gazebo_ros_plugins_msgs::GetFloat::Response & _res)` 

Get current value for the fluid density.

#### `public bool `[`SetOffsetVolume`](#classuuv__simulator__ros_1_1_underwater_object_r_o_s_plugin_1a473e7dae4ba36e061389cf4d193ce80d)`(uuv_gazebo_ros_plugins_msgs::SetFloat::Request & _req,uuv_gazebo_ros_plugins_msgs::SetFloat::Response & _res)` 

Set offset factor for the model's volume (this will alter the value for the buoyancy force)

#### `public bool `[`GetOffsetVolume`](#classuuv__simulator__ros_1_1_underwater_object_r_o_s_plugin_1a70d64b6da3a18257bb1b4b1edc9afb3b)`(uuv_gazebo_ros_plugins_msgs::GetFloat::Request & _req,uuv_gazebo_ros_plugins_msgs::GetFloat::Response & _res)` 

Return the offset factor for the model's volume.

#### `public bool `[`SetOffsetAddedMass`](#classuuv__simulator__ros_1_1_underwater_object_r_o_s_plugin_1ae062c4867e24ba3daf56032728fb3e9a)`(uuv_gazebo_ros_plugins_msgs::SetFloat::Request & _req,uuv_gazebo_ros_plugins_msgs::SetFloat::Response & _res)` 

Set the offset factor for the added-mass matrix.

#### `public bool `[`GetOffsetAddedMass`](#classuuv__simulator__ros_1_1_underwater_object_r_o_s_plugin_1a317123306ae032c3cfb408553ed0706c)`(uuv_gazebo_ros_plugins_msgs::GetFloat::Request & _req,uuv_gazebo_ros_plugins_msgs::GetFloat::Response & _res)` 

Return the offset factor for the added-mass matrix.

#### `public bool `[`SetOffsetLinearDamping`](#classuuv__simulator__ros_1_1_underwater_object_r_o_s_plugin_1a9b3127ae45a4972927bd7becc61a4cf4)`(uuv_gazebo_ros_plugins_msgs::SetFloat::Request & _req,uuv_gazebo_ros_plugins_msgs::SetFloat::Response & _res)` 

Set the offset factor for the linear damping matrix.

#### `public bool `[`GetOffsetLinearDamping`](#classuuv__simulator__ros_1_1_underwater_object_r_o_s_plugin_1a979a847fb03c318d23809ef7e516f980)`(uuv_gazebo_ros_plugins_msgs::GetFloat::Request & _req,uuv_gazebo_ros_plugins_msgs::GetFloat::Response & _res)` 

Return the offset factor for the linear damping matrix.

#### `public bool `[`SetOffsetLinearForwardSpeedDamping`](#classuuv__simulator__ros_1_1_underwater_object_r_o_s_plugin_1a85a1221c40202088731e56f1d7736bf1)`(uuv_gazebo_ros_plugins_msgs::SetFloat::Request & _req,uuv_gazebo_ros_plugins_msgs::SetFloat::Response & _res)` 

Set the offset factor for the linear forward speed damping matrix.

#### `public bool `[`GetOffsetLinearForwardSpeedDamping`](#classuuv__simulator__ros_1_1_underwater_object_r_o_s_plugin_1a8c63d709fc992f899ffbe1eced7b6cd8)`(uuv_gazebo_ros_plugins_msgs::GetFloat::Request & _req,uuv_gazebo_ros_plugins_msgs::GetFloat::Response & _res)` 

Return the offset factor for the linear forward speed damping matrix.

#### `public bool `[`SetOffsetNonLinearDamping`](#classuuv__simulator__ros_1_1_underwater_object_r_o_s_plugin_1a972ab56e380c00dcc489c0d9e9a4d0de)`(uuv_gazebo_ros_plugins_msgs::SetFloat::Request & _req,uuv_gazebo_ros_plugins_msgs::SetFloat::Response & _res)` 

Set the offset factor for the nonlinear damping matrix.

#### `public bool `[`GetOffsetNonLinearDamping`](#classuuv__simulator__ros_1_1_underwater_object_r_o_s_plugin_1abc734c754de497bf62b13de980649f70)`(uuv_gazebo_ros_plugins_msgs::GetFloat::Request & _req,uuv_gazebo_ros_plugins_msgs::GetFloat::Response & _res)` 

Return the offset factor for the nonlinear damping matrix.

#### `protected virtual void `[`PublishRestoringForce`](#classuuv__simulator__ros_1_1_underwater_object_r_o_s_plugin_1adf2dd5f72380c281f9176bd0e4e98f59)`(gazebo::physics::LinkPtr _link)` 

Publish restoring force.

#### Parameters
* `_link` Pointer to the link where the force information will be extracted from

#### `protected virtual void `[`PublishHydrodynamicWrenches`](#classuuv__simulator__ros_1_1_underwater_object_r_o_s_plugin_1a22cd26dfdc7d64c8fa3b0a8d5ac40682)`(gazebo::physics::LinkPtr _link)` 

Publish hydrodynamic wrenches.

#### Parameters
* `_link` Pointer to the link where the force information will be extracted from

#### `protected virtual void `[`GenWrenchMsg`](#classuuv__simulator__ros_1_1_underwater_object_r_o_s_plugin_1a62b50fa4ff5d5b36b78a2160bad1d500)`(ignition::math::Vector3d _force,ignition::math::Vector3d _torque,geometry_msgs::WrenchStamped & _output)` 

Returns the wrench message for debugging topics.

#### Parameters
* `_force` Force vector 

* `_torque` Torque vector 

* `_output` Stamped wrench message to be updated

#### `protected virtual void `[`InitDebug`](#classuuv__simulator__ros_1_1_underwater_object_r_o_s_plugin_1a5dbdc863b0902d14f77a3f31b585d0f8)`(gazebo::physics::LinkPtr _link,gazebo::HydrodynamicModelPtr _hydro)` 

Sets the topics used for publishing the intermediate data during the simulation.

#### Parameters
* `_link` Pointer to the link 

* `_hydro` Pointer to the hydrodynamic model

#### `protected virtual void `[`PublishCurrentVelocityMarker`](#classuuv__simulator__ros_1_1_underwater_object_r_o_s_plugin_1ae2defd15b338fe56edbbc87bfe364b6c)`()` 

Publishes the current velocity marker.

#### `protected virtual void `[`PublishIsSubmerged`](#classuuv__simulator__ros_1_1_underwater_object_r_o_s_plugin_1afa9d2c09358d243270ee454905dcdb23)`()` 

Publishes the state of the vehicle (is submerged)

Generated by [Moxygen](https://sourcey.com/moxygen)