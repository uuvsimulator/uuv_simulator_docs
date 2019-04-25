# class `uuv_simulator_ros::UnderwaterObjectROSPlugin` 

```
class uuv_simulator_ros::UnderwaterObjectROSPlugin
  : public UnderwaterObjectPlugin
```  

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public  `[`UnderwaterObjectROSPlugin`](#classuuv__simulator__ros_1_1_underwater_object_r_o_s_plugin_1a6d26a8a5c08e79c0a149a07cf61209e0)`()` | Constructor.
`public virtual  `[`~UnderwaterObjectROSPlugin`](#classuuv__simulator__ros_1_1_underwater_object_r_o_s_plugin_1ae1eb17f91cb1383400138b6ef241a06f)`()` | Destructor.
`public void `[`Load`](#classuuv__simulator__ros_1_1_underwater_object_r_o_s_plugin_1a86c5be6309611c623757fca4565051c9)`(gazebo::physics::ModelPtr _parent,sdf::ElementPtr _sdf)` | Load module and read parameters from SDF.
`public virtual void `[`Init`](#classuuv__simulator__ros_1_1_underwater_object_r_o_s_plugin_1a3401922bc6e94cfcb5db27a99d2e4f0a)`()` | Initialize Module.
`public virtual void `[`Reset`](#classuuv__simulator__ros_1_1_underwater_object_r_o_s_plugin_1ae0316192f5b26fa321f3e64dd46287b7)`()` | Reset Module.
`public virtual void `[`Update`](#classuuv__simulator__ros_1_1_underwater_object_r_o_s_plugin_1a8f81a22f771bc1203365de1438452e7a)`(const gazebo::common::UpdateInfo & _info)` | Update the simulation state.
`public void `[`UpdateLocalCurrentVelocity`](#classuuv__simulator__ros_1_1_underwater_object_r_o_s_plugin_1a8796c2736835dc203cb7f9c7e84a923e)`(const geometry_msgs::Vector3::ConstPtr & _msg)` | Update the local current velocity, this data will be used only if the useGlobalCurrent flag is set to false.
`public bool `[`SetUseGlobalCurrentVel`](#classuuv__simulator__ros_1_1_underwater_object_r_o_s_plugin_1a038402f422a3940e426eec798f6a0d39)`(uuv_gazebo_ros_plugins_msgs::SetUseGlobalCurrentVel::Request & _req,uuv_gazebo_ros_plugins_msgs::SetUseGlobalCurrentVel::Response & _res)` | Set flag to use the global current velocity topic input.
`public bool `[`GetModelProperties`](#classuuv__simulator__ros_1_1_underwater_object_r_o_s_plugin_1a36c121c67de5ba30cd0770fc9b60ea26)`(uuv_gazebo_ros_plugins_msgs::GetModelProperties::Request & _req,uuv_gazebo_ros_plugins_msgs::GetModelProperties::Response & _res)` | Return the model properties, along with parameters from the hydrodynamic and hydrostatic models.
`public bool `[`SetScalingAddedMass`](#classuuv__simulator__ros_1_1_underwater_object_r_o_s_plugin_1a5d6cd010fa2f18ae91147c03ee9d1408)`(uuv_gazebo_ros_plugins_msgs::SetFloat::Request & _req,uuv_gazebo_ros_plugins_msgs::SetFloat::Response & _res)` | Set the scaling factor for the added-mass matrix.
`public bool `[`GetScalingAddedMass`](#classuuv__simulator__ros_1_1_underwater_object_r_o_s_plugin_1ad8ee29496336a958fa59c6fc35026729)`(uuv_gazebo_ros_plugins_msgs::GetFloat::Request & _req,uuv_gazebo_ros_plugins_msgs::GetFloat::Response & _res)` | Return current scaling factor for the added-mass matrix.
`public bool `[`SetScalingDamping`](#classuuv__simulator__ros_1_1_underwater_object_r_o_s_plugin_1a67861c1e99ee10a9c64f96d6401b221d)`(uuv_gazebo_ros_plugins_msgs::SetFloat::Request & _req,uuv_gazebo_ros_plugins_msgs::SetFloat::Response & _res)` | Set a scaling factor for the overall damping matrix.
`public bool `[`GetScalingDamping`](#classuuv__simulator__ros_1_1_underwater_object_r_o_s_plugin_1adc480b2b52d0da8a9c1d1b700d7bacd6)`(uuv_gazebo_ros_plugins_msgs::GetFloat::Request & _req,uuv_gazebo_ros_plugins_msgs::GetFloat::Response & _res)` | Return the scaling factor for the overall damping matrix.
`public bool `[`SetScalingVolume`](#classuuv__simulator__ros_1_1_underwater_object_r_o_s_plugin_1a2569924791d708d8d879c0fec853b5f4)`(uuv_gazebo_ros_plugins_msgs::SetFloat::Request & _req,uuv_gazebo_ros_plugins_msgs::SetFloat::Response & _res)` | Set scaling factor for the model's volume used for buoyancy force computation.
`public bool `[`GetScalingVolume`](#classuuv__simulator__ros_1_1_underwater_object_r_o_s_plugin_1a9eb2881a288725f83c9924b7be498c81)`(uuv_gazebo_ros_plugins_msgs::GetFloat::Request & _req,uuv_gazebo_ros_plugins_msgs::GetFloat::Response & _res)` | Get scaling factor for the model's volume used for buoyancy force computation.
`public bool `[`SetFluidDensity`](#classuuv__simulator__ros_1_1_underwater_object_r_o_s_plugin_1ac254edcbd59acb26fd70b70acad679c9)`(uuv_gazebo_ros_plugins_msgs::SetFloat::Request & _req,uuv_gazebo_ros_plugins_msgs::SetFloat::Response & _res)` | Set new fluid density (this will alter the value for the buoyancy force)
`public bool `[`GetFluidDensity`](#classuuv__simulator__ros_1_1_underwater_object_r_o_s_plugin_1a92c568850087edd355359e967f42d966)`(uuv_gazebo_ros_plugins_msgs::GetFloat::Request & _req,uuv_gazebo_ros_plugins_msgs::GetFloat::Response & _res)` | Get current value for the fluid density.
`public bool `[`SetOffsetVolume`](#classuuv__simulator__ros_1_1_underwater_object_r_o_s_plugin_1a473e7dae4ba36e061389cf4d193ce80d)`(uuv_gazebo_ros_plugins_msgs::SetFloat::Request & _req,uuv_gazebo_ros_plugins_msgs::SetFloat::Response & _res)` | Set offset factor for the model's volume (this will alter the value for the buoyancy force)
`public bool `[`GetOffsetVolume`](#classuuv__simulator__ros_1_1_underwater_object_r_o_s_plugin_1a70d64b6da3a18257bb1b4b1edc9afb3b)`(uuv_gazebo_ros_plugins_msgs::GetFloat::Request & _req,uuv_gazebo_ros_plugins_msgs::GetFloat::Response & _res)` | Return the offset factor for the model's volume.
`public bool `[`SetOffsetAddedMass`](#classuuv__simulator__ros_1_1_underwater_object_r_o_s_plugin_1ae062c4867e24ba3daf56032728fb3e9a)`(uuv_gazebo_ros_plugins_msgs::SetFloat::Request & _req,uuv_gazebo_ros_plugins_msgs::SetFloat::Response & _res)` | Set the offset factor for the added-mass matrix.
`public bool `[`GetOffsetAddedMass`](#classuuv__simulator__ros_1_1_underwater_object_r_o_s_plugin_1a317123306ae032c3cfb408553ed0706c)`(uuv_gazebo_ros_plugins_msgs::GetFloat::Request & _req,uuv_gazebo_ros_plugins_msgs::GetFloat::Response & _res)` | Return the offset factor for the added-mass matrix.
`public bool `[`SetOffsetLinearDamping`](#classuuv__simulator__ros_1_1_underwater_object_r_o_s_plugin_1a9b3127ae45a4972927bd7becc61a4cf4)`(uuv_gazebo_ros_plugins_msgs::SetFloat::Request & _req,uuv_gazebo_ros_plugins_msgs::SetFloat::Response & _res)` | Set the offset factor for the linear damping matrix.
`public bool `[`GetOffsetLinearDamping`](#classuuv__simulator__ros_1_1_underwater_object_r_o_s_plugin_1a979a847fb03c318d23809ef7e516f980)`(uuv_gazebo_ros_plugins_msgs::GetFloat::Request & _req,uuv_gazebo_ros_plugins_msgs::GetFloat::Response & _res)` | Return the offset factor for the linear damping matrix.
`public bool `[`SetOffsetLinearForwardSpeedDamping`](#classuuv__simulator__ros_1_1_underwater_object_r_o_s_plugin_1a85a1221c40202088731e56f1d7736bf1)`(uuv_gazebo_ros_plugins_msgs::SetFloat::Request & _req,uuv_gazebo_ros_plugins_msgs::SetFloat::Response & _res)` | Set the offset factor for the linear forward speed damping matrix.
`public bool `[`GetOffsetLinearForwardSpeedDamping`](#classuuv__simulator__ros_1_1_underwater_object_r_o_s_plugin_1a8c63d709fc992f899ffbe1eced7b6cd8)`(uuv_gazebo_ros_plugins_msgs::GetFloat::Request & _req,uuv_gazebo_ros_plugins_msgs::GetFloat::Response & _res)` | Return the offset factor for the linear forward speed damping matrix.
`public bool `[`SetOffsetNonLinearDamping`](#classuuv__simulator__ros_1_1_underwater_object_r_o_s_plugin_1a972ab56e380c00dcc489c0d9e9a4d0de)`(uuv_gazebo_ros_plugins_msgs::SetFloat::Request & _req,uuv_gazebo_ros_plugins_msgs::SetFloat::Response & _res)` | Set the offset factor for the nonlinear damping matrix.
`public bool `[`GetOffsetNonLinearDamping`](#classuuv__simulator__ros_1_1_underwater_object_r_o_s_plugin_1abc734c754de497bf62b13de980649f70)`(uuv_gazebo_ros_plugins_msgs::GetFloat::Request & _req,uuv_gazebo_ros_plugins_msgs::GetFloat::Response & _res)` | Return the offset factor for the nonlinear damping matrix.
`protected virtual void `[`PublishRestoringForce`](#classuuv__simulator__ros_1_1_underwater_object_r_o_s_plugin_1adf2dd5f72380c281f9176bd0e4e98f59)`(gazebo::physics::LinkPtr _link)` | Publish restoring force.
`protected virtual void `[`PublishHydrodynamicWrenches`](#classuuv__simulator__ros_1_1_underwater_object_r_o_s_plugin_1a22cd26dfdc7d64c8fa3b0a8d5ac40682)`(gazebo::physics::LinkPtr _link)` | Publish hydrodynamic wrenches.
`protected virtual void `[`GenWrenchMsg`](#classuuv__simulator__ros_1_1_underwater_object_r_o_s_plugin_1a62b50fa4ff5d5b36b78a2160bad1d500)`(ignition::math::Vector3d _force,ignition::math::Vector3d _torque,geometry_msgs::WrenchStamped & _output)` | Returns the wrench message for debugging topics.
`protected virtual void `[`InitDebug`](#classuuv__simulator__ros_1_1_underwater_object_r_o_s_plugin_1a5dbdc863b0902d14f77a3f31b585d0f8)`(gazebo::physics::LinkPtr _link,gazebo::HydrodynamicModelPtr _hydro)` | Sets the topics used for publishing the intermediate data during the simulation.
`protected virtual void `[`PublishCurrentVelocityMarker`](#classuuv__simulator__ros_1_1_underwater_object_r_o_s_plugin_1ae2defd15b338fe56edbbc87bfe364b6c)`()` | Publishes the current velocity marker.
`protected virtual void `[`PublishIsSubmerged`](#classuuv__simulator__ros_1_1_underwater_object_r_o_s_plugin_1afa9d2c09358d243270ee454905dcdb23)`()` | Publishes the state of the vehicle (is submerged)

## Members

#### `public  `[`UnderwaterObjectROSPlugin`](#classuuv__simulator__ros_1_1_underwater_object_r_o_s_plugin_1a6d26a8a5c08e79c0a149a07cf61209e0)`()` 

Constructor.

#### `public virtual  `[`~UnderwaterObjectROSPlugin`](#classuuv__simulator__ros_1_1_underwater_object_r_o_s_plugin_1ae1eb17f91cb1383400138b6ef241a06f)`()` 

Destructor.

#### `public void `[`Load`](#classuuv__simulator__ros_1_1_underwater_object_r_o_s_plugin_1a86c5be6309611c623757fca4565051c9)`(gazebo::physics::ModelPtr _parent,sdf::ElementPtr _sdf)` 

Load module and read parameters from SDF.

#### `public virtual void `[`Init`](#classuuv__simulator__ros_1_1_underwater_object_r_o_s_plugin_1a3401922bc6e94cfcb5db27a99d2e4f0a)`()` 

Initialize Module.

#### `public virtual void `[`Reset`](#classuuv__simulator__ros_1_1_underwater_object_r_o_s_plugin_1ae0316192f5b26fa321f3e64dd46287b7)`()` 

Reset Module.

#### `public virtual void `[`Update`](#classuuv__simulator__ros_1_1_underwater_object_r_o_s_plugin_1a8f81a22f771bc1203365de1438452e7a)`(const gazebo::common::UpdateInfo & _info)` 

Update the simulation state.

#### Parameters
* `_info` Information used in the update event.

#### `public void `[`UpdateLocalCurrentVelocity`](#classuuv__simulator__ros_1_1_underwater_object_r_o_s_plugin_1a8796c2736835dc203cb7f9c7e84a923e)`(const geometry_msgs::Vector3::ConstPtr & _msg)` 

Update the local current velocity, this data will be used only if the useGlobalCurrent flag is set to false.

#### `public bool `[`SetUseGlobalCurrentVel`](#classuuv__simulator__ros_1_1_underwater_object_r_o_s_plugin_1a038402f422a3940e426eec798f6a0d39)`(uuv_gazebo_ros_plugins_msgs::SetUseGlobalCurrentVel::Request & _req,uuv_gazebo_ros_plugins_msgs::SetUseGlobalCurrentVel::Response & _res)` 

Set flag to use the global current velocity topic input.

#### `public bool `[`GetModelProperties`](#classuuv__simulator__ros_1_1_underwater_object_r_o_s_plugin_1a36c121c67de5ba30cd0770fc9b60ea26)`(uuv_gazebo_ros_plugins_msgs::GetModelProperties::Request & _req,uuv_gazebo_ros_plugins_msgs::GetModelProperties::Response & _res)` 

Return the model properties, along with parameters from the hydrodynamic and hydrostatic models.

#### `public bool `[`SetScalingAddedMass`](#classuuv__simulator__ros_1_1_underwater_object_r_o_s_plugin_1a5d6cd010fa2f18ae91147c03ee9d1408)`(uuv_gazebo_ros_plugins_msgs::SetFloat::Request & _req,uuv_gazebo_ros_plugins_msgs::SetFloat::Response & _res)` 

Set the scaling factor for the added-mass matrix.

#### `public bool `[`GetScalingAddedMass`](#classuuv__simulator__ros_1_1_underwater_object_r_o_s_plugin_1ad8ee29496336a958fa59c6fc35026729)`(uuv_gazebo_ros_plugins_msgs::GetFloat::Request & _req,uuv_gazebo_ros_plugins_msgs::GetFloat::Response & _res)` 

Return current scaling factor for the added-mass matrix.

#### `public bool `[`SetScalingDamping`](#classuuv__simulator__ros_1_1_underwater_object_r_o_s_plugin_1a67861c1e99ee10a9c64f96d6401b221d)`(uuv_gazebo_ros_plugins_msgs::SetFloat::Request & _req,uuv_gazebo_ros_plugins_msgs::SetFloat::Response & _res)` 

Set a scaling factor for the overall damping matrix.

#### `public bool `[`GetScalingDamping`](#classuuv__simulator__ros_1_1_underwater_object_r_o_s_plugin_1adc480b2b52d0da8a9c1d1b700d7bacd6)`(uuv_gazebo_ros_plugins_msgs::GetFloat::Request & _req,uuv_gazebo_ros_plugins_msgs::GetFloat::Response & _res)` 

Return the scaling factor for the overall damping matrix.

#### `public bool `[`SetScalingVolume`](#classuuv__simulator__ros_1_1_underwater_object_r_o_s_plugin_1a2569924791d708d8d879c0fec853b5f4)`(uuv_gazebo_ros_plugins_msgs::SetFloat::Request & _req,uuv_gazebo_ros_plugins_msgs::SetFloat::Response & _res)` 

Set scaling factor for the model's volume used for buoyancy force computation.

#### `public bool `[`GetScalingVolume`](#classuuv__simulator__ros_1_1_underwater_object_r_o_s_plugin_1a9eb2881a288725f83c9924b7be498c81)`(uuv_gazebo_ros_plugins_msgs::GetFloat::Request & _req,uuv_gazebo_ros_plugins_msgs::GetFloat::Response & _res)` 

Get scaling factor for the model's volume used for buoyancy force computation.

#### `public bool `[`SetFluidDensity`](#classuuv__simulator__ros_1_1_underwater_object_r_o_s_plugin_1ac254edcbd59acb26fd70b70acad679c9)`(uuv_gazebo_ros_plugins_msgs::SetFloat::Request & _req,uuv_gazebo_ros_plugins_msgs::SetFloat::Response & _res)` 

Set new fluid density (this will alter the value for the buoyancy force)

#### `public bool `[`GetFluidDensity`](#classuuv__simulator__ros_1_1_underwater_object_r_o_s_plugin_1a92c568850087edd355359e967f42d966)`(uuv_gazebo_ros_plugins_msgs::GetFloat::Request & _req,uuv_gazebo_ros_plugins_msgs::GetFloat::Response & _res)` 

Get current value for the fluid density.

#### `public bool `[`SetOffsetVolume`](#classuuv__simulator__ros_1_1_underwater_object_r_o_s_plugin_1a473e7dae4ba36e061389cf4d193ce80d)`(uuv_gazebo_ros_plugins_msgs::SetFloat::Request & _req,uuv_gazebo_ros_plugins_msgs::SetFloat::Response & _res)` 

Set offset factor for the model's volume (this will alter the value for the buoyancy force)

#### `public bool `[`GetOffsetVolume`](#classuuv__simulator__ros_1_1_underwater_object_r_o_s_plugin_1a70d64b6da3a18257bb1b4b1edc9afb3b)`(uuv_gazebo_ros_plugins_msgs::GetFloat::Request & _req,uuv_gazebo_ros_plugins_msgs::GetFloat::Response & _res)` 

Return the offset factor for the model's volume.

#### `public bool `[`SetOffsetAddedMass`](#classuuv__simulator__ros_1_1_underwater_object_r_o_s_plugin_1ae062c4867e24ba3daf56032728fb3e9a)`(uuv_gazebo_ros_plugins_msgs::SetFloat::Request & _req,uuv_gazebo_ros_plugins_msgs::SetFloat::Response & _res)` 

Set the offset factor for the added-mass matrix.

#### `public bool `[`GetOffsetAddedMass`](#classuuv__simulator__ros_1_1_underwater_object_r_o_s_plugin_1a317123306ae032c3cfb408553ed0706c)`(uuv_gazebo_ros_plugins_msgs::GetFloat::Request & _req,uuv_gazebo_ros_plugins_msgs::GetFloat::Response & _res)` 

Return the offset factor for the added-mass matrix.

#### `public bool `[`SetOffsetLinearDamping`](#classuuv__simulator__ros_1_1_underwater_object_r_o_s_plugin_1a9b3127ae45a4972927bd7becc61a4cf4)`(uuv_gazebo_ros_plugins_msgs::SetFloat::Request & _req,uuv_gazebo_ros_plugins_msgs::SetFloat::Response & _res)` 

Set the offset factor for the linear damping matrix.

#### `public bool `[`GetOffsetLinearDamping`](#classuuv__simulator__ros_1_1_underwater_object_r_o_s_plugin_1a979a847fb03c318d23809ef7e516f980)`(uuv_gazebo_ros_plugins_msgs::GetFloat::Request & _req,uuv_gazebo_ros_plugins_msgs::GetFloat::Response & _res)` 

Return the offset factor for the linear damping matrix.

#### `public bool `[`SetOffsetLinearForwardSpeedDamping`](#classuuv__simulator__ros_1_1_underwater_object_r_o_s_plugin_1a85a1221c40202088731e56f1d7736bf1)`(uuv_gazebo_ros_plugins_msgs::SetFloat::Request & _req,uuv_gazebo_ros_plugins_msgs::SetFloat::Response & _res)` 

Set the offset factor for the linear forward speed damping matrix.

#### `public bool `[`GetOffsetLinearForwardSpeedDamping`](#classuuv__simulator__ros_1_1_underwater_object_r_o_s_plugin_1a8c63d709fc992f899ffbe1eced7b6cd8)`(uuv_gazebo_ros_plugins_msgs::GetFloat::Request & _req,uuv_gazebo_ros_plugins_msgs::GetFloat::Response & _res)` 

Return the offset factor for the linear forward speed damping matrix.

#### `public bool `[`SetOffsetNonLinearDamping`](#classuuv__simulator__ros_1_1_underwater_object_r_o_s_plugin_1a972ab56e380c00dcc489c0d9e9a4d0de)`(uuv_gazebo_ros_plugins_msgs::SetFloat::Request & _req,uuv_gazebo_ros_plugins_msgs::SetFloat::Response & _res)` 

Set the offset factor for the nonlinear damping matrix.

#### `public bool `[`GetOffsetNonLinearDamping`](#classuuv__simulator__ros_1_1_underwater_object_r_o_s_plugin_1abc734c754de497bf62b13de980649f70)`(uuv_gazebo_ros_plugins_msgs::GetFloat::Request & _req,uuv_gazebo_ros_plugins_msgs::GetFloat::Response & _res)` 

Return the offset factor for the nonlinear damping matrix.

#### `protected virtual void `[`PublishRestoringForce`](#classuuv__simulator__ros_1_1_underwater_object_r_o_s_plugin_1adf2dd5f72380c281f9176bd0e4e98f59)`(gazebo::physics::LinkPtr _link)` 

Publish restoring force.

#### Parameters
* `_link` Pointer to the link where the force information will be extracted from

#### `protected virtual void `[`PublishHydrodynamicWrenches`](#classuuv__simulator__ros_1_1_underwater_object_r_o_s_plugin_1a22cd26dfdc7d64c8fa3b0a8d5ac40682)`(gazebo::physics::LinkPtr _link)` 

Publish hydrodynamic wrenches.

#### Parameters
* `_link` Pointer to the link where the force information will be extracted from

#### `protected virtual void `[`GenWrenchMsg`](#classuuv__simulator__ros_1_1_underwater_object_r_o_s_plugin_1a62b50fa4ff5d5b36b78a2160bad1d500)`(ignition::math::Vector3d _force,ignition::math::Vector3d _torque,geometry_msgs::WrenchStamped & _output)` 

Returns the wrench message for debugging topics.

#### Parameters
* `_force` Force vector 

* `_torque` Torque vector 

* `_output` Stamped wrench message to be updated

#### `protected virtual void `[`InitDebug`](#classuuv__simulator__ros_1_1_underwater_object_r_o_s_plugin_1a5dbdc863b0902d14f77a3f31b585d0f8)`(gazebo::physics::LinkPtr _link,gazebo::HydrodynamicModelPtr _hydro)` 

Sets the topics used for publishing the intermediate data during the simulation.

#### Parameters
* `_link` Pointer to the link 

* `_hydro` Pointer to the hydrodynamic model

#### `protected virtual void `[`PublishCurrentVelocityMarker`](#classuuv__simulator__ros_1_1_underwater_object_r_o_s_plugin_1ae2defd15b338fe56edbbc87bfe364b6c)`()` 

Publishes the current velocity marker.

#### `protected virtual void `[`PublishIsSubmerged`](#classuuv__simulator__ros_1_1_underwater_object_r_o_s_plugin_1afa9d2c09358d243270ee454905dcdb23)`()` 

Publishes the state of the vehicle (is submerged)

