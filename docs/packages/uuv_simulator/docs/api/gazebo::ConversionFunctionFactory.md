# class `gazebo::ConversionFunctionFactory` 

Factory singleton class that creates a [ConversionFunction](docs/packages/uuv_simulator/docs/api/gazebo::ConversionFunction.md#classgazebo_1_1_conversion_function) from sdf.

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public `[`ConversionFunction`](docs/packages/uuv_simulator/docs/api/gazebo::ConversionFunction.md#classgazebo_1_1_conversion_function)` * `[`CreateConversionFunction`](#classgazebo_1_1_conversion_function_factory_1a26d4ebd40ed459a7fb5ed382822ecc33)`(sdf::ElementPtr _sdf)` | Create a [ConversionFunction](docs/packages/uuv_simulator/docs/api/gazebo::ConversionFunction.md#classgazebo_1_1_conversion_function) object according to its sdf Description.
`public bool `[`RegisterCreator`](#classgazebo_1_1_conversion_function_factory_1ac25e17bcce4a2fd6f0cf42f2ead733b0)`(const std::string & _identifier,ConversionFunctionCreator _creator)` | Register a [ConversionFunction](docs/packages/uuv_simulator/docs/api/gazebo::ConversionFunction.md#classgazebo_1_1_conversion_function) class with its creator.

## Members

#### `public `[`ConversionFunction`](docs/packages/uuv_simulator/docs/api/gazebo::ConversionFunction.md#classgazebo_1_1_conversion_function)` * `[`CreateConversionFunction`](#classgazebo_1_1_conversion_function_factory_1a26d4ebd40ed459a7fb5ed382822ecc33)`(sdf::ElementPtr _sdf)` 

Create a [ConversionFunction](docs/packages/uuv_simulator/docs/api/gazebo::ConversionFunction.md#classgazebo_1_1_conversion_function) object according to its sdf Description.

#### `public bool `[`RegisterCreator`](#classgazebo_1_1_conversion_function_factory_1ac25e17bcce4a2fd6f0cf42f2ead733b0)`(const std::string & _identifier,ConversionFunctionCreator _creator)` 

Register a [ConversionFunction](docs/packages/uuv_simulator/docs/api/gazebo::ConversionFunction.md#classgazebo_1_1_conversion_function) class with its creator.

