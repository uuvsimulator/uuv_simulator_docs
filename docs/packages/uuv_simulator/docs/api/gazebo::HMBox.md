# class `gazebo::HMBox` 

```
class gazebo::HMBox
  : public gazebo::HMFossen
```  

Class containing the methods and attributes for a hydrodynamic model for a box in the fluid.

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public inline virtual std::string `[`GetType`](#classgazebo_1_1_h_m_box_1a6617b9acdab36fa004feb27b7a05f6ef)`()` | Return (derived) type of hydrodynamic model.
`public virtual void `[`Print`](#classgazebo_1_1_h_m_box_1a56a3123563c1f6dfa78a4f124d495c72)`(std::string _paramName,std::string _message)` | Prints parameters.
`protected double `[`Cd`](#classgazebo_1_1_h_m_box_1ac2c2cc1ea1fbb98b17f47ebede1261e3) | Drag coefficient.
`protected double `[`length`](#classgazebo_1_1_h_m_box_1a13e4a2034e9c0b727087c2525bd84acf) | Length of the box.
`protected double `[`width`](#classgazebo_1_1_h_m_box_1ab0d0b9465a2f7f595d5922d3ed45a9c4) | Width of the box.
`protected double `[`height`](#classgazebo_1_1_h_m_box_1a73325f0d7d5098892963503f5b6c3149) | Height of the box.
`protected  `[`HMBox`](#classgazebo_1_1_h_m_box_1af1d27f2047dbcfa9b979179f5f3ef870)`(sdf::ElementPtr _sdf,physics::LinkPtr _link)` | Constructor.

## Members

#### `public inline virtual std::string `[`GetType`](#classgazebo_1_1_h_m_box_1a6617b9acdab36fa004feb27b7a05f6ef)`()` 

Return (derived) type of hydrodynamic model.

#### `public virtual void `[`Print`](#classgazebo_1_1_h_m_box_1a56a3123563c1f6dfa78a4f124d495c72)`(std::string _paramName,std::string _message)` 

Prints parameters.

#### `protected double `[`Cd`](#classgazebo_1_1_h_m_box_1ac2c2cc1ea1fbb98b17f47ebede1261e3) 

Drag coefficient.

#### `protected double `[`length`](#classgazebo_1_1_h_m_box_1a13e4a2034e9c0b727087c2525bd84acf) 

Length of the box.

#### `protected double `[`width`](#classgazebo_1_1_h_m_box_1ab0d0b9465a2f7f595d5922d3ed45a9c4) 

Width of the box.

#### `protected double `[`height`](#classgazebo_1_1_h_m_box_1a73325f0d7d5098892963503f5b6c3149) 

Height of the box.

#### `protected  `[`HMBox`](#classgazebo_1_1_h_m_box_1af1d27f2047dbcfa9b979179f5f3ef870)`(sdf::ElementPtr _sdf,physics::LinkPtr _link)` 

Constructor.

