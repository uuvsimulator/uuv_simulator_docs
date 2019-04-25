# class `gazebo::ThrusterDynamicsYoerger` 

```
class gazebo::ThrusterDynamicsYoerger
  : public gazebo::Dynamics
```  

Yoerger's dynamic thruster model.

This is the lumped-parameter model of Yoerger et al.: The influence of thruster dynamics on underwater vehicle behavior and their incorporation into control system design. (1990)

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public inline virtual std::string `[`GetType`](#classgazebo_1_1_thruster_dynamics_yoerger_1a71e827ac4c6ed26139b35d0fb72f5c3e)`()` | Return (derived) type of dynamic system.
`public virtual double `[`update`](#classgazebo_1_1_thruster_dynamics_yoerger_1a0d43ff9c18a4caa3b056c50f4997de85)`(double _cmd,double _t)` | Update dynamical model given input value and time.

## Members

#### `public inline virtual std::string `[`GetType`](#classgazebo_1_1_thruster_dynamics_yoerger_1a71e827ac4c6ed26139b35d0fb72f5c3e)`()` 

Return (derived) type of dynamic system.

#### `public virtual double `[`update`](#classgazebo_1_1_thruster_dynamics_yoerger_1a0d43ff9c18a4caa3b056c50f4997de85)`(double _cmd,double _t)` 

Update dynamical model given input value and time.

