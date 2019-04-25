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

