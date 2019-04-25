# class `gazebo::ConversionFunctionBessa` 

```
class gazebo::ConversionFunctionBessa
  : public gazebo::ConversionFunction
```  

Asymmetric conversion function with dead-zone nonlinearity. This corresponds to what is called Model 2 in Bessa et al.: Dynamic Positioning of Underwater Robotic Vehicles with Thruster [Dynamics](docs/packages/uuv_simulator/docs/api/gazebo::Dynamics.md#classgazebo_1_1_dynamics) Compensation.

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public inline virtual std::string `[`GetType`](#classgazebo_1_1_conversion_function_bessa_1a31637f978fdc895689920238998b7926)`()` | Return (derived) type of conversion function.
`public virtual bool `[`GetParam`](#classgazebo_1_1_conversion_function_bessa_1ad47b4e53609b493924d3f0e76626f133)`(std::string _tag,double & _output)` | Return paramater in scalar form for the given tag.
`public virtual double `[`convert`](#classgazebo_1_1_conversion_function_bessa_1a2e863ecdfdeb289ada6d9045783d17a0)`(double _cmd)` | Convert thruster state (e.g. angular velocity) to thrust force.

## Members

#### `public inline virtual std::string `[`GetType`](#classgazebo_1_1_conversion_function_bessa_1a31637f978fdc895689920238998b7926)`()` 

Return (derived) type of conversion function.

#### `public virtual bool `[`GetParam`](#classgazebo_1_1_conversion_function_bessa_1ad47b4e53609b493924d3f0e76626f133)`(std::string _tag,double & _output)` 

Return paramater in scalar form for the given tag.

#### `public virtual double `[`convert`](#classgazebo_1_1_conversion_function_bessa_1a2e863ecdfdeb289ada6d9045783d17a0)`(double _cmd)` 

Convert thruster state (e.g. angular velocity) to thrust force.

