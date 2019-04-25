# class `gazebo::LiftDragTwoLines` 

```
class gazebo::LiftDragTwoLines
  : public gazebo::LiftDrag
```  

Lift&drag model that models lift/drag coeffs using two lines. This is based on Gazebo's LiftDragPlugin but implemented as a derived [LiftDrag](docs/packages/uuv_simulator/docs/api/gazebo::LiftDrag.md#classgazebo_1_1_lift_drag) model to allow using it in combination with the dynamics of a Fin.

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public inline virtual std::string `[`GetType`](#classgazebo_1_1_lift_drag_two_lines_1a541d5835070a1b626cd57c4291c805d0)`()` | Return (derived) type of dynamic system.
`public virtual ignition::math::Vector3d `[`compute`](#classgazebo_1_1_lift_drag_two_lines_1ae88266dfe7c1fc1818cdf0a998b37002)`(const ignition::math::Vector3d & _velL)` | Compute the lift and drag force.
`public virtual bool `[`GetParam`](#classgazebo_1_1_lift_drag_two_lines_1ac5ae08c5d1cbad85f259bcc5b84705b5)`(std::string _tag,double & _output)` | Return paramater in scalar form for the given tag.
`public virtual std::map< std::string, double > `[`GetListParams`](#classgazebo_1_1_lift_drag_two_lines_1ac1e2943c9ebef6ef3471fe293799b726)`()` | Return list of all parameters.
`protected double `[`area`](#classgazebo_1_1_lift_drag_two_lines_1a461fc127b2ec92301d715d6a6b4df69f) | Airfoil area.
`protected double `[`fluidDensity`](#classgazebo_1_1_lift_drag_two_lines_1ac5ea64aeb8b87292fe68a1c024d6d474) | Fluid density.
`protected double `[`a0`](#classgazebo_1_1_lift_drag_two_lines_1a01e4fdcf5d1cb823d782180c7b5e4ac7) | Original zero angle of attack location.
`protected double `[`alphaStall`](#classgazebo_1_1_lift_drag_two_lines_1a4215009b05c352436274ce81e0ddf8c4) | Stall angle.
`protected double `[`cla`](#classgazebo_1_1_lift_drag_two_lines_1a569349db608e180bf2ea30de181ee34a) | Lift coefficient without stall.
`protected double `[`claStall`](#classgazebo_1_1_lift_drag_two_lines_1ad2653c58c571861bd6510b30f3803d39) | Lift coefficient with stall.
`protected double `[`cda`](#classgazebo_1_1_lift_drag_two_lines_1a90b024b3933c2f2c5ee67c026af6b5c8) | Drag coefficient without stall.
`protected double `[`cdaStall`](#classgazebo_1_1_lift_drag_two_lines_1a369bf986130bde7cac35d088f00f8e7a) | Drag coefficient with stall.

## Members

#### `public inline virtual std::string `[`GetType`](#classgazebo_1_1_lift_drag_two_lines_1a541d5835070a1b626cd57c4291c805d0)`()` 

Return (derived) type of dynamic system.

#### `public virtual ignition::math::Vector3d `[`compute`](#classgazebo_1_1_lift_drag_two_lines_1ae88266dfe7c1fc1818cdf0a998b37002)`(const ignition::math::Vector3d & _velL)` 

Compute the lift and drag force.

#### `public virtual bool `[`GetParam`](#classgazebo_1_1_lift_drag_two_lines_1ac5ae08c5d1cbad85f259bcc5b84705b5)`(std::string _tag,double & _output)` 

Return paramater in scalar form for the given tag.

#### `public virtual std::map< std::string, double > `[`GetListParams`](#classgazebo_1_1_lift_drag_two_lines_1ac1e2943c9ebef6ef3471fe293799b726)`()` 

Return list of all parameters.

#### `protected double `[`area`](#classgazebo_1_1_lift_drag_two_lines_1a461fc127b2ec92301d715d6a6b4df69f) 

Airfoil area.

#### `protected double `[`fluidDensity`](#classgazebo_1_1_lift_drag_two_lines_1ac5ea64aeb8b87292fe68a1c024d6d474) 

Fluid density.

#### `protected double `[`a0`](#classgazebo_1_1_lift_drag_two_lines_1a01e4fdcf5d1cb823d782180c7b5e4ac7) 

Original zero angle of attack location.

#### `protected double `[`alphaStall`](#classgazebo_1_1_lift_drag_two_lines_1a4215009b05c352436274ce81e0ddf8c4) 

Stall angle.

#### `protected double `[`cla`](#classgazebo_1_1_lift_drag_two_lines_1a569349db608e180bf2ea30de181ee34a) 

Lift coefficient without stall.

#### `protected double `[`claStall`](#classgazebo_1_1_lift_drag_two_lines_1ad2653c58c571861bd6510b30f3803d39) 

Lift coefficient with stall.

#### `protected double `[`cda`](#classgazebo_1_1_lift_drag_two_lines_1a90b024b3933c2f2c5ee67c026af6b5c8) 

Drag coefficient without stall.

#### `protected double `[`cdaStall`](#classgazebo_1_1_lift_drag_two_lines_1a369bf986130bde7cac35d088f00f8e7a) 

Drag coefficient with stall.

