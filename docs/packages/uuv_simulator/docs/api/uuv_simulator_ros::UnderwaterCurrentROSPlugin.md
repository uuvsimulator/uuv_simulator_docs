# class `uuv_simulator_ros::UnderwaterCurrentROSPlugin` 

```
class uuv_simulator_ros::UnderwaterCurrentROSPlugin
  : public UnderwaterCurrentPlugin
```  

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public  `[`UnderwaterCurrentROSPlugin`](#classuuv__simulator__ros_1_1_underwater_current_r_o_s_plugin_1a495903eb436982545dffaaf2ef685877)`()` | Class constructor.
`public virtual  `[`~UnderwaterCurrentROSPlugin`](#classuuv__simulator__ros_1_1_underwater_current_r_o_s_plugin_1a144781a36c5f5df6f71ffc43fc0a8eb1)`()` | Class destructor.
`public void `[`Load`](#classuuv__simulator__ros_1_1_underwater_current_r_o_s_plugin_1a1a5b927b9afa3ad9e0ec3f37e47e4f67)`(gazebo::physics::WorldPtr _world,sdf::ElementPtr _sdf)` | Load module and read parameters from SDF.
`public bool `[`UpdateCurrentVelocityModel`](#classuuv__simulator__ros_1_1_underwater_current_r_o_s_plugin_1a703a1f33b7ba4a12bc337d01c923050c)`(uuv_world_ros_plugins_msgs::SetCurrentModel::Request & _req,uuv_world_ros_plugins_msgs::SetCurrentModel::Response & _res)` | Service call to update the parameters for the velocity Gauss-Markov process model.
`public bool `[`UpdateCurrentHorzAngleModel`](#classuuv__simulator__ros_1_1_underwater_current_r_o_s_plugin_1aa023f81b677c1599224b5cb61d2a998c)`(uuv_world_ros_plugins_msgs::SetCurrentModel::Request & _req,uuv_world_ros_plugins_msgs::SetCurrentModel::Response & _res)` | Service call to update the parameters for the horizontal angle Gauss-Markov process model.
`public bool `[`UpdateCurrentVertAngleModel`](#classuuv__simulator__ros_1_1_underwater_current_r_o_s_plugin_1a027e73b225b807cb2dc75baf1de9ec8c)`(uuv_world_ros_plugins_msgs::SetCurrentModel::Request & _req,uuv_world_ros_plugins_msgs::SetCurrentModel::Response & _res)` | Service call to update the parameters for the vertical angle Gauss-Markov process model.
`public bool `[`GetCurrentVelocityModel`](#classuuv__simulator__ros_1_1_underwater_current_r_o_s_plugin_1a0063203dbdd0ff00cc0b9dd36cb6c203)`(uuv_world_ros_plugins_msgs::GetCurrentModel::Request & _req,uuv_world_ros_plugins_msgs::GetCurrentModel::Response & _res)` | Service call to read the parameters for the velocity Gauss-Markov process model.
`public bool `[`GetCurrentHorzAngleModel`](#classuuv__simulator__ros_1_1_underwater_current_r_o_s_plugin_1ac122dcc0b978614443ae85a7cf3e071c)`(uuv_world_ros_plugins_msgs::GetCurrentModel::Request & _req,uuv_world_ros_plugins_msgs::GetCurrentModel::Response & _res)` | Service call to read the parameters for the horizontal angle Gauss-Markov process model.
`public bool `[`GetCurrentVertAngleModel`](#classuuv__simulator__ros_1_1_underwater_current_r_o_s_plugin_1a6ca3823687f0c1bf3cf7b32cc9e7f438)`(uuv_world_ros_plugins_msgs::GetCurrentModel::Request & _req,uuv_world_ros_plugins_msgs::GetCurrentModel::Response & _res)` | Service call to read the parameters for the vertical angle Gauss-Markov process model.
`public bool `[`UpdateCurrentVelocity`](#classuuv__simulator__ros_1_1_underwater_current_r_o_s_plugin_1a77152a67d11a9185b0caf2455afd5ce0)`(uuv_world_ros_plugins_msgs::SetCurrentVelocity::Request & _req,uuv_world_ros_plugins_msgs::SetCurrentVelocity::Response & _res)` | Service call to update the mean value of the flow velocity.
`public bool `[`UpdateHorzAngle`](#classuuv__simulator__ros_1_1_underwater_current_r_o_s_plugin_1ac0970ebff612f9682e833ad289698845)`(uuv_world_ros_plugins_msgs::SetCurrentDirection::Request & _req,uuv_world_ros_plugins_msgs::SetCurrentDirection::Response & _res)` | Service call to update the mean value of the horizontal angle.
`public bool `[`UpdateVertAngle`](#classuuv__simulator__ros_1_1_underwater_current_r_o_s_plugin_1ac1eabcb153dd2252519826766ac68252)`(uuv_world_ros_plugins_msgs::SetCurrentDirection::Request & _req,uuv_world_ros_plugins_msgs::SetCurrentDirection::Response & _res)` | Service call to update the mean value of the vertical angle.

## Members

#### `public  `[`UnderwaterCurrentROSPlugin`](#classuuv__simulator__ros_1_1_underwater_current_r_o_s_plugin_1a495903eb436982545dffaaf2ef685877)`()` 

Class constructor.

#### `public virtual  `[`~UnderwaterCurrentROSPlugin`](#classuuv__simulator__ros_1_1_underwater_current_r_o_s_plugin_1a144781a36c5f5df6f71ffc43fc0a8eb1)`()` 

Class destructor.

#### `public void `[`Load`](#classuuv__simulator__ros_1_1_underwater_current_r_o_s_plugin_1a1a5b927b9afa3ad9e0ec3f37e47e4f67)`(gazebo::physics::WorldPtr _world,sdf::ElementPtr _sdf)` 

Load module and read parameters from SDF.

#### `public bool `[`UpdateCurrentVelocityModel`](#classuuv__simulator__ros_1_1_underwater_current_r_o_s_plugin_1a703a1f33b7ba4a12bc337d01c923050c)`(uuv_world_ros_plugins_msgs::SetCurrentModel::Request & _req,uuv_world_ros_plugins_msgs::SetCurrentModel::Response & _res)` 

Service call to update the parameters for the velocity Gauss-Markov process model.

#### `public bool `[`UpdateCurrentHorzAngleModel`](#classuuv__simulator__ros_1_1_underwater_current_r_o_s_plugin_1aa023f81b677c1599224b5cb61d2a998c)`(uuv_world_ros_plugins_msgs::SetCurrentModel::Request & _req,uuv_world_ros_plugins_msgs::SetCurrentModel::Response & _res)` 

Service call to update the parameters for the horizontal angle Gauss-Markov process model.

#### `public bool `[`UpdateCurrentVertAngleModel`](#classuuv__simulator__ros_1_1_underwater_current_r_o_s_plugin_1a027e73b225b807cb2dc75baf1de9ec8c)`(uuv_world_ros_plugins_msgs::SetCurrentModel::Request & _req,uuv_world_ros_plugins_msgs::SetCurrentModel::Response & _res)` 

Service call to update the parameters for the vertical angle Gauss-Markov process model.

#### `public bool `[`GetCurrentVelocityModel`](#classuuv__simulator__ros_1_1_underwater_current_r_o_s_plugin_1a0063203dbdd0ff00cc0b9dd36cb6c203)`(uuv_world_ros_plugins_msgs::GetCurrentModel::Request & _req,uuv_world_ros_plugins_msgs::GetCurrentModel::Response & _res)` 

Service call to read the parameters for the velocity Gauss-Markov process model.

#### `public bool `[`GetCurrentHorzAngleModel`](#classuuv__simulator__ros_1_1_underwater_current_r_o_s_plugin_1ac122dcc0b978614443ae85a7cf3e071c)`(uuv_world_ros_plugins_msgs::GetCurrentModel::Request & _req,uuv_world_ros_plugins_msgs::GetCurrentModel::Response & _res)` 

Service call to read the parameters for the horizontal angle Gauss-Markov process model.

#### `public bool `[`GetCurrentVertAngleModel`](#classuuv__simulator__ros_1_1_underwater_current_r_o_s_plugin_1a6ca3823687f0c1bf3cf7b32cc9e7f438)`(uuv_world_ros_plugins_msgs::GetCurrentModel::Request & _req,uuv_world_ros_plugins_msgs::GetCurrentModel::Response & _res)` 

Service call to read the parameters for the vertical angle Gauss-Markov process model.

#### `public bool `[`UpdateCurrentVelocity`](#classuuv__simulator__ros_1_1_underwater_current_r_o_s_plugin_1a77152a67d11a9185b0caf2455afd5ce0)`(uuv_world_ros_plugins_msgs::SetCurrentVelocity::Request & _req,uuv_world_ros_plugins_msgs::SetCurrentVelocity::Response & _res)` 

Service call to update the mean value of the flow velocity.

#### `public bool `[`UpdateHorzAngle`](#classuuv__simulator__ros_1_1_underwater_current_r_o_s_plugin_1ac0970ebff612f9682e833ad289698845)`(uuv_world_ros_plugins_msgs::SetCurrentDirection::Request & _req,uuv_world_ros_plugins_msgs::SetCurrentDirection::Response & _res)` 

Service call to update the mean value of the horizontal angle.

#### `public bool `[`UpdateVertAngle`](#classuuv__simulator__ros_1_1_underwater_current_r_o_s_plugin_1ac1eabcb153dd2252519826766ac68252)`(uuv_world_ros_plugins_msgs::SetCurrentDirection::Request & _req,uuv_world_ros_plugins_msgs::SetCurrentDirection::Response & _res)` 

Service call to update the mean value of the vertical angle.

