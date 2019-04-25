# class `gazebo::UmbilicalPlugin` 

```
class gazebo::UmbilicalPlugin
  : public ModelPlugin
```  

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public  `[`UmbilicalPlugin`](#classgazebo_1_1_umbilical_plugin_1a057f26aba6131c97efcfad72864c1c96)`()` | Destructor.
`public  `[`~UmbilicalPlugin`](#classgazebo_1_1_umbilical_plugin_1afd11fddc7265c89ce53a665688ea4baa)`()` | Constructor.
`protected event::ConnectionPtr `[`updateConnection`](#classgazebo_1_1_umbilical_plugin_1a23741aa2b2775fb58db688c19b338c7f) | Pointer to the update event connection.
`protected gazebo::physics::ModelPtr `[`model`](#classgazebo_1_1_umbilical_plugin_1aa495d0dd46d56e18550dfa30ec6a5ccf) | Pointer to the model structure.
`protected gazebo::physics::WorldPtr `[`world`](#classgazebo_1_1_umbilical_plugin_1a9299893f7d97eb66ee07fb725ca165d4) | Pointer to the world plugin.
`protected gazebo::transport::NodePtr `[`node`](#classgazebo_1_1_umbilical_plugin_1a552cee3d43b51eb33048ad88120bf879) | Gazebo node.
`protected gazebo::transport::SubscriberPtr `[`flowSubscriber`](#classgazebo_1_1_umbilical_plugin_1a5f7d8aee1c7f91bcfdc680484a60b4db) | Subcriber to flow message.
`protected ignition::math::Vector3d `[`flowVelocity`](#classgazebo_1_1_umbilical_plugin_1a6b65710780f67008b0b167840d19d781) | Flow velocity vector read from topic.
`protected std::shared_ptr< `[`UmbilicalModel`](docs/packages/uuv_simulator/docs/api/gazebo::UmbilicalModel.md#classgazebo_1_1_umbilical_model)` > `[`umbilical`](#classgazebo_1_1_umbilical_plugin_1a02c19fdf4ddac48e3a46b5e72522c938) | Pointer to [UmbilicalModel](docs/packages/uuv_simulator/docs/api/gazebo::UmbilicalModel.md#classgazebo_1_1_umbilical_model) used in this plugin.
`protected virtual void `[`Load`](#classgazebo_1_1_umbilical_plugin_1af44b8802650eb0c0d9842558db614914)`(physics::ModelPtr _model,sdf::ElementPtr _sdf)` | Load plugin and its configuration from sdf.
`protected virtual void `[`OnUpdate`](#classgazebo_1_1_umbilical_plugin_1a27b0bf9ff8f9face03db37b7882e9195)`(const common::UpdateInfo &)` | Update callback from simulation.
`protected void `[`UpdateFlowVelocity`](#classgazebo_1_1_umbilical_plugin_1aafce9f28f1b7438e2585c9d5fe5d434c)`(ConstVector3dPtr & _msg)` | Reads flow velocity topic.

## Members

#### `public  `[`UmbilicalPlugin`](#classgazebo_1_1_umbilical_plugin_1a057f26aba6131c97efcfad72864c1c96)`()` 

Destructor.

#### `public  `[`~UmbilicalPlugin`](#classgazebo_1_1_umbilical_plugin_1afd11fddc7265c89ce53a665688ea4baa)`()` 

Constructor.

#### `protected event::ConnectionPtr `[`updateConnection`](#classgazebo_1_1_umbilical_plugin_1a23741aa2b2775fb58db688c19b338c7f) 

Pointer to the update event connection.

#### `protected gazebo::physics::ModelPtr `[`model`](#classgazebo_1_1_umbilical_plugin_1aa495d0dd46d56e18550dfa30ec6a5ccf) 

Pointer to the model structure.

#### `protected gazebo::physics::WorldPtr `[`world`](#classgazebo_1_1_umbilical_plugin_1a9299893f7d97eb66ee07fb725ca165d4) 

Pointer to the world plugin.

#### `protected gazebo::transport::NodePtr `[`node`](#classgazebo_1_1_umbilical_plugin_1a552cee3d43b51eb33048ad88120bf879) 

Gazebo node.

#### `protected gazebo::transport::SubscriberPtr `[`flowSubscriber`](#classgazebo_1_1_umbilical_plugin_1a5f7d8aee1c7f91bcfdc680484a60b4db) 

Subcriber to flow message.

#### `protected ignition::math::Vector3d `[`flowVelocity`](#classgazebo_1_1_umbilical_plugin_1a6b65710780f67008b0b167840d19d781) 

Flow velocity vector read from topic.

#### `protected std::shared_ptr< `[`UmbilicalModel`](docs/packages/uuv_simulator/docs/api/gazebo::UmbilicalModel.md#classgazebo_1_1_umbilical_model)` > `[`umbilical`](#classgazebo_1_1_umbilical_plugin_1a02c19fdf4ddac48e3a46b5e72522c938) 

Pointer to [UmbilicalModel](docs/packages/uuv_simulator/docs/api/gazebo::UmbilicalModel.md#classgazebo_1_1_umbilical_model) used in this plugin.

#### `protected virtual void `[`Load`](#classgazebo_1_1_umbilical_plugin_1af44b8802650eb0c0d9842558db614914)`(physics::ModelPtr _model,sdf::ElementPtr _sdf)` 

Load plugin and its configuration from sdf.

#### `protected virtual void `[`OnUpdate`](#classgazebo_1_1_umbilical_plugin_1a27b0bf9ff8f9face03db37b7882e9195)`(const common::UpdateInfo &)` 

Update callback from simulation.

#### `protected void `[`UpdateFlowVelocity`](#classgazebo_1_1_umbilical_plugin_1aafce9f28f1b7438e2585c9d5fe5d434c)`(ConstVector3dPtr & _msg)` 

Reads flow velocity topic.

