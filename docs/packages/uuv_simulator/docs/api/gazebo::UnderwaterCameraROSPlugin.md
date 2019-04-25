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

