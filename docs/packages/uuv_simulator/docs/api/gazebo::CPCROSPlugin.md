# class `gazebo::CPCROSPlugin` 

```
class gazebo::CPCROSPlugin
  : public gazebo::ROSBaseModelPlugin
```  

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public  `[`CPCROSPlugin`](#classgazebo_1_1_c_p_c_r_o_s_plugin_1abf89ec7c696e6b8e951d4de445ac48b0)`()` | Class constructor.
`public virtual  `[`~CPCROSPlugin`](#classgazebo_1_1_c_p_c_r_o_s_plugin_1a7343db5b061ebc15862d08845df1f5fd)`()` | Class destructor.
`public virtual void `[`Load`](#classgazebo_1_1_c_p_c_r_o_s_plugin_1a03283b375faba8649fa76a1a91b3540c)`(physics::ModelPtr _model,sdf::ElementPtr _sdf)` | Load the plugin.
`protected ros::Subscriber `[`particlesSub`](#classgazebo_1_1_c_p_c_r_o_s_plugin_1ae3fc2556d76aff734f95ecd211603dae) | Input topic for the plume particle point cloud.
`protected ros::Publisher `[`salinityPub`](#classgazebo_1_1_c_p_c_r_o_s_plugin_1aa583d13a2ea37a2551e4aec472a41242) | Output topic for salinity measurements based on the particle concentration.
`protected bool `[`updatingCloud`](#classgazebo_1_1_c_p_c_r_o_s_plugin_1ac796aa57d93c2e9d389631b1734b8732) | Flag to ensure the cloud and measurement update don't coincide.
`protected double `[`gamma`](#classgazebo_1_1_c_p_c_r_o_s_plugin_1a36f263fa3d261cee3f0521bb5aa2aadb) | Gamma velocity parameter for the smoothing function.
`protected double `[`gain`](#classgazebo_1_1_c_p_c_r_o_s_plugin_1afb382bc909b25221287384e58b5016ad) | Sensor gain.
`protected double `[`smoothingLength`](#classgazebo_1_1_c_p_c_r_o_s_plugin_1ab6ef0ff9f9bf89717618d2a6714de9a7) | 
`protected ros::Time `[`lastUpdateTimestamp`](#classgazebo_1_1_c_p_c_r_o_s_plugin_1a1fbc82365f09bd32d5122daf77a5252d) | Last update from the point cloud callback.
`protected uuv_sensor_ros_plugins_msgs::ChemicalParticleConcentration `[`outputMsg`](#classgazebo_1_1_c_p_c_r_o_s_plugin_1a5728f434aa04158487bb9b7028cb6c3e) | Output measurement topic.
`protected uuv_sensor_ros_plugins_msgs::Salinity `[`salinityMsg`](#classgazebo_1_1_c_p_c_r_o_s_plugin_1a1b752dffdf6538176fbdded30afe972e) | Output salinity measurement message.
`protected double `[`waterSalinityValue`](#classgazebo_1_1_c_p_c_r_o_s_plugin_1af826cad9b0845aa89b389ab9d05a8b44) | 
`protected double `[`plumeSalinityValue`](#classgazebo_1_1_c_p_c_r_o_s_plugin_1a503041ce7db678b30bf7da4fa4c2a02a) | 
`protected virtual bool `[`OnUpdate`](#classgazebo_1_1_c_p_c_r_o_s_plugin_1a40020feac24af0035cc376c00fb9d755)`(const common::UpdateInfo & _info)` | Update sensor measurement.
`protected virtual void `[`OnPlumeParticlesUpdate`](#classgazebo_1_1_c_p_c_r_o_s_plugin_1a4df41586ec6bca66f1b9cc6b1f80af73)`(const sensor_msgs::PointCloud::ConstPtr & _msg)` | Update callback from simulator.

## Members

#### `public  `[`CPCROSPlugin`](#classgazebo_1_1_c_p_c_r_o_s_plugin_1abf89ec7c696e6b8e951d4de445ac48b0)`()` 

Class constructor.

#### `public virtual  `[`~CPCROSPlugin`](#classgazebo_1_1_c_p_c_r_o_s_plugin_1a7343db5b061ebc15862d08845df1f5fd)`()` 

Class destructor.

#### `public virtual void `[`Load`](#classgazebo_1_1_c_p_c_r_o_s_plugin_1a03283b375faba8649fa76a1a91b3540c)`(physics::ModelPtr _model,sdf::ElementPtr _sdf)` 

Load the plugin.

#### `protected ros::Subscriber `[`particlesSub`](#classgazebo_1_1_c_p_c_r_o_s_plugin_1ae3fc2556d76aff734f95ecd211603dae) 

Input topic for the plume particle point cloud.

#### `protected ros::Publisher `[`salinityPub`](#classgazebo_1_1_c_p_c_r_o_s_plugin_1aa583d13a2ea37a2551e4aec472a41242) 

Output topic for salinity measurements based on the particle concentration.

#### `protected bool `[`updatingCloud`](#classgazebo_1_1_c_p_c_r_o_s_plugin_1ac796aa57d93c2e9d389631b1734b8732) 

Flag to ensure the cloud and measurement update don't coincide.

#### `protected double `[`gamma`](#classgazebo_1_1_c_p_c_r_o_s_plugin_1a36f263fa3d261cee3f0521bb5aa2aadb) 

Gamma velocity parameter for the smoothing function.

#### `protected double `[`gain`](#classgazebo_1_1_c_p_c_r_o_s_plugin_1afb382bc909b25221287384e58b5016ad) 

Sensor gain.

#### `protected double `[`smoothingLength`](#classgazebo_1_1_c_p_c_r_o_s_plugin_1ab6ef0ff9f9bf89717618d2a6714de9a7) 

#### `protected ros::Time `[`lastUpdateTimestamp`](#classgazebo_1_1_c_p_c_r_o_s_plugin_1a1fbc82365f09bd32d5122daf77a5252d) 

Last update from the point cloud callback.

#### `protected uuv_sensor_ros_plugins_msgs::ChemicalParticleConcentration `[`outputMsg`](#classgazebo_1_1_c_p_c_r_o_s_plugin_1a5728f434aa04158487bb9b7028cb6c3e) 

Output measurement topic.

#### `protected uuv_sensor_ros_plugins_msgs::Salinity `[`salinityMsg`](#classgazebo_1_1_c_p_c_r_o_s_plugin_1a1b752dffdf6538176fbdded30afe972e) 

Output salinity measurement message.

#### `protected double `[`waterSalinityValue`](#classgazebo_1_1_c_p_c_r_o_s_plugin_1af826cad9b0845aa89b389ab9d05a8b44) 

#### `protected double `[`plumeSalinityValue`](#classgazebo_1_1_c_p_c_r_o_s_plugin_1a503041ce7db678b30bf7da4fa4c2a02a) 

#### `protected virtual bool `[`OnUpdate`](#classgazebo_1_1_c_p_c_r_o_s_plugin_1a40020feac24af0035cc376c00fb9d755)`(const common::UpdateInfo & _info)` 

Update sensor measurement.

#### `protected virtual void `[`OnPlumeParticlesUpdate`](#classgazebo_1_1_c_p_c_r_o_s_plugin_1a4df41586ec6bca66f1b9cc6b1f80af73)`(const sensor_msgs::PointCloud::ConstPtr & _msg)` 

Update callback from simulator.

