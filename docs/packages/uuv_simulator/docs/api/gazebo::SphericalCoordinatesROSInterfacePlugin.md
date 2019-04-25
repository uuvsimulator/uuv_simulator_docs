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

