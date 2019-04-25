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

