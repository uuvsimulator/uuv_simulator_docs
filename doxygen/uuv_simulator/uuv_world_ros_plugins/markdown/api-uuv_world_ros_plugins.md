# Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`namespace `[`gazebo`](#namespacegazebo) | 
`namespace `[`uuv_simulator_ros`](#namespaceuuv__simulator__ros) | 

# namespace `gazebo` 

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`class `[`gazebo::SphericalCoordinatesROSInterfacePlugin`](#classgazebo_1_1_spherical_coordinates_r_o_s_interface_plugin) | 

# class `gazebo::SphericalCoordinatesROSInterfacePlugin` 

```
class gazebo::SphericalCoordinatesROSInterfacePlugin
  : public WorldPlugin
```  

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public  `[`SphericalCoordinatesROSInterfacePlugin`](#classgazebo_1_1_spherical_coordinates_r_o_s_interface_plugin_1a6bf1a00d18fac3a015684a1afc0820c3)`()` | Constructor.
`public virtual  `[`~SphericalCoordinatesROSInterfacePlugin`](#classgazebo_1_1_spherical_coordinates_r_o_s_interface_plugin_1a0ea8367ff22eeeac89fb5db34e2cde81)`()` | Destructor.
`public void `[`Load`](#classgazebo_1_1_spherical_coordinates_r_o_s_interface_plugin_1a8d0cef461af33093c256fdf1ccfd82c3)`(physics::WorldPtr _world,sdf::ElementPtr _sdf)` | Load module and read parameters from SDF.
`public bool `[`GetOriginSphericalCoord`](#classgazebo_1_1_spherical_coordinates_r_o_s_interface_plugin_1aa967b09744ddbe4072a4c8dc5e35a631)`(uuv_world_ros_plugins_msgs::GetOriginSphericalCoord::Request & _req,uuv_world_ros_plugins_msgs::GetOriginSphericalCoord::Response & _res)` | Service call that returns the origin in WGS84 standard.
`public bool `[`SetOriginSphericalCoord`](#classgazebo_1_1_spherical_coordinates_r_o_s_interface_plugin_1a0805453fc6658c5024cddf6907ca34bf)`(uuv_world_ros_plugins_msgs::SetOriginSphericalCoord::Request & _req,uuv_world_ros_plugins_msgs::SetOriginSphericalCoord::Response & _res)` | Service call that returns the origin in WGS84 standard.
`public bool `[`TransformToSphericalCoord`](#classgazebo_1_1_spherical_coordinates_r_o_s_interface_plugin_1a3e480b1393af8868ee975a7c32638ac0)`(uuv_world_ros_plugins_msgs::TransformToSphericalCoord::Request & _req,uuv_world_ros_plugins_msgs::TransformToSphericalCoord::Response & _res)` | Service call to transform from Cartesian to spherical coordinates.
`public bool `[`TransformFromSphericalCoord`](#classgazebo_1_1_spherical_coordinates_r_o_s_interface_plugin_1aa314576c573c750cf0d32b1191e86d03)`(uuv_world_ros_plugins_msgs::TransformFromSphericalCoord::Request & _req,uuv_world_ros_plugins_msgs::TransformFromSphericalCoord::Response & _res)` | Service call to transform from spherical to Cartesian coordinates.
`protected boost::scoped_ptr< ros::NodeHandle > `[`rosNode`](#classgazebo_1_1_spherical_coordinates_r_o_s_interface_plugin_1aea70e85edc45f5c16f6b4aa0deee4fc4) | Pointer to this ROS node's handle.
`protected event::ConnectionPtr `[`rosPublishConnection`](#classgazebo_1_1_spherical_coordinates_r_o_s_interface_plugin_1a7369e11fa96d90bfa45a24689869d719) | Connection for callbacks on update world.
`protected physics::WorldPtr `[`world`](#classgazebo_1_1_spherical_coordinates_r_o_s_interface_plugin_1a92dbd263f77ee75c67dfa8f7dbe7f45d) | Pointer to world.
`protected std::map< std::string, ros::ServiceServer > `[`worldServices`](#classgazebo_1_1_spherical_coordinates_r_o_s_interface_plugin_1a0f858a67ac5be296746f6b7075131261) | All underwater world services.

## Members

#### `public  `[`SphericalCoordinatesROSInterfacePlugin`](#classgazebo_1_1_spherical_coordinates_r_o_s_interface_plugin_1a6bf1a00d18fac3a015684a1afc0820c3)`()` 

Constructor.

#### `public virtual  `[`~SphericalCoordinatesROSInterfacePlugin`](#classgazebo_1_1_spherical_coordinates_r_o_s_interface_plugin_1a0ea8367ff22eeeac89fb5db34e2cde81)`()` 

Destructor.

#### `public void `[`Load`](#classgazebo_1_1_spherical_coordinates_r_o_s_interface_plugin_1a8d0cef461af33093c256fdf1ccfd82c3)`(physics::WorldPtr _world,sdf::ElementPtr _sdf)` 

Load module and read parameters from SDF.

#### `public bool `[`GetOriginSphericalCoord`](#classgazebo_1_1_spherical_coordinates_r_o_s_interface_plugin_1aa967b09744ddbe4072a4c8dc5e35a631)`(uuv_world_ros_plugins_msgs::GetOriginSphericalCoord::Request & _req,uuv_world_ros_plugins_msgs::GetOriginSphericalCoord::Response & _res)` 

Service call that returns the origin in WGS84 standard.

#### `public bool `[`SetOriginSphericalCoord`](#classgazebo_1_1_spherical_coordinates_r_o_s_interface_plugin_1a0805453fc6658c5024cddf6907ca34bf)`(uuv_world_ros_plugins_msgs::SetOriginSphericalCoord::Request & _req,uuv_world_ros_plugins_msgs::SetOriginSphericalCoord::Response & _res)` 

Service call that returns the origin in WGS84 standard.

#### `public bool `[`TransformToSphericalCoord`](#classgazebo_1_1_spherical_coordinates_r_o_s_interface_plugin_1a3e480b1393af8868ee975a7c32638ac0)`(uuv_world_ros_plugins_msgs::TransformToSphericalCoord::Request & _req,uuv_world_ros_plugins_msgs::TransformToSphericalCoord::Response & _res)` 

Service call to transform from Cartesian to spherical coordinates.

#### `public bool `[`TransformFromSphericalCoord`](#classgazebo_1_1_spherical_coordinates_r_o_s_interface_plugin_1aa314576c573c750cf0d32b1191e86d03)`(uuv_world_ros_plugins_msgs::TransformFromSphericalCoord::Request & _req,uuv_world_ros_plugins_msgs::TransformFromSphericalCoord::Response & _res)` 

Service call to transform from spherical to Cartesian coordinates.

#### `protected boost::scoped_ptr< ros::NodeHandle > `[`rosNode`](#classgazebo_1_1_spherical_coordinates_r_o_s_interface_plugin_1aea70e85edc45f5c16f6b4aa0deee4fc4) 

Pointer to this ROS node's handle.

#### `protected event::ConnectionPtr `[`rosPublishConnection`](#classgazebo_1_1_spherical_coordinates_r_o_s_interface_plugin_1a7369e11fa96d90bfa45a24689869d719) 

Connection for callbacks on update world.

#### `protected physics::WorldPtr `[`world`](#classgazebo_1_1_spherical_coordinates_r_o_s_interface_plugin_1a92dbd263f77ee75c67dfa8f7dbe7f45d) 

Pointer to world.

#### `protected std::map< std::string, ros::ServiceServer > `[`worldServices`](#classgazebo_1_1_spherical_coordinates_r_o_s_interface_plugin_1a0f858a67ac5be296746f6b7075131261) 

All underwater world services.

# namespace `uuv_simulator_ros` 

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`class `[`uuv_simulator_ros::UnderwaterCurrentROSPlugin`](#classuuv__simulator__ros_1_1_underwater_current_r_o_s_plugin) | 

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

Generated by [Moxygen](https://sourcey.com/moxygen)