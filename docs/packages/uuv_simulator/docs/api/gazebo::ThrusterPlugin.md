# class `gazebo::ThrusterPlugin` 

```
class gazebo::ThrusterPlugin
  : public ModelPlugin
```  

Class for the thruster plugin.

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public  `[`ThrusterPlugin`](#classgazebo_1_1_thruster_plugin_1a6b5841ff33686cc450313e03cf294d9c)`()` | Constructor.
`public virtual  `[`~ThrusterPlugin`](#classgazebo_1_1_thruster_plugin_1a06d1a5a37d484a2ce88329fd2fed8f59)`()` | Destructor.
`public virtual void `[`Load`](#classgazebo_1_1_thruster_plugin_1a1b4f788380387681886f65531ceb0f25)`(physics::ModelPtr _model,sdf::ElementPtr _sdf)` | 
`public virtual void `[`Init`](#classgazebo_1_1_thruster_plugin_1a976abc5ac54372004630800a7d83aa8e)`()` | 
`public virtual void `[`Reset`](#classgazebo_1_1_thruster_plugin_1a3a445ef9af6ff415eb3d2e319c232841)`()` | Custom plugin reset behavior.
`public void `[`Update`](#classgazebo_1_1_thruster_plugin_1a4cd1505e012721530e09cc346500ff12)`(const common::UpdateInfo & _info)` | Update the simulation state.
`protected std::shared_ptr< `[`Dynamics`](docs/packages/uuv_simulator/docs/api/gazebo::Dynamics.md#classgazebo_1_1_dynamics)` > `[`thrusterDynamics`](#classgazebo_1_1_thruster_plugin_1a2a5bdae0148178c1688362257e59dbfa) | Thruster dynamic model.
`protected std::shared_ptr< `[`ConversionFunction`](docs/packages/uuv_simulator/docs/api/gazebo::ConversionFunction.md#classgazebo_1_1_conversion_function)` > `[`conversionFunction`](#classgazebo_1_1_thruster_plugin_1aab369c9f214021b0e3372dd61907c257) | Thruster conversion function.
`protected event::ConnectionPtr `[`updateConnection`](#classgazebo_1_1_thruster_plugin_1a23c4d67fd108db7dabc2727244934a30) | Update event.
`protected physics::LinkPtr `[`thrusterLink`](#classgazebo_1_1_thruster_plugin_1a141de7a7aedb56861b9046ee7897399f) | Pointer to the thruster link.
`protected transport::NodePtr `[`node`](#classgazebo_1_1_thruster_plugin_1afedb1c79f0a9c060cd4bc6c1ef541b68) | Gazebo node.
`protected transport::SubscriberPtr `[`commandSubscriber`](#classgazebo_1_1_thruster_plugin_1ae4054a7444082b7f0195b3cf72bfad6f) | Subscriber to the reference signal topic.
`protected transport::PublisherPtr `[`thrustTopicPublisher`](#classgazebo_1_1_thruster_plugin_1a8ad82769e76b0844a87763446f03a267) | Publisher to the output thrust topic.
`protected double `[`inputCommand`](#classgazebo_1_1_thruster_plugin_1a617d0e909a0d82397d95954c8c103035) | Input command, typically desired angular velocity of the rotor.
`protected double `[`thrustForce`](#classgazebo_1_1_thruster_plugin_1a3dd6123930d825ae14ca56b253b9c8a2) | Latest thrust force in [N].
`protected common::Time `[`thrustForceStamp`](#classgazebo_1_1_thruster_plugin_1afc2f42b3a4d4dfe1d59bdb06a15bf8e7) | Time stamp of latest thrust force.
`protected physics::JointPtr `[`joint`](#classgazebo_1_1_thruster_plugin_1a5df1a3ae7ee6363498bf3221d7c70f93) | Optional: The rotor joint, used for visualization.
`protected double `[`clampMin`](#classgazebo_1_1_thruster_plugin_1ab2e98f8b4a89488d0455d7d57b84ec52) | : Optional: Commands less than this value will be clamped.
`protected double `[`clampMax`](#classgazebo_1_1_thruster_plugin_1a58ee9e27895d9921cc40cd0c64aa086d) | : Optional: Commands greater than this value will be clamped.
`protected double `[`thrustMin`](#classgazebo_1_1_thruster_plugin_1aad3011318655f542756926e0633de05e) | : Optional: Minimum thrust force output
`protected double `[`thrustMax`](#classgazebo_1_1_thruster_plugin_1a7730c8c0b69432591ab15e42f4deef35) | : Optional: Maximum thrust force output
`protected int `[`thrusterID`](#classgazebo_1_1_thruster_plugin_1a2e6fb5eaaa297788fabb51bd8dc578e3) | Thruster ID, used to generated topic names automatically.
`protected std::string `[`topicPrefix`](#classgazebo_1_1_thruster_plugin_1acde9d0318e86dfbc9e6e2af723ea9c3b) | Thruster topics prefix.
`protected double `[`gain`](#classgazebo_1_1_thruster_plugin_1a76067d3ea096103f7d6f3f43106e0e23) | : Optional: Gain factor: Desired angular velocity = command * gain
`protected bool `[`isOn`](#classgazebo_1_1_thruster_plugin_1a86031b28be7600d3eedaecf3d11a9ea5) | Optional: Flag to indicate if the thruster is turned on or off.
`protected double `[`thrustEfficiency`](#classgazebo_1_1_thruster_plugin_1a36d3369e6481b21d8450c012b21ea7a7) | Optional: Output thrust efficiency factor of the thruster.
`protected double `[`propellerEfficiency`](#classgazebo_1_1_thruster_plugin_1a0e8f044924d12715aba76aa95555641d) | Optional: Propeller angular velocity efficiency term.
`protected ignition::math::Vector3d `[`thrusterAxis`](#classgazebo_1_1_thruster_plugin_1a961eff0b01402bf7a56117a35e064b06) | The axis about which the thruster rotates.
`protected void `[`UpdateInput`](#classgazebo_1_1_thruster_plugin_1a8ede5b7013c52fd890a429f55a0d0c74)`(`[`ConstDoublePtr`](docs/packages/uuv_simulator/docs/api/ConstDoublePtr.md#_fin_plugin_8hh_1adec3148dfa71d908caf33660a62187d4)` & _msg)` | Callback for the input topic subscriber.

## Members

#### `public  `[`ThrusterPlugin`](#classgazebo_1_1_thruster_plugin_1a6b5841ff33686cc450313e03cf294d9c)`()` 

Constructor.

#### `public virtual  `[`~ThrusterPlugin`](#classgazebo_1_1_thruster_plugin_1a06d1a5a37d484a2ce88329fd2fed8f59)`()` 

Destructor.

#### `public virtual void `[`Load`](#classgazebo_1_1_thruster_plugin_1a1b4f788380387681886f65531ceb0f25)`(physics::ModelPtr _model,sdf::ElementPtr _sdf)` 

#### `public virtual void `[`Init`](#classgazebo_1_1_thruster_plugin_1a976abc5ac54372004630800a7d83aa8e)`()` 

#### `public virtual void `[`Reset`](#classgazebo_1_1_thruster_plugin_1a3a445ef9af6ff415eb3d2e319c232841)`()` 

Custom plugin reset behavior.

#### `public void `[`Update`](#classgazebo_1_1_thruster_plugin_1a4cd1505e012721530e09cc346500ff12)`(const common::UpdateInfo & _info)` 

Update the simulation state.

#### Parameters
* `_info` Information used in the update event.

#### `protected std::shared_ptr< `[`Dynamics`](docs/packages/uuv_simulator/docs/api/gazebo::Dynamics.md#classgazebo_1_1_dynamics)` > `[`thrusterDynamics`](#classgazebo_1_1_thruster_plugin_1a2a5bdae0148178c1688362257e59dbfa) 

Thruster dynamic model.

#### `protected std::shared_ptr< `[`ConversionFunction`](docs/packages/uuv_simulator/docs/api/gazebo::ConversionFunction.md#classgazebo_1_1_conversion_function)` > `[`conversionFunction`](#classgazebo_1_1_thruster_plugin_1aab369c9f214021b0e3372dd61907c257) 

Thruster conversion function.

#### `protected event::ConnectionPtr `[`updateConnection`](#classgazebo_1_1_thruster_plugin_1a23c4d67fd108db7dabc2727244934a30) 

Update event.

#### `protected physics::LinkPtr `[`thrusterLink`](#classgazebo_1_1_thruster_plugin_1a141de7a7aedb56861b9046ee7897399f) 

Pointer to the thruster link.

#### `protected transport::NodePtr `[`node`](#classgazebo_1_1_thruster_plugin_1afedb1c79f0a9c060cd4bc6c1ef541b68) 

Gazebo node.

#### `protected transport::SubscriberPtr `[`commandSubscriber`](#classgazebo_1_1_thruster_plugin_1ae4054a7444082b7f0195b3cf72bfad6f) 

Subscriber to the reference signal topic.

#### `protected transport::PublisherPtr `[`thrustTopicPublisher`](#classgazebo_1_1_thruster_plugin_1a8ad82769e76b0844a87763446f03a267) 

Publisher to the output thrust topic.

#### `protected double `[`inputCommand`](#classgazebo_1_1_thruster_plugin_1a617d0e909a0d82397d95954c8c103035) 

Input command, typically desired angular velocity of the rotor.

#### `protected double `[`thrustForce`](#classgazebo_1_1_thruster_plugin_1a3dd6123930d825ae14ca56b253b9c8a2) 

Latest thrust force in [N].

#### `protected common::Time `[`thrustForceStamp`](#classgazebo_1_1_thruster_plugin_1afc2f42b3a4d4dfe1d59bdb06a15bf8e7) 

Time stamp of latest thrust force.

#### `protected physics::JointPtr `[`joint`](#classgazebo_1_1_thruster_plugin_1a5df1a3ae7ee6363498bf3221d7c70f93) 

Optional: The rotor joint, used for visualization.

#### `protected double `[`clampMin`](#classgazebo_1_1_thruster_plugin_1ab2e98f8b4a89488d0455d7d57b84ec52) 

: Optional: Commands less than this value will be clamped.

#### `protected double `[`clampMax`](#classgazebo_1_1_thruster_plugin_1a58ee9e27895d9921cc40cd0c64aa086d) 

: Optional: Commands greater than this value will be clamped.

#### `protected double `[`thrustMin`](#classgazebo_1_1_thruster_plugin_1aad3011318655f542756926e0633de05e) 

: Optional: Minimum thrust force output

#### `protected double `[`thrustMax`](#classgazebo_1_1_thruster_plugin_1a7730c8c0b69432591ab15e42f4deef35) 

: Optional: Maximum thrust force output

#### `protected int `[`thrusterID`](#classgazebo_1_1_thruster_plugin_1a2e6fb5eaaa297788fabb51bd8dc578e3) 

Thruster ID, used to generated topic names automatically.

#### `protected std::string `[`topicPrefix`](#classgazebo_1_1_thruster_plugin_1acde9d0318e86dfbc9e6e2af723ea9c3b) 

Thruster topics prefix.

#### `protected double `[`gain`](#classgazebo_1_1_thruster_plugin_1a76067d3ea096103f7d6f3f43106e0e23) 

: Optional: Gain factor: Desired angular velocity = command * gain

#### `protected bool `[`isOn`](#classgazebo_1_1_thruster_plugin_1a86031b28be7600d3eedaecf3d11a9ea5) 

Optional: Flag to indicate if the thruster is turned on or off.

#### `protected double `[`thrustEfficiency`](#classgazebo_1_1_thruster_plugin_1a36d3369e6481b21d8450c012b21ea7a7) 

Optional: Output thrust efficiency factor of the thruster.

#### `protected double `[`propellerEfficiency`](#classgazebo_1_1_thruster_plugin_1a0e8f044924d12715aba76aa95555641d) 

Optional: Propeller angular velocity efficiency term.

#### `protected ignition::math::Vector3d `[`thrusterAxis`](#classgazebo_1_1_thruster_plugin_1a961eff0b01402bf7a56117a35e064b06) 

The axis about which the thruster rotates.

#### `protected void `[`UpdateInput`](#classgazebo_1_1_thruster_plugin_1a8ede5b7013c52fd890a429f55a0d0c74)`(`[`ConstDoublePtr`](docs/packages/uuv_simulator/docs/api/ConstDoublePtr.md#_fin_plugin_8hh_1adec3148dfa71d908caf33660a62187d4)` & _msg)` 

Callback for the input topic subscriber.

