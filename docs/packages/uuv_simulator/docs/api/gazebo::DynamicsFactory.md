# class `gazebo::DynamicsFactory` 

Factory singleton class that creates a ThrusterDynamics from sdf.

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public `[`Dynamics`](docs/packages/uuv_simulator/docs/api/gazebo::Dynamics.md#classgazebo_1_1_dynamics)` * `[`CreateDynamics`](#classgazebo_1_1_dynamics_factory_1a7c041d73164da84de4a4677e7df83c88)`(sdf::ElementPtr _sdf)` | Create ThrusterDynamics object according to its sdf Description.
`public bool `[`RegisterCreator`](#classgazebo_1_1_dynamics_factory_1a46196328ff7188a0bc741da2ab3c4441)`(const std::string & _identifier,DynamicsCreator _creator)` | Register a ThrusterDynamic class with its creator.

## Members

#### `public `[`Dynamics`](docs/packages/uuv_simulator/docs/api/gazebo::Dynamics.md#classgazebo_1_1_dynamics)` * `[`CreateDynamics`](#classgazebo_1_1_dynamics_factory_1a7c041d73164da84de4a4677e7df83c88)`(sdf::ElementPtr _sdf)` 

Create ThrusterDynamics object according to its sdf Description.

#### `public bool `[`RegisterCreator`](#classgazebo_1_1_dynamics_factory_1a46196328ff7188a0bc741da2ab3c4441)`(const std::string & _identifier,DynamicsCreator _creator)` 

Register a ThrusterDynamic class with its creator.

