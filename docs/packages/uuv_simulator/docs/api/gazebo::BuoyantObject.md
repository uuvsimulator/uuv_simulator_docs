# class `gazebo::BuoyantObject` 

Class describing the dynamics of a buoyant object, useful for simple representations of underwater structures.

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public  `[`BuoyantObject`](#classgazebo_1_1_buoyant_object_1a359805730b19387b09b949017f4ec98c)`(physics::LinkPtr _link)` | Constructor.
`public  `[`~BuoyantObject`](#classgazebo_1_1_buoyant_object_1aa2bce1d66c086f79021ede0af29b3c35)`()` | Destructor.
`public void `[`GetBuoyancyForce`](#classgazebo_1_1_buoyant_object_1a932cee34723b709eacc09b7faf06c160)`(const ignition::math::Pose3d & _pose,ignition::math::Vector3d & buoyancyForce,ignition::math::Vector3d & buoyancyTorque)` | Returns the buoyancy force vector in the world frame.
`public void `[`ApplyBuoyancyForce`](#classgazebo_1_1_buoyant_object_1a4921e5c67f56246c7db97354907e96b4)`()` | Applies buoyancy force on link.
`public void `[`SetVolume`](#classgazebo_1_1_buoyant_object_1af6d39e740bfb499c20066308dbd4c8db)`(double _volume)` | Sets the link's submerged volume.
`public double `[`GetVolume`](#classgazebo_1_1_buoyant_object_1ac68e8561a42b7a735df95b98bc36c9e2)`()` | Returns the stored link submerged volume.
`public void `[`SetFluidDensity`](#classgazebo_1_1_buoyant_object_1a678331bb1b31810e0e0cebfc3308e716)`(double _fluidDensity)` | Sets the fluid density in kg/m^3.
`public double `[`GetFluidDensity`](#classgazebo_1_1_buoyant_object_1aa5f4f9aa79af1d53bf2abac34c919e3f)`()` | Returns the stored fluid density.
`public void `[`SetCoB`](#classgazebo_1_1_buoyant_object_1ab8eb0fcd27dcc5e42493953b5f8a3fbf)`(const ignition::math::Vector3d & _centerOfBuoyancy)` | Sets the position of the center of buoyancy on the body frame.
`public ignition::math::Vector3d `[`GetCoB`](#classgazebo_1_1_buoyant_object_1ac650663010209205589444a1b6399d8f)`()` | Returns the stored center of buoyancy.
`public void `[`SetGravity`](#classgazebo_1_1_buoyant_object_1a58bf8302392511f120389455b20650d0)`(double _g)` | Set acceleration of gravity.
`public double `[`GetGravity`](#classgazebo_1_1_buoyant_object_1a30e79e6d2a15cc72f13f2bdbd4d8ca20)`()` | Get stored acceleration of gravity.
`public void `[`SetBoundingBox`](#classgazebo_1_1_buoyant_object_1aa882b38b3a34b53b63387e88b3cf35f8)`(const ignition::math::Box & _bBox)` | Sets bounding box.
`public void `[`SetStoreVector`](#classgazebo_1_1_buoyant_object_1a4eac79e88a01768d2ac57edb9f0c2165)`(std::string _tag)` | Adds a field in the hydroWrench map.
`public ignition::math::Vector3d `[`GetStoredVector`](#classgazebo_1_1_buoyant_object_1a54823aae49748ba43a3850a46e6bde54)`(std::string _tag)` | Get vector from the hydroWrench map.
`public void `[`SetDebugFlag`](#classgazebo_1_1_buoyant_object_1a82d4bf4144197aacc72af095b694646d)`(bool _debugOn)` | Set debug flag to store intermediate forces and torques.
`public bool `[`IsSubmerged`](#classgazebo_1_1_buoyant_object_1a8c463acfd7aff5617ae4eee3b7fce5bd)`()` | Returns true if the robot is completely submerged.
`public bool `[`IsNeutrallyBuoyant`](#classgazebo_1_1_buoyant_object_1a1963a046ea32ebd0c5ef8b84e47ffa12)`()` | Returns true if the link was set to be neutrally buoyant.
`public bool `[`GetDebugFlag`](#classgazebo_1_1_buoyant_object_1a83d4b9929c151d16c2b554a13f6eb999)`()` | Returns the debug flag.
`public void `[`SetNeutrallyBuoyant`](#classgazebo_1_1_buoyant_object_1a28274bff9fd823e3691241d10f4634ba)`()` | Sets this link as neutrally buoyant.
`protected double `[`volume`](#classgazebo_1_1_buoyant_object_1a5df478c848c90966d975f43d23273b68) | Volume of fluid displaced by the submerged object.
`protected double `[`scalingVolume`](#classgazebo_1_1_buoyant_object_1ad5478bc34170f61cc4c5dfa29bc2b652) | Scaling factor for the volume.
`protected double `[`offsetVolume`](#classgazebo_1_1_buoyant_object_1a87a15b7f37f66ac1042e3d2389c961ae) | Offset for the volume.
`protected double `[`fluidDensity`](#classgazebo_1_1_buoyant_object_1ac4f954fe80eef93dd1382cd56be9a8c4) | Fluid density.
`protected double `[`g`](#classgazebo_1_1_buoyant_object_1a10e218847e76c2f8d80f7d6e36936b07) | Acceleration of gravity.
`protected ignition::math::Vector3d `[`centerOfBuoyancy`](#classgazebo_1_1_buoyant_object_1ac117d052ffe3b6d64b68931fb02a7cfa) | Center of buoyancy in the body frame.
`protected ignition::math::Box `[`boundingBox`](#classgazebo_1_1_buoyant_object_1ad112205a7f3eafdd5d928053ddcf5b56) | TEMP for calculation of the buoyancy force close to the surface.
`protected std::map< std::string, ignition::math::Vector3d > `[`hydroWrench`](#classgazebo_1_1_buoyant_object_1aa4e2fa73e7befaa26e862b65b374d4cc) | Storage for hydrodynamic and hydrostatic forces and torques for debugging purposes.
`protected bool `[`debugFlag`](#classgazebo_1_1_buoyant_object_1ab0183045981acc20a4bb50bec6ef95df) | Debug flag, storing all intermediate forces and torques.
`protected bool `[`isSubmerged`](#classgazebo_1_1_buoyant_object_1a3cebc89074e9c099470dc07dc7b48d4c) | Is submerged flag.
`protected physics::LinkPtr `[`link`](#classgazebo_1_1_buoyant_object_1ac6c3d6cdb2429b08d460c8a73b425faa) | Pointer to the correspondent robot link.
`protected bool `[`neutrallyBuoyant`](#classgazebo_1_1_buoyant_object_1a7a708207b8bfa11a2b16fdd9760cf7fe) | If true, the restoring force will be equal to the gravitational.
`protected double `[`metacentricWidth`](#classgazebo_1_1_buoyant_object_1a9ab2bf6881f44a9295dca31c6e7c69f1) | 
`protected double `[`metacentricLength`](#classgazebo_1_1_buoyant_object_1a5f3d6b665a81d6e253f958e2a223cab5) | Metacentric length of the robot, used only for surface vessels and floating objects.
`protected double `[`waterLevelPlaneArea`](#classgazebo_1_1_buoyant_object_1a81cdf161131ba5c6b5d0b0375a13e6d4) | If the cross section area around water level of the surface vessel is not given, it will be computed from the object's bounding box.
`protected double `[`submergedHeight`](#classgazebo_1_1_buoyant_object_1ad83cee778e1d1851e3c951a1bbbed73e) | Height of the robot that is submerged (only for surface vessels)
`protected bool `[`isSurfaceVessel`](#classgazebo_1_1_buoyant_object_1a3418fd9dd6946135e0d36a5e47c4d47d) | Flag set to true if the information about the metacentric width and height is available.
`protected bool `[`isSurfaceVesselFloating`](#classgazebo_1_1_buoyant_object_1a894adcdaac90ad400378c15e893efefa) | Flag set to true if the vessel has reached its submerged height.
`protected void `[`StoreVector`](#classgazebo_1_1_buoyant_object_1a72cef0c40933fdad28fbb805ca392ad6)`(std::string _tag,ignition::math::Vector3d _vec)` | Store vector in the hydroWrench map if the field has been created.

## Members

#### `public  `[`BuoyantObject`](#classgazebo_1_1_buoyant_object_1a359805730b19387b09b949017f4ec98c)`(physics::LinkPtr _link)` 

Constructor.

#### `public  `[`~BuoyantObject`](#classgazebo_1_1_buoyant_object_1aa2bce1d66c086f79021ede0af29b3c35)`()` 

Destructor.

#### `public void `[`GetBuoyancyForce`](#classgazebo_1_1_buoyant_object_1a932cee34723b709eacc09b7faf06c160)`(const ignition::math::Pose3d & _pose,ignition::math::Vector3d & buoyancyForce,ignition::math::Vector3d & buoyancyTorque)` 

Returns the buoyancy force vector in the world frame.

#### `public void `[`ApplyBuoyancyForce`](#classgazebo_1_1_buoyant_object_1a4921e5c67f56246c7db97354907e96b4)`()` 

Applies buoyancy force on link.

#### `public void `[`SetVolume`](#classgazebo_1_1_buoyant_object_1af6d39e740bfb499c20066308dbd4c8db)`(double _volume)` 

Sets the link's submerged volume.

#### `public double `[`GetVolume`](#classgazebo_1_1_buoyant_object_1ac68e8561a42b7a735df95b98bc36c9e2)`()` 

Returns the stored link submerged volume.

#### `public void `[`SetFluidDensity`](#classgazebo_1_1_buoyant_object_1a678331bb1b31810e0e0cebfc3308e716)`(double _fluidDensity)` 

Sets the fluid density in kg/m^3.

#### `public double `[`GetFluidDensity`](#classgazebo_1_1_buoyant_object_1aa5f4f9aa79af1d53bf2abac34c919e3f)`()` 

Returns the stored fluid density.

#### `public void `[`SetCoB`](#classgazebo_1_1_buoyant_object_1ab8eb0fcd27dcc5e42493953b5f8a3fbf)`(const ignition::math::Vector3d & _centerOfBuoyancy)` 

Sets the position of the center of buoyancy on the body frame.

#### `public ignition::math::Vector3d `[`GetCoB`](#classgazebo_1_1_buoyant_object_1ac650663010209205589444a1b6399d8f)`()` 

Returns the stored center of buoyancy.

#### `public void `[`SetGravity`](#classgazebo_1_1_buoyant_object_1a58bf8302392511f120389455b20650d0)`(double _g)` 

Set acceleration of gravity.

#### `public double `[`GetGravity`](#classgazebo_1_1_buoyant_object_1a30e79e6d2a15cc72f13f2bdbd4d8ca20)`()` 

Get stored acceleration of gravity.

#### `public void `[`SetBoundingBox`](#classgazebo_1_1_buoyant_object_1aa882b38b3a34b53b63387e88b3cf35f8)`(const ignition::math::Box & _bBox)` 

Sets bounding box.

#### `public void `[`SetStoreVector`](#classgazebo_1_1_buoyant_object_1a4eac79e88a01768d2ac57edb9f0c2165)`(std::string _tag)` 

Adds a field in the hydroWrench map.

#### `public ignition::math::Vector3d `[`GetStoredVector`](#classgazebo_1_1_buoyant_object_1a54823aae49748ba43a3850a46e6bde54)`(std::string _tag)` 

Get vector from the hydroWrench map.

#### `public void `[`SetDebugFlag`](#classgazebo_1_1_buoyant_object_1a82d4bf4144197aacc72af095b694646d)`(bool _debugOn)` 

Set debug flag to store intermediate forces and torques.

#### `public bool `[`IsSubmerged`](#classgazebo_1_1_buoyant_object_1a8c463acfd7aff5617ae4eee3b7fce5bd)`()` 

Returns true if the robot is completely submerged.

#### `public bool `[`IsNeutrallyBuoyant`](#classgazebo_1_1_buoyant_object_1a1963a046ea32ebd0c5ef8b84e47ffa12)`()` 

Returns true if the link was set to be neutrally buoyant.

#### `public bool `[`GetDebugFlag`](#classgazebo_1_1_buoyant_object_1a83d4b9929c151d16c2b554a13f6eb999)`()` 

Returns the debug flag.

#### `public void `[`SetNeutrallyBuoyant`](#classgazebo_1_1_buoyant_object_1a28274bff9fd823e3691241d10f4634ba)`()` 

Sets this link as neutrally buoyant.

#### `protected double `[`volume`](#classgazebo_1_1_buoyant_object_1a5df478c848c90966d975f43d23273b68) 

Volume of fluid displaced by the submerged object.

#### `protected double `[`scalingVolume`](#classgazebo_1_1_buoyant_object_1ad5478bc34170f61cc4c5dfa29bc2b652) 

Scaling factor for the volume.

#### `protected double `[`offsetVolume`](#classgazebo_1_1_buoyant_object_1a87a15b7f37f66ac1042e3d2389c961ae) 

Offset for the volume.

#### `protected double `[`fluidDensity`](#classgazebo_1_1_buoyant_object_1ac4f954fe80eef93dd1382cd56be9a8c4) 

Fluid density.

#### `protected double `[`g`](#classgazebo_1_1_buoyant_object_1a10e218847e76c2f8d80f7d6e36936b07) 

Acceleration of gravity.

#### `protected ignition::math::Vector3d `[`centerOfBuoyancy`](#classgazebo_1_1_buoyant_object_1ac117d052ffe3b6d64b68931fb02a7cfa) 

Center of buoyancy in the body frame.

#### `protected ignition::math::Box `[`boundingBox`](#classgazebo_1_1_buoyant_object_1ad112205a7f3eafdd5d928053ddcf5b56) 

TEMP for calculation of the buoyancy force close to the surface.

#### `protected std::map< std::string, ignition::math::Vector3d > `[`hydroWrench`](#classgazebo_1_1_buoyant_object_1aa4e2fa73e7befaa26e862b65b374d4cc) 

Storage for hydrodynamic and hydrostatic forces and torques for debugging purposes.

#### `protected bool `[`debugFlag`](#classgazebo_1_1_buoyant_object_1ab0183045981acc20a4bb50bec6ef95df) 

Debug flag, storing all intermediate forces and torques.

#### `protected bool `[`isSubmerged`](#classgazebo_1_1_buoyant_object_1a3cebc89074e9c099470dc07dc7b48d4c) 

Is submerged flag.

#### `protected physics::LinkPtr `[`link`](#classgazebo_1_1_buoyant_object_1ac6c3d6cdb2429b08d460c8a73b425faa) 

Pointer to the correspondent robot link.

#### `protected bool `[`neutrallyBuoyant`](#classgazebo_1_1_buoyant_object_1a7a708207b8bfa11a2b16fdd9760cf7fe) 

If true, the restoring force will be equal to the gravitational.

#### `protected double `[`metacentricWidth`](#classgazebo_1_1_buoyant_object_1a9ab2bf6881f44a9295dca31c6e7c69f1) 

#### `protected double `[`metacentricLength`](#classgazebo_1_1_buoyant_object_1a5f3d6b665a81d6e253f958e2a223cab5) 

Metacentric length of the robot, used only for surface vessels and floating objects.

#### `protected double `[`waterLevelPlaneArea`](#classgazebo_1_1_buoyant_object_1a81cdf161131ba5c6b5d0b0375a13e6d4) 

If the cross section area around water level of the surface vessel is not given, it will be computed from the object's bounding box.

#### `protected double `[`submergedHeight`](#classgazebo_1_1_buoyant_object_1ad83cee778e1d1851e3c951a1bbbed73e) 

Height of the robot that is submerged (only for surface vessels)

#### `protected bool `[`isSurfaceVessel`](#classgazebo_1_1_buoyant_object_1a3418fd9dd6946135e0d36a5e47c4d47d) 

Flag set to true if the information about the metacentric width and height is available.

#### `protected bool `[`isSurfaceVesselFloating`](#classgazebo_1_1_buoyant_object_1a894adcdaac90ad400378c15e893efefa) 

Flag set to true if the vessel has reached its submerged height.

#### `protected void `[`StoreVector`](#classgazebo_1_1_buoyant_object_1a72cef0c40933fdad28fbb805ca392ad6)`(std::string _tag,ignition::math::Vector3d _vec)` 

Store vector in the hydroWrench map if the field has been created.

