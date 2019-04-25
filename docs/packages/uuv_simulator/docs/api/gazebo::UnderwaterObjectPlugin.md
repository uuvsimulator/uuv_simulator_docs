# class `gazebo::UnderwaterObjectPlugin` 

```
class gazebo::UnderwaterObjectPlugin
  : public ModelPlugin
```  

Gazebo model plugin class for underwater objects.

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public  `[`UnderwaterObjectPlugin`](#classgazebo_1_1_underwater_object_plugin_1ac875088ebde0583e6f3e07cdeaea53ae)`()` | Constructor.
`public virtual  `[`~UnderwaterObjectPlugin`](#classgazebo_1_1_underwater_object_plugin_1af97f83bac0327ebc2671839c56f44207)`()` | Destructor.
`public virtual void `[`Load`](#classgazebo_1_1_underwater_object_plugin_1acaa3bd6b66429cb588fbcba3ae70be74)`(gazebo::physics::ModelPtr _model,sdf::ElementPtr _sdf)` | 
`public virtual void `[`Init`](#classgazebo_1_1_underwater_object_plugin_1afbe0672e704e832adf5619fd7c34cd5c)`()` | 
`public virtual void `[`Update`](#classgazebo_1_1_underwater_object_plugin_1ad5893829b75bed2bb052bef467d6dcf4)`(const gazebo::common::UpdateInfo & _info)` | Update the simulation state.
`protected std::map< gazebo::physics::LinkPtr, `[`HydrodynamicModelPtr`](docs/packages/uuv_simulator/docs/api/HydrodynamicModelPtr.md#_hydrodynamic_model_8hh_1ab7e72448c3e86f93ab214d73c0cd4414)` > `[`models`](#classgazebo_1_1_underwater_object_plugin_1abbc883398252e410563c657648743e3e) | Pairs of links & corresponding hydrodynamic models.
`protected ignition::math::Vector3d `[`flowVelocity`](#classgazebo_1_1_underwater_object_plugin_1ac5bf6578ef4434438ba7d7647b69b971) | Flow velocity vector read from topic.
`protected gazebo::event::ConnectionPtr `[`updateConnection`](#classgazebo_1_1_underwater_object_plugin_1a1a4d81782ad2d21fc01598e0d9b42d27) | Update event.
`protected gazebo::physics::WorldPtr `[`world`](#classgazebo_1_1_underwater_object_plugin_1a9f16fc2908d17c0975331cc825d14cb0) | Pointer to the world plugin.
`protected gazebo::physics::ModelPtr `[`model`](#classgazebo_1_1_underwater_object_plugin_1a896d92ed527a0d9f7b47208614eaba0c) | Pointer to the model structure.
`protected gazebo::transport::NodePtr `[`node`](#classgazebo_1_1_underwater_object_plugin_1a5422d922731696d2767e5be09c2cb5c2) | Gazebo node.
`protected std::string `[`baseLinkName`](#classgazebo_1_1_underwater_object_plugin_1a08b0e6dfab6a63945ea6d1c71c858df1) | Name of vehicle's base_link.
`protected gazebo::transport::SubscriberPtr `[`flowSubscriber`](#classgazebo_1_1_underwater_object_plugin_1adb22008a9f57f11659e2b2a18d57bcc6) | Subcriber to flow message.
`protected bool `[`useGlobalCurrent`](#classgazebo_1_1_underwater_object_plugin_1a0bfd19ce74a42666f26fefa0ded488f3) | Flag to use the global current velocity or the individually assigned current velocity.
`protected std::map< std::string, gazebo::transport::PublisherPtr > `[`hydroPub`](#classgazebo_1_1_underwater_object_plugin_1a33989646c81bc47fe86dae3052846ea2) | Publishers of hydrodynamic and hydrostatic forces and torques in the case the debug flag is on.
`protected virtual void `[`Connect`](#classgazebo_1_1_underwater_object_plugin_1a7497acca39dc0a4f338bd863b002ec33)`()` | Connects the update event callback.
`protected void `[`UpdateFlowVelocity`](#classgazebo_1_1_underwater_object_plugin_1a22bb6d230cc76b4a838ffffe5a6ba722)`(ConstVector3dPtr & _msg)` | Reads flow velocity topic.
`protected virtual void `[`PublishCurrentVelocityMarker`](#classgazebo_1_1_underwater_object_plugin_1a89d8430bc839e0ff477fd893be829060)`()` | Publish current velocity marker.
`protected virtual void `[`PublishIsSubmerged`](#classgazebo_1_1_underwater_object_plugin_1adc2e3f16a6fa8ce79497b5664fb66b82)`()` | Publishes the state of the vehicle (is submerged)
`protected virtual void `[`PublishRestoringForce`](#classgazebo_1_1_underwater_object_plugin_1ae5da81b93706dded6de765628f57ad05)`(gazebo::physics::LinkPtr _link)` | Publish restoring force.
`protected virtual void `[`PublishHydrodynamicWrenches`](#classgazebo_1_1_underwater_object_plugin_1af1b5370bf8ebd626fd9eafb2b46075b9)`(gazebo::physics::LinkPtr _link)` | Publish hydrodynamic wrenches.
`protected virtual void `[`GenWrenchMsg`](#classgazebo_1_1_underwater_object_plugin_1a6deb4663c719f288b671539020257bb0)`(ignition::math::Vector3d _force,ignition::math::Vector3d _torque,gazebo::msgs::WrenchStamped & _output)` | Returns the wrench message for debugging topics.
`protected virtual void `[`InitDebug`](#classgazebo_1_1_underwater_object_plugin_1a86136f608b56ecd79bd6530f92724a75)`(gazebo::physics::LinkPtr _link,`[`gazebo::HydrodynamicModelPtr`](docs/packages/uuv_simulator/docs/api/HydrodynamicModelPtr.md#_hydrodynamic_model_8hh_1ab7e72448c3e86f93ab214d73c0cd4414)` _hydro)` | Sets the topics used for publishing the intermediate data during the simulation.

## Members

#### `public  `[`UnderwaterObjectPlugin`](#classgazebo_1_1_underwater_object_plugin_1ac875088ebde0583e6f3e07cdeaea53ae)`()` 

Constructor.

#### `public virtual  `[`~UnderwaterObjectPlugin`](#classgazebo_1_1_underwater_object_plugin_1af97f83bac0327ebc2671839c56f44207)`()` 

Destructor.

#### `public virtual void `[`Load`](#classgazebo_1_1_underwater_object_plugin_1acaa3bd6b66429cb588fbcba3ae70be74)`(gazebo::physics::ModelPtr _model,sdf::ElementPtr _sdf)` 

#### `public virtual void `[`Init`](#classgazebo_1_1_underwater_object_plugin_1afbe0672e704e832adf5619fd7c34cd5c)`()` 

#### `public virtual void `[`Update`](#classgazebo_1_1_underwater_object_plugin_1ad5893829b75bed2bb052bef467d6dcf4)`(const gazebo::common::UpdateInfo & _info)` 

Update the simulation state.

#### Parameters
* `_info` Information used in the update event.

#### `protected std::map< gazebo::physics::LinkPtr, `[`HydrodynamicModelPtr`](docs/packages/uuv_simulator/docs/api/HydrodynamicModelPtr.md#_hydrodynamic_model_8hh_1ab7e72448c3e86f93ab214d73c0cd4414)` > `[`models`](#classgazebo_1_1_underwater_object_plugin_1abbc883398252e410563c657648743e3e) 

Pairs of links & corresponding hydrodynamic models.

#### `protected ignition::math::Vector3d `[`flowVelocity`](#classgazebo_1_1_underwater_object_plugin_1ac5bf6578ef4434438ba7d7647b69b971) 

Flow velocity vector read from topic.

#### `protected gazebo::event::ConnectionPtr `[`updateConnection`](#classgazebo_1_1_underwater_object_plugin_1a1a4d81782ad2d21fc01598e0d9b42d27) 

Update event.

#### `protected gazebo::physics::WorldPtr `[`world`](#classgazebo_1_1_underwater_object_plugin_1a9f16fc2908d17c0975331cc825d14cb0) 

Pointer to the world plugin.

#### `protected gazebo::physics::ModelPtr `[`model`](#classgazebo_1_1_underwater_object_plugin_1a896d92ed527a0d9f7b47208614eaba0c) 

Pointer to the model structure.

#### `protected gazebo::transport::NodePtr `[`node`](#classgazebo_1_1_underwater_object_plugin_1a5422d922731696d2767e5be09c2cb5c2) 

Gazebo node.

#### `protected std::string `[`baseLinkName`](#classgazebo_1_1_underwater_object_plugin_1a08b0e6dfab6a63945ea6d1c71c858df1) 

Name of vehicle's base_link.

#### `protected gazebo::transport::SubscriberPtr `[`flowSubscriber`](#classgazebo_1_1_underwater_object_plugin_1adb22008a9f57f11659e2b2a18d57bcc6) 

Subcriber to flow message.

#### `protected bool `[`useGlobalCurrent`](#classgazebo_1_1_underwater_object_plugin_1a0bfd19ce74a42666f26fefa0ded488f3) 

Flag to use the global current velocity or the individually assigned current velocity.

#### `protected std::map< std::string, gazebo::transport::PublisherPtr > `[`hydroPub`](#classgazebo_1_1_underwater_object_plugin_1a33989646c81bc47fe86dae3052846ea2) 

Publishers of hydrodynamic and hydrostatic forces and torques in the case the debug flag is on.

#### `protected virtual void `[`Connect`](#classgazebo_1_1_underwater_object_plugin_1a7497acca39dc0a4f338bd863b002ec33)`()` 

Connects the update event callback.

#### `protected void `[`UpdateFlowVelocity`](#classgazebo_1_1_underwater_object_plugin_1a22bb6d230cc76b4a838ffffe5a6ba722)`(ConstVector3dPtr & _msg)` 

Reads flow velocity topic.

#### `protected virtual void `[`PublishCurrentVelocityMarker`](#classgazebo_1_1_underwater_object_plugin_1a89d8430bc839e0ff477fd893be829060)`()` 

Publish current velocity marker.

#### `protected virtual void `[`PublishIsSubmerged`](#classgazebo_1_1_underwater_object_plugin_1adc2e3f16a6fa8ce79497b5664fb66b82)`()` 

Publishes the state of the vehicle (is submerged)

#### `protected virtual void `[`PublishRestoringForce`](#classgazebo_1_1_underwater_object_plugin_1ae5da81b93706dded6de765628f57ad05)`(gazebo::physics::LinkPtr _link)` 

Publish restoring force.

#### Parameters
* `_link` Pointer to the link where the force information will be extracted from

#### `protected virtual void `[`PublishHydrodynamicWrenches`](#classgazebo_1_1_underwater_object_plugin_1af1b5370bf8ebd626fd9eafb2b46075b9)`(gazebo::physics::LinkPtr _link)` 

Publish hydrodynamic wrenches.

#### Parameters
* `_link` Pointer to the link where the force information will be extracted from

#### `protected virtual void `[`GenWrenchMsg`](#classgazebo_1_1_underwater_object_plugin_1a6deb4663c719f288b671539020257bb0)`(ignition::math::Vector3d _force,ignition::math::Vector3d _torque,gazebo::msgs::WrenchStamped & _output)` 

Returns the wrench message for debugging topics.

#### Parameters
* `_force` Force vector 

* `_torque` Torque vector 

* `_output` Stamped wrench message to be updated

#### `protected virtual void `[`InitDebug`](#classgazebo_1_1_underwater_object_plugin_1a86136f608b56ecd79bd6530f92724a75)`(gazebo::physics::LinkPtr _link,`[`gazebo::HydrodynamicModelPtr`](docs/packages/uuv_simulator/docs/api/HydrodynamicModelPtr.md#_hydrodynamic_model_8hh_1ab7e72448c3e86f93ab214d73c0cd4414)` _hydro)` 

Sets the topics used for publishing the intermediate data during the simulation.

#### Parameters
* `_link` Pointer to the link 

* `_hydro` Pointer to the hydrodynamic model

