# class `gazebo::LiftDragFactory` 

Factory singleton class that creates a [LiftDrag](docs/packages/uuv_simulator/docs/api/gazebo::LiftDrag.md#classgazebo_1_1_lift_drag) from sdf.

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public `[`LiftDrag`](docs/packages/uuv_simulator/docs/api/gazebo::LiftDrag.md#classgazebo_1_1_lift_drag)` * `[`CreateLiftDrag`](#classgazebo_1_1_lift_drag_factory_1a7a79c4e602ee766109f7ff64de1db8ac)`(sdf::ElementPtr _sdf)` | Create [LiftDrag](docs/packages/uuv_simulator/docs/api/gazebo::LiftDrag.md#classgazebo_1_1_lift_drag) object according to its sdf Description.
`public bool `[`RegisterCreator`](#classgazebo_1_1_lift_drag_factory_1addb70527ea530e2f7d260a077657f722)`(const std::string & _identifier,LiftDragCreator _creator)` | Register a [LiftDrag](docs/packages/uuv_simulator/docs/api/gazebo::LiftDrag.md#classgazebo_1_1_lift_drag) class with its creator.

## Members

#### `public `[`LiftDrag`](docs/packages/uuv_simulator/docs/api/gazebo::LiftDrag.md#classgazebo_1_1_lift_drag)` * `[`CreateLiftDrag`](#classgazebo_1_1_lift_drag_factory_1a7a79c4e602ee766109f7ff64de1db8ac)`(sdf::ElementPtr _sdf)` 

Create [LiftDrag](docs/packages/uuv_simulator/docs/api/gazebo::LiftDrag.md#classgazebo_1_1_lift_drag) object according to its sdf Description.

#### `public bool `[`RegisterCreator`](#classgazebo_1_1_lift_drag_factory_1addb70527ea530e2f7d260a077657f722)`(const std::string & _identifier,LiftDragCreator _creator)` 

Register a [LiftDrag](docs/packages/uuv_simulator/docs/api/gazebo::LiftDrag.md#classgazebo_1_1_lift_drag) class with its creator.

