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

