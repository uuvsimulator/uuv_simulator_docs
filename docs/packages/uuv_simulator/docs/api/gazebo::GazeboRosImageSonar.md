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

