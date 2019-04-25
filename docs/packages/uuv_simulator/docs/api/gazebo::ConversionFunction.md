# class `gazebo::ConversionFunction` 

Abstact base class for a thruster conversion function.

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public inline virtual  `[`~ConversionFunction`](#classgazebo_1_1_conversion_function_1afc13b3997ac95f70425ec5fc830d927c)`()` | Destructor.
`public std::string `[`GetType`](#classgazebo_1_1_conversion_function_1ac0d2640de379ea86c087491c70bc6189)`()` | Return (derived) type of conversion function.
`public bool `[`GetParam`](#classgazebo_1_1_conversion_function_1a18c78fd782a8603afa893adc2a26f1a4)`(std::string _tag,double & _output)` | Return paramater in vector form for the given tag.
`public inline virtual std::map< double, double > `[`GetTable`](#classgazebo_1_1_conversion_function_1a9e0c3b99751eeaf95f96dd49ed0351a2)`()` | Return input and output vectors of the lookup table.
`public double `[`convert`](#classgazebo_1_1_conversion_function_1ac71ae91ae6e91ae177b8255477a2b950)`(double _cmd)` | Convert thruster state (e.g. angular velocity) to thrust force.
`protected inline  `[`ConversionFunction`](#classgazebo_1_1_conversion_function_1a70689912f6f1f316a84f2dea2e10050d)`()` | Protected constructor: Use the factory instead.

## Members

#### `public inline virtual  `[`~ConversionFunction`](#classgazebo_1_1_conversion_function_1afc13b3997ac95f70425ec5fc830d927c)`()` 

Destructor.

#### `public std::string `[`GetType`](#classgazebo_1_1_conversion_function_1ac0d2640de379ea86c087491c70bc6189)`()` 

Return (derived) type of conversion function.

#### `public bool `[`GetParam`](#classgazebo_1_1_conversion_function_1a18c78fd782a8603afa893adc2a26f1a4)`(std::string _tag,double & _output)` 

Return paramater in vector form for the given tag.

#### `public inline virtual std::map< double, double > `[`GetTable`](#classgazebo_1_1_conversion_function_1a9e0c3b99751eeaf95f96dd49ed0351a2)`()` 

Return input and output vectors of the lookup table.

#### `public double `[`convert`](#classgazebo_1_1_conversion_function_1ac71ae91ae6e91ae177b8255477a2b950)`(double _cmd)` 

Convert thruster state (e.g. angular velocity) to thrust force.

#### `protected inline  `[`ConversionFunction`](#classgazebo_1_1_conversion_function_1a70689912f6f1f316a84f2dea2e10050d)`()` 

Protected constructor: Use the factory instead.

