# class `gazebo::HMCylinder` 

```
class gazebo::HMCylinder
  : public gazebo::HMFossen
```  

Class containing the methods and attributes for a hydrodynamic model for a cylinder in the fluid.

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public inline virtual std::string `[`GetType`](#classgazebo_1_1_h_m_cylinder_1af03d6bf3387a364000b7f40fca710ec5)`()` | Return (derived) type of hydrodynamic model.
`public virtual void `[`Print`](#classgazebo_1_1_h_m_cylinder_1afacc200562d7f89d6b04bf18a1d0cfb7)`(std::string _paramName,std::string _message)` | Prints parameters.
`protected double `[`length`](#classgazebo_1_1_h_m_cylinder_1a396afa964665d8f0702391b2cfdf6cc4) | Length of the cylinder.
`protected double `[`radius`](#classgazebo_1_1_h_m_cylinder_1aba2dc883b09294d82f9a87cc197e4a25) | Sphere radius.
`protected std::string `[`axis`](#classgazebo_1_1_h_m_cylinder_1ae872f7cb144c935dd22e84e33b1cdf7e) | Name of the unit rotation axis (just a tag for x, y or z)
`protected double `[`dimRatio`](#classgazebo_1_1_h_m_cylinder_1af173fe2078a149180c5bd7a36c746265) | Ratio between length and diameter.
`protected double `[`cdCirc`](#classgazebo_1_1_h_m_cylinder_1af6ee1fcee5b899e82b5ffdd114d01c49) | Approximated drag coefficient for the circular area.
`protected double `[`cdLength`](#classgazebo_1_1_h_m_cylinder_1a2c81fea33f924981d87c7213d75916fe) | Approximated drag coefficient for the rectangular section.
`protected  `[`HMCylinder`](#classgazebo_1_1_h_m_cylinder_1a84ee35b71884652b527c57e80620176f)`(sdf::ElementPtr _sdf,physics::LinkPtr _link)` | 

## Members

#### `public inline virtual std::string `[`GetType`](#classgazebo_1_1_h_m_cylinder_1af03d6bf3387a364000b7f40fca710ec5)`()` 

Return (derived) type of hydrodynamic model.

#### `public virtual void `[`Print`](#classgazebo_1_1_h_m_cylinder_1afacc200562d7f89d6b04bf18a1d0cfb7)`(std::string _paramName,std::string _message)` 

Prints parameters.

#### `protected double `[`length`](#classgazebo_1_1_h_m_cylinder_1a396afa964665d8f0702391b2cfdf6cc4) 

Length of the cylinder.

#### `protected double `[`radius`](#classgazebo_1_1_h_m_cylinder_1aba2dc883b09294d82f9a87cc197e4a25) 

Sphere radius.

#### `protected std::string `[`axis`](#classgazebo_1_1_h_m_cylinder_1ae872f7cb144c935dd22e84e33b1cdf7e) 

Name of the unit rotation axis (just a tag for x, y or z)

#### `protected double `[`dimRatio`](#classgazebo_1_1_h_m_cylinder_1af173fe2078a149180c5bd7a36c746265) 

Ratio between length and diameter.

#### `protected double `[`cdCirc`](#classgazebo_1_1_h_m_cylinder_1af6ee1fcee5b899e82b5ffdd114d01c49) 

Approximated drag coefficient for the circular area.

#### `protected double `[`cdLength`](#classgazebo_1_1_h_m_cylinder_1a2c81fea33f924981d87c7213d75916fe) 

Approximated drag coefficient for the rectangular section.

#### `protected  `[`HMCylinder`](#classgazebo_1_1_h_m_cylinder_1a84ee35b71884652b527c57e80620176f)`(sdf::ElementPtr _sdf,physics::LinkPtr _link)` 

