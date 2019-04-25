# class `gazebo::HMSpheroid` 

```
class gazebo::HMSpheroid
  : public gazebo::HMFossen
```  

Class containing the methods and attributes for a hydrodynamic model for a spheroid in the fluid Reference: Antonelli - Underwater Robots.

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public inline virtual std::string `[`GetType`](#classgazebo_1_1_h_m_spheroid_1a2af19270ed7d89121ad909c2d295d2ff)`()` | Return (derived) type of hydrodynamic model.
`public virtual void `[`Print`](#classgazebo_1_1_h_m_spheroid_1a76aa73929b7c32a19d578bea07dea1f1)`(std::string _paramName,std::string _message)` | Prints parameters.
`protected double `[`length`](#classgazebo_1_1_h_m_spheroid_1a3de304ad70f38d3ef85501c5533c39a3) | Length of the sphroid.
`protected double `[`radius`](#classgazebo_1_1_h_m_spheroid_1a1aab5b64e948769bf729157ce0f3ae8d) | Prolate spheroid's smaller radius.
`protected  `[`HMSpheroid`](#classgazebo_1_1_h_m_spheroid_1afdf9b645d329cd9d774375d2f167d03d)`(sdf::ElementPtr _sdf,physics::LinkPtr _link)` | 

## Members

#### `public inline virtual std::string `[`GetType`](#classgazebo_1_1_h_m_spheroid_1a2af19270ed7d89121ad909c2d295d2ff)`()` 

Return (derived) type of hydrodynamic model.

#### `public virtual void `[`Print`](#classgazebo_1_1_h_m_spheroid_1a76aa73929b7c32a19d578bea07dea1f1)`(std::string _paramName,std::string _message)` 

Prints parameters.

#### `protected double `[`length`](#classgazebo_1_1_h_m_spheroid_1a3de304ad70f38d3ef85501c5533c39a3) 

Length of the sphroid.

#### `protected double `[`radius`](#classgazebo_1_1_h_m_spheroid_1a1aab5b64e948769bf729157ce0f3ae8d) 

Prolate spheroid's smaller radius.

#### `protected  `[`HMSpheroid`](#classgazebo_1_1_h_m_spheroid_1afdf9b645d329cd9d774375d2f167d03d)`(sdf::ElementPtr _sdf,physics::LinkPtr _link)` 

