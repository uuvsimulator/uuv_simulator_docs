# class `gazebo::ThrusterDynamicsBessa` 

```
class gazebo::ThrusterDynamicsBessa
  : public gazebo::Dynamics
```  

Bessa's dynamic thruster model.

This is "Model 2" described in Bessa et al.: Dynamic Positioning of Underwater Robotic Vehicles with Thruster [Dynamics](docs/packages/uuv_simulator/docs/api/gazebo::Dynamics.md#classgazebo_1_1_dynamics) Compensation.

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public inline virtual std::string `[`GetType`](#classgazebo_1_1_thruster_dynamics_bessa_1a141b10b080998366163f31793fd93a78)`()` | Return (derived) type of dynamic system.
`public virtual double `[`update`](#classgazebo_1_1_thruster_dynamics_bessa_1a4eaffe57006894124ec0f62987785996)`(double _cmd,double _t)` | Update dynamical model given input value and time.

## Members

#### `public inline virtual std::string `[`GetType`](#classgazebo_1_1_thruster_dynamics_bessa_1a141b10b080998366163f31793fd93a78)`()` 

Return (derived) type of dynamic system.

#### `public virtual double `[`update`](#classgazebo_1_1_thruster_dynamics_bessa_1a4eaffe57006894124ec0f62987785996)`(double _cmd,double _t)` 

Update dynamical model given input value and time.

