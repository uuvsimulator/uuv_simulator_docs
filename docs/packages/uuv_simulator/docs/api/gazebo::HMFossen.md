# class `gazebo::HMFossen` 

```
class gazebo::HMFossen
  : public gazebo::HydrodynamicModel
```  

Class containting the methods and attributes for a Fossen robot-like hydrodynamic model. The restoring forces are applied by the [BuoyantObject](docs/packages/uuv_simulator/docs/api/gazebo::BuoyantObject.md#classgazebo_1_1_buoyant_object) class methods. Using the plugin for UUV models will use both this and the buoyant object class definitions, therefore the restoring forces were not inherited here. References:

* Fossen, Thor, "Handbook of Marine Craft and Hydrodynamics and Motion
      Control", 2011

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public inline virtual std::string `[`GetType`](#classgazebo_1_1_h_m_fossen_1aab89ea21b6813039f229fc7b9a8fcc0d)`()` | Return (derived) type of hydrodynamic model.
`public virtual void `[`Print`](#classgazebo_1_1_h_m_fossen_1abd8c4e6caecac0a09fdbfa4d7d6b3b54)`(std::string _paramName,std::string _message)` | Prints parameters.
`public virtual bool `[`GetParam`](#classgazebo_1_1_h_m_fossen_1aef89b7d0c921eed479aea9f825de8883)`(std::string _tag,std::vector< double > & _output)` | Return paramater in vector form for the given tag.
`public virtual bool `[`GetParam`](#classgazebo_1_1_h_m_fossen_1acc9a5f5880cc346390a036f8561127ee)`(std::string _tag,double & _output)` | Return paramater in scalar form for the given tag.
`public virtual bool `[`SetParam`](#classgazebo_1_1_h_m_fossen_1ad312189912d8613083fc53570ed07ae0)`(std::string _tag,double _input)` | Set scalar parameter.
`public virtual void `[`ApplyHydrodynamicForces`](#classgazebo_1_1_h_m_fossen_1ad13894a8127a248f9c8c79678266ed07)`(double time,const ignition::math::Vector3d & _flowVelWorld)` | Computation of the hydrodynamic forces.
`protected `[`Eigen::Matrix6d`](docs/packages/uuv_simulator/docs/api/Matrix6d.md#_def_8hh_1ab6f8b8b11b0f6350ed45e7cd3437207f)` `[`Ma`](#classgazebo_1_1_h_m_fossen_1a2a31c659331c826a6d80abe7755e473e) | Added-mass matrix.
`protected double `[`scalingAddedMass`](#classgazebo_1_1_h_m_fossen_1ada6f90d47445047d905e8fe3794885ac) | Scaling of the added-mass matrix.
`protected double `[`offsetAddedMass`](#classgazebo_1_1_h_m_fossen_1ab326125b3b49893d7492f4778d6ace55) | Offset for the added-mass matrix.
`protected `[`Eigen::Matrix6d`](docs/packages/uuv_simulator/docs/api/Matrix6d.md#_def_8hh_1ab6f8b8b11b0f6350ed45e7cd3437207f)` `[`Ca`](#classgazebo_1_1_h_m_fossen_1aafd51761404afd9b1e98f0b1ecb0b14f) | Added-mass associated Coriolis matrix.
`protected `[`Eigen::Matrix6d`](docs/packages/uuv_simulator/docs/api/Matrix6d.md#_def_8hh_1ab6f8b8b11b0f6350ed45e7cd3437207f)` `[`D`](#classgazebo_1_1_h_m_fossen_1a20df2ff4d0a155b41c275d37e621e32f) | Damping matrix.
`protected double `[`scalingDamping`](#classgazebo_1_1_h_m_fossen_1a5d5f9e75be8dbbd2b8bbfbc81ba55cf3) | Scaling of the damping matrix.
`protected double `[`offsetLinearDamping`](#classgazebo_1_1_h_m_fossen_1adc9dd4195791aab3ebaf12bdbe2e293e) | Offset for the linear damping matrix.
`protected double `[`offsetLinForwardSpeedDamping`](#classgazebo_1_1_h_m_fossen_1a1c9074d7810329daca5f3ea42e6307cb) | Offset for the linear damping matrix.
`protected double `[`offsetNonLinDamping`](#classgazebo_1_1_h_m_fossen_1a6e2bfe2801f2697f0e0c087a45158ff3) | Offset for the linear damping matrix.
`protected `[`Eigen::Matrix6d`](docs/packages/uuv_simulator/docs/api/Matrix6d.md#_def_8hh_1ab6f8b8b11b0f6350ed45e7cd3437207f)` `[`DLin`](#classgazebo_1_1_h_m_fossen_1a1301b0130643ce7d55b8ff238afdc264) | Linear damping matrix.
`protected `[`Eigen::Matrix6d`](docs/packages/uuv_simulator/docs/api/Matrix6d.md#_def_8hh_1ab6f8b8b11b0f6350ed45e7cd3437207f)` `[`DLinForwardSpeed`](#classgazebo_1_1_h_m_fossen_1a9a2cc66ad71a7fc9ce904f5cc27a36f0) | Linear damping matrix proportional only to the forward speed (useful for modeling AUVs). From [1], according to Newman (1977), there is a damping force component that linearly increases with the presence of forward speed, particularly so for slender bodies.
`protected `[`Eigen::Matrix6d`](docs/packages/uuv_simulator/docs/api/Matrix6d.md#_def_8hh_1ab6f8b8b11b0f6350ed45e7cd3437207f)` `[`DNonLin`](#classgazebo_1_1_h_m_fossen_1a3219a54c0be1a8a1e186b33dde95d6b5) | Nonlinear damping coefficients.
`protected std::vector< double > `[`linearDampCoef`](#classgazebo_1_1_h_m_fossen_1aaaee5e4e341d1f3fccba9c832429712d) | Linear damping coefficients.
`protected std::vector< double > `[`quadDampCoef`](#classgazebo_1_1_h_m_fossen_1a062e26123041365e16822bc2059fe3d1) | Quadratic damping coefficients.
`protected  `[`REGISTER_HYDRODYNAMICMODEL`](#classgazebo_1_1_h_m_fossen_1ab3a59be3a5e9037575ee6f4878e96d8b)`(`[`HMFossen`](#classgazebo_1_1_h_m_fossen)`)` | Register this model with the factory.
`protected  `[`HMFossen`](#classgazebo_1_1_h_m_fossen_1a9b9fcbd9ca518c9cd41300e0f9d43ee5)`(sdf::ElementPtr _sdf,physics::LinkPtr _link)` | 
`protected void `[`ComputeAddedCoriolisMatrix`](#classgazebo_1_1_h_m_fossen_1afe97af45fc44777a04b4f1c81519b07b)`(const `[`Eigen::Vector6d`](docs/packages/uuv_simulator/docs/api/Vector6d.md#_def_8hh_1a09219f5e0b822edbf24b125e0e2a4fe0)` & _vel,const `[`Eigen::Matrix6d`](docs/packages/uuv_simulator/docs/api/Matrix6d.md#_def_8hh_1ab6f8b8b11b0f6350ed45e7cd3437207f)` & _Ma,`[`Eigen::Matrix6d`](docs/packages/uuv_simulator/docs/api/Matrix6d.md#_def_8hh_1ab6f8b8b11b0f6350ed45e7cd3437207f)` & _Ca) const` | Computes the added-mass Coriolis matrix Ca.
`protected void `[`ComputeDampingMatrix`](#classgazebo_1_1_h_m_fossen_1a19624761792eac92864647ebee971196)`(const `[`Eigen::Vector6d`](docs/packages/uuv_simulator/docs/api/Vector6d.md#_def_8hh_1a09219f5e0b822edbf24b125e0e2a4fe0)` & _vel,`[`Eigen::Matrix6d`](docs/packages/uuv_simulator/docs/api/Matrix6d.md#_def_8hh_1ab6f8b8b11b0f6350ed45e7cd3437207f)` & _D) const` | Updates the damping matrix for the current velocity.
`protected `[`Eigen::Matrix6d`](docs/packages/uuv_simulator/docs/api/Matrix6d.md#_def_8hh_1ab6f8b8b11b0f6350ed45e7cd3437207f)` `[`GetAddedMass`](#classgazebo_1_1_h_m_fossen_1a555bb01ef30396e3b39fa26bf6a79848)`() const` | Returns the added-mass matrix with the scaling and offset.

## Members

#### `public inline virtual std::string `[`GetType`](#classgazebo_1_1_h_m_fossen_1aab89ea21b6813039f229fc7b9a8fcc0d)`()` 

Return (derived) type of hydrodynamic model.

#### `public virtual void `[`Print`](#classgazebo_1_1_h_m_fossen_1abd8c4e6caecac0a09fdbfa4d7d6b3b54)`(std::string _paramName,std::string _message)` 

Prints parameters.

#### `public virtual bool `[`GetParam`](#classgazebo_1_1_h_m_fossen_1aef89b7d0c921eed479aea9f825de8883)`(std::string _tag,std::vector< double > & _output)` 

Return paramater in vector form for the given tag.

#### `public virtual bool `[`GetParam`](#classgazebo_1_1_h_m_fossen_1acc9a5f5880cc346390a036f8561127ee)`(std::string _tag,double & _output)` 

Return paramater in scalar form for the given tag.

#### `public virtual bool `[`SetParam`](#classgazebo_1_1_h_m_fossen_1ad312189912d8613083fc53570ed07ae0)`(std::string _tag,double _input)` 

Set scalar parameter.

#### `public virtual void `[`ApplyHydrodynamicForces`](#classgazebo_1_1_h_m_fossen_1ad13894a8127a248f9c8c79678266ed07)`(double time,const ignition::math::Vector3d & _flowVelWorld)` 

Computation of the hydrodynamic forces.

#### `protected `[`Eigen::Matrix6d`](docs/packages/uuv_simulator/docs/api/Matrix6d.md#_def_8hh_1ab6f8b8b11b0f6350ed45e7cd3437207f)` `[`Ma`](#classgazebo_1_1_h_m_fossen_1a2a31c659331c826a6d80abe7755e473e) 

Added-mass matrix.

#### `protected double `[`scalingAddedMass`](#classgazebo_1_1_h_m_fossen_1ada6f90d47445047d905e8fe3794885ac) 

Scaling of the added-mass matrix.

#### `protected double `[`offsetAddedMass`](#classgazebo_1_1_h_m_fossen_1ab326125b3b49893d7492f4778d6ace55) 

Offset for the added-mass matrix.

#### `protected `[`Eigen::Matrix6d`](docs/packages/uuv_simulator/docs/api/Matrix6d.md#_def_8hh_1ab6f8b8b11b0f6350ed45e7cd3437207f)` `[`Ca`](#classgazebo_1_1_h_m_fossen_1aafd51761404afd9b1e98f0b1ecb0b14f) 

Added-mass associated Coriolis matrix.

#### `protected `[`Eigen::Matrix6d`](docs/packages/uuv_simulator/docs/api/Matrix6d.md#_def_8hh_1ab6f8b8b11b0f6350ed45e7cd3437207f)` `[`D`](#classgazebo_1_1_h_m_fossen_1a20df2ff4d0a155b41c275d37e621e32f) 

Damping matrix.

#### `protected double `[`scalingDamping`](#classgazebo_1_1_h_m_fossen_1a5d5f9e75be8dbbd2b8bbfbc81ba55cf3) 

Scaling of the damping matrix.

#### `protected double `[`offsetLinearDamping`](#classgazebo_1_1_h_m_fossen_1adc9dd4195791aab3ebaf12bdbe2e293e) 

Offset for the linear damping matrix.

#### `protected double `[`offsetLinForwardSpeedDamping`](#classgazebo_1_1_h_m_fossen_1a1c9074d7810329daca5f3ea42e6307cb) 

Offset for the linear damping matrix.

#### `protected double `[`offsetNonLinDamping`](#classgazebo_1_1_h_m_fossen_1a6e2bfe2801f2697f0e0c087a45158ff3) 

Offset for the linear damping matrix.

#### `protected `[`Eigen::Matrix6d`](docs/packages/uuv_simulator/docs/api/Matrix6d.md#_def_8hh_1ab6f8b8b11b0f6350ed45e7cd3437207f)` `[`DLin`](#classgazebo_1_1_h_m_fossen_1a1301b0130643ce7d55b8ff238afdc264) 

Linear damping matrix.

#### `protected `[`Eigen::Matrix6d`](docs/packages/uuv_simulator/docs/api/Matrix6d.md#_def_8hh_1ab6f8b8b11b0f6350ed45e7cd3437207f)` `[`DLinForwardSpeed`](#classgazebo_1_1_h_m_fossen_1a9a2cc66ad71a7fc9ce904f5cc27a36f0) 

Linear damping matrix proportional only to the forward speed (useful for modeling AUVs). From [1], according to Newman (1977), there is a damping force component that linearly increases with the presence of forward speed, particularly so for slender bodies.

References: [1] Refsnes - 2007 - Nonlinear model-based control of slender body AUVs

#### `protected `[`Eigen::Matrix6d`](docs/packages/uuv_simulator/docs/api/Matrix6d.md#_def_8hh_1ab6f8b8b11b0f6350ed45e7cd3437207f)` `[`DNonLin`](#classgazebo_1_1_h_m_fossen_1a3219a54c0be1a8a1e186b33dde95d6b5) 

Nonlinear damping coefficients.

#### `protected std::vector< double > `[`linearDampCoef`](#classgazebo_1_1_h_m_fossen_1aaaee5e4e341d1f3fccba9c832429712d) 

Linear damping coefficients.

#### `protected std::vector< double > `[`quadDampCoef`](#classgazebo_1_1_h_m_fossen_1a062e26123041365e16822bc2059fe3d1) 

Quadratic damping coefficients.

#### `protected  `[`REGISTER_HYDRODYNAMICMODEL`](#classgazebo_1_1_h_m_fossen_1ab3a59be3a5e9037575ee6f4878e96d8b)`(`[`HMFossen`](#classgazebo_1_1_h_m_fossen)`)` 

Register this model with the factory.

#### `protected  `[`HMFossen`](#classgazebo_1_1_h_m_fossen_1a9b9fcbd9ca518c9cd41300e0f9d43ee5)`(sdf::ElementPtr _sdf,physics::LinkPtr _link)` 

#### `protected void `[`ComputeAddedCoriolisMatrix`](#classgazebo_1_1_h_m_fossen_1afe97af45fc44777a04b4f1c81519b07b)`(const `[`Eigen::Vector6d`](docs/packages/uuv_simulator/docs/api/Vector6d.md#_def_8hh_1a09219f5e0b822edbf24b125e0e2a4fe0)` & _vel,const `[`Eigen::Matrix6d`](docs/packages/uuv_simulator/docs/api/Matrix6d.md#_def_8hh_1ab6f8b8b11b0f6350ed45e7cd3437207f)` & _Ma,`[`Eigen::Matrix6d`](docs/packages/uuv_simulator/docs/api/Matrix6d.md#_def_8hh_1ab6f8b8b11b0f6350ed45e7cd3437207f)` & _Ca) const` 

Computes the added-mass Coriolis matrix Ca.

#### `protected void `[`ComputeDampingMatrix`](#classgazebo_1_1_h_m_fossen_1a19624761792eac92864647ebee971196)`(const `[`Eigen::Vector6d`](docs/packages/uuv_simulator/docs/api/Vector6d.md#_def_8hh_1a09219f5e0b822edbf24b125e0e2a4fe0)` & _vel,`[`Eigen::Matrix6d`](docs/packages/uuv_simulator/docs/api/Matrix6d.md#_def_8hh_1ab6f8b8b11b0f6350ed45e7cd3437207f)` & _D) const` 

Updates the damping matrix for the current velocity.

#### `protected `[`Eigen::Matrix6d`](docs/packages/uuv_simulator/docs/api/Matrix6d.md#_def_8hh_1ab6f8b8b11b0f6350ed45e7cd3437207f)` `[`GetAddedMass`](#classgazebo_1_1_h_m_fossen_1a555bb01ef30396e3b39fa26bf6a79848)`() const` 

Returns the added-mass matrix with the scaling and offset.

