# Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`namespace `[`gazebo`](#namespacegazebo) | 

# namespace `gazebo` 

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`class `[`gazebo::GaussMarkovProcess`](#classgazebo_1_1_gauss_markov_process) | Implementation of a Gauss-Markov process to model the current velocity and direction according to [1] [1] Fossen, Thor I. Handbook of marine craft hydrodynamics and motion control. John Wiley & Sons, 2011.
`class `[`gazebo::UnderwaterCurrentPlugin`](#classgazebo_1_1_underwater_current_plugin) | Class for the underwater current plugin TODO: Add option to make the underwater current also a function of depth to comply with DNV.

# class `gazebo::GaussMarkovProcess` 

Implementation of a Gauss-Markov process to model the current velocity and direction according to [1] [1] Fossen, Thor I. Handbook of marine craft hydrodynamics and motion control. John Wiley & Sons, 2011.

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public double `[`var`](#classgazebo_1_1_gauss_markov_process_1a1e4fb7902c13ed7f5ed4b081b8c750a1) | Process variable.
`public double `[`mean`](#classgazebo_1_1_gauss_markov_process_1ac245edf6d8fa0b6926cb8d83d29e3457) | Mean process value.
`public double `[`min`](#classgazebo_1_1_gauss_markov_process_1a5becb64490649244d6ee0370dd9e9952) | Minimum limit for the process variable.
`public double `[`max`](#classgazebo_1_1_gauss_markov_process_1a36c94fb3fd89d6b8ec095ff2fd61fd1a) | Maximum limit for the process variable.
`public double `[`mu`](#classgazebo_1_1_gauss_markov_process_1af0c51962ec2392d734c0ee79f45866a8) | Process constant, if zero, process becomes a random walk.
`public double `[`noiseAmp`](#classgazebo_1_1_gauss_markov_process_1a094afee00b782c741a5edfdea42f0644) | Gaussian white noise amplitude.
`public double `[`lastUpdate`](#classgazebo_1_1_gauss_markov_process_1a21d7006da353d3a20fdb0faba2a24da7) | Timestamp for the last update.
`public  `[`GaussMarkovProcess`](#classgazebo_1_1_gauss_markov_process_1af1e11c49f71e6fd8f260f69db1e45e61)`()` | Class constructor.
`public void `[`Reset`](#classgazebo_1_1_gauss_markov_process_1abb7d9286aa8162e074b64188908017fe)`()` | Resets the process parameters.
`public bool `[`SetModel`](#classgazebo_1_1_gauss_markov_process_1aa987aee49f6f4a2f460138c93b11d3e8)`(double _mean,double _min,double _max,double _mu,double _noise)` | Sets all the necessary parameters for the computation.
`public bool `[`SetMean`](#classgazebo_1_1_gauss_markov_process_1a02d2ce1deb17930eb2b6d87ffc93d3f0)`(double _mean)` | Set mean process value.
`public double `[`Update`](#classgazebo_1_1_gauss_markov_process_1a4fe5c320c4fbdf4c6e5211381cf6e96a)`(double _time)` | Update function for a new time stamp.
`public void `[`Print`](#classgazebo_1_1_gauss_markov_process_1a5933e94170a0b8ab0b32e8eaba5281bf)`()` | Print current model paramters.

## Members

#### `public double `[`var`](#classgazebo_1_1_gauss_markov_process_1a1e4fb7902c13ed7f5ed4b081b8c750a1) 

Process variable.

#### `public double `[`mean`](#classgazebo_1_1_gauss_markov_process_1ac245edf6d8fa0b6926cb8d83d29e3457) 

Mean process value.

#### `public double `[`min`](#classgazebo_1_1_gauss_markov_process_1a5becb64490649244d6ee0370dd9e9952) 

Minimum limit for the process variable.

#### `public double `[`max`](#classgazebo_1_1_gauss_markov_process_1a36c94fb3fd89d6b8ec095ff2fd61fd1a) 

Maximum limit for the process variable.

#### `public double `[`mu`](#classgazebo_1_1_gauss_markov_process_1af0c51962ec2392d734c0ee79f45866a8) 

Process constant, if zero, process becomes a random walk.

#### `public double `[`noiseAmp`](#classgazebo_1_1_gauss_markov_process_1a094afee00b782c741a5edfdea42f0644) 

Gaussian white noise amplitude.

#### `public double `[`lastUpdate`](#classgazebo_1_1_gauss_markov_process_1a21d7006da353d3a20fdb0faba2a24da7) 

Timestamp for the last update.

#### `public  `[`GaussMarkovProcess`](#classgazebo_1_1_gauss_markov_process_1af1e11c49f71e6fd8f260f69db1e45e61)`()` 

Class constructor.

#### `public void `[`Reset`](#classgazebo_1_1_gauss_markov_process_1abb7d9286aa8162e074b64188908017fe)`()` 

Resets the process parameters.

#### `public bool `[`SetModel`](#classgazebo_1_1_gauss_markov_process_1aa987aee49f6f4a2f460138c93b11d3e8)`(double _mean,double _min,double _max,double _mu,double _noise)` 

Sets all the necessary parameters for the computation.

#### Parameters
* `_mean` Mean value 

* `_min` Minimum limit 

* `_max` Maximum limit 

* `_mu` Process constant 

* `_noise` Amplitude for the Gaussian white noise 

#### Returns
True, if all parameters were valid

#### `public bool `[`SetMean`](#classgazebo_1_1_gauss_markov_process_1a02d2ce1deb17930eb2b6d87ffc93d3f0)`(double _mean)` 

Set mean process value.

#### Parameters
* `_mean` New mean value 

#### Returns
True, if value inside the limit range

#### `public double `[`Update`](#classgazebo_1_1_gauss_markov_process_1a4fe5c320c4fbdf4c6e5211381cf6e96a)`(double _time)` 

Update function for a new time stamp.

#### Parameters
* `_time` Current time stamp

#### `public void `[`Print`](#classgazebo_1_1_gauss_markov_process_1a5933e94170a0b8ab0b32e8eaba5281bf)`()` 

Print current model paramters.

# class `gazebo::UnderwaterCurrentPlugin` 

```
class gazebo::UnderwaterCurrentPlugin
  : public WorldPlugin
```  

Class for the underwater current plugin TODO: Add option to make the underwater current also a function of depth to comply with DNV.

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public  `[`UnderwaterCurrentPlugin`](#classgazebo_1_1_underwater_current_plugin_1a53ab68e44476969bf9f060e5d373dd7f)`()` | Class constructor.
`public virtual  `[`~UnderwaterCurrentPlugin`](#classgazebo_1_1_underwater_current_plugin_1a6c6a579c9dec4ea61acfa9a9d4fa7600)`()` | Class destructor.
`public virtual void `[`Load`](#classgazebo_1_1_underwater_current_plugin_1a4bf93316f588c10868ed5dba85a14e78)`(physics::WorldPtr _world,sdf::ElementPtr _sdf)` | 
`public virtual void `[`Init`](#classgazebo_1_1_underwater_current_plugin_1a88d6932fa23c36f7628fbc424c323cc8)`()` | 
`public void `[`Update`](#classgazebo_1_1_underwater_current_plugin_1adb9ca73dfee4c4ac0f98e1d87dcd2aa8)`(const common::UpdateInfo & _info)` | Update the simulation state.
`protected event::ConnectionPtr `[`updateConnection`](#classgazebo_1_1_underwater_current_plugin_1a23c0101c0c3c71f512727a4a3ba75d28) | Update event.
`protected physics::WorldPtr `[`world`](#classgazebo_1_1_underwater_current_plugin_1a3a758a0e71061bcdc7ca82c2bfab6fc4) | Pointer to world.
`protected sdf::ElementPtr `[`sdf`](#classgazebo_1_1_underwater_current_plugin_1ad082f3db4ccdc319ce003add6a21c18f) | Pointer to sdf.
`protected bool `[`hasSurface`](#classgazebo_1_1_underwater_current_plugin_1a4654b0504fbad298f0d73357ab17a131) | True if the sea surface is present.
`protected transport::NodePtr `[`node`](#classgazebo_1_1_underwater_current_plugin_1a92e9794c05da0bba890d582232cc0f85) | Pointer to a node for communication.
`protected std::map< std::string, transport::PublisherPtr > `[`publishers`](#classgazebo_1_1_underwater_current_plugin_1a1590e7fe4479c23286fde33697bf365f) | Map of publishers.
`protected std::string `[`currentVelocityTopic`](#classgazebo_1_1_underwater_current_plugin_1a4ac6ce6988a4ef57df89e865ea658c79) | Current velocity topic.
`protected std::string `[`ns`](#classgazebo_1_1_underwater_current_plugin_1a5bdd48d0cd5a5895935bd7326bf8863d) | Namespace for topics and services.
`protected `[`GaussMarkovProcess`](#classgazebo_1_1_gauss_markov_process)` `[`currentVelModel`](#classgazebo_1_1_underwater_current_plugin_1af97217b7fc6ee9e751cdabfeb8615499) | Gauss-Markov process instance for the current velocity.
`protected `[`GaussMarkovProcess`](#classgazebo_1_1_gauss_markov_process)` `[`currentHorzAngleModel`](#classgazebo_1_1_underwater_current_plugin_1af31b1c5721c123f7e4057765d3692a6d) | Gauss-Markov process instance for horizontal angle model.
`protected `[`GaussMarkovProcess`](#classgazebo_1_1_gauss_markov_process)` `[`currentVertAngleModel`](#classgazebo_1_1_underwater_current_plugin_1ac0dfdc167921e5a4066e46c56283b2ec) | Gauss-Markov process instance for vertical angle model.
`protected common::Time `[`lastUpdate`](#classgazebo_1_1_underwater_current_plugin_1a7db4c296d502c5c0133ad3ce0f088ec7) | Last update time stamp.
`protected ignition::math::Vector3d `[`currentVelocity`](#classgazebo_1_1_underwater_current_plugin_1a4b2a08f71f1a6aa4f8404d363d446385) | Current linear velocity vector.
`protected void `[`PublishCurrentVelocity`](#classgazebo_1_1_underwater_current_plugin_1a4587e4131fa4978b360f8e2510502a3a)`()` | Publish current velocity and the pose of its frame.

## Members

#### `public  `[`UnderwaterCurrentPlugin`](#classgazebo_1_1_underwater_current_plugin_1a53ab68e44476969bf9f060e5d373dd7f)`()` 

Class constructor.

#### `public virtual  `[`~UnderwaterCurrentPlugin`](#classgazebo_1_1_underwater_current_plugin_1a6c6a579c9dec4ea61acfa9a9d4fa7600)`()` 

Class destructor.

#### `public virtual void `[`Load`](#classgazebo_1_1_underwater_current_plugin_1a4bf93316f588c10868ed5dba85a14e78)`(physics::WorldPtr _world,sdf::ElementPtr _sdf)` 

#### `public virtual void `[`Init`](#classgazebo_1_1_underwater_current_plugin_1a88d6932fa23c36f7628fbc424c323cc8)`()` 

#### `public void `[`Update`](#classgazebo_1_1_underwater_current_plugin_1adb9ca73dfee4c4ac0f98e1d87dcd2aa8)`(const common::UpdateInfo & _info)` 

Update the simulation state.

#### Parameters
* `_info` Information used in the update event.

#### `protected event::ConnectionPtr `[`updateConnection`](#classgazebo_1_1_underwater_current_plugin_1a23c0101c0c3c71f512727a4a3ba75d28) 

Update event.

#### `protected physics::WorldPtr `[`world`](#classgazebo_1_1_underwater_current_plugin_1a3a758a0e71061bcdc7ca82c2bfab6fc4) 

Pointer to world.

#### `protected sdf::ElementPtr `[`sdf`](#classgazebo_1_1_underwater_current_plugin_1ad082f3db4ccdc319ce003add6a21c18f) 

Pointer to sdf.

#### `protected bool `[`hasSurface`](#classgazebo_1_1_underwater_current_plugin_1a4654b0504fbad298f0d73357ab17a131) 

True if the sea surface is present.

#### `protected transport::NodePtr `[`node`](#classgazebo_1_1_underwater_current_plugin_1a92e9794c05da0bba890d582232cc0f85) 

Pointer to a node for communication.

#### `protected std::map< std::string, transport::PublisherPtr > `[`publishers`](#classgazebo_1_1_underwater_current_plugin_1a1590e7fe4479c23286fde33697bf365f) 

Map of publishers.

#### `protected std::string `[`currentVelocityTopic`](#classgazebo_1_1_underwater_current_plugin_1a4ac6ce6988a4ef57df89e865ea658c79) 

Current velocity topic.

#### `protected std::string `[`ns`](#classgazebo_1_1_underwater_current_plugin_1a5bdd48d0cd5a5895935bd7326bf8863d) 

Namespace for topics and services.

#### `protected `[`GaussMarkovProcess`](#classgazebo_1_1_gauss_markov_process)` `[`currentVelModel`](#classgazebo_1_1_underwater_current_plugin_1af97217b7fc6ee9e751cdabfeb8615499) 

Gauss-Markov process instance for the current velocity.

#### `protected `[`GaussMarkovProcess`](#classgazebo_1_1_gauss_markov_process)` `[`currentHorzAngleModel`](#classgazebo_1_1_underwater_current_plugin_1af31b1c5721c123f7e4057765d3692a6d) 

Gauss-Markov process instance for horizontal angle model.

#### `protected `[`GaussMarkovProcess`](#classgazebo_1_1_gauss_markov_process)` `[`currentVertAngleModel`](#classgazebo_1_1_underwater_current_plugin_1ac0dfdc167921e5a4066e46c56283b2ec) 

Gauss-Markov process instance for vertical angle model.

#### `protected common::Time `[`lastUpdate`](#classgazebo_1_1_underwater_current_plugin_1a7db4c296d502c5c0133ad3ce0f088ec7) 

Last update time stamp.

#### `protected ignition::math::Vector3d `[`currentVelocity`](#classgazebo_1_1_underwater_current_plugin_1a4b2a08f71f1a6aa4f8404d363d446385) 

Current linear velocity vector.

#### `protected void `[`PublishCurrentVelocity`](#classgazebo_1_1_underwater_current_plugin_1a4587e4131fa4978b360f8e2510502a3a)`()` 

Publish current velocity and the pose of its frame.

Generated by [Moxygen](https://sourcey.com/moxygen)