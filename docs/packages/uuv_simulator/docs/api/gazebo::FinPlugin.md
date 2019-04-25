# class `gazebo::FinPlugin` 

```
class gazebo::FinPlugin
  : public ModelPlugin
```  

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public  `[`FinPlugin`](#classgazebo_1_1_fin_plugin_1a347a9d485eb98d0c0d1ce181cf3530e7)`()` | Constructor.
`public virtual  `[`~FinPlugin`](#classgazebo_1_1_fin_plugin_1a6bfb47239eaef146985a19a5005ba320)`()` | Destructor.
`public virtual void `[`Load`](#classgazebo_1_1_fin_plugin_1a2229e6e90a612c37da8bbf1110c54f53)`(physics::ModelPtr _model,sdf::ElementPtr _sdf)` | 
`public virtual void `[`Init`](#classgazebo_1_1_fin_plugin_1a674d8c80971e173b7066fa2a52ae8388)`()` | 
`public void `[`OnUpdate`](#classgazebo_1_1_fin_plugin_1ab4612d0093ed8b1fd0e24f780f584889)`(const common::UpdateInfo & _info)` | Update the simulation state.
`protected std::shared_ptr< `[`Dynamics`](docs/packages/uuv_simulator/docs/api/gazebo::Dynamics.md#classgazebo_1_1_dynamics)` > `[`dynamics`](#classgazebo_1_1_fin_plugin_1ad0a0e94fc62d04d9a08f119e72919420) | Fin dynamic model.
`protected std::shared_ptr< `[`LiftDrag`](docs/packages/uuv_simulator/docs/api/gazebo::LiftDrag.md#classgazebo_1_1_lift_drag)` > `[`liftdrag`](#classgazebo_1_1_fin_plugin_1a59d7567aa36e7d6882d1dd11c9ab75d0) | Lift&Drag model.
`protected event::ConnectionPtr `[`updateConnection`](#classgazebo_1_1_fin_plugin_1a217cde139114bb0f1415f73b82538e00) | Update event.
`protected transport::NodePtr `[`node`](#classgazebo_1_1_fin_plugin_1a2acefe090abcbd138a230391e577d187) | Gazebo node.
`protected physics::JointPtr `[`joint`](#classgazebo_1_1_fin_plugin_1af5fbe5a75a59199af8e92e17b2546841) | The fin joint.
`protected physics::LinkPtr `[`link`](#classgazebo_1_1_fin_plugin_1aa2a49d7b7c718265296063be66767375) | The fin link.
`protected transport::SubscriberPtr `[`commandSubscriber`](#classgazebo_1_1_fin_plugin_1a5d58c432064cc3c9c94b3ed0bd8a52a3) | Subscriber to the reference signal topic.
`protected transport::PublisherPtr `[`anglePublisher`](#classgazebo_1_1_fin_plugin_1a17fc907ce5376d31010075d2c127e0a9) | Publisher to the output thrust topic.
`protected ignition::math::Vector3d `[`finForce`](#classgazebo_1_1_fin_plugin_1ae0cfeae0cbbf51ed8ad3d88710a7bf95) | Force component calculated from the lift and drag module.
`protected double `[`inputCommand`](#classgazebo_1_1_fin_plugin_1ac748f61691360a841314e3d92ee7cfdd) | Latest input command.
`protected int `[`finID`](#classgazebo_1_1_fin_plugin_1a0d357d22e70731d4f0da1e2eb16dbec9) | Fin ID.
`protected std::string `[`topicPrefix`](#classgazebo_1_1_fin_plugin_1ae595f9a8c9d7d00439935c3a95a7ec42) | Topic prefix.
`protected double `[`angle`](#classgazebo_1_1_fin_plugin_1a030388a1a36c2f58f0baa34605eb0d15) | Latest fin angle in [rad].
`protected common::Time `[`angleStamp`](#classgazebo_1_1_fin_plugin_1a4fb2db18a81a9a7cf8f2f5376b3e5d02) | Time stamp of latest thrust force.
`protected transport::SubscriberPtr `[`currentSubscriber`](#classgazebo_1_1_fin_plugin_1a3940ad05bd8930b1d866154116939a07) | Subcriber to current message.
`protected ignition::math::Vector3d `[`currentVelocity`](#classgazebo_1_1_fin_plugin_1adc8117b6c3169bbcccc25ba63ba4276e) | Current velocity vector read from topic.
`protected void `[`UpdateInput`](#classgazebo_1_1_fin_plugin_1ad20391361f5206bde332a229251c7f38)`(`[`ConstDoublePtr`](docs/packages/uuv_simulator/docs/api/ConstDoublePtr.md#_fin_plugin_8hh_1adec3148dfa71d908caf33660a62187d4)` & _msg)` | Callback for the input topic subscriber.
`protected void `[`UpdateCurrentVelocity`](#classgazebo_1_1_fin_plugin_1aaf4c2da2058c877cbffdd0dc6d94c0ee)`(ConstVector3dPtr & _msg)` | Reads current velocity topic.

## Members

#### `public  `[`FinPlugin`](#classgazebo_1_1_fin_plugin_1a347a9d485eb98d0c0d1ce181cf3530e7)`()` 

Constructor.

#### `public virtual  `[`~FinPlugin`](#classgazebo_1_1_fin_plugin_1a6bfb47239eaef146985a19a5005ba320)`()` 

Destructor.

#### `public virtual void `[`Load`](#classgazebo_1_1_fin_plugin_1a2229e6e90a612c37da8bbf1110c54f53)`(physics::ModelPtr _model,sdf::ElementPtr _sdf)` 

#### `public virtual void `[`Init`](#classgazebo_1_1_fin_plugin_1a674d8c80971e173b7066fa2a52ae8388)`()` 

#### `public void `[`OnUpdate`](#classgazebo_1_1_fin_plugin_1ab4612d0093ed8b1fd0e24f780f584889)`(const common::UpdateInfo & _info)` 

Update the simulation state.

#### Parameters
* `_info` Information used in the update event.

#### `protected std::shared_ptr< `[`Dynamics`](docs/packages/uuv_simulator/docs/api/gazebo::Dynamics.md#classgazebo_1_1_dynamics)` > `[`dynamics`](#classgazebo_1_1_fin_plugin_1ad0a0e94fc62d04d9a08f119e72919420) 

Fin dynamic model.

#### `protected std::shared_ptr< `[`LiftDrag`](docs/packages/uuv_simulator/docs/api/gazebo::LiftDrag.md#classgazebo_1_1_lift_drag)` > `[`liftdrag`](#classgazebo_1_1_fin_plugin_1a59d7567aa36e7d6882d1dd11c9ab75d0) 

Lift&Drag model.

#### `protected event::ConnectionPtr `[`updateConnection`](#classgazebo_1_1_fin_plugin_1a217cde139114bb0f1415f73b82538e00) 

Update event.

#### `protected transport::NodePtr `[`node`](#classgazebo_1_1_fin_plugin_1a2acefe090abcbd138a230391e577d187) 

Gazebo node.

#### `protected physics::JointPtr `[`joint`](#classgazebo_1_1_fin_plugin_1af5fbe5a75a59199af8e92e17b2546841) 

The fin joint.

#### `protected physics::LinkPtr `[`link`](#classgazebo_1_1_fin_plugin_1aa2a49d7b7c718265296063be66767375) 

The fin link.

#### `protected transport::SubscriberPtr `[`commandSubscriber`](#classgazebo_1_1_fin_plugin_1a5d58c432064cc3c9c94b3ed0bd8a52a3) 

Subscriber to the reference signal topic.

#### `protected transport::PublisherPtr `[`anglePublisher`](#classgazebo_1_1_fin_plugin_1a17fc907ce5376d31010075d2c127e0a9) 

Publisher to the output thrust topic.

#### `protected ignition::math::Vector3d `[`finForce`](#classgazebo_1_1_fin_plugin_1ae0cfeae0cbbf51ed8ad3d88710a7bf95) 

Force component calculated from the lift and drag module.

#### `protected double `[`inputCommand`](#classgazebo_1_1_fin_plugin_1ac748f61691360a841314e3d92ee7cfdd) 

Latest input command.

#### `protected int `[`finID`](#classgazebo_1_1_fin_plugin_1a0d357d22e70731d4f0da1e2eb16dbec9) 

Fin ID.

#### `protected std::string `[`topicPrefix`](#classgazebo_1_1_fin_plugin_1ae595f9a8c9d7d00439935c3a95a7ec42) 

Topic prefix.

#### `protected double `[`angle`](#classgazebo_1_1_fin_plugin_1a030388a1a36c2f58f0baa34605eb0d15) 

Latest fin angle in [rad].

#### `protected common::Time `[`angleStamp`](#classgazebo_1_1_fin_plugin_1a4fb2db18a81a9a7cf8f2f5376b3e5d02) 

Time stamp of latest thrust force.

#### `protected transport::SubscriberPtr `[`currentSubscriber`](#classgazebo_1_1_fin_plugin_1a3940ad05bd8930b1d866154116939a07) 

Subcriber to current message.

#### `protected ignition::math::Vector3d `[`currentVelocity`](#classgazebo_1_1_fin_plugin_1adc8117b6c3169bbcccc25ba63ba4276e) 

Current velocity vector read from topic.

#### `protected void `[`UpdateInput`](#classgazebo_1_1_fin_plugin_1ad20391361f5206bde332a229251c7f38)`(`[`ConstDoublePtr`](docs/packages/uuv_simulator/docs/api/ConstDoublePtr.md#_fin_plugin_8hh_1adec3148dfa71d908caf33660a62187d4)` & _msg)` 

Callback for the input topic subscriber.

#### `protected void `[`UpdateCurrentVelocity`](#classgazebo_1_1_fin_plugin_1aaf4c2da2058c877cbffdd0dc6d94c0ee)`(ConstVector3dPtr & _msg)` 

Reads current velocity topic.

