# class `gazebo::UmbilicalModelFactory` 

Factory singleton class that creates an [UmbilicalModel](docs/packages/uuv_simulator/docs/api/gazebo::UmbilicalModel.md#classgazebo_1_1_umbilical_model) from sdf.

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public `[`UmbilicalModel`](docs/packages/uuv_simulator/docs/api/gazebo::UmbilicalModel.md#classgazebo_1_1_umbilical_model)` * `[`CreateUmbilicalModel`](#classgazebo_1_1_umbilical_model_factory_1ac7a7245f47500ee02e68f84c5e7a5032)`(sdf::ElementPtr _sdf,physics::ModelPtr _model)` | Create a [ConversionFunction](docs/packages/uuv_simulator/docs/api/gazebo::ConversionFunction.md#classgazebo_1_1_conversion_function) object according to its sdf Description.
`public bool `[`RegisterCreator`](#classgazebo_1_1_umbilical_model_factory_1a97c20262e741c090c7616f082a23869e)`(const std::string & _identifier,UmbilicalModelCreator _creator)` | Register an [UmbilicalModel](docs/packages/uuv_simulator/docs/api/gazebo::UmbilicalModel.md#classgazebo_1_1_umbilical_model) class with its creator.

## Members

#### `public `[`UmbilicalModel`](docs/packages/uuv_simulator/docs/api/gazebo::UmbilicalModel.md#classgazebo_1_1_umbilical_model)` * `[`CreateUmbilicalModel`](#classgazebo_1_1_umbilical_model_factory_1ac7a7245f47500ee02e68f84c5e7a5032)`(sdf::ElementPtr _sdf,physics::ModelPtr _model)` 

Create a [ConversionFunction](docs/packages/uuv_simulator/docs/api/gazebo::ConversionFunction.md#classgazebo_1_1_conversion_function) object according to its sdf Description.

#### `public bool `[`RegisterCreator`](#classgazebo_1_1_umbilical_model_factory_1a97c20262e741c090c7616f082a23869e)`(const std::string & _identifier,UmbilicalModelCreator _creator)` 

Register an [UmbilicalModel](docs/packages/uuv_simulator/docs/api/gazebo::UmbilicalModel.md#classgazebo_1_1_umbilical_model) class with its creator.

