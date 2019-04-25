# class `gazebo::ConversionFunctionBasic` 

```
class gazebo::ConversionFunctionBasic
  : public gazebo::ConversionFunction
```  

The most basic conversion function: Thrust = const.*w*abs(w) This corresponds to what is attrributed to Yoerger et al. and called Model 1 in Bessa et al.: Dynamic Positioning of Underwater Robotic Vehicles with Thruster [Dynamics](docs/packages/uuv_simulator/docs/api/gazebo::Dynamics.md#classgazebo_1_1_dynamics) Compensation.

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public inline virtual std::string `[`GetType`](#classgazebo_1_1_conversion_function_basic_1a2ce48db471c7706abede19a724ef08fe)`()` | Return (derived) type of conversion function.
`public virtual bool `[`GetParam`](#classgazebo_1_1_conversion_function_basic_1a943dbcaa6720093a775ebb7f3a1e3bea)`(std::string _tag,double & _output)` | Return paramater in scalar form for the given tag.
`public virtual double `[`convert`](#classgazebo_1_1_conversion_function_basic_1a8f10f33118aeda7560214d915cee892e)`(double _cmd)` | Convert thruster state (e.g. angular velocity) to thrust force.

## Members

#### `public inline virtual std::string `[`GetType`](#classgazebo_1_1_conversion_function_basic_1a2ce48db471c7706abede19a724ef08fe)`()` 

Return (derived) type of conversion function.

#### `public virtual bool `[`GetParam`](#classgazebo_1_1_conversion_function_basic_1a943dbcaa6720093a775ebb7f3a1e3bea)`(std::string _tag,double & _output)` 

Return paramater in scalar form for the given tag.

#### `public virtual double `[`convert`](#classgazebo_1_1_conversion_function_basic_1a8f10f33118aeda7560214d915cee892e)`(double _cmd)` 

Convert thruster state (e.g. angular velocity) to thrust force.

