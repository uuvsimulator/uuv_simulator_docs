# class `gazebo::HydrodynamicModelFactory` 

Factory singleton class that creates a [HydrodynamicModel](docs/packages/uuv_simulator/docs/api/gazebo::HydrodynamicModel.md#classgazebo_1_1_hydrodynamic_model) from sdf.

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public `[`HydrodynamicModel`](docs/packages/uuv_simulator/docs/api/gazebo::HydrodynamicModel.md#classgazebo_1_1_hydrodynamic_model)` * `[`CreateHydrodynamicModel`](#classgazebo_1_1_hydrodynamic_model_factory_1a4113b1faaf8277574e4a4b3854f51884)`(sdf::ElementPtr _sdf,physics::LinkPtr _link)` | Create [HydrodynamicModel](docs/packages/uuv_simulator/docs/api/gazebo::HydrodynamicModel.md#classgazebo_1_1_hydrodynamic_model) object according to its sdf Description.
`public bool `[`RegisterCreator`](#classgazebo_1_1_hydrodynamic_model_factory_1acc1cc6c8730ee4e0d558d4fbfa96ecb5)`(const std::string & _identifier,HydrodynamicModelCreator _creator)` | Register a class with its creator.

## Members

#### `public `[`HydrodynamicModel`](docs/packages/uuv_simulator/docs/api/gazebo::HydrodynamicModel.md#classgazebo_1_1_hydrodynamic_model)` * `[`CreateHydrodynamicModel`](#classgazebo_1_1_hydrodynamic_model_factory_1a4113b1faaf8277574e4a4b3854f51884)`(sdf::ElementPtr _sdf,physics::LinkPtr _link)` 

Create [HydrodynamicModel](docs/packages/uuv_simulator/docs/api/gazebo::HydrodynamicModel.md#classgazebo_1_1_hydrodynamic_model) object according to its sdf Description.

#### `public bool `[`RegisterCreator`](#classgazebo_1_1_hydrodynamic_model_factory_1acc1cc6c8730ee4e0d558d4fbfa96ecb5)`(const std::string & _identifier,HydrodynamicModelCreator _creator)` 

Register a class with its creator.

