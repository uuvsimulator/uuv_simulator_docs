# class `gazebo::UmbilicalModel` 

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public inline virtual  `[`~UmbilicalModel`](#classgazebo_1_1_umbilical_model_1a6219268fde521f1873477227342e22f8)`()` | Destructor.
`public virtual void `[`Init`](#classgazebo_1_1_umbilical_model_1adbc3a2261e2f18bf139ebcd4bdad9a2e)`()` | Initialize model.
`public void `[`OnUpdate`](#classgazebo_1_1_umbilical_model_1ae2c720369c5eea2d3562a73d9031571b)`(const common::UpdateInfo & _info,const ignition::math::Vector3d & _flow)` | Update Umbilical (and apply forces)
`protected physics::ModelPtr `[`model`](#classgazebo_1_1_umbilical_model_1a48ea9fa0b8db157b948b1a6f21e94be1) | Gazebo model to which this umbilical belongs.
`protected physics::LinkPtr `[`connector`](#classgazebo_1_1_umbilical_model_1a83ea6576e2b766d962be574e576413bd) | Moving connector link of this umbilical.
`protected inline  `[`UmbilicalModel`](#classgazebo_1_1_umbilical_model_1a71941e80b15a64440d87138956e93774)`()` | Protected constructor: Use the factory instead.

## Members

#### `public inline virtual  `[`~UmbilicalModel`](#classgazebo_1_1_umbilical_model_1a6219268fde521f1873477227342e22f8)`()` 

Destructor.

#### `public virtual void `[`Init`](#classgazebo_1_1_umbilical_model_1adbc3a2261e2f18bf139ebcd4bdad9a2e)`()` 

Initialize model.

#### `public void `[`OnUpdate`](#classgazebo_1_1_umbilical_model_1ae2c720369c5eea2d3562a73d9031571b)`(const common::UpdateInfo & _info,const ignition::math::Vector3d & _flow)` 

Update Umbilical (and apply forces)

#### `protected physics::ModelPtr `[`model`](#classgazebo_1_1_umbilical_model_1a48ea9fa0b8db157b948b1a6f21e94be1) 

Gazebo model to which this umbilical belongs.

#### `protected physics::LinkPtr `[`connector`](#classgazebo_1_1_umbilical_model_1a83ea6576e2b766d962be574e576413bd) 

Moving connector link of this umbilical.

#### `protected inline  `[`UmbilicalModel`](#classgazebo_1_1_umbilical_model_1a71941e80b15a64440d87138956e93774)`()` 

Protected constructor: Use the factory instead.

