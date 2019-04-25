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

