# class `gazebo::ROSBaseModelPlugin` 

```
class gazebo::ROSBaseModelPlugin
  : public gazebo::ROSBasePlugin
  : public ModelPlugin
```  

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public  `[`ROSBaseModelPlugin`](#classgazebo_1_1_r_o_s_base_model_plugin_1ab63bd687291a8642150cb00a94900014)`()` | Class constructor.
`public virtual  `[`~ROSBaseModelPlugin`](#classgazebo_1_1_r_o_s_base_model_plugin_1a3e34768f99ceff93e43a6befc5ca1c03)`()` | Class destructor.
`protected physics::ModelPtr `[`model`](#classgazebo_1_1_r_o_s_base_model_plugin_1af03370cfa624905d6098556d815828b3) | Pointer to the model.
`protected physics::LinkPtr `[`link`](#classgazebo_1_1_r_o_s_base_model_plugin_1ac405387fd2fcf90b48b368104031367d) | Pointer to the link.
`protected bool `[`enableLocalNEDFrame`](#classgazebo_1_1_r_o_s_base_model_plugin_1a3ebccbacd16defded57b77d970bcb95c) | True if a the local NED frame needs to be broadcasted.
`protected tf::TransformBroadcaster * `[`tfBroadcaster`](#classgazebo_1_1_r_o_s_base_model_plugin_1ab2ee1727cd20681c8a5f3a33462cc694) | TF broadcaster for the local NED frame.
`protected ignition::math::Pose3d `[`localNEDFrame`](#classgazebo_1_1_r_o_s_base_model_plugin_1abc302dfd65e4b45c3e11721afedb21d7) | Pose of the local NED frame wrt link frame.
`protected tf::StampedTransform `[`tfLocalNEDFrame`](#classgazebo_1_1_r_o_s_base_model_plugin_1a3648c84096f1fff1390c53557a782fd1) | Local NED TF frame.
`protected virtual void `[`Load`](#classgazebo_1_1_r_o_s_base_model_plugin_1a9201b96ddee1a64ce43e59f3cf1ff2e9)`(physics::ModelPtr _model,sdf::ElementPtr _sdf)` | Load plugin and its configuration from sdf,.
`protected virtual bool `[`OnUpdate`](#classgazebo_1_1_r_o_s_base_model_plugin_1a51b6e630508d410ddfe1a76573ef75fb)`(const common::UpdateInfo &)` | Update callback from simulation.
`protected void `[`SendLocalNEDTransform`](#classgazebo_1_1_r_o_s_base_model_plugin_1a11c3832798f58c446a5d0d69343ad181)`()` | Returns true if the base_link_ned frame exists.

## Members

#### `public  `[`ROSBaseModelPlugin`](#classgazebo_1_1_r_o_s_base_model_plugin_1ab63bd687291a8642150cb00a94900014)`()` 

Class constructor.

#### `public virtual  `[`~ROSBaseModelPlugin`](#classgazebo_1_1_r_o_s_base_model_plugin_1a3e34768f99ceff93e43a6befc5ca1c03)`()` 

Class destructor.

#### `protected physics::ModelPtr `[`model`](#classgazebo_1_1_r_o_s_base_model_plugin_1af03370cfa624905d6098556d815828b3) 

Pointer to the model.

#### `protected physics::LinkPtr `[`link`](#classgazebo_1_1_r_o_s_base_model_plugin_1ac405387fd2fcf90b48b368104031367d) 

Pointer to the link.

#### `protected bool `[`enableLocalNEDFrame`](#classgazebo_1_1_r_o_s_base_model_plugin_1a3ebccbacd16defded57b77d970bcb95c) 

True if a the local NED frame needs to be broadcasted.

#### `protected tf::TransformBroadcaster * `[`tfBroadcaster`](#classgazebo_1_1_r_o_s_base_model_plugin_1ab2ee1727cd20681c8a5f3a33462cc694) 

TF broadcaster for the local NED frame.

#### `protected ignition::math::Pose3d `[`localNEDFrame`](#classgazebo_1_1_r_o_s_base_model_plugin_1abc302dfd65e4b45c3e11721afedb21d7) 

Pose of the local NED frame wrt link frame.

#### `protected tf::StampedTransform `[`tfLocalNEDFrame`](#classgazebo_1_1_r_o_s_base_model_plugin_1a3648c84096f1fff1390c53557a782fd1) 

Local NED TF frame.

#### `protected virtual void `[`Load`](#classgazebo_1_1_r_o_s_base_model_plugin_1a9201b96ddee1a64ce43e59f3cf1ff2e9)`(physics::ModelPtr _model,sdf::ElementPtr _sdf)` 

Load plugin and its configuration from sdf,.

#### `protected virtual bool `[`OnUpdate`](#classgazebo_1_1_r_o_s_base_model_plugin_1a51b6e630508d410ddfe1a76573ef75fb)`(const common::UpdateInfo &)` 

Update callback from simulation.

#### `protected void `[`SendLocalNEDTransform`](#classgazebo_1_1_r_o_s_base_model_plugin_1a11c3832798f58c446a5d0d69343ad181)`()` 

Returns true if the base_link_ned frame exists.

