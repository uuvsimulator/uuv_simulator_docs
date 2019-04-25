# class `gazebo::LiftDrag` 

Abstract base class for Lift&Drag models.

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public inline virtual  `[`~LiftDrag`](#classgazebo_1_1_lift_drag_1a7025e5299778dfb25ee8e1eaed4ecb83)`()` | Destructor.
`public std::string `[`GetType`](#classgazebo_1_1_lift_drag_1ad8a25e574ba7f75b30e8813b315010b3)`()` | Return (derived) type of lift&drag model.
`public ignition::math::Vector3d `[`compute`](#classgazebo_1_1_lift_drag_1ac20f4dbd4ea08d8d9d0852f8e2b128b0)`(const ignition::math::Vector3d & _velL)` | Compute the lift and drag force.
`public bool `[`GetParam`](#classgazebo_1_1_lift_drag_1a4e2d58afb4af2ba7c0f169cd8fcebb3b)`(std::string _tag,double & _output)` | Return paramater in vector form for the given tag.
`public std::map< std::string, double > `[`GetListParams`](#classgazebo_1_1_lift_drag_1a7d35e963ce57451f5939ccff9a956285)`()` | Return list of all parameters.
`protected double `[`prevTime`](#classgazebo_1_1_lift_drag_1aa062dc13d3a5c4b9d6de277cc578eee7) | Time of last state update.
`protected double `[`state`](#classgazebo_1_1_lift_drag_1a73cd43d69e94ce2a392abe437c732cb0) | Latest state.
`protected inline  `[`LiftDrag`](#classgazebo_1_1_lift_drag_1aa9f53de408dfca89a517be7dbcd673c6)`()` | Protected constructor: Use the factory for object creation.

## Members

#### `public inline virtual  `[`~LiftDrag`](#classgazebo_1_1_lift_drag_1a7025e5299778dfb25ee8e1eaed4ecb83)`()` 

Destructor.

#### `public std::string `[`GetType`](#classgazebo_1_1_lift_drag_1ad8a25e574ba7f75b30e8813b315010b3)`()` 

Return (derived) type of lift&drag model.

#### `public ignition::math::Vector3d `[`compute`](#classgazebo_1_1_lift_drag_1ac20f4dbd4ea08d8d9d0852f8e2b128b0)`(const ignition::math::Vector3d & _velL)` 

Compute the lift and drag force.

#### `public bool `[`GetParam`](#classgazebo_1_1_lift_drag_1a4e2d58afb4af2ba7c0f169cd8fcebb3b)`(std::string _tag,double & _output)` 

Return paramater in vector form for the given tag.

#### `public std::map< std::string, double > `[`GetListParams`](#classgazebo_1_1_lift_drag_1a7d35e963ce57451f5939ccff9a956285)`()` 

Return list of all parameters.

#### `protected double `[`prevTime`](#classgazebo_1_1_lift_drag_1aa062dc13d3a5c4b9d6de277cc578eee7) 

Time of last state update.

#### `protected double `[`state`](#classgazebo_1_1_lift_drag_1a73cd43d69e94ce2a392abe437c732cb0) 

Latest state.

#### `protected inline  `[`LiftDrag`](#classgazebo_1_1_lift_drag_1aa9f53de408dfca89a517be7dbcd673c6)`()` 

Protected constructor: Use the factory for object creation.

