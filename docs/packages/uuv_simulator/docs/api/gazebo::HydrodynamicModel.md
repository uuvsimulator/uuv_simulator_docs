# class `gazebo::HydrodynamicModel` 

```
class gazebo::HydrodynamicModel
  : public gazebo::BuoyantObject
```  

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public std::string `[`GetType`](#classgazebo_1_1_hydrodynamic_model_1a16e39024389414178442d4278c16222a)`()` | Returns type of model.
`public void `[`ApplyHydrodynamicForces`](#classgazebo_1_1_hydrodynamic_model_1a365a5ea0d71ad3ec3d79f985c42c2417)`(double time,const ignition::math::Vector3d & _flowVelWorld)` | Computation of the hydrodynamic forces.
`public void `[`Print`](#classgazebo_1_1_hydrodynamic_model_1aead6d1b6eefebe5034bb86adcbf1169a)`(std::string _paramName,std::string _message)` | Prints parameters.
`public bool `[`GetParam`](#classgazebo_1_1_hydrodynamic_model_1ac123271c564f843fb280713704d20f7e)`(std::string _tag,std::vector< double > & _output)` | Return paramater in vector form for the given tag.
`public bool `[`GetParam`](#classgazebo_1_1_hydrodynamic_model_1addaa35736ce4bc798ab70ace59a0a9e8)`(std::string _tag,double & _output)` | Return paramater in vector form for the given tag.
`public bool `[`SetParam`](#classgazebo_1_1_hydrodynamic_model_1a173db3079e94e656abcaf44d61ea3ba2)`(std::string _tag,double _input)` | Set a scalar parameters.
`protected `[`Eigen::Vector6d`](docs/packages/uuv_simulator/docs/api/Vector6d.md#_def_8hh_1a09219f5e0b822edbf24b125e0e2a4fe0)` `[`filteredAcc`](#classgazebo_1_1_hydrodynamic_model_1a9d402a541867397d32247de6746ab5de) | Filtered linear & angular acceleration vector in link frame. This is used to prevent the model to become unstable given that Gazebo only calls the update function at the beginning or at the end of a iteration of the physics engine.
`protected double `[`lastTime`](#classgazebo_1_1_hydrodynamic_model_1a212a914dc81067558c637d308773e23e) | Last timestamp (in seconds) at which ApplyHydrodynamicForces was called.
`protected `[`Eigen::Vector6d`](docs/packages/uuv_simulator/docs/api/Vector6d.md#_def_8hh_1a09219f5e0b822edbf24b125e0e2a4fe0)` `[`lastVelRel`](#classgazebo_1_1_hydrodynamic_model_1affd2dff3e08a26ac9e00ee2ebaff6016) | Last body-fixed relative velocity (nu_R in Fossen's equations)
`protected std::vector< std::string > `[`params`](#classgazebo_1_1_hydrodynamic_model_1a6152abe7eda7e10157ed72696d87be38) | List of parameters needed from the SDF element.
`protected double `[`Re`](#classgazebo_1_1_hydrodynamic_model_1ae82075119ebbf0d7f3f0ea13b6aeb6cf) | Reynolds number (not used by all models)
`protected double `[`temperature`](#classgazebo_1_1_hydrodynamic_model_1adf0cb47bd32f552c285f4cf5eeec9d36) | Temperature (not used by all models)
`protected  `[`HydrodynamicModel`](#classgazebo_1_1_hydrodynamic_model_1aac68d5a44688757965ccf0e9d648c8b8)`(sdf::ElementPtr _sdf,physics::LinkPtr _link)` | Protected constructor: Use the factory for object creation.
`protected void `[`ComputeAcc`](#classgazebo_1_1_hydrodynamic_model_1abb6cf4e433202d163b1276d67434ace2)`(`[`Eigen::Vector6d`](docs/packages/uuv_simulator/docs/api/Vector6d.md#_def_8hh_1a09219f5e0b822edbf24b125e0e2a4fe0)` _velRel,double _time,double _alpha)` | Filter acceleration (fix due to the update structure of Gazebo)
`protected bool `[`CheckParams`](#classgazebo_1_1_hydrodynamic_model_1a729f90fa3933d2fd9aeed5fdb7838f1b)`(sdf::ElementPtr _sdf)` | Returns true if all parameters are available from the SDF element.
`protected ignition::math::Vector3d `[`ToNED`](#classgazebo_1_1_hydrodynamic_model_1a46a25bbc280aa3d466268756c7362809)`(ignition::math::Vector3d _vec)` | Convert vector to comply with the NED reference frame.
`protected ignition::math::Vector3d `[`FromNED`](#classgazebo_1_1_hydrodynamic_model_1a715caa11d851a41265d0d682301e3781)`(ignition::math::Vector3d _vec)` | Convert vector to comply with the NED reference frame.

## Members

#### `public std::string `[`GetType`](#classgazebo_1_1_hydrodynamic_model_1a16e39024389414178442d4278c16222a)`()` 

Returns type of model.

#### `public void `[`ApplyHydrodynamicForces`](#classgazebo_1_1_hydrodynamic_model_1a365a5ea0d71ad3ec3d79f985c42c2417)`(double time,const ignition::math::Vector3d & _flowVelWorld)` 

Computation of the hydrodynamic forces.

#### `public void `[`Print`](#classgazebo_1_1_hydrodynamic_model_1aead6d1b6eefebe5034bb86adcbf1169a)`(std::string _paramName,std::string _message)` 

Prints parameters.

#### `public bool `[`GetParam`](#classgazebo_1_1_hydrodynamic_model_1ac123271c564f843fb280713704d20f7e)`(std::string _tag,std::vector< double > & _output)` 

Return paramater in vector form for the given tag.

#### `public bool `[`GetParam`](#classgazebo_1_1_hydrodynamic_model_1addaa35736ce4bc798ab70ace59a0a9e8)`(std::string _tag,double & _output)` 

Return paramater in vector form for the given tag.

#### `public bool `[`SetParam`](#classgazebo_1_1_hydrodynamic_model_1a173db3079e94e656abcaf44d61ea3ba2)`(std::string _tag,double _input)` 

Set a scalar parameters.

#### `protected `[`Eigen::Vector6d`](docs/packages/uuv_simulator/docs/api/Vector6d.md#_def_8hh_1a09219f5e0b822edbf24b125e0e2a4fe0)` `[`filteredAcc`](#classgazebo_1_1_hydrodynamic_model_1a9d402a541867397d32247de6746ab5de) 

Filtered linear & angular acceleration vector in link frame. This is used to prevent the model to become unstable given that Gazebo only calls the update function at the beginning or at the end of a iteration of the physics engine.

#### `protected double `[`lastTime`](#classgazebo_1_1_hydrodynamic_model_1a212a914dc81067558c637d308773e23e) 

Last timestamp (in seconds) at which ApplyHydrodynamicForces was called.

#### `protected `[`Eigen::Vector6d`](docs/packages/uuv_simulator/docs/api/Vector6d.md#_def_8hh_1a09219f5e0b822edbf24b125e0e2a4fe0)` `[`lastVelRel`](#classgazebo_1_1_hydrodynamic_model_1affd2dff3e08a26ac9e00ee2ebaff6016) 

Last body-fixed relative velocity (nu_R in Fossen's equations)

#### `protected std::vector< std::string > `[`params`](#classgazebo_1_1_hydrodynamic_model_1a6152abe7eda7e10157ed72696d87be38) 

List of parameters needed from the SDF element.

#### `protected double `[`Re`](#classgazebo_1_1_hydrodynamic_model_1ae82075119ebbf0d7f3f0ea13b6aeb6cf) 

Reynolds number (not used by all models)

#### `protected double `[`temperature`](#classgazebo_1_1_hydrodynamic_model_1adf0cb47bd32f552c285f4cf5eeec9d36) 

Temperature (not used by all models)

#### `protected  `[`HydrodynamicModel`](#classgazebo_1_1_hydrodynamic_model_1aac68d5a44688757965ccf0e9d648c8b8)`(sdf::ElementPtr _sdf,physics::LinkPtr _link)` 

Protected constructor: Use the factory for object creation.

#### `protected void `[`ComputeAcc`](#classgazebo_1_1_hydrodynamic_model_1abb6cf4e433202d163b1276d67434ace2)`(`[`Eigen::Vector6d`](docs/packages/uuv_simulator/docs/api/Vector6d.md#_def_8hh_1a09219f5e0b822edbf24b125e0e2a4fe0)` _velRel,double _time,double _alpha)` 

Filter acceleration (fix due to the update structure of Gazebo)

#### `protected bool `[`CheckParams`](#classgazebo_1_1_hydrodynamic_model_1a729f90fa3933d2fd9aeed5fdb7838f1b)`(sdf::ElementPtr _sdf)` 

Returns true if all parameters are available from the SDF element.

#### `protected ignition::math::Vector3d `[`ToNED`](#classgazebo_1_1_hydrodynamic_model_1a46a25bbc280aa3d466268756c7362809)`(ignition::math::Vector3d _vec)` 

Convert vector to comply with the NED reference frame.

#### `protected ignition::math::Vector3d `[`FromNED`](#classgazebo_1_1_hydrodynamic_model_1a715caa11d851a41265d0d682301e3781)`(ignition::math::Vector3d _vec)` 

Convert vector to comply with the NED reference frame.

