# class `gazebo::ConversionFunctionLinearInterp` 

```
class gazebo::ConversionFunctionLinearInterp
  : public gazebo::ConversionFunction
```  

Conversion using linear interpolation between given data points.

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public inline virtual std::string `[`GetType`](#classgazebo_1_1_conversion_function_linear_interp_1a949ed2e6176730ef0322a25a1a86c92c)`()` | Return (derived) type of conversion function.
`public virtual bool `[`GetParam`](#classgazebo_1_1_conversion_function_linear_interp_1aa443515bbf8913e8d5fef758a6f21b71)`(std::string _tag,double & _output)` | Return paramater in scalar form for the given tag.
`public virtual std::map< double, double > `[`GetTable`](#classgazebo_1_1_conversion_function_linear_interp_1a2252ec3701319511a8d7ef2bbdf25a70)`()` | Return input and output vectors of the lookup table.
`public virtual double `[`convert`](#classgazebo_1_1_conversion_function_linear_interp_1ae0bfc703bbbe5eef389fedf5565b10c1)`(double _cmd)` | Convert thruster state (e.g. angular velocity) to thrust force.

## Members

#### `public inline virtual std::string `[`GetType`](#classgazebo_1_1_conversion_function_linear_interp_1a949ed2e6176730ef0322a25a1a86c92c)`()` 

Return (derived) type of conversion function.

#### `public virtual bool `[`GetParam`](#classgazebo_1_1_conversion_function_linear_interp_1aa443515bbf8913e8d5fef758a6f21b71)`(std::string _tag,double & _output)` 

Return paramater in scalar form for the given tag.

#### `public virtual std::map< double, double > `[`GetTable`](#classgazebo_1_1_conversion_function_linear_interp_1a2252ec3701319511a8d7ef2bbdf25a70)`()` 

Return input and output vectors of the lookup table.

#### `public virtual double `[`convert`](#classgazebo_1_1_conversion_function_linear_interp_1ae0bfc703bbbe5eef389fedf5565b10c1)`(double _cmd)` 

Convert thruster state (e.g. angular velocity) to thrust force.

