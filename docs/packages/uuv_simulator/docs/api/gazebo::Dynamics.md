# class `gazebo::Dynamics` 

Abstract base class for thruster dynamics.

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public inline virtual  `[`~Dynamics`](#classgazebo_1_1_dynamics_1a93c023678bcde05d9cc280afe071b889)`()` | Destructor.
`public std::string `[`GetType`](#classgazebo_1_1_dynamics_1ae9efe1854032da39ab230063c0303549)`()` | Return (derived) type of thruster dynamics.
`public double `[`update`](#classgazebo_1_1_dynamics_1a7cae772ac89944d52757c7883d75f93a)`(double _cmd,double _t)` | Update the dynamic model.
`public virtual void `[`Reset`](#classgazebo_1_1_dynamics_1a4ca9ecc33bdd2e3cf8a42a928a9eec8f)`()` | 
`protected double `[`prevTime`](#classgazebo_1_1_dynamics_1a27de443c5e85c6ab6ddcbb31e880d4b2) | Time of last state update.
`protected double `[`state`](#classgazebo_1_1_dynamics_1a4c2f128d2d0ef4d312936f66106cf229) | Latest state.
`protected inline  `[`Dynamics`](#classgazebo_1_1_dynamics_1a4e590f9f7264d3d7e22c08d9b7737f1a)`()` | Protected constructor: Use the factory for object creation.

## Members

#### `public inline virtual  `[`~Dynamics`](#classgazebo_1_1_dynamics_1a93c023678bcde05d9cc280afe071b889)`()` 

Destructor.

#### `public std::string `[`GetType`](#classgazebo_1_1_dynamics_1ae9efe1854032da39ab230063c0303549)`()` 

Return (derived) type of thruster dynamics.

#### `public double `[`update`](#classgazebo_1_1_dynamics_1a7cae772ac89944d52757c7883d75f93a)`(double _cmd,double _t)` 

Update the dynamic model.

#### Parameters
* `_cmd` The commanded value. 

* `_t` Time stamp of command.

#### `public virtual void `[`Reset`](#classgazebo_1_1_dynamics_1a4ca9ecc33bdd2e3cf8a42a928a9eec8f)`()` 

#### `protected double `[`prevTime`](#classgazebo_1_1_dynamics_1a27de443c5e85c6ab6ddcbb31e880d4b2) 

Time of last state update.

#### `protected double `[`state`](#classgazebo_1_1_dynamics_1a4c2f128d2d0ef4d312936f66106cf229) 

Latest state.

#### `protected inline  `[`Dynamics`](#classgazebo_1_1_dynamics_1a4e590f9f7264d3d7e22c08d9b7737f1a)`()` 

Protected constructor: Use the factory for object creation.

