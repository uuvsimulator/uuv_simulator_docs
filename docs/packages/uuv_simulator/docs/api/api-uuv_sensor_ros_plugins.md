# Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`namespace `[`gazebo`](#namespacegazebo) | 
`class `[`FirstOrderFilter`](#class_first_order_filter) | 

# namespace `gazebo` 

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public template<>`  <br/>`bool `[`GetSDFParam`](#_common_8hh_1acd5769609414bbc3be35ee1457d0d417)`(sdf::ElementPtr sdf,const std::string & name,T & param,const T & default_value,const bool & verbose)`            | Obtains a parameter from sdf.
`class `[`gazebo::CPCROSPlugin`](#classgazebo_1_1_c_p_c_r_o_s_plugin) | 
`class `[`gazebo::DVLROSPlugin`](#classgazebo_1_1_d_v_l_r_o_s_plugin) | TODO: Modify computation of velocity using the beams.
`class `[`gazebo::GazeboRosImageSonar`](#classgazebo_1_1_gazebo_ros_image_sonar) | 
`class `[`gazebo::GPSROSPlugin`](#classgazebo_1_1_g_p_s_r_o_s_plugin) | 
`class `[`gazebo::IMUROSPlugin`](#classgazebo_1_1_i_m_u_r_o_s_plugin) | 
`class `[`gazebo::MagnetometerROSPlugin`](#classgazebo_1_1_magnetometer_r_o_s_plugin) | 
`class `[`gazebo::PoseGTROSPlugin`](#classgazebo_1_1_pose_g_t_r_o_s_plugin) | 
`class `[`gazebo::ROSBaseModelPlugin`](#classgazebo_1_1_r_o_s_base_model_plugin) | 
`class `[`gazebo::ROSBasePlugin`](#classgazebo_1_1_r_o_s_base_plugin) | 
`class `[`gazebo::ROSBaseSensorPlugin`](#classgazebo_1_1_r_o_s_base_sensor_plugin) | 
`class `[`gazebo::RPTROSPlugin`](#classgazebo_1_1_r_p_t_r_o_s_plugin) | 
`class `[`gazebo::SubseaPressureROSPlugin`](#classgazebo_1_1_subsea_pressure_r_o_s_plugin) | 
`class `[`gazebo::UnderwaterCameraROSPlugin`](#classgazebo_1_1_underwater_camera_r_o_s_plugin) | 
`struct `[`gazebo::IMUParameters`](#structgazebo_1_1_i_m_u_parameters) | [IMUParameters](#structgazebo_1_1_i_m_u_parameters) stores all IMU model parameters. A description of these parameters can be found here: [https://github.com/ethz-asl/kalibr/wiki/IMU-Noise-Model-and-Intrinsics](https://github.com/ethz-asl/kalibr/wiki/IMU-Noise-Model-and-Intrinsics).
`struct `[`gazebo::MagnetometerParameters`](#structgazebo_1_1_magnetometer_parameters) | 

## Members

#### `public template<>`  <br/>`bool `[`GetSDFParam`](#_common_8hh_1acd5769609414bbc3be35ee1457d0d417)`(sdf::ElementPtr sdf,const std::string & name,T & param,const T & default_value,const bool & verbose)` 

Obtains a parameter from sdf.

#### Parameters
* `sdf` Pointer to the sdf object. 

* `name` Name of the parameter. 

* `param` Param Variable to write the parameter to. 

* `default_value` Default value, if the parameter not available. 

* `verbose` If true, gzerror if the parameter is not available.

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

# class `gazebo::DVLROSPlugin` 

```
class gazebo::DVLROSPlugin
  : public gazebo::ROSBaseModelPlugin
```  

TODO: Modify computation of velocity using the beams.

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public  `[`DVLROSPlugin`](#classgazebo_1_1_d_v_l_r_o_s_plugin_1aad4cc11ec091d06a2be743656c7bbcce)`()` | Class constructor.
`public virtual  `[`~DVLROSPlugin`](#classgazebo_1_1_d_v_l_r_o_s_plugin_1a5941c8fe25d52a179799bb526dfd96de)`()` | Class destructor.
`public virtual void `[`Load`](#classgazebo_1_1_d_v_l_r_o_s_plugin_1ad64840822bab803a6f89d589fe6c0a9f)`(physics::ModelPtr _model,sdf::ElementPtr _sdf)` | Load the plugin.
`protected bool `[`beamTransformsInitialized`](#classgazebo_1_1_d_v_l_r_o_s_plugin_1a7b6d84d3d3ffcc2e54cf865ed6710cb1) | 
`protected double `[`altitude`](#classgazebo_1_1_d_v_l_r_o_s_plugin_1af131a2d137189651208e48467bdbad39) | Measured altitude in meters.
`protected uuv_sensor_ros_plugins_msgs::DVL `[`dvlROSMsg`](#classgazebo_1_1_d_v_l_r_o_s_plugin_1a81fb6aaf15da16ca61e98ef9794a0835) | ROS DVL message.
`protected std::vector< uuv_sensor_ros_plugins_msgs::DVLBeam > `[`dvlBeamMsgs`](#classgazebo_1_1_d_v_l_r_o_s_plugin_1a481fb7aadbe65df012fa2d19166a7d85) | 
`protected ros::Publisher `[`twistPub`](#classgazebo_1_1_d_v_l_r_o_s_plugin_1ac2f169c3c79a3514cfdf497ce6a74e2d) | ROS publisher for twist data.
`protected geometry_msgs::TwistWithCovarianceStamped `[`twistROSMsg`](#classgazebo_1_1_d_v_l_r_o_s_plugin_1afaaaa0dcc7b097b488f60b7098ff8ec5) | Store pose message since many attributes do not change (cov.).
`protected std::vector< std::string > `[`beamsLinkNames`](#classgazebo_1_1_d_v_l_r_o_s_plugin_1ad08e09dd6d967aa9a2696065213c3493) | List of beam links.
`protected std::vector< std::string > `[`beamTopics`](#classgazebo_1_1_d_v_l_r_o_s_plugin_1a4f5c496dc3d8efa87aadfa2f7d7b4c97) | List of beam topics.
`protected std::vector< ignition::math::Pose3d > `[`beamPoses`](#classgazebo_1_1_d_v_l_r_o_s_plugin_1ad8ac639cddfd52b709b8e77712c72762) | List of poses of each beam wrt to the DVL frame.
`protected boost::shared_ptr< message_filters::TimeSynchronizer< sensor_msgs::Range, sensor_msgs::Range, sensor_msgs::Range, sensor_msgs::Range > > `[`syncBeamMessages`](#classgazebo_1_1_d_v_l_r_o_s_plugin_1a2d14489a3859fa9174b3c5ec1476d3ed) | 
`protected boost::shared_ptr< message_filters::Subscriber< sensor_msgs::Range > > `[`beamSub0`](#classgazebo_1_1_d_v_l_r_o_s_plugin_1adf8fa77ac7f82dcd6171fdf8025983b7) | 
`protected boost::shared_ptr< message_filters::Subscriber< sensor_msgs::Range > > `[`beamSub1`](#classgazebo_1_1_d_v_l_r_o_s_plugin_1ac8deb87d1aa20d511770855840e985a4) | 
`protected boost::shared_ptr< message_filters::Subscriber< sensor_msgs::Range > > `[`beamSub2`](#classgazebo_1_1_d_v_l_r_o_s_plugin_1a9065bb4c8131a3df384cab8d986c8741) | 
`protected boost::shared_ptr< message_filters::Subscriber< sensor_msgs::Range > > `[`beamSub3`](#classgazebo_1_1_d_v_l_r_o_s_plugin_1a4dbd1c10241a9508b74ac95ba68a5b08) | 
`protected tf::TransformListener `[`transformListener`](#classgazebo_1_1_d_v_l_r_o_s_plugin_1adabd0c5f1f49b0aa1f893e5cda8a25c5) | 
`protected virtual bool `[`OnUpdate`](#classgazebo_1_1_d_v_l_r_o_s_plugin_1a2ce9099e6bd976d4d845bc9c16741125)`(const common::UpdateInfo & _info)` | Update sensor measurement.
`protected void `[`OnBeamCallback`](#classgazebo_1_1_d_v_l_r_o_s_plugin_1a6196f3792d05d27c197321fa760b6e0f)`(const sensor_msgs::RangeConstPtr & _range0,const sensor_msgs::RangeConstPtr & _range1,const sensor_msgs::RangeConstPtr & _range2,const sensor_msgs::RangeConstPtr & _range3)` | Get beam Range message update.
`protected bool `[`UpdateBeamTransforms`](#classgazebo_1_1_d_v_l_r_o_s_plugin_1aafc0126ca7732b8f01ca383dc3ace22f)`()` | Updates the poses of each beam wrt the DVL frame.

## Members

#### `public  `[`DVLROSPlugin`](#classgazebo_1_1_d_v_l_r_o_s_plugin_1aad4cc11ec091d06a2be743656c7bbcce)`()` 

Class constructor.

#### `public virtual  `[`~DVLROSPlugin`](#classgazebo_1_1_d_v_l_r_o_s_plugin_1a5941c8fe25d52a179799bb526dfd96de)`()` 

Class destructor.

#### `public virtual void `[`Load`](#classgazebo_1_1_d_v_l_r_o_s_plugin_1ad64840822bab803a6f89d589fe6c0a9f)`(physics::ModelPtr _model,sdf::ElementPtr _sdf)` 

Load the plugin.

#### `protected bool `[`beamTransformsInitialized`](#classgazebo_1_1_d_v_l_r_o_s_plugin_1a7b6d84d3d3ffcc2e54cf865ed6710cb1) 

#### `protected double `[`altitude`](#classgazebo_1_1_d_v_l_r_o_s_plugin_1af131a2d137189651208e48467bdbad39) 

Measured altitude in meters.

#### `protected uuv_sensor_ros_plugins_msgs::DVL `[`dvlROSMsg`](#classgazebo_1_1_d_v_l_r_o_s_plugin_1a81fb6aaf15da16ca61e98ef9794a0835) 

ROS DVL message.

#### `protected std::vector< uuv_sensor_ros_plugins_msgs::DVLBeam > `[`dvlBeamMsgs`](#classgazebo_1_1_d_v_l_r_o_s_plugin_1a481fb7aadbe65df012fa2d19166a7d85) 

#### `protected ros::Publisher `[`twistPub`](#classgazebo_1_1_d_v_l_r_o_s_plugin_1ac2f169c3c79a3514cfdf497ce6a74e2d) 

ROS publisher for twist data.

#### `protected geometry_msgs::TwistWithCovarianceStamped `[`twistROSMsg`](#classgazebo_1_1_d_v_l_r_o_s_plugin_1afaaaa0dcc7b097b488f60b7098ff8ec5) 

Store pose message since many attributes do not change (cov.).

#### `protected std::vector< std::string > `[`beamsLinkNames`](#classgazebo_1_1_d_v_l_r_o_s_plugin_1ad08e09dd6d967aa9a2696065213c3493) 

List of beam links.

#### `protected std::vector< std::string > `[`beamTopics`](#classgazebo_1_1_d_v_l_r_o_s_plugin_1a4f5c496dc3d8efa87aadfa2f7d7b4c97) 

List of beam topics.

#### `protected std::vector< ignition::math::Pose3d > `[`beamPoses`](#classgazebo_1_1_d_v_l_r_o_s_plugin_1ad8ac639cddfd52b709b8e77712c72762) 

List of poses of each beam wrt to the DVL frame.

#### `protected boost::shared_ptr< message_filters::TimeSynchronizer< sensor_msgs::Range, sensor_msgs::Range, sensor_msgs::Range, sensor_msgs::Range > > `[`syncBeamMessages`](#classgazebo_1_1_d_v_l_r_o_s_plugin_1a2d14489a3859fa9174b3c5ec1476d3ed) 

#### `protected boost::shared_ptr< message_filters::Subscriber< sensor_msgs::Range > > `[`beamSub0`](#classgazebo_1_1_d_v_l_r_o_s_plugin_1adf8fa77ac7f82dcd6171fdf8025983b7) 

#### `protected boost::shared_ptr< message_filters::Subscriber< sensor_msgs::Range > > `[`beamSub1`](#classgazebo_1_1_d_v_l_r_o_s_plugin_1ac8deb87d1aa20d511770855840e985a4) 

#### `protected boost::shared_ptr< message_filters::Subscriber< sensor_msgs::Range > > `[`beamSub2`](#classgazebo_1_1_d_v_l_r_o_s_plugin_1a9065bb4c8131a3df384cab8d986c8741) 

#### `protected boost::shared_ptr< message_filters::Subscriber< sensor_msgs::Range > > `[`beamSub3`](#classgazebo_1_1_d_v_l_r_o_s_plugin_1a4dbd1c10241a9508b74ac95ba68a5b08) 

#### `protected tf::TransformListener `[`transformListener`](#classgazebo_1_1_d_v_l_r_o_s_plugin_1adabd0c5f1f49b0aa1f893e5cda8a25c5) 

#### `protected virtual bool `[`OnUpdate`](#classgazebo_1_1_d_v_l_r_o_s_plugin_1a2ce9099e6bd976d4d845bc9c16741125)`(const common::UpdateInfo & _info)` 

Update sensor measurement.

#### `protected void `[`OnBeamCallback`](#classgazebo_1_1_d_v_l_r_o_s_plugin_1a6196f3792d05d27c197321fa760b6e0f)`(const sensor_msgs::RangeConstPtr & _range0,const sensor_msgs::RangeConstPtr & _range1,const sensor_msgs::RangeConstPtr & _range2,const sensor_msgs::RangeConstPtr & _range3)` 

Get beam Range message update.

#### `protected bool `[`UpdateBeamTransforms`](#classgazebo_1_1_d_v_l_r_o_s_plugin_1aafc0126ca7732b8f01ca383dc3ace22f)`()` 

Updates the poses of each beam wrt the DVL frame.

# class `gazebo::GazeboRosImageSonar` 

```
class gazebo::GazeboRosImageSonar
  : public SensorPlugin
  : private GazeboRosCameraUtils
```  

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public  `[`GazeboRosImageSonar`](#classgazebo_1_1_gazebo_ros_image_sonar_1a9fb946272527f8dff40658553986b0e4)`()` | Constructor.
`public  `[`~GazeboRosImageSonar`](#classgazebo_1_1_gazebo_ros_image_sonar_1a4db6c96c5b7844bbdc65cf50cf233be6)`()` | Destructor.
`public virtual void `[`Load`](#classgazebo_1_1_gazebo_ros_image_sonar_1a572dcea1d62a05f9f2ba2f278c7eb369)`(sensors::SensorPtr _parent,sdf::ElementPtr _sdf)` | Load the plugin.
`public virtual void `[`Advertise`](#classgazebo_1_1_gazebo_ros_image_sonar_1ab4d294c942ec9805d38b5ab651d79611)`()` | Advertise point cloud and depth image.
`protected ros::Publisher `[`depth_image_camera_info_pub_`](#classgazebo_1_1_gazebo_ros_image_sonar_1af5163cef4707acb546dc9975defc98dc) | 
`protected unsigned int `[`width`](#classgazebo_1_1_gazebo_ros_image_sonar_1a88da9dd6b15bc621dd949c18649db749) | 
`protected unsigned int `[`height`](#classgazebo_1_1_gazebo_ros_image_sonar_1aecb1e1936f2ede4f10b7739a2eda7079) | 
`protected unsigned int `[`depth`](#classgazebo_1_1_gazebo_ros_image_sonar_1a52b86e01dad173d75096c226b732858e) | 
`protected std::string `[`format`](#classgazebo_1_1_gazebo_ros_image_sonar_1a6a18cb1b4864f357afab29e25509a48a) | 
`protected cv::Mat `[`dist_matrix_`](#classgazebo_1_1_gazebo_ros_image_sonar_1a7597c8b023cef37ed021f8a2a18cd1c3) | 
`protected std::vector< std::vector< int > > `[`angle_range_indices_`](#classgazebo_1_1_gazebo_ros_image_sonar_1af1bd49503473a5d08cd3291782afef60) | 
`protected std::vector< int > `[`angle_nbr_indices_`](#classgazebo_1_1_gazebo_ros_image_sonar_1a3d5dc5e58d03bf4ac127b0596deff327) | 
`protected sensors::DepthCameraSensorPtr `[`parentSensor`](#classgazebo_1_1_gazebo_ros_image_sonar_1a1b65cb9b2e8a150a94a643052ddfe9e6) | 
`protected rendering::DepthCameraPtr `[`depthCamera`](#classgazebo_1_1_gazebo_ros_image_sonar_1a12b3ba852307631c5697dddd40d9d79b) | 
`protected virtual void `[`OnNewDepthFrame`](#classgazebo_1_1_gazebo_ros_image_sonar_1a8d42e68da5678b0a5cb85291790e5ddf)`(const float * _image,unsigned int _width,unsigned int _height,unsigned int _depth,const std::string & _format)` | Update the controller.
`protected virtual void `[`OnNewRGBPointCloud`](#classgazebo_1_1_gazebo_ros_image_sonar_1a38389595a6606d68a9c9d0c0203d4c7f)`(const float * _pcd,unsigned int _width,unsigned int _height,unsigned int _depth,const std::string & _format)` | Update the controller.
`protected virtual void `[`OnNewImageFrame`](#classgazebo_1_1_gazebo_ros_image_sonar_1a9dab1f74d823f6df56c384e6af18da22)`(const unsigned char * _image,unsigned int _width,unsigned int _height,unsigned int _depth,const std::string & _format)` | Update the controller.
`protected virtual void `[`PublishCameraInfo`](#classgazebo_1_1_gazebo_ros_image_sonar_1ae0b9b5f9320d9430c41ba208605b7c7e)`()` | 

## Members

#### `public  `[`GazeboRosImageSonar`](#classgazebo_1_1_gazebo_ros_image_sonar_1a9fb946272527f8dff40658553986b0e4)`()` 

Constructor.

#### Parameters
* `parent` The parent entity, must be a Model or a Sensor

#### `public  `[`~GazeboRosImageSonar`](#classgazebo_1_1_gazebo_ros_image_sonar_1a4db6c96c5b7844bbdc65cf50cf233be6)`()` 

Destructor.

#### `public virtual void `[`Load`](#classgazebo_1_1_gazebo_ros_image_sonar_1a572dcea1d62a05f9f2ba2f278c7eb369)`(sensors::SensorPtr _parent,sdf::ElementPtr _sdf)` 

Load the plugin.

#### Parameters
* `take` in SDF root element

#### `public virtual void `[`Advertise`](#classgazebo_1_1_gazebo_ros_image_sonar_1ab4d294c942ec9805d38b5ab651d79611)`()` 

Advertise point cloud and depth image.

#### `protected ros::Publisher `[`depth_image_camera_info_pub_`](#classgazebo_1_1_gazebo_ros_image_sonar_1af5163cef4707acb546dc9975defc98dc) 

#### `protected unsigned int `[`width`](#classgazebo_1_1_gazebo_ros_image_sonar_1a88da9dd6b15bc621dd949c18649db749) 

#### `protected unsigned int `[`height`](#classgazebo_1_1_gazebo_ros_image_sonar_1aecb1e1936f2ede4f10b7739a2eda7079) 

#### `protected unsigned int `[`depth`](#classgazebo_1_1_gazebo_ros_image_sonar_1a52b86e01dad173d75096c226b732858e) 

#### `protected std::string `[`format`](#classgazebo_1_1_gazebo_ros_image_sonar_1a6a18cb1b4864f357afab29e25509a48a) 

#### `protected cv::Mat `[`dist_matrix_`](#classgazebo_1_1_gazebo_ros_image_sonar_1a7597c8b023cef37ed021f8a2a18cd1c3) 

#### `protected std::vector< std::vector< int > > `[`angle_range_indices_`](#classgazebo_1_1_gazebo_ros_image_sonar_1af1bd49503473a5d08cd3291782afef60) 

#### `protected std::vector< int > `[`angle_nbr_indices_`](#classgazebo_1_1_gazebo_ros_image_sonar_1a3d5dc5e58d03bf4ac127b0596deff327) 

#### `protected sensors::DepthCameraSensorPtr `[`parentSensor`](#classgazebo_1_1_gazebo_ros_image_sonar_1a1b65cb9b2e8a150a94a643052ddfe9e6) 

#### `protected rendering::DepthCameraPtr `[`depthCamera`](#classgazebo_1_1_gazebo_ros_image_sonar_1a12b3ba852307631c5697dddd40d9d79b) 

#### `protected virtual void `[`OnNewDepthFrame`](#classgazebo_1_1_gazebo_ros_image_sonar_1a8d42e68da5678b0a5cb85291790e5ddf)`(const float * _image,unsigned int _width,unsigned int _height,unsigned int _depth,const std::string & _format)` 

Update the controller.

#### `protected virtual void `[`OnNewRGBPointCloud`](#classgazebo_1_1_gazebo_ros_image_sonar_1a38389595a6606d68a9c9d0c0203d4c7f)`(const float * _pcd,unsigned int _width,unsigned int _height,unsigned int _depth,const std::string & _format)` 

Update the controller.

#### `protected virtual void `[`OnNewImageFrame`](#classgazebo_1_1_gazebo_ros_image_sonar_1a9dab1f74d823f6df56c384e6af18da22)`(const unsigned char * _image,unsigned int _width,unsigned int _height,unsigned int _depth,const std::string & _format)` 

Update the controller.

#### `protected virtual void `[`PublishCameraInfo`](#classgazebo_1_1_gazebo_ros_image_sonar_1ae0b9b5f9320d9430c41ba208605b7c7e)`()` 

# class `gazebo::GPSROSPlugin` 

```
class gazebo::GPSROSPlugin
  : public gazebo::ROSBaseSensorPlugin
```  

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public  `[`GPSROSPlugin`](#classgazebo_1_1_g_p_s_r_o_s_plugin_1ab969180b479e77d98f8cb29e8c94b269)`()` | Class constructor.
`public virtual  `[`~GPSROSPlugin`](#classgazebo_1_1_g_p_s_r_o_s_plugin_1ae4a602032a43f1a3cc904fa4ff938fc3)`()` | Class destructor.
`public virtual void `[`Load`](#classgazebo_1_1_g_p_s_r_o_s_plugin_1ac59efd08373c7f691308609836a2a03d)`(sensors::SensorPtr _parent,sdf::ElementPtr _sdf)` | Load module and read parameters from SDF.
`public bool `[`OnUpdateGPS`](#classgazebo_1_1_g_p_s_r_o_s_plugin_1a255822b5790c6202d5ab5f3bca0eca8b)`()` | Update GPS ROS message.
`protected sensors::GpsSensorPtr `[`gazeboGPSSensor`](#classgazebo_1_1_g_p_s_r_o_s_plugin_1aaa97f3a5236f6c5d9914d042848f97d6) | Pointer to the parent sensor.
`protected sensor_msgs::NavSatFix `[`gpsMessage`](#classgazebo_1_1_g_p_s_r_o_s_plugin_1aa365281835351f7720482bd36611733d) | Output GPS ROS message.

## Members

#### `public  `[`GPSROSPlugin`](#classgazebo_1_1_g_p_s_r_o_s_plugin_1ab969180b479e77d98f8cb29e8c94b269)`()` 

Class constructor.

#### `public virtual  `[`~GPSROSPlugin`](#classgazebo_1_1_g_p_s_r_o_s_plugin_1ae4a602032a43f1a3cc904fa4ff938fc3)`()` 

Class destructor.

#### `public virtual void `[`Load`](#classgazebo_1_1_g_p_s_r_o_s_plugin_1ac59efd08373c7f691308609836a2a03d)`(sensors::SensorPtr _parent,sdf::ElementPtr _sdf)` 

Load module and read parameters from SDF.

#### `public bool `[`OnUpdateGPS`](#classgazebo_1_1_g_p_s_r_o_s_plugin_1a255822b5790c6202d5ab5f3bca0eca8b)`()` 

Update GPS ROS message.

#### `protected sensors::GpsSensorPtr `[`gazeboGPSSensor`](#classgazebo_1_1_g_p_s_r_o_s_plugin_1aaa97f3a5236f6c5d9914d042848f97d6) 

Pointer to the parent sensor.

#### `protected sensor_msgs::NavSatFix `[`gpsMessage`](#classgazebo_1_1_g_p_s_r_o_s_plugin_1aa365281835351f7720482bd36611733d) 

Output GPS ROS message.

# class `gazebo::IMUROSPlugin` 

```
class gazebo::IMUROSPlugin
  : public gazebo::ROSBaseModelPlugin
```  

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public  `[`IMUROSPlugin`](#classgazebo_1_1_i_m_u_r_o_s_plugin_1a5c7035a09686f2688c235b17a3d8a7db)`()` | Class constructor.
`public virtual  `[`~IMUROSPlugin`](#classgazebo_1_1_i_m_u_r_o_s_plugin_1ab19c7cfef17c9a660f495841e494edd6)`()` | Class destructor.
`public virtual void `[`Load`](#classgazebo_1_1_i_m_u_r_o_s_plugin_1a91f9dd3cb212d8b2207e4b51bd06bc79)`(physics::ModelPtr _model,sdf::ElementPtr _sdf)` | Load the plugin.
`protected ignition::math::Vector3d `[`measLinearAcc`](#classgazebo_1_1_i_m_u_r_o_s_plugin_1ae376a7d63023a8fe4246251a59fe3636) | Last measurement of linear acceleration..
`protected ignition::math::Vector3d `[`measAngularVel`](#classgazebo_1_1_i_m_u_r_o_s_plugin_1aa8b6ebdfdd7c36570214121a479185ae) | Last measurement of angular velocity.
`protected ignition::math::Quaterniond `[`measOrientation`](#classgazebo_1_1_i_m_u_r_o_s_plugin_1a237f775ebb67751d4c0a3dd5b806b1b5) | (Simulation) time when the last sensor measurement was generated.
`protected ignition::math::Vector3d `[`gravityWorld`](#classgazebo_1_1_i_m_u_r_o_s_plugin_1ac5c80e66a5029f008a776dd3ca5c7585) | Gravity vector wrt. reference frame.
`protected ignition::math::Vector3d `[`gyroscopeBias`](#classgazebo_1_1_i_m_u_r_o_s_plugin_1a78de6a1ae264ea41a4297b6789120cc9) | Current (drifting) gyroscope bias.
`protected ignition::math::Vector3d `[`accelerometerBias`](#classgazebo_1_1_i_m_u_r_o_s_plugin_1aedcd0a802dc7598c88347bdad2e952e4) | Current (drifting) accelerometer bias.
`protected ignition::math::Vector3d `[`gyroscopeTurnOnBias`](#classgazebo_1_1_i_m_u_r_o_s_plugin_1a5f49ef5082c887fe00818b1153ad8d43) | Constant turn-on gyroscope bias.
`protected ignition::math::Vector3d `[`accelerometerTurnOnBias`](#classgazebo_1_1_i_m_u_r_o_s_plugin_1a21b7f5a23e79eeb076bc89182890e5a3) | Constant turn-on accelerometer bias.
`protected `[`IMUParameters`](#structgazebo_1_1_i_m_u_parameters)` `[`imuParameters`](#classgazebo_1_1_i_m_u_r_o_s_plugin_1a9c4660a48d5365bd6c1465e8e2e33f57) | IMU model parameters.
`protected sensor_msgs::Imu `[`imuROSMessage`](#classgazebo_1_1_i_m_u_r_o_s_plugin_1a9270c9a643245555dffac3768f380fc4) | ROS IMU message.
`protected virtual bool `[`OnUpdate`](#classgazebo_1_1_i_m_u_r_o_s_plugin_1aa15397b1f75e506ddb42841966306392)`(const common::UpdateInfo & _info)` | Update sensor measurement.
`protected void `[`AddNoise`](#classgazebo_1_1_i_m_u_r_o_s_plugin_1af354ab1547a4509481807e08c959655f)`(ignition::math::Vector3d & _linAcc,ignition::math::Vector3d & _angVel,ignition::math::Quaterniond & _orientation,double _dt)` | Apply and add nosie model to ideal measurements.

## Members

#### `public  `[`IMUROSPlugin`](#classgazebo_1_1_i_m_u_r_o_s_plugin_1a5c7035a09686f2688c235b17a3d8a7db)`()` 

Class constructor.

#### `public virtual  `[`~IMUROSPlugin`](#classgazebo_1_1_i_m_u_r_o_s_plugin_1ab19c7cfef17c9a660f495841e494edd6)`()` 

Class destructor.

#### `public virtual void `[`Load`](#classgazebo_1_1_i_m_u_r_o_s_plugin_1a91f9dd3cb212d8b2207e4b51bd06bc79)`(physics::ModelPtr _model,sdf::ElementPtr _sdf)` 

Load the plugin.

#### `protected ignition::math::Vector3d `[`measLinearAcc`](#classgazebo_1_1_i_m_u_r_o_s_plugin_1ae376a7d63023a8fe4246251a59fe3636) 

Last measurement of linear acceleration..

#### `protected ignition::math::Vector3d `[`measAngularVel`](#classgazebo_1_1_i_m_u_r_o_s_plugin_1aa8b6ebdfdd7c36570214121a479185ae) 

Last measurement of angular velocity.

#### `protected ignition::math::Quaterniond `[`measOrientation`](#classgazebo_1_1_i_m_u_r_o_s_plugin_1a237f775ebb67751d4c0a3dd5b806b1b5) 

(Simulation) time when the last sensor measurement was generated.

#### `protected ignition::math::Vector3d `[`gravityWorld`](#classgazebo_1_1_i_m_u_r_o_s_plugin_1ac5c80e66a5029f008a776dd3ca5c7585) 

Gravity vector wrt. reference frame.

#### `protected ignition::math::Vector3d `[`gyroscopeBias`](#classgazebo_1_1_i_m_u_r_o_s_plugin_1a78de6a1ae264ea41a4297b6789120cc9) 

Current (drifting) gyroscope bias.

#### `protected ignition::math::Vector3d `[`accelerometerBias`](#classgazebo_1_1_i_m_u_r_o_s_plugin_1aedcd0a802dc7598c88347bdad2e952e4) 

Current (drifting) accelerometer bias.

#### `protected ignition::math::Vector3d `[`gyroscopeTurnOnBias`](#classgazebo_1_1_i_m_u_r_o_s_plugin_1a5f49ef5082c887fe00818b1153ad8d43) 

Constant turn-on gyroscope bias.

#### `protected ignition::math::Vector3d `[`accelerometerTurnOnBias`](#classgazebo_1_1_i_m_u_r_o_s_plugin_1a21b7f5a23e79eeb076bc89182890e5a3) 

Constant turn-on accelerometer bias.

#### `protected `[`IMUParameters`](#structgazebo_1_1_i_m_u_parameters)` `[`imuParameters`](#classgazebo_1_1_i_m_u_r_o_s_plugin_1a9c4660a48d5365bd6c1465e8e2e33f57) 

IMU model parameters.

#### `protected sensor_msgs::Imu `[`imuROSMessage`](#classgazebo_1_1_i_m_u_r_o_s_plugin_1a9270c9a643245555dffac3768f380fc4) 

ROS IMU message.

#### `protected virtual bool `[`OnUpdate`](#classgazebo_1_1_i_m_u_r_o_s_plugin_1aa15397b1f75e506ddb42841966306392)`(const common::UpdateInfo & _info)` 

Update sensor measurement.

#### `protected void `[`AddNoise`](#classgazebo_1_1_i_m_u_r_o_s_plugin_1af354ab1547a4509481807e08c959655f)`(ignition::math::Vector3d & _linAcc,ignition::math::Vector3d & _angVel,ignition::math::Quaterniond & _orientation,double _dt)` 

Apply and add nosie model to ideal measurements.

# class `gazebo::MagnetometerROSPlugin` 

```
class gazebo::MagnetometerROSPlugin
  : public gazebo::ROSBaseModelPlugin
```  

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public  `[`MagnetometerROSPlugin`](#classgazebo_1_1_magnetometer_r_o_s_plugin_1a6eaa4d0461db8bc1dd03a6efb2046049)`()` | Class constructor.
`public virtual  `[`~MagnetometerROSPlugin`](#classgazebo_1_1_magnetometer_r_o_s_plugin_1a5c394ca9a12d4da9d15d91337194a282)`()` | Class destructor.
`public virtual void `[`Load`](#classgazebo_1_1_magnetometer_r_o_s_plugin_1aa8d9083af5fae036731f513b94a029a1)`(physics::ModelPtr _model,sdf::ElementPtr _sdf)` | Load the plugin.
`protected `[`MagnetometerParameters`](#structgazebo_1_1_magnetometer_parameters)` `[`parameters`](#classgazebo_1_1_magnetometer_r_o_s_plugin_1a417aaca91431fb47e949ae947a3c595a) | Magnetometer configuration parameters:
`protected ignition::math::Vector3d `[`magneticFieldWorld`](#classgazebo_1_1_magnetometer_r_o_s_plugin_1a79e45d104255fac396dba8e868ae79df) | Reference magnetic field in world frame:
`protected ignition::math::Vector3d `[`turnOnBias`](#classgazebo_1_1_magnetometer_r_o_s_plugin_1ab4723d042e1d2b382e73cc0e2219e4e9) | Constant turn-on bias [muT].
`protected ignition::math::Vector3d `[`measMagneticField`](#classgazebo_1_1_magnetometer_r_o_s_plugin_1a7ead881188c3d53928ba95569672cba6) | Last measurement of magnetic field.
`protected sensor_msgs::MagneticField `[`rosMsg`](#classgazebo_1_1_magnetometer_r_o_s_plugin_1ad2c2f64e76ecc2f24afa4c6c6810821c) | ROS message.
`protected virtual bool `[`OnUpdate`](#classgazebo_1_1_magnetometer_r_o_s_plugin_1a1834c8718fa80c4e1b26c62a2e9a407f)`(const common::UpdateInfo & _info)` | Update sensor measurement.

## Members

#### `public  `[`MagnetometerROSPlugin`](#classgazebo_1_1_magnetometer_r_o_s_plugin_1a6eaa4d0461db8bc1dd03a6efb2046049)`()` 

Class constructor.

#### `public virtual  `[`~MagnetometerROSPlugin`](#classgazebo_1_1_magnetometer_r_o_s_plugin_1a5c394ca9a12d4da9d15d91337194a282)`()` 

Class destructor.

#### `public virtual void `[`Load`](#classgazebo_1_1_magnetometer_r_o_s_plugin_1aa8d9083af5fae036731f513b94a029a1)`(physics::ModelPtr _model,sdf::ElementPtr _sdf)` 

Load the plugin.

#### `protected `[`MagnetometerParameters`](#structgazebo_1_1_magnetometer_parameters)` `[`parameters`](#classgazebo_1_1_magnetometer_r_o_s_plugin_1a417aaca91431fb47e949ae947a3c595a) 

Magnetometer configuration parameters:

#### `protected ignition::math::Vector3d `[`magneticFieldWorld`](#classgazebo_1_1_magnetometer_r_o_s_plugin_1a79e45d104255fac396dba8e868ae79df) 

Reference magnetic field in world frame:

#### `protected ignition::math::Vector3d `[`turnOnBias`](#classgazebo_1_1_magnetometer_r_o_s_plugin_1ab4723d042e1d2b382e73cc0e2219e4e9) 

Constant turn-on bias [muT].

#### `protected ignition::math::Vector3d `[`measMagneticField`](#classgazebo_1_1_magnetometer_r_o_s_plugin_1a7ead881188c3d53928ba95569672cba6) 

Last measurement of magnetic field.

#### `protected sensor_msgs::MagneticField `[`rosMsg`](#classgazebo_1_1_magnetometer_r_o_s_plugin_1ad2c2f64e76ecc2f24afa4c6c6810821c) 

ROS message.

#### `protected virtual bool `[`OnUpdate`](#classgazebo_1_1_magnetometer_r_o_s_plugin_1a1834c8718fa80c4e1b26c62a2e9a407f)`(const common::UpdateInfo & _info)` 

Update sensor measurement.

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

# class `gazebo::ROSBaseModelPlugin` 

```
class gazebo::ROSBaseModelPlugin
  : public gazebo::ROSBasePlugin
  : public ModelPlugin
```  

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public  `[`ROSBaseModelPlugin`](#classgazebo_1_1_r_o_s_base_model_plugin_1ab63bd687291a8642150cb00a94900014)`()` | Class constructor.
`public virtual  `[`~ROSBaseModelPlugin`](#classgazebo_1_1_r_o_s_base_model_plugin_1a3e34768f99ceff93e43a6befc5ca1c03)`()` | Class destructor.
`protected physics::ModelPtr `[`model`](#classgazebo_1_1_r_o_s_base_model_plugin_1af03370cfa624905d6098556d815828b3) | Pointer to the model.
`protected physics::LinkPtr `[`link`](#classgazebo_1_1_r_o_s_base_model_plugin_1ac405387fd2fcf90b48b368104031367d) | Pointer to the link.
`protected bool `[`enableLocalNEDFrame`](#classgazebo_1_1_r_o_s_base_model_plugin_1a3ebccbacd16defded57b77d970bcb95c) | True if a the local NED frame needs to be broadcasted.
`protected tf::TransformBroadcaster * `[`tfBroadcaster`](#classgazebo_1_1_r_o_s_base_model_plugin_1ab2ee1727cd20681c8a5f3a33462cc694) | TF broadcaster for the local NED frame.
`protected ignition::math::Pose3d `[`localNEDFrame`](#classgazebo_1_1_r_o_s_base_model_plugin_1abc302dfd65e4b45c3e11721afedb21d7) | Pose of the local NED frame wrt link frame.
`protected tf::StampedTransform `[`tfLocalNEDFrame`](#classgazebo_1_1_r_o_s_base_model_plugin_1a3648c84096f1fff1390c53557a782fd1) | Local NED TF frame.
`protected virtual void `[`Load`](#classgazebo_1_1_r_o_s_base_model_plugin_1a9201b96ddee1a64ce43e59f3cf1ff2e9)`(physics::ModelPtr _model,sdf::ElementPtr _sdf)` | Load plugin and its configuration from sdf,.
`protected virtual bool `[`OnUpdate`](#classgazebo_1_1_r_o_s_base_model_plugin_1a51b6e630508d410ddfe1a76573ef75fb)`(const common::UpdateInfo &)` | Update callback from simulation.
`protected void `[`SendLocalNEDTransform`](#classgazebo_1_1_r_o_s_base_model_plugin_1a11c3832798f58c446a5d0d69343ad181)`()` | Returns true if the base_link_ned frame exists.

## Members

#### `public  `[`ROSBaseModelPlugin`](#classgazebo_1_1_r_o_s_base_model_plugin_1ab63bd687291a8642150cb00a94900014)`()` 

Class constructor.

#### `public virtual  `[`~ROSBaseModelPlugin`](#classgazebo_1_1_r_o_s_base_model_plugin_1a3e34768f99ceff93e43a6befc5ca1c03)`()` 

Class destructor.

#### `protected physics::ModelPtr `[`model`](#classgazebo_1_1_r_o_s_base_model_plugin_1af03370cfa624905d6098556d815828b3) 

Pointer to the model.

#### `protected physics::LinkPtr `[`link`](#classgazebo_1_1_r_o_s_base_model_plugin_1ac405387fd2fcf90b48b368104031367d) 

Pointer to the link.

#### `protected bool `[`enableLocalNEDFrame`](#classgazebo_1_1_r_o_s_base_model_plugin_1a3ebccbacd16defded57b77d970bcb95c) 

True if a the local NED frame needs to be broadcasted.

#### `protected tf::TransformBroadcaster * `[`tfBroadcaster`](#classgazebo_1_1_r_o_s_base_model_plugin_1ab2ee1727cd20681c8a5f3a33462cc694) 

TF broadcaster for the local NED frame.

#### `protected ignition::math::Pose3d `[`localNEDFrame`](#classgazebo_1_1_r_o_s_base_model_plugin_1abc302dfd65e4b45c3e11721afedb21d7) 

Pose of the local NED frame wrt link frame.

#### `protected tf::StampedTransform `[`tfLocalNEDFrame`](#classgazebo_1_1_r_o_s_base_model_plugin_1a3648c84096f1fff1390c53557a782fd1) 

Local NED TF frame.

#### `protected virtual void `[`Load`](#classgazebo_1_1_r_o_s_base_model_plugin_1a9201b96ddee1a64ce43e59f3cf1ff2e9)`(physics::ModelPtr _model,sdf::ElementPtr _sdf)` 

Load plugin and its configuration from sdf,.

#### `protected virtual bool `[`OnUpdate`](#classgazebo_1_1_r_o_s_base_model_plugin_1a51b6e630508d410ddfe1a76573ef75fb)`(const common::UpdateInfo &)` 

Update callback from simulation.

#### `protected void `[`SendLocalNEDTransform`](#classgazebo_1_1_r_o_s_base_model_plugin_1a11c3832798f58c446a5d0d69343ad181)`()` 

Returns true if the base_link_ned frame exists.

# class `gazebo::ROSBasePlugin` 

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public  `[`ROSBasePlugin`](#classgazebo_1_1_r_o_s_base_plugin_1a0435db27811265bd28476844b1aebb7d)`()` | Class constructor.
`public virtual  `[`~ROSBasePlugin`](#classgazebo_1_1_r_o_s_base_plugin_1a085d18e1e808fae36b6bf3dce476c7e5)`()` | Class destructor.
`public bool `[`InitBasePlugin`](#classgazebo_1_1_r_o_s_base_plugin_1a74ff905293eb8caa7becbc5404a97fc6)`(sdf::ElementPtr _sdf)` | Initialize base plugin.
`public bool `[`OnUpdate`](#classgazebo_1_1_r_o_s_base_plugin_1a02aa79b255cb8f0847998f774cb03b32)`(const common::UpdateInfo &)` | Update callback from simulation.
`public bool `[`AddNoiseModel`](#classgazebo_1_1_r_o_s_base_plugin_1abd97192b9712ae6a05d41d158c05f57a)`(std::string _name,double _sigma)` | Add noise normal distribution to the list.
`protected std::string `[`robotNamespace`](#classgazebo_1_1_r_o_s_base_plugin_1a9a9e059aec0a41dd012223d3ea3c9fe9) | Robot namespace.
`protected std::string `[`sensorOutputTopic`](#classgazebo_1_1_r_o_s_base_plugin_1a818f107bc9e165a3cc8016fd6859f86a) | Name of the sensor's output topic.
`protected physics::WorldPtr `[`world`](#classgazebo_1_1_r_o_s_base_plugin_1a24f910550057c819c246f5c3f74dae5a) | Pointer to the world.
`protected event::ConnectionPtr `[`updateConnection`](#classgazebo_1_1_r_o_s_base_plugin_1a1d7b676bec7c29b2bd021b47ecd32bb5) | Pointer to the update event connection.
`protected common::Time `[`lastMeasurementTime`](#classgazebo_1_1_r_o_s_base_plugin_1ac3798d56f9ea70175d99ab80106b4319) | (Simulation) time when the last sensor measurement was generated.
`protected double `[`updateRate`](#classgazebo_1_1_r_o_s_base_plugin_1adbcb691eba2efdd0156d5422bd1cf03f) | Sensor update rate.
`protected double `[`noiseSigma`](#classgazebo_1_1_r_o_s_base_plugin_1aef76766a171b7b9c0c236ff5987800f9) | Noise standard deviation.
`protected double `[`noiseAmp`](#classgazebo_1_1_r_o_s_base_plugin_1a6a7695e4dc91f9504a3ee88d5da94102) | Noise amplitude.
`protected bool `[`gazeboMsgEnabled`](#classgazebo_1_1_r_o_s_base_plugin_1a03fadaa69a0c77dc81153d5059c2cfb4) | Flag set to true if the Gazebo sensors messages are supposed to be published as well (it can avoid unnecessary overhead in case) the sensor messages needed are only ROS messages.
`protected std::default_random_engine `[`rndGen`](#classgazebo_1_1_r_o_s_base_plugin_1ac9f7d735298e4c0017e34ff652295fd3) | Pseudo random number generator.
`protected std::map< std::string, std::normal_distribution< double > > `[`noiseModels`](#classgazebo_1_1_r_o_s_base_plugin_1aec1fe60d8e12867115754d7f89689da2) | Normal distribution describing the noise models.
`protected std_msgs::Bool `[`isOn`](#classgazebo_1_1_r_o_s_base_plugin_1a217d66ec1fe4002468300e0c409bfb32) | Flag to control the generation of output messages.
`protected boost::shared_ptr< ros::NodeHandle > `[`rosNode`](#classgazebo_1_1_r_o_s_base_plugin_1a6b907bcd7669d3907f3c78e654fcca88) | ROS node handle for communication with ROS.
`protected transport::NodePtr `[`gazeboNode`](#classgazebo_1_1_r_o_s_base_plugin_1a6444bffce26cd7c1d31ab1b3abd990c7) | Gazebo's node handle for transporting measurement messages.
`protected ros::Publisher `[`rosSensorOutputPub`](#classgazebo_1_1_r_o_s_base_plugin_1aff7eafda5f899aa2304a870d1418a300) | Gazebo's publisher for transporting measurement messages.
`protected transport::PublisherPtr `[`gazeboSensorOutputPub`](#classgazebo_1_1_r_o_s_base_plugin_1a00461d61554c0a38b03892488a43eefb) | Gazebo's publisher for transporting measurement messages.
`protected ros::ServiceServer `[`changeSensorSrv`](#classgazebo_1_1_r_o_s_base_plugin_1a4a9b8a250d6c0c4e8148fa96c8dcc395) | Service server object.
`protected ros::Publisher `[`pluginStatePub`](#classgazebo_1_1_r_o_s_base_plugin_1a0a405302b38096d97a25c18879de03ee) | ROS publisher for the switchable sensor data.
`protected ignition::math::Pose3d `[`referenceFrame`](#classgazebo_1_1_r_o_s_base_plugin_1aa788862de11b763facdf51ac105c535d) | Pose of the reference frame wrt world frame.
`protected ros::Subscriber `[`tfStaticSub`](#classgazebo_1_1_r_o_s_base_plugin_1a0d5b3d85ee84ddd0e722a4e1dbd83d83) | ROS subscriber for the TF static reference frame.
`protected std::string `[`referenceFrameID`](#classgazebo_1_1_r_o_s_base_plugin_1a02ca6231d0a2961fe6a63002de9a5ad4) | Frame ID of the reference frame.
`protected bool `[`isReferenceInit`](#classgazebo_1_1_r_o_s_base_plugin_1a9004a71899294df66fe56bd6adcc187c) | Flag set to true if reference frame initialized.
`protected physics::LinkPtr `[`referenceLink`](#classgazebo_1_1_r_o_s_base_plugin_1a34ff72f4617839866a593d0c1a00f375) | Reference link.
`protected bool `[`IsOn`](#classgazebo_1_1_r_o_s_base_plugin_1a8c02e25afa29c264aa3a262b277a3723)`()` | Returns true if the plugin is activated.
`protected void `[`PublishState`](#classgazebo_1_1_r_o_s_base_plugin_1a0185c958f2ce8b30a1c5dc078bbd7b0e)`()` | Publish the current state of the plugin.
`protected bool `[`ChangeSensorState`](#classgazebo_1_1_r_o_s_base_plugin_1a47e246ab8e3e9fe1b7f032ee7bd8af16)`(uuv_sensor_ros_plugins_msgs::ChangeSensorState::Request & _req,uuv_sensor_ros_plugins_msgs::ChangeSensorState::Response & _res)` | Change sensor state (ON/OFF)
`protected void `[`GetTFMessage`](#classgazebo_1_1_r_o_s_base_plugin_1a465f66f7ecad8aa9e0f9e7d5fd0159d9)`(const tf::tfMessage::ConstPtr & _msg)` | Callback function for the static TF message.
`protected double `[`GetGaussianNoise`](#classgazebo_1_1_r_o_s_base_plugin_1ae1fd5e5059943e83865efa837e52e3a7)`(double _amp)` | Returns noise value for a function with zero mean from the default Gaussian noise model.
`protected double `[`GetGaussianNoise`](#classgazebo_1_1_r_o_s_base_plugin_1a69d2da0f2848ba0153756afbb331e447)`(std::string _name,double _amp)` | Returns noise value for a function with zero mean from a Gaussian noise model according to the model name.
`protected bool `[`EnableMeasurement`](#classgazebo_1_1_r_o_s_base_plugin_1af12a92a0ddf7c3c07163d32d6d95c655)`(const common::UpdateInfo & _info) const` | Enables generation of simulated measurement if the timeout since the last update has been reached.
`protected void `[`UpdateReferenceFramePose`](#classgazebo_1_1_r_o_s_base_plugin_1a768035af5fb258d9c07c4d7fd5049700)`()` | Updates the pose of the reference frame wrt the world frame.

## Members

#### `public  `[`ROSBasePlugin`](#classgazebo_1_1_r_o_s_base_plugin_1a0435db27811265bd28476844b1aebb7d)`()` 

Class constructor.

#### `public virtual  `[`~ROSBasePlugin`](#classgazebo_1_1_r_o_s_base_plugin_1a085d18e1e808fae36b6bf3dce476c7e5)`()` 

Class destructor.

#### `public bool `[`InitBasePlugin`](#classgazebo_1_1_r_o_s_base_plugin_1a74ff905293eb8caa7becbc5404a97fc6)`(sdf::ElementPtr _sdf)` 

Initialize base plugin.

#### `public bool `[`OnUpdate`](#classgazebo_1_1_r_o_s_base_plugin_1a02aa79b255cb8f0847998f774cb03b32)`(const common::UpdateInfo &)` 

Update callback from simulation.

#### `public bool `[`AddNoiseModel`](#classgazebo_1_1_r_o_s_base_plugin_1abd97192b9712ae6a05d41d158c05f57a)`(std::string _name,double _sigma)` 

Add noise normal distribution to the list.

#### `protected std::string `[`robotNamespace`](#classgazebo_1_1_r_o_s_base_plugin_1a9a9e059aec0a41dd012223d3ea3c9fe9) 

Robot namespace.

#### `protected std::string `[`sensorOutputTopic`](#classgazebo_1_1_r_o_s_base_plugin_1a818f107bc9e165a3cc8016fd6859f86a) 

Name of the sensor's output topic.

#### `protected physics::WorldPtr `[`world`](#classgazebo_1_1_r_o_s_base_plugin_1a24f910550057c819c246f5c3f74dae5a) 

Pointer to the world.

#### `protected event::ConnectionPtr `[`updateConnection`](#classgazebo_1_1_r_o_s_base_plugin_1a1d7b676bec7c29b2bd021b47ecd32bb5) 

Pointer to the update event connection.

#### `protected common::Time `[`lastMeasurementTime`](#classgazebo_1_1_r_o_s_base_plugin_1ac3798d56f9ea70175d99ab80106b4319) 

(Simulation) time when the last sensor measurement was generated.

#### `protected double `[`updateRate`](#classgazebo_1_1_r_o_s_base_plugin_1adbcb691eba2efdd0156d5422bd1cf03f) 

Sensor update rate.

#### `protected double `[`noiseSigma`](#classgazebo_1_1_r_o_s_base_plugin_1aef76766a171b7b9c0c236ff5987800f9) 

Noise standard deviation.

#### `protected double `[`noiseAmp`](#classgazebo_1_1_r_o_s_base_plugin_1a6a7695e4dc91f9504a3ee88d5da94102) 

Noise amplitude.

#### `protected bool `[`gazeboMsgEnabled`](#classgazebo_1_1_r_o_s_base_plugin_1a03fadaa69a0c77dc81153d5059c2cfb4) 

Flag set to true if the Gazebo sensors messages are supposed to be published as well (it can avoid unnecessary overhead in case) the sensor messages needed are only ROS messages.

#### `protected std::default_random_engine `[`rndGen`](#classgazebo_1_1_r_o_s_base_plugin_1ac9f7d735298e4c0017e34ff652295fd3) 

Pseudo random number generator.

#### `protected std::map< std::string, std::normal_distribution< double > > `[`noiseModels`](#classgazebo_1_1_r_o_s_base_plugin_1aec1fe60d8e12867115754d7f89689da2) 

Normal distribution describing the noise models.

#### `protected std_msgs::Bool `[`isOn`](#classgazebo_1_1_r_o_s_base_plugin_1a217d66ec1fe4002468300e0c409bfb32) 

Flag to control the generation of output messages.

#### `protected boost::shared_ptr< ros::NodeHandle > `[`rosNode`](#classgazebo_1_1_r_o_s_base_plugin_1a6b907bcd7669d3907f3c78e654fcca88) 

ROS node handle for communication with ROS.

#### `protected transport::NodePtr `[`gazeboNode`](#classgazebo_1_1_r_o_s_base_plugin_1a6444bffce26cd7c1d31ab1b3abd990c7) 

Gazebo's node handle for transporting measurement messages.

#### `protected ros::Publisher `[`rosSensorOutputPub`](#classgazebo_1_1_r_o_s_base_plugin_1aff7eafda5f899aa2304a870d1418a300) 

Gazebo's publisher for transporting measurement messages.

#### `protected transport::PublisherPtr `[`gazeboSensorOutputPub`](#classgazebo_1_1_r_o_s_base_plugin_1a00461d61554c0a38b03892488a43eefb) 

Gazebo's publisher for transporting measurement messages.

#### `protected ros::ServiceServer `[`changeSensorSrv`](#classgazebo_1_1_r_o_s_base_plugin_1a4a9b8a250d6c0c4e8148fa96c8dcc395) 

Service server object.

#### `protected ros::Publisher `[`pluginStatePub`](#classgazebo_1_1_r_o_s_base_plugin_1a0a405302b38096d97a25c18879de03ee) 

ROS publisher for the switchable sensor data.

#### `protected ignition::math::Pose3d `[`referenceFrame`](#classgazebo_1_1_r_o_s_base_plugin_1aa788862de11b763facdf51ac105c535d) 

Pose of the reference frame wrt world frame.

#### `protected ros::Subscriber `[`tfStaticSub`](#classgazebo_1_1_r_o_s_base_plugin_1a0d5b3d85ee84ddd0e722a4e1dbd83d83) 

ROS subscriber for the TF static reference frame.

#### `protected std::string `[`referenceFrameID`](#classgazebo_1_1_r_o_s_base_plugin_1a02ca6231d0a2961fe6a63002de9a5ad4) 

Frame ID of the reference frame.

#### `protected bool `[`isReferenceInit`](#classgazebo_1_1_r_o_s_base_plugin_1a9004a71899294df66fe56bd6adcc187c) 

Flag set to true if reference frame initialized.

#### `protected physics::LinkPtr `[`referenceLink`](#classgazebo_1_1_r_o_s_base_plugin_1a34ff72f4617839866a593d0c1a00f375) 

Reference link.

#### `protected bool `[`IsOn`](#classgazebo_1_1_r_o_s_base_plugin_1a8c02e25afa29c264aa3a262b277a3723)`()` 

Returns true if the plugin is activated.

#### `protected void `[`PublishState`](#classgazebo_1_1_r_o_s_base_plugin_1a0185c958f2ce8b30a1c5dc078bbd7b0e)`()` 

Publish the current state of the plugin.

#### `protected bool `[`ChangeSensorState`](#classgazebo_1_1_r_o_s_base_plugin_1a47e246ab8e3e9fe1b7f032ee7bd8af16)`(uuv_sensor_ros_plugins_msgs::ChangeSensorState::Request & _req,uuv_sensor_ros_plugins_msgs::ChangeSensorState::Response & _res)` 

Change sensor state (ON/OFF)

#### `protected void `[`GetTFMessage`](#classgazebo_1_1_r_o_s_base_plugin_1a465f66f7ecad8aa9e0f9e7d5fd0159d9)`(const tf::tfMessage::ConstPtr & _msg)` 

Callback function for the static TF message.

#### `protected double `[`GetGaussianNoise`](#classgazebo_1_1_r_o_s_base_plugin_1ae1fd5e5059943e83865efa837e52e3a7)`(double _amp)` 

Returns noise value for a function with zero mean from the default Gaussian noise model.

#### `protected double `[`GetGaussianNoise`](#classgazebo_1_1_r_o_s_base_plugin_1a69d2da0f2848ba0153756afbb331e447)`(std::string _name,double _amp)` 

Returns noise value for a function with zero mean from a Gaussian noise model according to the model name.

#### `protected bool `[`EnableMeasurement`](#classgazebo_1_1_r_o_s_base_plugin_1af12a92a0ddf7c3c07163d32d6d95c655)`(const common::UpdateInfo & _info) const` 

Enables generation of simulated measurement if the timeout since the last update has been reached.

#### `protected void `[`UpdateReferenceFramePose`](#classgazebo_1_1_r_o_s_base_plugin_1a768035af5fb258d9c07c4d7fd5049700)`()` 

Updates the pose of the reference frame wrt the world frame.

# class `gazebo::ROSBaseSensorPlugin` 

```
class gazebo::ROSBaseSensorPlugin
  : public gazebo::ROSBasePlugin
  : public SensorPlugin
```  

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public  `[`ROSBaseSensorPlugin`](#classgazebo_1_1_r_o_s_base_sensor_plugin_1a5f5f2144542f249de769ec638cfdfee5)`()` | Class constructor.
`public virtual  `[`~ROSBaseSensorPlugin`](#classgazebo_1_1_r_o_s_base_sensor_plugin_1a3c7adf8a507fbae48749f761f5d43b53)`()` | Class destructor.
`protected sensors::SensorPtr `[`parentSensor`](#classgazebo_1_1_r_o_s_base_sensor_plugin_1a34cac9a5589143a2f8ab2623d47c8ac4) | Pointer to the parent sensor.
`protected virtual void `[`Load`](#classgazebo_1_1_r_o_s_base_sensor_plugin_1a2ad16341faa4fadef2e3347ce2c8907a)`(sensors::SensorPtr _model,sdf::ElementPtr _sdf)` | Load plugin and its configuration from sdf,.
`protected virtual bool `[`OnUpdate`](#classgazebo_1_1_r_o_s_base_sensor_plugin_1a299ecabab8d2cbb768618dd509279e11)`(const common::UpdateInfo &)` | Update callback from simulation.

## Members

#### `public  `[`ROSBaseSensorPlugin`](#classgazebo_1_1_r_o_s_base_sensor_plugin_1a5f5f2144542f249de769ec638cfdfee5)`()` 

Class constructor.

#### `public virtual  `[`~ROSBaseSensorPlugin`](#classgazebo_1_1_r_o_s_base_sensor_plugin_1a3c7adf8a507fbae48749f761f5d43b53)`()` 

Class destructor.

#### `protected sensors::SensorPtr `[`parentSensor`](#classgazebo_1_1_r_o_s_base_sensor_plugin_1a34cac9a5589143a2f8ab2623d47c8ac4) 

Pointer to the parent sensor.

#### `protected virtual void `[`Load`](#classgazebo_1_1_r_o_s_base_sensor_plugin_1a2ad16341faa4fadef2e3347ce2c8907a)`(sensors::SensorPtr _model,sdf::ElementPtr _sdf)` 

Load plugin and its configuration from sdf,.

#### `protected virtual bool `[`OnUpdate`](#classgazebo_1_1_r_o_s_base_sensor_plugin_1a299ecabab8d2cbb768618dd509279e11)`(const common::UpdateInfo &)` 

Update callback from simulation.

# class `gazebo::RPTROSPlugin` 

```
class gazebo::RPTROSPlugin
  : public gazebo::ROSBaseModelPlugin
```  

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public  `[`RPTROSPlugin`](#classgazebo_1_1_r_p_t_r_o_s_plugin_1a657fc78325cb07243a81e215f5138eca)`()` | Class constructor.
`public virtual  `[`~RPTROSPlugin`](#classgazebo_1_1_r_p_t_r_o_s_plugin_1a9d2ac490915bf9e382483acfda626973)`()` | Class destructor.
`public virtual void `[`Load`](#classgazebo_1_1_r_p_t_r_o_s_plugin_1a69902969c25c0cc413899848e9b77296)`(physics::ModelPtr _model,sdf::ElementPtr _sdf)` | Load the plugin.
`protected ignition::math::Vector3d `[`position`](#classgazebo_1_1_r_p_t_r_o_s_plugin_1a8fd907c796413bfd0985520d2527c56b) | Latest measured position.
`protected uuv_sensor_ros_plugins_msgs::PositionWithCovarianceStamped `[`rosMessage`](#classgazebo_1_1_r_p_t_r_o_s_plugin_1ac866e78fbe92ce2cda59b1d0d2a067c4) | Store message since many attributes do not change (cov.).
`protected virtual bool `[`OnUpdate`](#classgazebo_1_1_r_p_t_r_o_s_plugin_1a1a354ec7d3a72bf8313d84bb044f8fce)`(const common::UpdateInfo & _info)` | Update sensor measurement.

## Members

#### `public  `[`RPTROSPlugin`](#classgazebo_1_1_r_p_t_r_o_s_plugin_1a657fc78325cb07243a81e215f5138eca)`()` 

Class constructor.

#### `public virtual  `[`~RPTROSPlugin`](#classgazebo_1_1_r_p_t_r_o_s_plugin_1a9d2ac490915bf9e382483acfda626973)`()` 

Class destructor.

#### `public virtual void `[`Load`](#classgazebo_1_1_r_p_t_r_o_s_plugin_1a69902969c25c0cc413899848e9b77296)`(physics::ModelPtr _model,sdf::ElementPtr _sdf)` 

Load the plugin.

#### `protected ignition::math::Vector3d `[`position`](#classgazebo_1_1_r_p_t_r_o_s_plugin_1a8fd907c796413bfd0985520d2527c56b) 

Latest measured position.

#### `protected uuv_sensor_ros_plugins_msgs::PositionWithCovarianceStamped `[`rosMessage`](#classgazebo_1_1_r_p_t_r_o_s_plugin_1ac866e78fbe92ce2cda59b1d0d2a067c4) 

Store message since many attributes do not change (cov.).

#### `protected virtual bool `[`OnUpdate`](#classgazebo_1_1_r_p_t_r_o_s_plugin_1a1a354ec7d3a72bf8313d84bb044f8fce)`(const common::UpdateInfo & _info)` 

Update sensor measurement.

# class `gazebo::SubseaPressureROSPlugin` 

```
class gazebo::SubseaPressureROSPlugin
  : public gazebo::ROSBaseModelPlugin
```  

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public  `[`SubseaPressureROSPlugin`](#classgazebo_1_1_subsea_pressure_r_o_s_plugin_1a47f980a1ea644753d5142dc1e57e781e)`()` | Class constructor.
`public  `[`~SubseaPressureROSPlugin`](#classgazebo_1_1_subsea_pressure_r_o_s_plugin_1ad0f101bb1409a2b8954036eb9e25b734)`()` | Class destructor.
`public virtual void `[`Load`](#classgazebo_1_1_subsea_pressure_r_o_s_plugin_1a217c4fafaaba64b533dacbe906a01cf1)`(physics::ModelPtr _model,sdf::ElementPtr _sdf)` | Load the plugin.
`protected double `[`saturation`](#classgazebo_1_1_subsea_pressure_r_o_s_plugin_1aacf4f877eb2e21f3e6e1362985c77198) | Sensor saturation (max. value for output pressure in Pa)
`protected bool `[`estimateDepth`](#classgazebo_1_1_subsea_pressure_r_o_s_plugin_1a2b8e32c2bda5fb24d426be8d9a6ef934) | If flag is set to true, estimate depth according to pressure measurement.
`protected double `[`standardPressure`](#classgazebo_1_1_subsea_pressure_r_o_s_plugin_1a523d3a012251a4c06dd3496535f1ddc5) | Standard pressure.
`protected double `[`kPaPerM`](#classgazebo_1_1_subsea_pressure_r_o_s_plugin_1a955abbff8454905f89687886ba27cae4) | Factor of kPa per meter.
`protected virtual bool `[`OnUpdate`](#classgazebo_1_1_subsea_pressure_r_o_s_plugin_1a17a9977c098924d6f7511ff6dd2d3cc4)`(const common::UpdateInfo & _info)` | Update sensor measurement.

## Members

#### `public  `[`SubseaPressureROSPlugin`](#classgazebo_1_1_subsea_pressure_r_o_s_plugin_1a47f980a1ea644753d5142dc1e57e781e)`()` 

Class constructor.

#### `public  `[`~SubseaPressureROSPlugin`](#classgazebo_1_1_subsea_pressure_r_o_s_plugin_1ad0f101bb1409a2b8954036eb9e25b734)`()` 

Class destructor.

#### `public virtual void `[`Load`](#classgazebo_1_1_subsea_pressure_r_o_s_plugin_1a217c4fafaaba64b533dacbe906a01cf1)`(physics::ModelPtr _model,sdf::ElementPtr _sdf)` 

Load the plugin.

#### `protected double `[`saturation`](#classgazebo_1_1_subsea_pressure_r_o_s_plugin_1aacf4f877eb2e21f3e6e1362985c77198) 

Sensor saturation (max. value for output pressure in Pa)

#### `protected bool `[`estimateDepth`](#classgazebo_1_1_subsea_pressure_r_o_s_plugin_1a2b8e32c2bda5fb24d426be8d9a6ef934) 

If flag is set to true, estimate depth according to pressure measurement.

#### `protected double `[`standardPressure`](#classgazebo_1_1_subsea_pressure_r_o_s_plugin_1a523d3a012251a4c06dd3496535f1ddc5) 

Standard pressure.

#### `protected double `[`kPaPerM`](#classgazebo_1_1_subsea_pressure_r_o_s_plugin_1a955abbff8454905f89687886ba27cae4) 

Factor of kPa per meter.

#### `protected virtual bool `[`OnUpdate`](#classgazebo_1_1_subsea_pressure_r_o_s_plugin_1a17a9977c098924d6f7511ff6dd2d3cc4)`(const common::UpdateInfo & _info)` 

Update sensor measurement.

# class `gazebo::UnderwaterCameraROSPlugin` 

```
class gazebo::UnderwaterCameraROSPlugin
  : public DepthCameraPlugin
  : public GazeboRosCameraUtils
```  

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public  `[`UnderwaterCameraROSPlugin`](#classgazebo_1_1_underwater_camera_r_o_s_plugin_1a30ef76059ce0c418f49fb1614131d2c6)`()` | Class constructor.
`public virtual  `[`~UnderwaterCameraROSPlugin`](#classgazebo_1_1_underwater_camera_r_o_s_plugin_1a828fa0975b3cba41b68a62f8358ba385)`()` | Class destructor.
`public void `[`Load`](#classgazebo_1_1_underwater_camera_r_o_s_plugin_1a0869c206ca23b9d3fac7050b781ea1d9)`(sensors::SensorPtr _sensor,sdf::ElementPtr _sdf)` | Load plugin and its configuration from sdf.
`public virtual void `[`OnNewDepthFrame`](#classgazebo_1_1_underwater_camera_r_o_s_plugin_1ae4d4b78964a4d9f96c94eeee0024db7a)`(const float * _image,unsigned int _width,unsigned int _height,unsigned int _depth,const std::string & _format)` | 
`public virtual void `[`OnNewRGBPointCloud`](#classgazebo_1_1_underwater_camera_r_o_s_plugin_1a305692fde5e85e1c67979e5dda0e8d92)`(const float * _pcd,unsigned int _width,unsigned int _height,unsigned int _depth,const std::string & _format)` | Update the controller.
`public virtual void `[`OnNewImageFrame`](#classgazebo_1_1_underwater_camera_r_o_s_plugin_1a63e82d6b0e757494e16136e802c1a31e)`(const unsigned char * _image,unsigned int _width,unsigned int _height,unsigned int _depth,const std::string & _format)` | 
`protected const float * `[`lastDepth`](#classgazebo_1_1_underwater_camera_r_o_s_plugin_1a33c316acb34194733ada8a58f781eebf) | Temporarily store pointer to previous depth image.
`protected unsigned char * `[`lastImage`](#classgazebo_1_1_underwater_camera_r_o_s_plugin_1a00df8cda79b648f2253aa762c68ca0c3) | Latest simulated image.
`protected float * `[`depth2rangeLUT`](#classgazebo_1_1_underwater_camera_r_o_s_plugin_1a2bae4ac2590d3e2e790d9ea21245980d) | Depth to range lookup table (LUT)
`protected float `[`attenuation`](#classgazebo_1_1_underwater_camera_r_o_s_plugin_1a371ed93a4a2ddda2cbb7d13ee65a4523) | Attenuation constants per channel (RGB)
`protected unsigned char `[`background`](#classgazebo_1_1_underwater_camera_r_o_s_plugin_1a5d8510b4c8fb17a57158411b65afecff) | Background constants per channel (RGB)
`protected virtual void `[`SimulateUnderwater`](#classgazebo_1_1_underwater_camera_r_o_s_plugin_1ace5d8a3a6b4ddc5049d573197c1c98dc)`(const cv::Mat & _inputImage,const cv::Mat & _inputDepth,cv::Mat & _outputImage)` | Add underwater light damping to image.

## Members

#### `public  `[`UnderwaterCameraROSPlugin`](#classgazebo_1_1_underwater_camera_r_o_s_plugin_1a30ef76059ce0c418f49fb1614131d2c6)`()` 

Class constructor.

#### `public virtual  `[`~UnderwaterCameraROSPlugin`](#classgazebo_1_1_underwater_camera_r_o_s_plugin_1a828fa0975b3cba41b68a62f8358ba385)`()` 

Class destructor.

#### `public void `[`Load`](#classgazebo_1_1_underwater_camera_r_o_s_plugin_1a0869c206ca23b9d3fac7050b781ea1d9)`(sensors::SensorPtr _sensor,sdf::ElementPtr _sdf)` 

Load plugin and its configuration from sdf.

#### `public virtual void `[`OnNewDepthFrame`](#classgazebo_1_1_underwater_camera_r_o_s_plugin_1ae4d4b78964a4d9f96c94eeee0024db7a)`(const float * _image,unsigned int _width,unsigned int _height,unsigned int _depth,const std::string & _format)` 

#### `public virtual void `[`OnNewRGBPointCloud`](#classgazebo_1_1_underwater_camera_r_o_s_plugin_1a305692fde5e85e1c67979e5dda0e8d92)`(const float * _pcd,unsigned int _width,unsigned int _height,unsigned int _depth,const std::string & _format)` 

Update the controller.

#### `public virtual void `[`OnNewImageFrame`](#classgazebo_1_1_underwater_camera_r_o_s_plugin_1a63e82d6b0e757494e16136e802c1a31e)`(const unsigned char * _image,unsigned int _width,unsigned int _height,unsigned int _depth,const std::string & _format)` 

#### `protected const float * `[`lastDepth`](#classgazebo_1_1_underwater_camera_r_o_s_plugin_1a33c316acb34194733ada8a58f781eebf) 

Temporarily store pointer to previous depth image.

#### `protected unsigned char * `[`lastImage`](#classgazebo_1_1_underwater_camera_r_o_s_plugin_1a00df8cda79b648f2253aa762c68ca0c3) 

Latest simulated image.

#### `protected float * `[`depth2rangeLUT`](#classgazebo_1_1_underwater_camera_r_o_s_plugin_1a2bae4ac2590d3e2e790d9ea21245980d) 

Depth to range lookup table (LUT)

#### `protected float `[`attenuation`](#classgazebo_1_1_underwater_camera_r_o_s_plugin_1a371ed93a4a2ddda2cbb7d13ee65a4523) 

Attenuation constants per channel (RGB)

#### `protected unsigned char `[`background`](#classgazebo_1_1_underwater_camera_r_o_s_plugin_1a5d8510b4c8fb17a57158411b65afecff) 

Background constants per channel (RGB)

#### `protected virtual void `[`SimulateUnderwater`](#classgazebo_1_1_underwater_camera_r_o_s_plugin_1ace5d8a3a6b4ddc5049d573197c1c98dc)`(const cv::Mat & _inputImage,const cv::Mat & _inputDepth,cv::Mat & _outputImage)` 

Add underwater light damping to image.

# struct `gazebo::IMUParameters` 

[IMUParameters](#structgazebo_1_1_i_m_u_parameters) stores all IMU model parameters. A description of these parameters can be found here: [https://github.com/ethz-asl/kalibr/wiki/IMU-Noise-Model-and-Intrinsics](https://github.com/ethz-asl/kalibr/wiki/IMU-Noise-Model-and-Intrinsics).

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public double `[`gyroscopeNoiseDensity`](#structgazebo_1_1_i_m_u_parameters_1a25f7a443bbabe24709fef7902f253686) | Gyroscope noise density (two-sided spectrum) [rad/s/sqrt(Hz)].
`public double `[`gyroscopeRandomWalk`](#structgazebo_1_1_i_m_u_parameters_1ae252c3f9cc0692111ce5d34603db2c1b) | Gyroscope bias random walk [rad/s/s/sqrt(Hz)].
`public double `[`gyroscopeBiasCorrelationTime`](#structgazebo_1_1_i_m_u_parameters_1ab9fa9588c7a67ae9c38e71910a510661) | Gyroscope bias correlation time constant [s].
`public double `[`gyroscopeTurnOnBiasSigma`](#structgazebo_1_1_i_m_u_parameters_1aa90e85c829fb5a8a7079c670feaa1513) | Gyroscope turn on bias standard deviation [rad/s].
`public double `[`accelerometerNoiseDensity`](#structgazebo_1_1_i_m_u_parameters_1a2b4bca730c38f081af8c9b73f4b6bad4) | Accelerometer noise density (two-sided spectrum) [m/s^2/sqrt(Hz)].
`public double `[`accelerometerRandomWalk`](#structgazebo_1_1_i_m_u_parameters_1a2d6b2fd03ddb35a1e61653745bbfb8fb) | Accelerometer bias random walk. [m/s^2/s/sqrt(Hz)].
`public double `[`accelerometerBiasCorrelationTime`](#structgazebo_1_1_i_m_u_parameters_1ae3ee5ba06f1f4c1982bfd85d50edf07d) | Accelerometer bias correlation time constant [s].
`public double `[`accelerometerTurnOnBiasSigma`](#structgazebo_1_1_i_m_u_parameters_1ad9ed56456fb2bfbe95d4caeb73631613) | Accelerometer turn on bias standard deviation [m/s^2].
`public double `[`orientationNoise`](#structgazebo_1_1_i_m_u_parameters_1a6c283963ffe5ce1e1552238d3bd00541) | Standard deviation of orientation noise per axis [rad].
`public inline  `[`IMUParameters`](#structgazebo_1_1_i_m_u_parameters_1a458153650853d5e46e0c8ebfbcc3982f)`()` | Constructor.

## Members

#### `public double `[`gyroscopeNoiseDensity`](#structgazebo_1_1_i_m_u_parameters_1a25f7a443bbabe24709fef7902f253686) 

Gyroscope noise density (two-sided spectrum) [rad/s/sqrt(Hz)].

#### `public double `[`gyroscopeRandomWalk`](#structgazebo_1_1_i_m_u_parameters_1ae252c3f9cc0692111ce5d34603db2c1b) 

Gyroscope bias random walk [rad/s/s/sqrt(Hz)].

#### `public double `[`gyroscopeBiasCorrelationTime`](#structgazebo_1_1_i_m_u_parameters_1ab9fa9588c7a67ae9c38e71910a510661) 

Gyroscope bias correlation time constant [s].

#### `public double `[`gyroscopeTurnOnBiasSigma`](#structgazebo_1_1_i_m_u_parameters_1aa90e85c829fb5a8a7079c670feaa1513) 

Gyroscope turn on bias standard deviation [rad/s].

#### `public double `[`accelerometerNoiseDensity`](#structgazebo_1_1_i_m_u_parameters_1a2b4bca730c38f081af8c9b73f4b6bad4) 

Accelerometer noise density (two-sided spectrum) [m/s^2/sqrt(Hz)].

#### `public double `[`accelerometerRandomWalk`](#structgazebo_1_1_i_m_u_parameters_1a2d6b2fd03ddb35a1e61653745bbfb8fb) 

Accelerometer bias random walk. [m/s^2/s/sqrt(Hz)].

#### `public double `[`accelerometerBiasCorrelationTime`](#structgazebo_1_1_i_m_u_parameters_1ae3ee5ba06f1f4c1982bfd85d50edf07d) 

Accelerometer bias correlation time constant [s].

#### `public double `[`accelerometerTurnOnBiasSigma`](#structgazebo_1_1_i_m_u_parameters_1ad9ed56456fb2bfbe95d4caeb73631613) 

Accelerometer turn on bias standard deviation [m/s^2].

#### `public double `[`orientationNoise`](#structgazebo_1_1_i_m_u_parameters_1a6c283963ffe5ce1e1552238d3bd00541) 

Standard deviation of orientation noise per axis [rad].

#### `public inline  `[`IMUParameters`](#structgazebo_1_1_i_m_u_parameters_1a458153650853d5e46e0c8ebfbcc3982f)`()` 

Constructor.

# struct `gazebo::MagnetometerParameters` 

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public double `[`intensity`](#structgazebo_1_1_magnetometer_parameters_1a491c6f8673f7fcfcee9dabee3075c0a8) | Intensity of reference earth magnetic field [muT].
`public double `[`heading`](#structgazebo_1_1_magnetometer_parameters_1aff42219e1267659647462ac09569da35) | Heading angle of reference earth magnetic field [rad].
`public double `[`declination`](#structgazebo_1_1_magnetometer_parameters_1ad52b97932b1b5b9d16d70448c4993fb2) | Declination of reference earth magnetic field [rad].
`public double `[`inclination`](#structgazebo_1_1_magnetometer_parameters_1a9b30e81a8cbe572c5ca121912857a2a5) | Inclination of reference earth magnetic field [rad].
`public double `[`noiseXY`](#structgazebo_1_1_magnetometer_parameters_1aa450d4be7a8de28821c651eb7407d063) | Discrete-time standard dev. of output noise in xy-axis [muT].
`public double `[`noiseZ`](#structgazebo_1_1_magnetometer_parameters_1a46c2fbe7d7d4a5b2c82fcb2ef14dfb7b) | Discrete-time standard dev. of output noise in z-axis [muT].
`public double `[`turnOnBias`](#structgazebo_1_1_magnetometer_parameters_1a13009930015f1ca248500227b224319b) | Standard deviation of constant systematic offset of measurements [muT].

## Members

#### `public double `[`intensity`](#structgazebo_1_1_magnetometer_parameters_1a491c6f8673f7fcfcee9dabee3075c0a8) 

Intensity of reference earth magnetic field [muT].

#### `public double `[`heading`](#structgazebo_1_1_magnetometer_parameters_1aff42219e1267659647462ac09569da35) 

Heading angle of reference earth magnetic field [rad].

#### `public double `[`declination`](#structgazebo_1_1_magnetometer_parameters_1ad52b97932b1b5b9d16d70448c4993fb2) 

Declination of reference earth magnetic field [rad].

#### `public double `[`inclination`](#structgazebo_1_1_magnetometer_parameters_1a9b30e81a8cbe572c5ca121912857a2a5) 

Inclination of reference earth magnetic field [rad].

#### `public double `[`noiseXY`](#structgazebo_1_1_magnetometer_parameters_1aa450d4be7a8de28821c651eb7407d063) 

Discrete-time standard dev. of output noise in xy-axis [muT].

#### `public double `[`noiseZ`](#structgazebo_1_1_magnetometer_parameters_1a46c2fbe7d7d4a5b2c82fcb2ef14dfb7b) 

Discrete-time standard dev. of output noise in z-axis [muT].

#### `public double `[`turnOnBias`](#structgazebo_1_1_magnetometer_parameters_1a13009930015f1ca248500227b224319b) 

Standard deviation of constant systematic offset of measurements [muT].

# class `FirstOrderFilter` 

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public inline  `[`FirstOrderFilter`](#class_first_order_filter_1a69ca7302a06941315d5e315a6ed726b7)`(double timeConstantUp,double timeConstantDown,T initialState)` | 
`public inline T `[`updateFilter`](#class_first_order_filter_1a2f2fa033f6d23d6fe789c0455ebc49c4)`(T inputState,double samplingTime)` | 
`public inline  `[`~FirstOrderFilter`](#class_first_order_filter_1a8e8a8a7fc06a34578f5c18d44af7300b)`()` | 
`protected double `[`timeConstantUp_`](#class_first_order_filter_1abf96f40acfd447b1f6eedbfa8bd9ad00) | 
`protected double `[`timeConstantDown_`](#class_first_order_filter_1a8b6fdd458ba76b911e527945eb10e394) | 
`protected T `[`previousState_`](#class_first_order_filter_1aeac705e33da04871e0f222d24ef8ece6) | 

## Members

#### `public inline  `[`FirstOrderFilter`](#class_first_order_filter_1a69ca7302a06941315d5e315a6ed726b7)`(double timeConstantUp,double timeConstantDown,T initialState)` 

#### `public inline T `[`updateFilter`](#class_first_order_filter_1a2f2fa033f6d23d6fe789c0455ebc49c4)`(T inputState,double samplingTime)` 

#### `public inline  `[`~FirstOrderFilter`](#class_first_order_filter_1a8e8a8a7fc06a34578f5c18d44af7300b)`()` 

#### `protected double `[`timeConstantUp_`](#class_first_order_filter_1abf96f40acfd447b1f6eedbfa8bd9ad00) 

#### `protected double `[`timeConstantDown_`](#class_first_order_filter_1a8b6fdd458ba76b911e527945eb10e394) 

#### `protected T `[`previousState_`](#class_first_order_filter_1aeac705e33da04871e0f222d24ef8ece6) 

Generated by [Moxygen](https://sourcey.com/moxygen)