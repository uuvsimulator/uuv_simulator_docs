# class `gazebo::LiftDragQuadratic` 

```
class gazebo::LiftDragQuadratic
  : public gazebo::LiftDrag
```  

Basic quadratic (Hugin) lift&drag model, page 18 from [1]. [1] Engelhardtsen, Øystein. "3D AUV Collision Avoidance." (2007).

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public inline virtual std::string `[`GetType`](#classgazebo_1_1_lift_drag_quadratic_1a1e9fd0549b24b7148e12011a0f294eb5)`()` | Return (derived) type of dynamic system.
`public virtual ignition::math::Vector3d `[`compute`](#classgazebo_1_1_lift_drag_quadratic_1ae187246d00eb5202a72faa5828ab2f00)`(const ignition::math::Vector3d & velL)` | Compute the lift and drag force.
`public virtual bool `[`GetParam`](#classgazebo_1_1_lift_drag_quadratic_1add46239f7abd7ed73c700c6cfb0dc63a)`(std::string _tag,double & _output)` | Return paramater in scalar form for the given tag.
`public virtual std::map< std::string, double > `[`GetListParams`](#classgazebo_1_1_lift_drag_quadratic_1abeb288db759bcc85f8e6414e4c07e326)`()` | Return list of all parameters.
`protected double `[`liftConstant`](#classgazebo_1_1_lift_drag_quadratic_1abbe2a7518c24690bee23fe9bde91092e) | Lift constant.
`protected double `[`dragConstant`](#classgazebo_1_1_lift_drag_quadratic_1a78a7b21bef504b05c84da40ed47699ad) | Drag constant.

## Members

#### `public inline virtual std::string `[`GetType`](#classgazebo_1_1_lift_drag_quadratic_1a1e9fd0549b24b7148e12011a0f294eb5)`()` 

Return (derived) type of dynamic system.

#### `public virtual ignition::math::Vector3d `[`compute`](#classgazebo_1_1_lift_drag_quadratic_1ae187246d00eb5202a72faa5828ab2f00)`(const ignition::math::Vector3d & velL)` 

Compute the lift and drag force.

#### `public virtual bool `[`GetParam`](#classgazebo_1_1_lift_drag_quadratic_1add46239f7abd7ed73c700c6cfb0dc63a)`(std::string _tag,double & _output)` 

Return paramater in scalar form for the given tag.

#### `public virtual std::map< std::string, double > `[`GetListParams`](#classgazebo_1_1_lift_drag_quadratic_1abeb288db759bcc85f8e6414e4c07e326)`()` 

Return list of all parameters.

#### `protected double `[`liftConstant`](#classgazebo_1_1_lift_drag_quadratic_1abbe2a7518c24690bee23fe9bde91092e) 

Lift constant.

#### `protected double `[`dragConstant`](#classgazebo_1_1_lift_drag_quadratic_1a78a7b21bef504b05c84da40ed47699ad) 

Drag constant.

