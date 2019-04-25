# class `gazebo::HMSphere` 

```
class gazebo::HMSphere
  : public gazebo::HMFossen
```  

Class containing the methods and attributes for a hydrodynamic model for a sphere in the fluid.

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public inline virtual std::string `[`GetType`](#classgazebo_1_1_h_m_sphere_1a6ee346960d84c9013955972feb52cc8b)`()` | Return (derived) type of hydrodynamic model.
`public virtual void `[`Print`](#classgazebo_1_1_h_m_sphere_1acd4564627261d2b9b3008760a4a478d7)`(std::string _paramName,std::string _message)` | Prints parameters.
`protected double `[`radius`](#classgazebo_1_1_h_m_sphere_1a53a9704c540fd283d50118a870d9a8b1) | Sphere radius.
`protected double `[`Cd`](#classgazebo_1_1_h_m_sphere_1a61c1e959e29f452df6dda720e5f6b5c1) | Drag coefficient.
`protected double `[`areaSection`](#classgazebo_1_1_h_m_sphere_1a5081baf0c9306d417ad644e227687b68) | Area of the cross section.
`protected  `[`REGISTER_HYDRODYNAMICMODEL`](#classgazebo_1_1_h_m_sphere_1aeaadb6a68613b17755780a3de522ff5c)`(`[`HMSphere`](#classgazebo_1_1_h_m_sphere)`)` | Register this model with the factory.
`protected  `[`HMSphere`](#classgazebo_1_1_h_m_sphere_1aa7e66a6a55d3eb381c258de70f0b81a6)`(sdf::ElementPtr _sdf,physics::LinkPtr _link)` | 

## Members

#### `public inline virtual std::string `[`GetType`](#classgazebo_1_1_h_m_sphere_1a6ee346960d84c9013955972feb52cc8b)`()` 

Return (derived) type of hydrodynamic model.

#### `public virtual void `[`Print`](#classgazebo_1_1_h_m_sphere_1acd4564627261d2b9b3008760a4a478d7)`(std::string _paramName,std::string _message)` 

Prints parameters.

#### `protected double `[`radius`](#classgazebo_1_1_h_m_sphere_1a53a9704c540fd283d50118a870d9a8b1) 

Sphere radius.

#### `protected double `[`Cd`](#classgazebo_1_1_h_m_sphere_1a61c1e959e29f452df6dda720e5f6b5c1) 

Drag coefficient.

#### `protected double `[`areaSection`](#classgazebo_1_1_h_m_sphere_1a5081baf0c9306d417ad644e227687b68) 

Area of the cross section.

#### `protected  `[`REGISTER_HYDRODYNAMICMODEL`](#classgazebo_1_1_h_m_sphere_1aeaadb6a68613b17755780a3de522ff5c)`(`[`HMSphere`](#classgazebo_1_1_h_m_sphere)`)` 

Register this model with the factory.

#### `protected  `[`HMSphere`](#classgazebo_1_1_h_m_sphere_1aa7e66a6a55d3eb381c258de70f0b81a6)`(sdf::ElementPtr _sdf,physics::LinkPtr _link)` 

