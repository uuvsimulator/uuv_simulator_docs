# class `gazebo::PoseGTROSPlugin` 

```
class gazebo::PoseGTROSPlugin
  : public gazebo::ROSBaseModelPlugin
```  

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public  `[`PoseGTROSPlugin`](#classgazebo_1_1_pose_g_t_r_o_s_plugin_1a7abaecb1897e10ef38f5c5263950a730)`()` | Class constructor.
`public  `[`~PoseGTROSPlugin`](#classgazebo_1_1_pose_g_t_r_o_s_plugin_1a448aa8217a27d318a9a79a7e7a917e5e)`()` | Class destructor.
`public virtual void `[`Load`](#classgazebo_1_1_pose_g_t_r_o_s_plugin_1a4c7e55e320c5619ea3d0b09d9760e2e1)`(physics::ModelPtr _model,sdf::ElementPtr _sdf)` | Load the plugin.
`protected ros::Publisher `[`nedOdomPub`](#classgazebo_1_1_pose_g_t_r_o_s_plugin_1aa55d65fca015d905281a5b69628c495f) | 
`protected ignition::math::Pose3d `[`offset`](#classgazebo_1_1_pose_g_t_r_o_s_plugin_1ad4c38844932e1e6a64007d3748cff494) | Pose offset.
`protected std::string `[`nedFrameID`](#classgazebo_1_1_pose_g_t_r_o_s_plugin_1a7f84ad70de3354b002b6327e7a0ecf7e) | 
`protected ignition::math::Pose3d `[`nedTransform`](#classgazebo_1_1_pose_g_t_r_o_s_plugin_1a594808116873fcad831599977614bd3f) | 
`protected bool `[`nedTransformIsInit`](#classgazebo_1_1_pose_g_t_r_o_s_plugin_1a0e2710fa47f04bc4b9d25d1627e3bbef) | 
`protected bool `[`publishNEDOdom`](#classgazebo_1_1_pose_g_t_r_o_s_plugin_1ad3c7c125394996b330019c99a63d7cd6) | 
`protected tf2_ros::Buffer `[`tfBuffer`](#classgazebo_1_1_pose_g_t_r_o_s_plugin_1add9cef7d74fe3ff0ed10da1b57788c64) | 
`protected boost::shared_ptr< tf2_ros::TransformListener > `[`tfListener`](#classgazebo_1_1_pose_g_t_r_o_s_plugin_1a3dc3aec17e8738157998914e32bc1acb) | 
`protected ignition::math::Vector3d `[`lastLinVel`](#classgazebo_1_1_pose_g_t_r_o_s_plugin_1a2ea18a63dfbff05817e762429c924e2d) | 
`protected ignition::math::Vector3d `[`lastAngVel`](#classgazebo_1_1_pose_g_t_r_o_s_plugin_1a77c7789e7eff6c351b68155fae3c72f7) | 
`protected ignition::math::Vector3d `[`linAcc`](#classgazebo_1_1_pose_g_t_r_o_s_plugin_1aea054e850fd2c5fd602b7f50497e6f1f) | 
`protected ignition::math::Vector3d `[`angAcc`](#classgazebo_1_1_pose_g_t_r_o_s_plugin_1a9e08e99ad4ba46d70c5e6f93815304f2) | 
`protected ignition::math::Vector3d `[`lastRefLinVel`](#classgazebo_1_1_pose_g_t_r_o_s_plugin_1ad148ae9dd9d04f5e5ee1408e7d790d76) | 
`protected ignition::math::Vector3d `[`lastRefAngVel`](#classgazebo_1_1_pose_g_t_r_o_s_plugin_1a734eee58528e7db340a35f8dd1bc2b11) | 
`protected ignition::math::Vector3d `[`refLinAcc`](#classgazebo_1_1_pose_g_t_r_o_s_plugin_1a003e8c587b2daacdc3fa77ba7591f07f) | 
`protected ignition::math::Vector3d `[`refAngAcc`](#classgazebo_1_1_pose_g_t_r_o_s_plugin_1a117b4dd179871a23bb91c2f3e6d61753) | 
`protected virtual bool `[`OnUpdate`](#classgazebo_1_1_pose_g_t_r_o_s_plugin_1a9b34da677b1f4b34d07fd02c4c44a8d2)`(const common::UpdateInfo & _info)` | Update sensor measurement.
`protected void `[`PublishNEDOdomMessage`](#classgazebo_1_1_pose_g_t_r_o_s_plugin_1a637b2ff059028539ec9f9c314482bd0f)`(common::Time _time,ignition::math::Pose3d _pose,ignition::math::Vector3d _linVel,ignition::math::Vector3d _angVel)` | 
`protected void `[`PublishOdomMessage`](#classgazebo_1_1_pose_g_t_r_o_s_plugin_1af9985dc3356397d382584c21bde650a6)`(common::Time _time,ignition::math::Pose3d _pose,ignition::math::Vector3d _linVel,ignition::math::Vector3d _angVel)` | 
`protected void `[`UpdateNEDTransform`](#classgazebo_1_1_pose_g_t_r_o_s_plugin_1af83bca7f0f2aee70389d6e88c7c597f6)`()` | 

## Members

#### `public  `[`PoseGTROSPlugin`](#classgazebo_1_1_pose_g_t_r_o_s_plugin_1a7abaecb1897e10ef38f5c5263950a730)`()` 

Class constructor.

#### `public  `[`~PoseGTROSPlugin`](#classgazebo_1_1_pose_g_t_r_o_s_plugin_1a448aa8217a27d318a9a79a7e7a917e5e)`()` 

Class destructor.

#### `public virtual void `[`Load`](#classgazebo_1_1_pose_g_t_r_o_s_plugin_1a4c7e55e320c5619ea3d0b09d9760e2e1)`(physics::ModelPtr _model,sdf::ElementPtr _sdf)` 

Load the plugin.

#### `protected ros::Publisher `[`nedOdomPub`](#classgazebo_1_1_pose_g_t_r_o_s_plugin_1aa55d65fca015d905281a5b69628c495f) 

#### `protected ignition::math::Pose3d `[`offset`](#classgazebo_1_1_pose_g_t_r_o_s_plugin_1ad4c38844932e1e6a64007d3748cff494) 

Pose offset.

#### `protected std::string `[`nedFrameID`](#classgazebo_1_1_pose_g_t_r_o_s_plugin_1a7f84ad70de3354b002b6327e7a0ecf7e) 

#### `protected ignition::math::Pose3d `[`nedTransform`](#classgazebo_1_1_pose_g_t_r_o_s_plugin_1a594808116873fcad831599977614bd3f) 

#### `protected bool `[`nedTransformIsInit`](#classgazebo_1_1_pose_g_t_r_o_s_plugin_1a0e2710fa47f04bc4b9d25d1627e3bbef) 

#### `protected bool `[`publishNEDOdom`](#classgazebo_1_1_pose_g_t_r_o_s_plugin_1ad3c7c125394996b330019c99a63d7cd6) 

#### `protected tf2_ros::Buffer `[`tfBuffer`](#classgazebo_1_1_pose_g_t_r_o_s_plugin_1add9cef7d74fe3ff0ed10da1b57788c64) 

#### `protected boost::shared_ptr< tf2_ros::TransformListener > `[`tfListener`](#classgazebo_1_1_pose_g_t_r_o_s_plugin_1a3dc3aec17e8738157998914e32bc1acb) 

#### `protected ignition::math::Vector3d `[`lastLinVel`](#classgazebo_1_1_pose_g_t_r_o_s_plugin_1a2ea18a63dfbff05817e762429c924e2d) 

#### `protected ignition::math::Vector3d `[`lastAngVel`](#classgazebo_1_1_pose_g_t_r_o_s_plugin_1a77c7789e7eff6c351b68155fae3c72f7) 

#### `protected ignition::math::Vector3d `[`linAcc`](#classgazebo_1_1_pose_g_t_r_o_s_plugin_1aea054e850fd2c5fd602b7f50497e6f1f) 

#### `protected ignition::math::Vector3d `[`angAcc`](#classgazebo_1_1_pose_g_t_r_o_s_plugin_1a9e08e99ad4ba46d70c5e6f93815304f2) 

#### `protected ignition::math::Vector3d `[`lastRefLinVel`](#classgazebo_1_1_pose_g_t_r_o_s_plugin_1ad148ae9dd9d04f5e5ee1408e7d790d76) 

#### `protected ignition::math::Vector3d `[`lastRefAngVel`](#classgazebo_1_1_pose_g_t_r_o_s_plugin_1a734eee58528e7db340a35f8dd1bc2b11) 

#### `protected ignition::math::Vector3d `[`refLinAcc`](#classgazebo_1_1_pose_g_t_r_o_s_plugin_1a003e8c587b2daacdc3fa77ba7591f07f) 

#### `protected ignition::math::Vector3d `[`refAngAcc`](#classgazebo_1_1_pose_g_t_r_o_s_plugin_1a117b4dd179871a23bb91c2f3e6d61753) 

#### `protected virtual bool `[`OnUpdate`](#classgazebo_1_1_pose_g_t_r_o_s_plugin_1a9b34da677b1f4b34d07fd02c4c44a8d2)`(const common::UpdateInfo & _info)` 

Update sensor measurement.

#### `protected void `[`PublishNEDOdomMessage`](#classgazebo_1_1_pose_g_t_r_o_s_plugin_1a637b2ff059028539ec9f9c314482bd0f)`(common::Time _time,ignition::math::Pose3d _pose,ignition::math::Vector3d _linVel,ignition::math::Vector3d _angVel)` 

#### `protected void `[`PublishOdomMessage`](#classgazebo_1_1_pose_g_t_r_o_s_plugin_1af9985dc3356397d382584c21bde650a6)`(common::Time _time,ignition::math::Pose3d _pose,ignition::math::Vector3d _linVel,ignition::math::Vector3d _angVel)` 

#### `protected void `[`UpdateNEDTransform`](#classgazebo_1_1_pose_g_t_r_o_s_plugin_1af83bca7f0f2aee70389d6e88c7c597f6)`()` 

