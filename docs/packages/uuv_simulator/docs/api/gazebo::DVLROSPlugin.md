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

