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

