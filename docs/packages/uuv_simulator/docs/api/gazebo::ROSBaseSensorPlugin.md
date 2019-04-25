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

