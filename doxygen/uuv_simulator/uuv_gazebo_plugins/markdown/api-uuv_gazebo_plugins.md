# Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`namespace `[`gazebo`](#namespacegazebo) | 

# namespace `gazebo` 

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public inline std::vector< double > `[`Str2Vector`](#_def_8hh_1a2cebe56ebe3fea83f705b81b63478ab3)`(std::string _input)`            | Conversion of a string to a double vector.
`public inline Eigen::Matrix3d `[`CrossProductOperator`](#_def_8hh_1af0c92548f7f8577ab4baf1e3ea1bad8c)`(Eigen::Vector3d _x)`            | Returns the cross product operator matrix for Eigen vectors.
`public inline Eigen::Matrix3d `[`CrossProductOperator`](#_def_8hh_1afdae7b4473d28927d48943e02ffb6997)`(ignition::math::Vector3d _x)`            | Returns the cross product operator matrix for Gazebo vectors.
`public inline Eigen::Vector3d `[`ToEigen`](#_def_8hh_1a1ef93fe6b4298908bce62e78f6ccbec1)`(const ignition::math::Vector3d & _x)`            | 
`public inline Eigen::Matrix3d `[`ToEigen`](#_def_8hh_1a6e99d53b62183beec10906544a332398)`(const ignition::math::Matrix3d & _x)`            | 
`public inline `[`Eigen::Vector6d`](#_def_8hh_1a09219f5e0b822edbf24b125e0e2a4fe0)` `[`EigenStack`](#_def_8hh_1a0bfe56e41fbcc76d068fdb8c64bc9658)`(const ignition::math::Vector3d & _x,const ignition::math::Vector3d & _y)`            | 
`public inline ignition::math::Vector3d `[`Vec3dToGazebo`](#_def_8hh_1abf74a848ac8e88250e20d2f9c527a035)`(const Eigen::Vector3d & _x)`            | 
`public inline ignition::math::Matrix3d `[`Mat3dToGazebo`](#_def_8hh_1ab6be531ba3f076aa302787cc0f08b8a0)`(const Eigen::Matrix3d & _x)`            | 
`public  `[`REGISTER_DYNAMICS_CREATOR`](#_dynamics_8cc_1a4449aff6ae35a1c889f8bd3bee7cef38)`(`[`DynamicsZeroOrder`](#classgazebo_1_1_dynamics_zero_order)`,&`[`DynamicsZeroOrder::create`](#classgazebo_1_1_dynamics_zero_order_1a24a60d5e8102bb6a24e08b7a345a2e60)`)`            | 
`public  `[`REGISTER_DYNAMICS_CREATOR`](#_dynamics_8cc_1ab5566bd0a552bb647e261f0fa4636ac9)`(`[`DynamicsFirstOrder`](#classgazebo_1_1_dynamics_first_order)`,&`[`DynamicsFirstOrder::create`](#classgazebo_1_1_dynamics_first_order_1ac7d44c0d877c788f980dedd406ff321c)`)`            | 
`public  `[`REGISTER_DYNAMICS_CREATOR`](#_dynamics_8cc_1aa763285ed8d3d33598c48f5366a2a159)`(`[`ThrusterDynamicsYoerger`](#classgazebo_1_1_thruster_dynamics_yoerger)`,&`[`ThrusterDynamicsYoerger::create`](#classgazebo_1_1_thruster_dynamics_yoerger_1ad08fced9cdaf6148887f23f34d40acb3)`)`            | 
`public  `[`REGISTER_DYNAMICS_CREATOR`](#_dynamics_8cc_1ad9384305982bbb7ccb903654cf44d174)`(`[`ThrusterDynamicsBessa`](#classgazebo_1_1_thruster_dynamics_bessa)`,&`[`ThrusterDynamicsBessa::create`](#classgazebo_1_1_thruster_dynamics_bessa_1a8a27b37a3fdf08d44bb12d458de4c062)`)`            | 
`public  `[`REGISTER_HYDRODYNAMICMODEL_CREATOR`](#_hydrodynamic_model_8cc_1a389aad33a29388be8ba649233c4b2388)`(`[`HMFossen`](#classgazebo_1_1_h_m_fossen)`,&`[`HMFossen::create`](#classgazebo_1_1_h_m_fossen_1a4473fe62590315c62a74d57a49561c3d)`)`            | 
`public  `[`REGISTER_HYDRODYNAMICMODEL_CREATOR`](#_hydrodynamic_model_8cc_1aa9493417a195f7fa86f7be6e3df8733f)`(`[`HMSphere`](#classgazebo_1_1_h_m_sphere)`,&`[`HMSphere::create`](#classgazebo_1_1_h_m_sphere_1aba02ae4b4e986947c89b3552b2661ddf)`)`            | 
`public  `[`REGISTER_HYDRODYNAMICMODEL_CREATOR`](#_hydrodynamic_model_8cc_1ad4101ddb1453ef95ec71ca2e1c15b6bb)`(`[`HMCylinder`](#classgazebo_1_1_h_m_cylinder)`,&`[`HMCylinder::create`](#classgazebo_1_1_h_m_cylinder_1a76f0a8d44b4bb95f0b6d4f854ce2be21)`)`            | 
`public  `[`REGISTER_HYDRODYNAMICMODEL_CREATOR`](#_hydrodynamic_model_8cc_1a099465f483f1fcfc9ef96bbcbe6c10d7)`(`[`HMSpheroid`](#classgazebo_1_1_h_m_spheroid)`,&`[`HMSpheroid::create`](#classgazebo_1_1_h_m_spheroid_1acca3b046f41e6fc364d744bc3e6d0486)`)`            | 
`public  `[`REGISTER_HYDRODYNAMICMODEL_CREATOR`](#_hydrodynamic_model_8cc_1a74769739d76bc34176d05d2e9b35b3d2)`(`[`HMBox`](#classgazebo_1_1_h_m_box)`,&`[`HMBox::create`](#classgazebo_1_1_h_m_box_1a7e70ec74041e24838fb2597020444bc3)`)`            | 
`public  `[`REGISTER_LIFTDRAG_CREATOR`](#_lift_drag_model_8cc_1a3a7c3e09fa3f79d2777967d0962b54b9)`(`[`LiftDragQuadratic`](#classgazebo_1_1_lift_drag_quadratic)`,&`[`LiftDragQuadratic::create`](#classgazebo_1_1_lift_drag_quadratic_1a668607ebeb1636d049a7178d96761abf)`)`            | 
`public  `[`REGISTER_LIFTDRAG_CREATOR`](#_lift_drag_model_8cc_1ab5100d02a5113eea87d0e30645be00fa)`(`[`LiftDragTwoLines`](#classgazebo_1_1_lift_drag_two_lines)`,&`[`LiftDragTwoLines::create`](#classgazebo_1_1_lift_drag_two_lines_1ac5e46b28d2ee07f3d483a217b1e04394)`)`            | 
`public  `[`REGISTER_CONVERSIONFUNCTION_CREATOR`](#_thruster_conversion_fcn_8cc_1ab4b8624453357262a7c8ee726f493362)`(`[`ConversionFunctionBasic`](#classgazebo_1_1_conversion_function_basic)`,&`[`ConversionFunctionBasic::create`](#classgazebo_1_1_conversion_function_basic_1a9f93dad90325e745d6fa34bedd9cfb21)`)`            | 
`public  `[`REGISTER_CONVERSIONFUNCTION_CREATOR`](#_thruster_conversion_fcn_8cc_1aa19a1211c0e03422138d85e67d6e401b)`(`[`ConversionFunctionBessa`](#classgazebo_1_1_conversion_function_bessa)`,&`[`ConversionFunctionBessa::create`](#classgazebo_1_1_conversion_function_bessa_1a7935156beb3d0055e7a43b01973dcc99)`)`            | 
`public  `[`REGISTER_CONVERSIONFUNCTION_CREATOR`](#_thruster_conversion_fcn_8cc_1a6a10547af4c30411a1f3cf9c5c7575f3)`(`[`ConversionFunctionLinearInterp`](#classgazebo_1_1_conversion_function_linear_interp)`,&`[`ConversionFunctionLinearInterp::create`](#classgazebo_1_1_conversion_function_linear_interp_1ad1a03fe3738aa5dd88638ea07e499743)`)`            | 
`public  `[`GZ_REGISTER_MODEL_PLUGIN`](#_umbilical_plugin_8cc_1aa0457d29fbe099affb59c08843bb121a)`(`[`UmbilicalPlugin`](#classgazebo_1_1_umbilical_plugin)`)`            | 
`class `[`gazebo::BuoyantObject`](#classgazebo_1_1_buoyant_object) | Class describing the dynamics of a buoyant object, useful for simple representations of underwater structures.
`class `[`gazebo::ConversionFunction`](#classgazebo_1_1_conversion_function) | Abstact base class for a thruster conversion function.
`class `[`gazebo::ConversionFunctionBasic`](#classgazebo_1_1_conversion_function_basic) | The most basic conversion function: Thrust = const.*w*abs(w) This corresponds to what is attrributed to Yoerger et al. and called Model 1 in Bessa et al.: Dynamic Positioning of Underwater Robotic Vehicles with Thruster [Dynamics](#classgazebo_1_1_dynamics) Compensation.
`class `[`gazebo::ConversionFunctionBessa`](#classgazebo_1_1_conversion_function_bessa) | Asymmetric conversion function with dead-zone nonlinearity. This corresponds to what is called Model 2 in Bessa et al.: Dynamic Positioning of Underwater Robotic Vehicles with Thruster [Dynamics](#classgazebo_1_1_dynamics) Compensation.
`class `[`gazebo::ConversionFunctionFactory`](#classgazebo_1_1_conversion_function_factory) | Factory singleton class that creates a [ConversionFunction](#classgazebo_1_1_conversion_function) from sdf.
`class `[`gazebo::ConversionFunctionLinearInterp`](#classgazebo_1_1_conversion_function_linear_interp) | Conversion using linear interpolation between given data points.
`class `[`gazebo::Dynamics`](#classgazebo_1_1_dynamics) | Abstract base class for thruster dynamics.
`class `[`gazebo::DynamicsFactory`](#classgazebo_1_1_dynamics_factory) | Factory singleton class that creates a ThrusterDynamics from sdf.
`class `[`gazebo::DynamicsFirstOrder`](#classgazebo_1_1_dynamics_first_order) | First-order dynamic system.
`class `[`gazebo::DynamicsZeroOrder`](#classgazebo_1_1_dynamics_zero_order) | Trivial (no dynamics) zero-order dynamic system.
`class `[`gazebo::FinPlugin`](#classgazebo_1_1_fin_plugin) | 
`class `[`gazebo::HMBox`](#classgazebo_1_1_h_m_box) | Class containing the methods and attributes for a hydrodynamic model for a box in the fluid.
`class `[`gazebo::HMCylinder`](#classgazebo_1_1_h_m_cylinder) | Class containing the methods and attributes for a hydrodynamic model for a cylinder in the fluid.
`class `[`gazebo::HMFossen`](#classgazebo_1_1_h_m_fossen) | Class containting the methods and attributes for a Fossen robot-like hydrodynamic model. The restoring forces are applied by the [BuoyantObject](#classgazebo_1_1_buoyant_object) class methods. Using the plugin for UUV models will use both this and the buoyant object class definitions, therefore the restoring forces were not inherited here. References:
`class `[`gazebo::HMSphere`](#classgazebo_1_1_h_m_sphere) | Class containing the methods and attributes for a hydrodynamic model for a sphere in the fluid.
`class `[`gazebo::HMSpheroid`](#classgazebo_1_1_h_m_spheroid) | Class containing the methods and attributes for a hydrodynamic model for a spheroid in the fluid Reference: Antonelli - Underwater Robots.
`class `[`gazebo::HydrodynamicModel`](#classgazebo_1_1_hydrodynamic_model) | 
`class `[`gazebo::HydrodynamicModelFactory`](#classgazebo_1_1_hydrodynamic_model_factory) | Factory singleton class that creates a [HydrodynamicModel](#classgazebo_1_1_hydrodynamic_model) from sdf.
`class `[`gazebo::LiftDrag`](#classgazebo_1_1_lift_drag) | Abstract base class for Lift&Drag models.
`class `[`gazebo::LiftDragFactory`](#classgazebo_1_1_lift_drag_factory) | Factory singleton class that creates a [LiftDrag](#classgazebo_1_1_lift_drag) from sdf.
`class `[`gazebo::LiftDragQuadratic`](#classgazebo_1_1_lift_drag_quadratic) | Basic quadratic (Hugin) lift&drag model, page 18 from [1]. [1] Engelhardtsen, Øystein. "3D AUV Collision Avoidance." (2007).
`class `[`gazebo::LiftDragTwoLines`](#classgazebo_1_1_lift_drag_two_lines) | Lift&drag model that models lift/drag coeffs using two lines. This is based on Gazebo's LiftDragPlugin but implemented as a derived [LiftDrag](#classgazebo_1_1_lift_drag) model to allow using it in combination with the dynamics of a Fin.
`class `[`gazebo::ThrusterDynamicsBessa`](#classgazebo_1_1_thruster_dynamics_bessa) | Bessa's dynamic thruster model.
`class `[`gazebo::ThrusterDynamicsYoerger`](#classgazebo_1_1_thruster_dynamics_yoerger) | Yoerger's dynamic thruster model.
`class `[`gazebo::ThrusterPlugin`](#classgazebo_1_1_thruster_plugin) | Class for the thruster plugin.
`class `[`gazebo::UmbilicalModel`](#classgazebo_1_1_umbilical_model) | 
`class `[`gazebo::UmbilicalModelBerg`](#classgazebo_1_1_umbilical_model_berg) | 
`class `[`gazebo::UmbilicalModelFactory`](#classgazebo_1_1_umbilical_model_factory) | Factory singleton class that creates an [UmbilicalModel](#classgazebo_1_1_umbilical_model) from sdf.
`class `[`gazebo::UmbilicalPlugin`](#classgazebo_1_1_umbilical_plugin) | 
`class `[`gazebo::UmbilicalSegment`](#classgazebo_1_1_umbilical_segment) | 
`class `[`gazebo::UnderwaterObjectPlugin`](#classgazebo_1_1_underwater_object_plugin) | Gazebo model plugin class for underwater objects.

## Members

#### `public inline std::vector< double > `[`Str2Vector`](#_def_8hh_1a2cebe56ebe3fea83f705b81b63478ab3)`(std::string _input)` 

Conversion of a string to a double vector.

#### `public inline Eigen::Matrix3d `[`CrossProductOperator`](#_def_8hh_1af0c92548f7f8577ab4baf1e3ea1bad8c)`(Eigen::Vector3d _x)` 

Returns the cross product operator matrix for Eigen vectors.

#### `public inline Eigen::Matrix3d `[`CrossProductOperator`](#_def_8hh_1afdae7b4473d28927d48943e02ffb6997)`(ignition::math::Vector3d _x)` 

Returns the cross product operator matrix for Gazebo vectors.

#### `public inline Eigen::Vector3d `[`ToEigen`](#_def_8hh_1a1ef93fe6b4298908bce62e78f6ccbec1)`(const ignition::math::Vector3d & _x)` 

#### `public inline Eigen::Matrix3d `[`ToEigen`](#_def_8hh_1a6e99d53b62183beec10906544a332398)`(const ignition::math::Matrix3d & _x)` 

#### `public inline `[`Eigen::Vector6d`](#_def_8hh_1a09219f5e0b822edbf24b125e0e2a4fe0)` `[`EigenStack`](#_def_8hh_1a0bfe56e41fbcc76d068fdb8c64bc9658)`(const ignition::math::Vector3d & _x,const ignition::math::Vector3d & _y)` 

#### `public inline ignition::math::Vector3d `[`Vec3dToGazebo`](#_def_8hh_1abf74a848ac8e88250e20d2f9c527a035)`(const Eigen::Vector3d & _x)` 

#### `public inline ignition::math::Matrix3d `[`Mat3dToGazebo`](#_def_8hh_1ab6be531ba3f076aa302787cc0f08b8a0)`(const Eigen::Matrix3d & _x)` 

#### `public  `[`REGISTER_DYNAMICS_CREATOR`](#_dynamics_8cc_1a4449aff6ae35a1c889f8bd3bee7cef38)`(`[`DynamicsZeroOrder`](#classgazebo_1_1_dynamics_zero_order)`,&`[`DynamicsZeroOrder::create`](#classgazebo_1_1_dynamics_zero_order_1a24a60d5e8102bb6a24e08b7a345a2e60)`)` 

#### `public  `[`REGISTER_DYNAMICS_CREATOR`](#_dynamics_8cc_1ab5566bd0a552bb647e261f0fa4636ac9)`(`[`DynamicsFirstOrder`](#classgazebo_1_1_dynamics_first_order)`,&`[`DynamicsFirstOrder::create`](#classgazebo_1_1_dynamics_first_order_1ac7d44c0d877c788f980dedd406ff321c)`)` 

#### `public  `[`REGISTER_DYNAMICS_CREATOR`](#_dynamics_8cc_1aa763285ed8d3d33598c48f5366a2a159)`(`[`ThrusterDynamicsYoerger`](#classgazebo_1_1_thruster_dynamics_yoerger)`,&`[`ThrusterDynamicsYoerger::create`](#classgazebo_1_1_thruster_dynamics_yoerger_1ad08fced9cdaf6148887f23f34d40acb3)`)` 

#### `public  `[`REGISTER_DYNAMICS_CREATOR`](#_dynamics_8cc_1ad9384305982bbb7ccb903654cf44d174)`(`[`ThrusterDynamicsBessa`](#classgazebo_1_1_thruster_dynamics_bessa)`,&`[`ThrusterDynamicsBessa::create`](#classgazebo_1_1_thruster_dynamics_bessa_1a8a27b37a3fdf08d44bb12d458de4c062)`)` 

#### `public  `[`REGISTER_HYDRODYNAMICMODEL_CREATOR`](#_hydrodynamic_model_8cc_1a389aad33a29388be8ba649233c4b2388)`(`[`HMFossen`](#classgazebo_1_1_h_m_fossen)`,&`[`HMFossen::create`](#classgazebo_1_1_h_m_fossen_1a4473fe62590315c62a74d57a49561c3d)`)` 

#### `public  `[`REGISTER_HYDRODYNAMICMODEL_CREATOR`](#_hydrodynamic_model_8cc_1aa9493417a195f7fa86f7be6e3df8733f)`(`[`HMSphere`](#classgazebo_1_1_h_m_sphere)`,&`[`HMSphere::create`](#classgazebo_1_1_h_m_sphere_1aba02ae4b4e986947c89b3552b2661ddf)`)` 

#### `public  `[`REGISTER_HYDRODYNAMICMODEL_CREATOR`](#_hydrodynamic_model_8cc_1ad4101ddb1453ef95ec71ca2e1c15b6bb)`(`[`HMCylinder`](#classgazebo_1_1_h_m_cylinder)`,&`[`HMCylinder::create`](#classgazebo_1_1_h_m_cylinder_1a76f0a8d44b4bb95f0b6d4f854ce2be21)`)` 

#### `public  `[`REGISTER_HYDRODYNAMICMODEL_CREATOR`](#_hydrodynamic_model_8cc_1a099465f483f1fcfc9ef96bbcbe6c10d7)`(`[`HMSpheroid`](#classgazebo_1_1_h_m_spheroid)`,&`[`HMSpheroid::create`](#classgazebo_1_1_h_m_spheroid_1acca3b046f41e6fc364d744bc3e6d0486)`)` 

#### `public  `[`REGISTER_HYDRODYNAMICMODEL_CREATOR`](#_hydrodynamic_model_8cc_1a74769739d76bc34176d05d2e9b35b3d2)`(`[`HMBox`](#classgazebo_1_1_h_m_box)`,&`[`HMBox::create`](#classgazebo_1_1_h_m_box_1a7e70ec74041e24838fb2597020444bc3)`)` 

#### `public  `[`REGISTER_LIFTDRAG_CREATOR`](#_lift_drag_model_8cc_1a3a7c3e09fa3f79d2777967d0962b54b9)`(`[`LiftDragQuadratic`](#classgazebo_1_1_lift_drag_quadratic)`,&`[`LiftDragQuadratic::create`](#classgazebo_1_1_lift_drag_quadratic_1a668607ebeb1636d049a7178d96761abf)`)` 

#### `public  `[`REGISTER_LIFTDRAG_CREATOR`](#_lift_drag_model_8cc_1ab5100d02a5113eea87d0e30645be00fa)`(`[`LiftDragTwoLines`](#classgazebo_1_1_lift_drag_two_lines)`,&`[`LiftDragTwoLines::create`](#classgazebo_1_1_lift_drag_two_lines_1ac5e46b28d2ee07f3d483a217b1e04394)`)` 

#### `public  `[`REGISTER_CONVERSIONFUNCTION_CREATOR`](#_thruster_conversion_fcn_8cc_1ab4b8624453357262a7c8ee726f493362)`(`[`ConversionFunctionBasic`](#classgazebo_1_1_conversion_function_basic)`,&`[`ConversionFunctionBasic::create`](#classgazebo_1_1_conversion_function_basic_1a9f93dad90325e745d6fa34bedd9cfb21)`)` 

#### `public  `[`REGISTER_CONVERSIONFUNCTION_CREATOR`](#_thruster_conversion_fcn_8cc_1aa19a1211c0e03422138d85e67d6e401b)`(`[`ConversionFunctionBessa`](#classgazebo_1_1_conversion_function_bessa)`,&`[`ConversionFunctionBessa::create`](#classgazebo_1_1_conversion_function_bessa_1a7935156beb3d0055e7a43b01973dcc99)`)` 

#### `public  `[`REGISTER_CONVERSIONFUNCTION_CREATOR`](#_thruster_conversion_fcn_8cc_1a6a10547af4c30411a1f3cf9c5c7575f3)`(`[`ConversionFunctionLinearInterp`](#classgazebo_1_1_conversion_function_linear_interp)`,&`[`ConversionFunctionLinearInterp::create`](#classgazebo_1_1_conversion_function_linear_interp_1ad1a03fe3738aa5dd88638ea07e499743)`)` 

#### `public  `[`GZ_REGISTER_MODEL_PLUGIN`](#_umbilical_plugin_8cc_1aa0457d29fbe099affb59c08843bb121a)`(`[`UmbilicalPlugin`](#classgazebo_1_1_umbilical_plugin)`)` 

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

# class `gazebo::ConversionFunction` 

Abstact base class for a thruster conversion function.

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public inline virtual  `[`~ConversionFunction`](#classgazebo_1_1_conversion_function_1afc13b3997ac95f70425ec5fc830d927c)`()` | Destructor.
`public std::string `[`GetType`](#classgazebo_1_1_conversion_function_1ac0d2640de379ea86c087491c70bc6189)`()` | Return (derived) type of conversion function.
`public bool `[`GetParam`](#classgazebo_1_1_conversion_function_1a18c78fd782a8603afa893adc2a26f1a4)`(std::string _tag,double & _output)` | Return paramater in vector form for the given tag.
`public inline virtual std::map< double, double > `[`GetTable`](#classgazebo_1_1_conversion_function_1a9e0c3b99751eeaf95f96dd49ed0351a2)`()` | Return input and output vectors of the lookup table.
`public double `[`convert`](#classgazebo_1_1_conversion_function_1ac71ae91ae6e91ae177b8255477a2b950)`(double _cmd)` | Convert thruster state (e.g. angular velocity) to thrust force.
`protected inline  `[`ConversionFunction`](#classgazebo_1_1_conversion_function_1a70689912f6f1f316a84f2dea2e10050d)`()` | Protected constructor: Use the factory instead.

## Members

#### `public inline virtual  `[`~ConversionFunction`](#classgazebo_1_1_conversion_function_1afc13b3997ac95f70425ec5fc830d927c)`()` 

Destructor.

#### `public std::string `[`GetType`](#classgazebo_1_1_conversion_function_1ac0d2640de379ea86c087491c70bc6189)`()` 

Return (derived) type of conversion function.

#### `public bool `[`GetParam`](#classgazebo_1_1_conversion_function_1a18c78fd782a8603afa893adc2a26f1a4)`(std::string _tag,double & _output)` 

Return paramater in vector form for the given tag.

#### `public inline virtual std::map< double, double > `[`GetTable`](#classgazebo_1_1_conversion_function_1a9e0c3b99751eeaf95f96dd49ed0351a2)`()` 

Return input and output vectors of the lookup table.

#### `public double `[`convert`](#classgazebo_1_1_conversion_function_1ac71ae91ae6e91ae177b8255477a2b950)`(double _cmd)` 

Convert thruster state (e.g. angular velocity) to thrust force.

#### `protected inline  `[`ConversionFunction`](#classgazebo_1_1_conversion_function_1a70689912f6f1f316a84f2dea2e10050d)`()` 

Protected constructor: Use the factory instead.

# class `gazebo::ConversionFunctionBasic` 

```
class gazebo::ConversionFunctionBasic
  : public gazebo::ConversionFunction
```  

The most basic conversion function: Thrust = const.*w*abs(w) This corresponds to what is attrributed to Yoerger et al. and called Model 1 in Bessa et al.: Dynamic Positioning of Underwater Robotic Vehicles with Thruster [Dynamics](#classgazebo_1_1_dynamics) Compensation.

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public inline virtual std::string `[`GetType`](#classgazebo_1_1_conversion_function_basic_1a2ce48db471c7706abede19a724ef08fe)`()` | Return (derived) type of conversion function.
`public virtual bool `[`GetParam`](#classgazebo_1_1_conversion_function_basic_1a943dbcaa6720093a775ebb7f3a1e3bea)`(std::string _tag,double & _output)` | Return paramater in scalar form for the given tag.
`public virtual double `[`convert`](#classgazebo_1_1_conversion_function_basic_1a8f10f33118aeda7560214d915cee892e)`(double _cmd)` | Convert thruster state (e.g. angular velocity) to thrust force.

## Members

#### `public inline virtual std::string `[`GetType`](#classgazebo_1_1_conversion_function_basic_1a2ce48db471c7706abede19a724ef08fe)`()` 

Return (derived) type of conversion function.

#### `public virtual bool `[`GetParam`](#classgazebo_1_1_conversion_function_basic_1a943dbcaa6720093a775ebb7f3a1e3bea)`(std::string _tag,double & _output)` 

Return paramater in scalar form for the given tag.

#### `public virtual double `[`convert`](#classgazebo_1_1_conversion_function_basic_1a8f10f33118aeda7560214d915cee892e)`(double _cmd)` 

Convert thruster state (e.g. angular velocity) to thrust force.

# class `gazebo::ConversionFunctionBessa` 

```
class gazebo::ConversionFunctionBessa
  : public gazebo::ConversionFunction
```  

Asymmetric conversion function with dead-zone nonlinearity. This corresponds to what is called Model 2 in Bessa et al.: Dynamic Positioning of Underwater Robotic Vehicles with Thruster [Dynamics](#classgazebo_1_1_dynamics) Compensation.

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public inline virtual std::string `[`GetType`](#classgazebo_1_1_conversion_function_bessa_1a31637f978fdc895689920238998b7926)`()` | Return (derived) type of conversion function.
`public virtual bool `[`GetParam`](#classgazebo_1_1_conversion_function_bessa_1ad47b4e53609b493924d3f0e76626f133)`(std::string _tag,double & _output)` | Return paramater in scalar form for the given tag.
`public virtual double `[`convert`](#classgazebo_1_1_conversion_function_bessa_1a2e863ecdfdeb289ada6d9045783d17a0)`(double _cmd)` | Convert thruster state (e.g. angular velocity) to thrust force.

## Members

#### `public inline virtual std::string `[`GetType`](#classgazebo_1_1_conversion_function_bessa_1a31637f978fdc895689920238998b7926)`()` 

Return (derived) type of conversion function.

#### `public virtual bool `[`GetParam`](#classgazebo_1_1_conversion_function_bessa_1ad47b4e53609b493924d3f0e76626f133)`(std::string _tag,double & _output)` 

Return paramater in scalar form for the given tag.

#### `public virtual double `[`convert`](#classgazebo_1_1_conversion_function_bessa_1a2e863ecdfdeb289ada6d9045783d17a0)`(double _cmd)` 

Convert thruster state (e.g. angular velocity) to thrust force.

# class `gazebo::ConversionFunctionFactory` 

Factory singleton class that creates a [ConversionFunction](#classgazebo_1_1_conversion_function) from sdf.

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public `[`ConversionFunction`](#classgazebo_1_1_conversion_function)` * `[`CreateConversionFunction`](#classgazebo_1_1_conversion_function_factory_1a26d4ebd40ed459a7fb5ed382822ecc33)`(sdf::ElementPtr _sdf)` | Create a [ConversionFunction](#classgazebo_1_1_conversion_function) object according to its sdf Description.
`public bool `[`RegisterCreator`](#classgazebo_1_1_conversion_function_factory_1ac25e17bcce4a2fd6f0cf42f2ead733b0)`(const std::string & _identifier,ConversionFunctionCreator _creator)` | Register a [ConversionFunction](#classgazebo_1_1_conversion_function) class with its creator.

## Members

#### `public `[`ConversionFunction`](#classgazebo_1_1_conversion_function)` * `[`CreateConversionFunction`](#classgazebo_1_1_conversion_function_factory_1a26d4ebd40ed459a7fb5ed382822ecc33)`(sdf::ElementPtr _sdf)` 

Create a [ConversionFunction](#classgazebo_1_1_conversion_function) object according to its sdf Description.

#### `public bool `[`RegisterCreator`](#classgazebo_1_1_conversion_function_factory_1ac25e17bcce4a2fd6f0cf42f2ead733b0)`(const std::string & _identifier,ConversionFunctionCreator _creator)` 

Register a [ConversionFunction](#classgazebo_1_1_conversion_function) class with its creator.

# class `gazebo::ConversionFunctionLinearInterp` 

```
class gazebo::ConversionFunctionLinearInterp
  : public gazebo::ConversionFunction
```  

Conversion using linear interpolation between given data points.

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public inline virtual std::string `[`GetType`](#classgazebo_1_1_conversion_function_linear_interp_1a949ed2e6176730ef0322a25a1a86c92c)`()` | Return (derived) type of conversion function.
`public virtual bool `[`GetParam`](#classgazebo_1_1_conversion_function_linear_interp_1aa443515bbf8913e8d5fef758a6f21b71)`(std::string _tag,double & _output)` | Return paramater in scalar form for the given tag.
`public virtual std::map< double, double > `[`GetTable`](#classgazebo_1_1_conversion_function_linear_interp_1a2252ec3701319511a8d7ef2bbdf25a70)`()` | Return input and output vectors of the lookup table.
`public virtual double `[`convert`](#classgazebo_1_1_conversion_function_linear_interp_1ae0bfc703bbbe5eef389fedf5565b10c1)`(double _cmd)` | Convert thruster state (e.g. angular velocity) to thrust force.

## Members

#### `public inline virtual std::string `[`GetType`](#classgazebo_1_1_conversion_function_linear_interp_1a949ed2e6176730ef0322a25a1a86c92c)`()` 

Return (derived) type of conversion function.

#### `public virtual bool `[`GetParam`](#classgazebo_1_1_conversion_function_linear_interp_1aa443515bbf8913e8d5fef758a6f21b71)`(std::string _tag,double & _output)` 

Return paramater in scalar form for the given tag.

#### `public virtual std::map< double, double > `[`GetTable`](#classgazebo_1_1_conversion_function_linear_interp_1a2252ec3701319511a8d7ef2bbdf25a70)`()` 

Return input and output vectors of the lookup table.

#### `public virtual double `[`convert`](#classgazebo_1_1_conversion_function_linear_interp_1ae0bfc703bbbe5eef389fedf5565b10c1)`(double _cmd)` 

Convert thruster state (e.g. angular velocity) to thrust force.

# class `gazebo::Dynamics` 

Abstract base class for thruster dynamics.

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public inline virtual  `[`~Dynamics`](#classgazebo_1_1_dynamics_1a93c023678bcde05d9cc280afe071b889)`()` | Destructor.
`public std::string `[`GetType`](#classgazebo_1_1_dynamics_1ae9efe1854032da39ab230063c0303549)`()` | Return (derived) type of thruster dynamics.
`public double `[`update`](#classgazebo_1_1_dynamics_1a7cae772ac89944d52757c7883d75f93a)`(double _cmd,double _t)` | Update the dynamic model.
`public virtual void `[`Reset`](#classgazebo_1_1_dynamics_1a4ca9ecc33bdd2e3cf8a42a928a9eec8f)`()` | 
`protected double `[`prevTime`](#classgazebo_1_1_dynamics_1a27de443c5e85c6ab6ddcbb31e880d4b2) | Time of last state update.
`protected double `[`state`](#classgazebo_1_1_dynamics_1a4c2f128d2d0ef4d312936f66106cf229) | Latest state.
`protected inline  `[`Dynamics`](#classgazebo_1_1_dynamics_1a4e590f9f7264d3d7e22c08d9b7737f1a)`()` | Protected constructor: Use the factory for object creation.

## Members

#### `public inline virtual  `[`~Dynamics`](#classgazebo_1_1_dynamics_1a93c023678bcde05d9cc280afe071b889)`()` 

Destructor.

#### `public std::string `[`GetType`](#classgazebo_1_1_dynamics_1ae9efe1854032da39ab230063c0303549)`()` 

Return (derived) type of thruster dynamics.

#### `public double `[`update`](#classgazebo_1_1_dynamics_1a7cae772ac89944d52757c7883d75f93a)`(double _cmd,double _t)` 

Update the dynamic model.

#### Parameters
* `_cmd` The commanded value. 

* `_t` Time stamp of command.

#### `public virtual void `[`Reset`](#classgazebo_1_1_dynamics_1a4ca9ecc33bdd2e3cf8a42a928a9eec8f)`()` 

#### `protected double `[`prevTime`](#classgazebo_1_1_dynamics_1a27de443c5e85c6ab6ddcbb31e880d4b2) 

Time of last state update.

#### `protected double `[`state`](#classgazebo_1_1_dynamics_1a4c2f128d2d0ef4d312936f66106cf229) 

Latest state.

#### `protected inline  `[`Dynamics`](#classgazebo_1_1_dynamics_1a4e590f9f7264d3d7e22c08d9b7737f1a)`()` 

Protected constructor: Use the factory for object creation.

# class `gazebo::DynamicsFactory` 

Factory singleton class that creates a ThrusterDynamics from sdf.

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public `[`Dynamics`](#classgazebo_1_1_dynamics)` * `[`CreateDynamics`](#classgazebo_1_1_dynamics_factory_1a7c041d73164da84de4a4677e7df83c88)`(sdf::ElementPtr _sdf)` | Create ThrusterDynamics object according to its sdf Description.
`public bool `[`RegisterCreator`](#classgazebo_1_1_dynamics_factory_1a46196328ff7188a0bc741da2ab3c4441)`(const std::string & _identifier,DynamicsCreator _creator)` | Register a ThrusterDynamic class with its creator.

## Members

#### `public `[`Dynamics`](#classgazebo_1_1_dynamics)` * `[`CreateDynamics`](#classgazebo_1_1_dynamics_factory_1a7c041d73164da84de4a4677e7df83c88)`(sdf::ElementPtr _sdf)` 

Create ThrusterDynamics object according to its sdf Description.

#### `public bool `[`RegisterCreator`](#classgazebo_1_1_dynamics_factory_1a46196328ff7188a0bc741da2ab3c4441)`(const std::string & _identifier,DynamicsCreator _creator)` 

Register a ThrusterDynamic class with its creator.

# class `gazebo::DynamicsFirstOrder` 

```
class gazebo::DynamicsFirstOrder
  : public gazebo::Dynamics
```  

First-order dynamic system.

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public inline virtual std::string `[`GetType`](#classgazebo_1_1_dynamics_first_order_1a976f58c938b8ca01939d2e9590b75998)`()` | Return (derived) type of dynamic system.
`public virtual double `[`update`](#classgazebo_1_1_dynamics_first_order_1af22a9290175ba3af09ef326bd136dd7f)`(double _cmd,double _t)` | Update dynamical model given input value and time.

## Members

#### `public inline virtual std::string `[`GetType`](#classgazebo_1_1_dynamics_first_order_1a976f58c938b8ca01939d2e9590b75998)`()` 

Return (derived) type of dynamic system.

#### `public virtual double `[`update`](#classgazebo_1_1_dynamics_first_order_1af22a9290175ba3af09ef326bd136dd7f)`(double _cmd,double _t)` 

Update dynamical model given input value and time.

# class `gazebo::DynamicsZeroOrder` 

```
class gazebo::DynamicsZeroOrder
  : public gazebo::Dynamics
```  

Trivial (no dynamics) zero-order dynamic system.

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public inline virtual std::string `[`GetType`](#classgazebo_1_1_dynamics_zero_order_1a1a4108039cf597688a76c54c75272822)`()` | Return (derived) type of dynamic system.
`public virtual double `[`update`](#classgazebo_1_1_dynamics_zero_order_1ae65354f33fab89db306180c59cb60090)`(double _cmd,double _t)` | Update dynamical model given input value and time.

## Members

#### `public inline virtual std::string `[`GetType`](#classgazebo_1_1_dynamics_zero_order_1a1a4108039cf597688a76c54c75272822)`()` 

Return (derived) type of dynamic system.

#### `public virtual double `[`update`](#classgazebo_1_1_dynamics_zero_order_1ae65354f33fab89db306180c59cb60090)`(double _cmd,double _t)` 

Update dynamical model given input value and time.

# class `gazebo::FinPlugin` 

```
class gazebo::FinPlugin
  : public ModelPlugin
```  

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public  `[`FinPlugin`](#classgazebo_1_1_fin_plugin_1a347a9d485eb98d0c0d1ce181cf3530e7)`()` | Constructor.
`public virtual  `[`~FinPlugin`](#classgazebo_1_1_fin_plugin_1a6bfb47239eaef146985a19a5005ba320)`()` | Destructor.
`public virtual void `[`Load`](#classgazebo_1_1_fin_plugin_1a2229e6e90a612c37da8bbf1110c54f53)`(physics::ModelPtr _model,sdf::ElementPtr _sdf)` | 
`public virtual void `[`Init`](#classgazebo_1_1_fin_plugin_1a674d8c80971e173b7066fa2a52ae8388)`()` | 
`public void `[`OnUpdate`](#classgazebo_1_1_fin_plugin_1ab4612d0093ed8b1fd0e24f780f584889)`(const common::UpdateInfo & _info)` | Update the simulation state.
`protected std::shared_ptr< `[`Dynamics`](#classgazebo_1_1_dynamics)` > `[`dynamics`](#classgazebo_1_1_fin_plugin_1ad0a0e94fc62d04d9a08f119e72919420) | Fin dynamic model.
`protected std::shared_ptr< `[`LiftDrag`](#classgazebo_1_1_lift_drag)` > `[`liftdrag`](#classgazebo_1_1_fin_plugin_1a59d7567aa36e7d6882d1dd11c9ab75d0) | Lift&Drag model.
`protected event::ConnectionPtr `[`updateConnection`](#classgazebo_1_1_fin_plugin_1a217cde139114bb0f1415f73b82538e00) | Update event.
`protected transport::NodePtr `[`node`](#classgazebo_1_1_fin_plugin_1a2acefe090abcbd138a230391e577d187) | Gazebo node.
`protected physics::JointPtr `[`joint`](#classgazebo_1_1_fin_plugin_1af5fbe5a75a59199af8e92e17b2546841) | The fin joint.
`protected physics::LinkPtr `[`link`](#classgazebo_1_1_fin_plugin_1aa2a49d7b7c718265296063be66767375) | The fin link.
`protected transport::SubscriberPtr `[`commandSubscriber`](#classgazebo_1_1_fin_plugin_1a5d58c432064cc3c9c94b3ed0bd8a52a3) | Subscriber to the reference signal topic.
`protected transport::PublisherPtr `[`anglePublisher`](#classgazebo_1_1_fin_plugin_1a17fc907ce5376d31010075d2c127e0a9) | Publisher to the output thrust topic.
`protected ignition::math::Vector3d `[`finForce`](#classgazebo_1_1_fin_plugin_1ae0cfeae0cbbf51ed8ad3d88710a7bf95) | Force component calculated from the lift and drag module.
`protected double `[`inputCommand`](#classgazebo_1_1_fin_plugin_1ac748f61691360a841314e3d92ee7cfdd) | Latest input command.
`protected int `[`finID`](#classgazebo_1_1_fin_plugin_1a0d357d22e70731d4f0da1e2eb16dbec9) | Fin ID.
`protected std::string `[`topicPrefix`](#classgazebo_1_1_fin_plugin_1ae595f9a8c9d7d00439935c3a95a7ec42) | Topic prefix.
`protected double `[`angle`](#classgazebo_1_1_fin_plugin_1a030388a1a36c2f58f0baa34605eb0d15) | Latest fin angle in [rad].
`protected common::Time `[`angleStamp`](#classgazebo_1_1_fin_plugin_1a4fb2db18a81a9a7cf8f2f5376b3e5d02) | Time stamp of latest thrust force.
`protected transport::SubscriberPtr `[`currentSubscriber`](#classgazebo_1_1_fin_plugin_1a3940ad05bd8930b1d866154116939a07) | Subcriber to current message.
`protected ignition::math::Vector3d `[`currentVelocity`](#classgazebo_1_1_fin_plugin_1adc8117b6c3169bbcccc25ba63ba4276e) | Current velocity vector read from topic.
`protected void `[`UpdateInput`](#classgazebo_1_1_fin_plugin_1ad20391361f5206bde332a229251c7f38)`(`[`ConstDoublePtr`](#_fin_plugin_8hh_1adec3148dfa71d908caf33660a62187d4)` & _msg)` | Callback for the input topic subscriber.
`protected void `[`UpdateCurrentVelocity`](#classgazebo_1_1_fin_plugin_1aaf4c2da2058c877cbffdd0dc6d94c0ee)`(ConstVector3dPtr & _msg)` | Reads current velocity topic.

## Members

#### `public  `[`FinPlugin`](#classgazebo_1_1_fin_plugin_1a347a9d485eb98d0c0d1ce181cf3530e7)`()` 

Constructor.

#### `public virtual  `[`~FinPlugin`](#classgazebo_1_1_fin_plugin_1a6bfb47239eaef146985a19a5005ba320)`()` 

Destructor.

#### `public virtual void `[`Load`](#classgazebo_1_1_fin_plugin_1a2229e6e90a612c37da8bbf1110c54f53)`(physics::ModelPtr _model,sdf::ElementPtr _sdf)` 

#### `public virtual void `[`Init`](#classgazebo_1_1_fin_plugin_1a674d8c80971e173b7066fa2a52ae8388)`()` 

#### `public void `[`OnUpdate`](#classgazebo_1_1_fin_plugin_1ab4612d0093ed8b1fd0e24f780f584889)`(const common::UpdateInfo & _info)` 

Update the simulation state.

#### Parameters
* `_info` Information used in the update event.

#### `protected std::shared_ptr< `[`Dynamics`](#classgazebo_1_1_dynamics)` > `[`dynamics`](#classgazebo_1_1_fin_plugin_1ad0a0e94fc62d04d9a08f119e72919420) 

Fin dynamic model.

#### `protected std::shared_ptr< `[`LiftDrag`](#classgazebo_1_1_lift_drag)` > `[`liftdrag`](#classgazebo_1_1_fin_plugin_1a59d7567aa36e7d6882d1dd11c9ab75d0) 

Lift&Drag model.

#### `protected event::ConnectionPtr `[`updateConnection`](#classgazebo_1_1_fin_plugin_1a217cde139114bb0f1415f73b82538e00) 

Update event.

#### `protected transport::NodePtr `[`node`](#classgazebo_1_1_fin_plugin_1a2acefe090abcbd138a230391e577d187) 

Gazebo node.

#### `protected physics::JointPtr `[`joint`](#classgazebo_1_1_fin_plugin_1af5fbe5a75a59199af8e92e17b2546841) 

The fin joint.

#### `protected physics::LinkPtr `[`link`](#classgazebo_1_1_fin_plugin_1aa2a49d7b7c718265296063be66767375) 

The fin link.

#### `protected transport::SubscriberPtr `[`commandSubscriber`](#classgazebo_1_1_fin_plugin_1a5d58c432064cc3c9c94b3ed0bd8a52a3) 

Subscriber to the reference signal topic.

#### `protected transport::PublisherPtr `[`anglePublisher`](#classgazebo_1_1_fin_plugin_1a17fc907ce5376d31010075d2c127e0a9) 

Publisher to the output thrust topic.

#### `protected ignition::math::Vector3d `[`finForce`](#classgazebo_1_1_fin_plugin_1ae0cfeae0cbbf51ed8ad3d88710a7bf95) 

Force component calculated from the lift and drag module.

#### `protected double `[`inputCommand`](#classgazebo_1_1_fin_plugin_1ac748f61691360a841314e3d92ee7cfdd) 

Latest input command.

#### `protected int `[`finID`](#classgazebo_1_1_fin_plugin_1a0d357d22e70731d4f0da1e2eb16dbec9) 

Fin ID.

#### `protected std::string `[`topicPrefix`](#classgazebo_1_1_fin_plugin_1ae595f9a8c9d7d00439935c3a95a7ec42) 

Topic prefix.

#### `protected double `[`angle`](#classgazebo_1_1_fin_plugin_1a030388a1a36c2f58f0baa34605eb0d15) 

Latest fin angle in [rad].

#### `protected common::Time `[`angleStamp`](#classgazebo_1_1_fin_plugin_1a4fb2db18a81a9a7cf8f2f5376b3e5d02) 

Time stamp of latest thrust force.

#### `protected transport::SubscriberPtr `[`currentSubscriber`](#classgazebo_1_1_fin_plugin_1a3940ad05bd8930b1d866154116939a07) 

Subcriber to current message.

#### `protected ignition::math::Vector3d `[`currentVelocity`](#classgazebo_1_1_fin_plugin_1adc8117b6c3169bbcccc25ba63ba4276e) 

Current velocity vector read from topic.

#### `protected void `[`UpdateInput`](#classgazebo_1_1_fin_plugin_1ad20391361f5206bde332a229251c7f38)`(`[`ConstDoublePtr`](#_fin_plugin_8hh_1adec3148dfa71d908caf33660a62187d4)` & _msg)` 

Callback for the input topic subscriber.

#### `protected void `[`UpdateCurrentVelocity`](#classgazebo_1_1_fin_plugin_1aaf4c2da2058c877cbffdd0dc6d94c0ee)`(ConstVector3dPtr & _msg)` 

Reads current velocity topic.

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

# class `gazebo::HMFossen` 

```
class gazebo::HMFossen
  : public gazebo::HydrodynamicModel
```  

Class containting the methods and attributes for a Fossen robot-like hydrodynamic model. The restoring forces are applied by the [BuoyantObject](#classgazebo_1_1_buoyant_object) class methods. Using the plugin for UUV models will use both this and the buoyant object class definitions, therefore the restoring forces were not inherited here. References:

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
`protected `[`Eigen::Matrix6d`](#_def_8hh_1ab6f8b8b11b0f6350ed45e7cd3437207f)` `[`Ma`](#classgazebo_1_1_h_m_fossen_1a2a31c659331c826a6d80abe7755e473e) | Added-mass matrix.
`protected double `[`scalingAddedMass`](#classgazebo_1_1_h_m_fossen_1ada6f90d47445047d905e8fe3794885ac) | Scaling of the added-mass matrix.
`protected double `[`offsetAddedMass`](#classgazebo_1_1_h_m_fossen_1ab326125b3b49893d7492f4778d6ace55) | Offset for the added-mass matrix.
`protected `[`Eigen::Matrix6d`](#_def_8hh_1ab6f8b8b11b0f6350ed45e7cd3437207f)` `[`Ca`](#classgazebo_1_1_h_m_fossen_1aafd51761404afd9b1e98f0b1ecb0b14f) | Added-mass associated Coriolis matrix.
`protected `[`Eigen::Matrix6d`](#_def_8hh_1ab6f8b8b11b0f6350ed45e7cd3437207f)` `[`D`](#classgazebo_1_1_h_m_fossen_1a20df2ff4d0a155b41c275d37e621e32f) | Damping matrix.
`protected double `[`scalingDamping`](#classgazebo_1_1_h_m_fossen_1a5d5f9e75be8dbbd2b8bbfbc81ba55cf3) | Scaling of the damping matrix.
`protected double `[`offsetLinearDamping`](#classgazebo_1_1_h_m_fossen_1adc9dd4195791aab3ebaf12bdbe2e293e) | Offset for the linear damping matrix.
`protected double `[`offsetLinForwardSpeedDamping`](#classgazebo_1_1_h_m_fossen_1a1c9074d7810329daca5f3ea42e6307cb) | Offset for the linear damping matrix.
`protected double `[`offsetNonLinDamping`](#classgazebo_1_1_h_m_fossen_1a6e2bfe2801f2697f0e0c087a45158ff3) | Offset for the linear damping matrix.
`protected `[`Eigen::Matrix6d`](#_def_8hh_1ab6f8b8b11b0f6350ed45e7cd3437207f)` `[`DLin`](#classgazebo_1_1_h_m_fossen_1a1301b0130643ce7d55b8ff238afdc264) | Linear damping matrix.
`protected `[`Eigen::Matrix6d`](#_def_8hh_1ab6f8b8b11b0f6350ed45e7cd3437207f)` `[`DLinForwardSpeed`](#classgazebo_1_1_h_m_fossen_1a9a2cc66ad71a7fc9ce904f5cc27a36f0) | Linear damping matrix proportional only to the forward speed (useful for modeling AUVs). From [1], according to Newman (1977), there is a damping force component that linearly increases with the presence of forward speed, particularly so for slender bodies.
`protected `[`Eigen::Matrix6d`](#_def_8hh_1ab6f8b8b11b0f6350ed45e7cd3437207f)` `[`DNonLin`](#classgazebo_1_1_h_m_fossen_1a3219a54c0be1a8a1e186b33dde95d6b5) | Nonlinear damping coefficients.
`protected std::vector< double > `[`linearDampCoef`](#classgazebo_1_1_h_m_fossen_1aaaee5e4e341d1f3fccba9c832429712d) | Linear damping coefficients.
`protected std::vector< double > `[`quadDampCoef`](#classgazebo_1_1_h_m_fossen_1a062e26123041365e16822bc2059fe3d1) | Quadratic damping coefficients.
`protected  `[`REGISTER_HYDRODYNAMICMODEL`](#classgazebo_1_1_h_m_fossen_1ab3a59be3a5e9037575ee6f4878e96d8b)`(`[`HMFossen`](#classgazebo_1_1_h_m_fossen)`)` | Register this model with the factory.
`protected  `[`HMFossen`](#classgazebo_1_1_h_m_fossen_1a9b9fcbd9ca518c9cd41300e0f9d43ee5)`(sdf::ElementPtr _sdf,physics::LinkPtr _link)` | 
`protected void `[`ComputeAddedCoriolisMatrix`](#classgazebo_1_1_h_m_fossen_1afe97af45fc44777a04b4f1c81519b07b)`(const `[`Eigen::Vector6d`](#_def_8hh_1a09219f5e0b822edbf24b125e0e2a4fe0)` & _vel,const `[`Eigen::Matrix6d`](#_def_8hh_1ab6f8b8b11b0f6350ed45e7cd3437207f)` & _Ma,`[`Eigen::Matrix6d`](#_def_8hh_1ab6f8b8b11b0f6350ed45e7cd3437207f)` & _Ca) const` | Computes the added-mass Coriolis matrix Ca.
`protected void `[`ComputeDampingMatrix`](#classgazebo_1_1_h_m_fossen_1a19624761792eac92864647ebee971196)`(const `[`Eigen::Vector6d`](#_def_8hh_1a09219f5e0b822edbf24b125e0e2a4fe0)` & _vel,`[`Eigen::Matrix6d`](#_def_8hh_1ab6f8b8b11b0f6350ed45e7cd3437207f)` & _D) const` | Updates the damping matrix for the current velocity.
`protected `[`Eigen::Matrix6d`](#_def_8hh_1ab6f8b8b11b0f6350ed45e7cd3437207f)` `[`GetAddedMass`](#classgazebo_1_1_h_m_fossen_1a555bb01ef30396e3b39fa26bf6a79848)`() const` | Returns the added-mass matrix with the scaling and offset.

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

#### `protected `[`Eigen::Matrix6d`](#_def_8hh_1ab6f8b8b11b0f6350ed45e7cd3437207f)` `[`Ma`](#classgazebo_1_1_h_m_fossen_1a2a31c659331c826a6d80abe7755e473e) 

Added-mass matrix.

#### `protected double `[`scalingAddedMass`](#classgazebo_1_1_h_m_fossen_1ada6f90d47445047d905e8fe3794885ac) 

Scaling of the added-mass matrix.

#### `protected double `[`offsetAddedMass`](#classgazebo_1_1_h_m_fossen_1ab326125b3b49893d7492f4778d6ace55) 

Offset for the added-mass matrix.

#### `protected `[`Eigen::Matrix6d`](#_def_8hh_1ab6f8b8b11b0f6350ed45e7cd3437207f)` `[`Ca`](#classgazebo_1_1_h_m_fossen_1aafd51761404afd9b1e98f0b1ecb0b14f) 

Added-mass associated Coriolis matrix.

#### `protected `[`Eigen::Matrix6d`](#_def_8hh_1ab6f8b8b11b0f6350ed45e7cd3437207f)` `[`D`](#classgazebo_1_1_h_m_fossen_1a20df2ff4d0a155b41c275d37e621e32f) 

Damping matrix.

#### `protected double `[`scalingDamping`](#classgazebo_1_1_h_m_fossen_1a5d5f9e75be8dbbd2b8bbfbc81ba55cf3) 

Scaling of the damping matrix.

#### `protected double `[`offsetLinearDamping`](#classgazebo_1_1_h_m_fossen_1adc9dd4195791aab3ebaf12bdbe2e293e) 

Offset for the linear damping matrix.

#### `protected double `[`offsetLinForwardSpeedDamping`](#classgazebo_1_1_h_m_fossen_1a1c9074d7810329daca5f3ea42e6307cb) 

Offset for the linear damping matrix.

#### `protected double `[`offsetNonLinDamping`](#classgazebo_1_1_h_m_fossen_1a6e2bfe2801f2697f0e0c087a45158ff3) 

Offset for the linear damping matrix.

#### `protected `[`Eigen::Matrix6d`](#_def_8hh_1ab6f8b8b11b0f6350ed45e7cd3437207f)` `[`DLin`](#classgazebo_1_1_h_m_fossen_1a1301b0130643ce7d55b8ff238afdc264) 

Linear damping matrix.

#### `protected `[`Eigen::Matrix6d`](#_def_8hh_1ab6f8b8b11b0f6350ed45e7cd3437207f)` `[`DLinForwardSpeed`](#classgazebo_1_1_h_m_fossen_1a9a2cc66ad71a7fc9ce904f5cc27a36f0) 

Linear damping matrix proportional only to the forward speed (useful for modeling AUVs). From [1], according to Newman (1977), there is a damping force component that linearly increases with the presence of forward speed, particularly so for slender bodies.

References: [1] Refsnes - 2007 - Nonlinear model-based control of slender body AUVs

#### `protected `[`Eigen::Matrix6d`](#_def_8hh_1ab6f8b8b11b0f6350ed45e7cd3437207f)` `[`DNonLin`](#classgazebo_1_1_h_m_fossen_1a3219a54c0be1a8a1e186b33dde95d6b5) 

Nonlinear damping coefficients.

#### `protected std::vector< double > `[`linearDampCoef`](#classgazebo_1_1_h_m_fossen_1aaaee5e4e341d1f3fccba9c832429712d) 

Linear damping coefficients.

#### `protected std::vector< double > `[`quadDampCoef`](#classgazebo_1_1_h_m_fossen_1a062e26123041365e16822bc2059fe3d1) 

Quadratic damping coefficients.

#### `protected  `[`REGISTER_HYDRODYNAMICMODEL`](#classgazebo_1_1_h_m_fossen_1ab3a59be3a5e9037575ee6f4878e96d8b)`(`[`HMFossen`](#classgazebo_1_1_h_m_fossen)`)` 

Register this model with the factory.

#### `protected  `[`HMFossen`](#classgazebo_1_1_h_m_fossen_1a9b9fcbd9ca518c9cd41300e0f9d43ee5)`(sdf::ElementPtr _sdf,physics::LinkPtr _link)` 

#### `protected void `[`ComputeAddedCoriolisMatrix`](#classgazebo_1_1_h_m_fossen_1afe97af45fc44777a04b4f1c81519b07b)`(const `[`Eigen::Vector6d`](#_def_8hh_1a09219f5e0b822edbf24b125e0e2a4fe0)` & _vel,const `[`Eigen::Matrix6d`](#_def_8hh_1ab6f8b8b11b0f6350ed45e7cd3437207f)` & _Ma,`[`Eigen::Matrix6d`](#_def_8hh_1ab6f8b8b11b0f6350ed45e7cd3437207f)` & _Ca) const` 

Computes the added-mass Coriolis matrix Ca.

#### `protected void `[`ComputeDampingMatrix`](#classgazebo_1_1_h_m_fossen_1a19624761792eac92864647ebee971196)`(const `[`Eigen::Vector6d`](#_def_8hh_1a09219f5e0b822edbf24b125e0e2a4fe0)` & _vel,`[`Eigen::Matrix6d`](#_def_8hh_1ab6f8b8b11b0f6350ed45e7cd3437207f)` & _D) const` 

Updates the damping matrix for the current velocity.

#### `protected `[`Eigen::Matrix6d`](#_def_8hh_1ab6f8b8b11b0f6350ed45e7cd3437207f)` `[`GetAddedMass`](#classgazebo_1_1_h_m_fossen_1a555bb01ef30396e3b39fa26bf6a79848)`() const` 

Returns the added-mass matrix with the scaling and offset.

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

# class `gazebo::HydrodynamicModel` 

```
class gazebo::HydrodynamicModel
  : public gazebo::BuoyantObject
```  

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public std::string `[`GetType`](#classgazebo_1_1_hydrodynamic_model_1a16e39024389414178442d4278c16222a)`()` | Returns type of model.
`public void `[`ApplyHydrodynamicForces`](#classgazebo_1_1_hydrodynamic_model_1a365a5ea0d71ad3ec3d79f985c42c2417)`(double time,const ignition::math::Vector3d & _flowVelWorld)` | Computation of the hydrodynamic forces.
`public void `[`Print`](#classgazebo_1_1_hydrodynamic_model_1aead6d1b6eefebe5034bb86adcbf1169a)`(std::string _paramName,std::string _message)` | Prints parameters.
`public bool `[`GetParam`](#classgazebo_1_1_hydrodynamic_model_1ac123271c564f843fb280713704d20f7e)`(std::string _tag,std::vector< double > & _output)` | Return paramater in vector form for the given tag.
`public bool `[`GetParam`](#classgazebo_1_1_hydrodynamic_model_1addaa35736ce4bc798ab70ace59a0a9e8)`(std::string _tag,double & _output)` | Return paramater in vector form for the given tag.
`public bool `[`SetParam`](#classgazebo_1_1_hydrodynamic_model_1a173db3079e94e656abcaf44d61ea3ba2)`(std::string _tag,double _input)` | Set a scalar parameters.
`protected `[`Eigen::Vector6d`](#_def_8hh_1a09219f5e0b822edbf24b125e0e2a4fe0)` `[`filteredAcc`](#classgazebo_1_1_hydrodynamic_model_1a9d402a541867397d32247de6746ab5de) | Filtered linear & angular acceleration vector in link frame. This is used to prevent the model to become unstable given that Gazebo only calls the update function at the beginning or at the end of a iteration of the physics engine.
`protected double `[`lastTime`](#classgazebo_1_1_hydrodynamic_model_1a212a914dc81067558c637d308773e23e) | Last timestamp (in seconds) at which ApplyHydrodynamicForces was called.
`protected `[`Eigen::Vector6d`](#_def_8hh_1a09219f5e0b822edbf24b125e0e2a4fe0)` `[`lastVelRel`](#classgazebo_1_1_hydrodynamic_model_1affd2dff3e08a26ac9e00ee2ebaff6016) | Last body-fixed relative velocity (nu_R in Fossen's equations)
`protected std::vector< std::string > `[`params`](#classgazebo_1_1_hydrodynamic_model_1a6152abe7eda7e10157ed72696d87be38) | List of parameters needed from the SDF element.
`protected double `[`Re`](#classgazebo_1_1_hydrodynamic_model_1ae82075119ebbf0d7f3f0ea13b6aeb6cf) | Reynolds number (not used by all models)
`protected double `[`temperature`](#classgazebo_1_1_hydrodynamic_model_1adf0cb47bd32f552c285f4cf5eeec9d36) | Temperature (not used by all models)
`protected  `[`HydrodynamicModel`](#classgazebo_1_1_hydrodynamic_model_1aac68d5a44688757965ccf0e9d648c8b8)`(sdf::ElementPtr _sdf,physics::LinkPtr _link)` | Protected constructor: Use the factory for object creation.
`protected void `[`ComputeAcc`](#classgazebo_1_1_hydrodynamic_model_1abb6cf4e433202d163b1276d67434ace2)`(`[`Eigen::Vector6d`](#_def_8hh_1a09219f5e0b822edbf24b125e0e2a4fe0)` _velRel,double _time,double _alpha)` | Filter acceleration (fix due to the update structure of Gazebo)
`protected bool `[`CheckParams`](#classgazebo_1_1_hydrodynamic_model_1a729f90fa3933d2fd9aeed5fdb7838f1b)`(sdf::ElementPtr _sdf)` | Returns true if all parameters are available from the SDF element.
`protected ignition::math::Vector3d `[`ToNED`](#classgazebo_1_1_hydrodynamic_model_1a46a25bbc280aa3d466268756c7362809)`(ignition::math::Vector3d _vec)` | Convert vector to comply with the NED reference frame.
`protected ignition::math::Vector3d `[`FromNED`](#classgazebo_1_1_hydrodynamic_model_1a715caa11d851a41265d0d682301e3781)`(ignition::math::Vector3d _vec)` | Convert vector to comply with the NED reference frame.

## Members

#### `public std::string `[`GetType`](#classgazebo_1_1_hydrodynamic_model_1a16e39024389414178442d4278c16222a)`()` 

Returns type of model.

#### `public void `[`ApplyHydrodynamicForces`](#classgazebo_1_1_hydrodynamic_model_1a365a5ea0d71ad3ec3d79f985c42c2417)`(double time,const ignition::math::Vector3d & _flowVelWorld)` 

Computation of the hydrodynamic forces.

#### `public void `[`Print`](#classgazebo_1_1_hydrodynamic_model_1aead6d1b6eefebe5034bb86adcbf1169a)`(std::string _paramName,std::string _message)` 

Prints parameters.

#### `public bool `[`GetParam`](#classgazebo_1_1_hydrodynamic_model_1ac123271c564f843fb280713704d20f7e)`(std::string _tag,std::vector< double > & _output)` 

Return paramater in vector form for the given tag.

#### `public bool `[`GetParam`](#classgazebo_1_1_hydrodynamic_model_1addaa35736ce4bc798ab70ace59a0a9e8)`(std::string _tag,double & _output)` 

Return paramater in vector form for the given tag.

#### `public bool `[`SetParam`](#classgazebo_1_1_hydrodynamic_model_1a173db3079e94e656abcaf44d61ea3ba2)`(std::string _tag,double _input)` 

Set a scalar parameters.

#### `protected `[`Eigen::Vector6d`](#_def_8hh_1a09219f5e0b822edbf24b125e0e2a4fe0)` `[`filteredAcc`](#classgazebo_1_1_hydrodynamic_model_1a9d402a541867397d32247de6746ab5de) 

Filtered linear & angular acceleration vector in link frame. This is used to prevent the model to become unstable given that Gazebo only calls the update function at the beginning or at the end of a iteration of the physics engine.

#### `protected double `[`lastTime`](#classgazebo_1_1_hydrodynamic_model_1a212a914dc81067558c637d308773e23e) 

Last timestamp (in seconds) at which ApplyHydrodynamicForces was called.

#### `protected `[`Eigen::Vector6d`](#_def_8hh_1a09219f5e0b822edbf24b125e0e2a4fe0)` `[`lastVelRel`](#classgazebo_1_1_hydrodynamic_model_1affd2dff3e08a26ac9e00ee2ebaff6016) 

Last body-fixed relative velocity (nu_R in Fossen's equations)

#### `protected std::vector< std::string > `[`params`](#classgazebo_1_1_hydrodynamic_model_1a6152abe7eda7e10157ed72696d87be38) 

List of parameters needed from the SDF element.

#### `protected double `[`Re`](#classgazebo_1_1_hydrodynamic_model_1ae82075119ebbf0d7f3f0ea13b6aeb6cf) 

Reynolds number (not used by all models)

#### `protected double `[`temperature`](#classgazebo_1_1_hydrodynamic_model_1adf0cb47bd32f552c285f4cf5eeec9d36) 

Temperature (not used by all models)

#### `protected  `[`HydrodynamicModel`](#classgazebo_1_1_hydrodynamic_model_1aac68d5a44688757965ccf0e9d648c8b8)`(sdf::ElementPtr _sdf,physics::LinkPtr _link)` 

Protected constructor: Use the factory for object creation.

#### `protected void `[`ComputeAcc`](#classgazebo_1_1_hydrodynamic_model_1abb6cf4e433202d163b1276d67434ace2)`(`[`Eigen::Vector6d`](#_def_8hh_1a09219f5e0b822edbf24b125e0e2a4fe0)` _velRel,double _time,double _alpha)` 

Filter acceleration (fix due to the update structure of Gazebo)

#### `protected bool `[`CheckParams`](#classgazebo_1_1_hydrodynamic_model_1a729f90fa3933d2fd9aeed5fdb7838f1b)`(sdf::ElementPtr _sdf)` 

Returns true if all parameters are available from the SDF element.

#### `protected ignition::math::Vector3d `[`ToNED`](#classgazebo_1_1_hydrodynamic_model_1a46a25bbc280aa3d466268756c7362809)`(ignition::math::Vector3d _vec)` 

Convert vector to comply with the NED reference frame.

#### `protected ignition::math::Vector3d `[`FromNED`](#classgazebo_1_1_hydrodynamic_model_1a715caa11d851a41265d0d682301e3781)`(ignition::math::Vector3d _vec)` 

Convert vector to comply with the NED reference frame.

# class `gazebo::HydrodynamicModelFactory` 

Factory singleton class that creates a [HydrodynamicModel](#classgazebo_1_1_hydrodynamic_model) from sdf.

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public `[`HydrodynamicModel`](#classgazebo_1_1_hydrodynamic_model)` * `[`CreateHydrodynamicModel`](#classgazebo_1_1_hydrodynamic_model_factory_1a4113b1faaf8277574e4a4b3854f51884)`(sdf::ElementPtr _sdf,physics::LinkPtr _link)` | Create [HydrodynamicModel](#classgazebo_1_1_hydrodynamic_model) object according to its sdf Description.
`public bool `[`RegisterCreator`](#classgazebo_1_1_hydrodynamic_model_factory_1acc1cc6c8730ee4e0d558d4fbfa96ecb5)`(const std::string & _identifier,HydrodynamicModelCreator _creator)` | Register a class with its creator.

## Members

#### `public `[`HydrodynamicModel`](#classgazebo_1_1_hydrodynamic_model)` * `[`CreateHydrodynamicModel`](#classgazebo_1_1_hydrodynamic_model_factory_1a4113b1faaf8277574e4a4b3854f51884)`(sdf::ElementPtr _sdf,physics::LinkPtr _link)` 

Create [HydrodynamicModel](#classgazebo_1_1_hydrodynamic_model) object according to its sdf Description.

#### `public bool `[`RegisterCreator`](#classgazebo_1_1_hydrodynamic_model_factory_1acc1cc6c8730ee4e0d558d4fbfa96ecb5)`(const std::string & _identifier,HydrodynamicModelCreator _creator)` 

Register a class with its creator.

# class `gazebo::LiftDrag` 

Abstract base class for Lift&Drag models.

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public inline virtual  `[`~LiftDrag`](#classgazebo_1_1_lift_drag_1a7025e5299778dfb25ee8e1eaed4ecb83)`()` | Destructor.
`public std::string `[`GetType`](#classgazebo_1_1_lift_drag_1ad8a25e574ba7f75b30e8813b315010b3)`()` | Return (derived) type of lift&drag model.
`public ignition::math::Vector3d `[`compute`](#classgazebo_1_1_lift_drag_1ac20f4dbd4ea08d8d9d0852f8e2b128b0)`(const ignition::math::Vector3d & _velL)` | Compute the lift and drag force.
`public bool `[`GetParam`](#classgazebo_1_1_lift_drag_1a4e2d58afb4af2ba7c0f169cd8fcebb3b)`(std::string _tag,double & _output)` | Return paramater in vector form for the given tag.
`public std::map< std::string, double > `[`GetListParams`](#classgazebo_1_1_lift_drag_1a7d35e963ce57451f5939ccff9a956285)`()` | Return list of all parameters.
`protected double `[`prevTime`](#classgazebo_1_1_lift_drag_1aa062dc13d3a5c4b9d6de277cc578eee7) | Time of last state update.
`protected double `[`state`](#classgazebo_1_1_lift_drag_1a73cd43d69e94ce2a392abe437c732cb0) | Latest state.
`protected inline  `[`LiftDrag`](#classgazebo_1_1_lift_drag_1aa9f53de408dfca89a517be7dbcd673c6)`()` | Protected constructor: Use the factory for object creation.

## Members

#### `public inline virtual  `[`~LiftDrag`](#classgazebo_1_1_lift_drag_1a7025e5299778dfb25ee8e1eaed4ecb83)`()` 

Destructor.

#### `public std::string `[`GetType`](#classgazebo_1_1_lift_drag_1ad8a25e574ba7f75b30e8813b315010b3)`()` 

Return (derived) type of lift&drag model.

#### `public ignition::math::Vector3d `[`compute`](#classgazebo_1_1_lift_drag_1ac20f4dbd4ea08d8d9d0852f8e2b128b0)`(const ignition::math::Vector3d & _velL)` 

Compute the lift and drag force.

#### `public bool `[`GetParam`](#classgazebo_1_1_lift_drag_1a4e2d58afb4af2ba7c0f169cd8fcebb3b)`(std::string _tag,double & _output)` 

Return paramater in vector form for the given tag.

#### `public std::map< std::string, double > `[`GetListParams`](#classgazebo_1_1_lift_drag_1a7d35e963ce57451f5939ccff9a956285)`()` 

Return list of all parameters.

#### `protected double `[`prevTime`](#classgazebo_1_1_lift_drag_1aa062dc13d3a5c4b9d6de277cc578eee7) 

Time of last state update.

#### `protected double `[`state`](#classgazebo_1_1_lift_drag_1a73cd43d69e94ce2a392abe437c732cb0) 

Latest state.

#### `protected inline  `[`LiftDrag`](#classgazebo_1_1_lift_drag_1aa9f53de408dfca89a517be7dbcd673c6)`()` 

Protected constructor: Use the factory for object creation.

# class `gazebo::LiftDragFactory` 

Factory singleton class that creates a [LiftDrag](#classgazebo_1_1_lift_drag) from sdf.

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public `[`LiftDrag`](#classgazebo_1_1_lift_drag)` * `[`CreateLiftDrag`](#classgazebo_1_1_lift_drag_factory_1a7a79c4e602ee766109f7ff64de1db8ac)`(sdf::ElementPtr _sdf)` | Create [LiftDrag](#classgazebo_1_1_lift_drag) object according to its sdf Description.
`public bool `[`RegisterCreator`](#classgazebo_1_1_lift_drag_factory_1addb70527ea530e2f7d260a077657f722)`(const std::string & _identifier,LiftDragCreator _creator)` | Register a [LiftDrag](#classgazebo_1_1_lift_drag) class with its creator.

## Members

#### `public `[`LiftDrag`](#classgazebo_1_1_lift_drag)` * `[`CreateLiftDrag`](#classgazebo_1_1_lift_drag_factory_1a7a79c4e602ee766109f7ff64de1db8ac)`(sdf::ElementPtr _sdf)` 

Create [LiftDrag](#classgazebo_1_1_lift_drag) object according to its sdf Description.

#### `public bool `[`RegisterCreator`](#classgazebo_1_1_lift_drag_factory_1addb70527ea530e2f7d260a077657f722)`(const std::string & _identifier,LiftDragCreator _creator)` 

Register a [LiftDrag](#classgazebo_1_1_lift_drag) class with its creator.

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

# class `gazebo::LiftDragTwoLines` 

```
class gazebo::LiftDragTwoLines
  : public gazebo::LiftDrag
```  

Lift&drag model that models lift/drag coeffs using two lines. This is based on Gazebo's LiftDragPlugin but implemented as a derived [LiftDrag](#classgazebo_1_1_lift_drag) model to allow using it in combination with the dynamics of a Fin.

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

# class `gazebo::ThrusterDynamicsBessa` 

```
class gazebo::ThrusterDynamicsBessa
  : public gazebo::Dynamics
```  

Bessa's dynamic thruster model.

This is "Model 2" described in Bessa et al.: Dynamic Positioning of Underwater Robotic Vehicles with Thruster [Dynamics](#classgazebo_1_1_dynamics) Compensation.

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public inline virtual std::string `[`GetType`](#classgazebo_1_1_thruster_dynamics_bessa_1a141b10b080998366163f31793fd93a78)`()` | Return (derived) type of dynamic system.
`public virtual double `[`update`](#classgazebo_1_1_thruster_dynamics_bessa_1a4eaffe57006894124ec0f62987785996)`(double _cmd,double _t)` | Update dynamical model given input value and time.

## Members

#### `public inline virtual std::string `[`GetType`](#classgazebo_1_1_thruster_dynamics_bessa_1a141b10b080998366163f31793fd93a78)`()` 

Return (derived) type of dynamic system.

#### `public virtual double `[`update`](#classgazebo_1_1_thruster_dynamics_bessa_1a4eaffe57006894124ec0f62987785996)`(double _cmd,double _t)` 

Update dynamical model given input value and time.

# class `gazebo::ThrusterDynamicsYoerger` 

```
class gazebo::ThrusterDynamicsYoerger
  : public gazebo::Dynamics
```  

Yoerger's dynamic thruster model.

This is the lumped-parameter model of Yoerger et al.: The influence of thruster dynamics on underwater vehicle behavior and their incorporation into control system design. (1990)

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public inline virtual std::string `[`GetType`](#classgazebo_1_1_thruster_dynamics_yoerger_1a71e827ac4c6ed26139b35d0fb72f5c3e)`()` | Return (derived) type of dynamic system.
`public virtual double `[`update`](#classgazebo_1_1_thruster_dynamics_yoerger_1a0d43ff9c18a4caa3b056c50f4997de85)`(double _cmd,double _t)` | Update dynamical model given input value and time.

## Members

#### `public inline virtual std::string `[`GetType`](#classgazebo_1_1_thruster_dynamics_yoerger_1a71e827ac4c6ed26139b35d0fb72f5c3e)`()` 

Return (derived) type of dynamic system.

#### `public virtual double `[`update`](#classgazebo_1_1_thruster_dynamics_yoerger_1a0d43ff9c18a4caa3b056c50f4997de85)`(double _cmd,double _t)` 

Update dynamical model given input value and time.

# class `gazebo::ThrusterPlugin` 

```
class gazebo::ThrusterPlugin
  : public ModelPlugin
```  

Class for the thruster plugin.

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public  `[`ThrusterPlugin`](#classgazebo_1_1_thruster_plugin_1a6b5841ff33686cc450313e03cf294d9c)`()` | Constructor.
`public virtual  `[`~ThrusterPlugin`](#classgazebo_1_1_thruster_plugin_1a06d1a5a37d484a2ce88329fd2fed8f59)`()` | Destructor.
`public virtual void `[`Load`](#classgazebo_1_1_thruster_plugin_1a1b4f788380387681886f65531ceb0f25)`(physics::ModelPtr _model,sdf::ElementPtr _sdf)` | 
`public virtual void `[`Init`](#classgazebo_1_1_thruster_plugin_1a976abc5ac54372004630800a7d83aa8e)`()` | 
`public virtual void `[`Reset`](#classgazebo_1_1_thruster_plugin_1a3a445ef9af6ff415eb3d2e319c232841)`()` | Custom plugin reset behavior.
`public void `[`Update`](#classgazebo_1_1_thruster_plugin_1a4cd1505e012721530e09cc346500ff12)`(const common::UpdateInfo & _info)` | Update the simulation state.
`protected std::shared_ptr< `[`Dynamics`](#classgazebo_1_1_dynamics)` > `[`thrusterDynamics`](#classgazebo_1_1_thruster_plugin_1a2a5bdae0148178c1688362257e59dbfa) | Thruster dynamic model.
`protected std::shared_ptr< `[`ConversionFunction`](#classgazebo_1_1_conversion_function)` > `[`conversionFunction`](#classgazebo_1_1_thruster_plugin_1aab369c9f214021b0e3372dd61907c257) | Thruster conversion function.
`protected event::ConnectionPtr `[`updateConnection`](#classgazebo_1_1_thruster_plugin_1a23c4d67fd108db7dabc2727244934a30) | Update event.
`protected physics::LinkPtr `[`thrusterLink`](#classgazebo_1_1_thruster_plugin_1a141de7a7aedb56861b9046ee7897399f) | Pointer to the thruster link.
`protected transport::NodePtr `[`node`](#classgazebo_1_1_thruster_plugin_1afedb1c79f0a9c060cd4bc6c1ef541b68) | Gazebo node.
`protected transport::SubscriberPtr `[`commandSubscriber`](#classgazebo_1_1_thruster_plugin_1ae4054a7444082b7f0195b3cf72bfad6f) | Subscriber to the reference signal topic.
`protected transport::PublisherPtr `[`thrustTopicPublisher`](#classgazebo_1_1_thruster_plugin_1a8ad82769e76b0844a87763446f03a267) | Publisher to the output thrust topic.
`protected double `[`inputCommand`](#classgazebo_1_1_thruster_plugin_1a617d0e909a0d82397d95954c8c103035) | Input command, typically desired angular velocity of the rotor.
`protected double `[`thrustForce`](#classgazebo_1_1_thruster_plugin_1a3dd6123930d825ae14ca56b253b9c8a2) | Latest thrust force in [N].
`protected common::Time `[`thrustForceStamp`](#classgazebo_1_1_thruster_plugin_1afc2f42b3a4d4dfe1d59bdb06a15bf8e7) | Time stamp of latest thrust force.
`protected physics::JointPtr `[`joint`](#classgazebo_1_1_thruster_plugin_1a5df1a3ae7ee6363498bf3221d7c70f93) | Optional: The rotor joint, used for visualization.
`protected double `[`clampMin`](#classgazebo_1_1_thruster_plugin_1ab2e98f8b4a89488d0455d7d57b84ec52) | : Optional: Commands less than this value will be clamped.
`protected double `[`clampMax`](#classgazebo_1_1_thruster_plugin_1a58ee9e27895d9921cc40cd0c64aa086d) | : Optional: Commands greater than this value will be clamped.
`protected double `[`thrustMin`](#classgazebo_1_1_thruster_plugin_1aad3011318655f542756926e0633de05e) | : Optional: Minimum thrust force output
`protected double `[`thrustMax`](#classgazebo_1_1_thruster_plugin_1a7730c8c0b69432591ab15e42f4deef35) | : Optional: Maximum thrust force output
`protected int `[`thrusterID`](#classgazebo_1_1_thruster_plugin_1a2e6fb5eaaa297788fabb51bd8dc578e3) | Thruster ID, used to generated topic names automatically.
`protected std::string `[`topicPrefix`](#classgazebo_1_1_thruster_plugin_1acde9d0318e86dfbc9e6e2af723ea9c3b) | Thruster topics prefix.
`protected double `[`gain`](#classgazebo_1_1_thruster_plugin_1a76067d3ea096103f7d6f3f43106e0e23) | : Optional: Gain factor: Desired angular velocity = command * gain
`protected bool `[`isOn`](#classgazebo_1_1_thruster_plugin_1a86031b28be7600d3eedaecf3d11a9ea5) | Optional: Flag to indicate if the thruster is turned on or off.
`protected double `[`thrustEfficiency`](#classgazebo_1_1_thruster_plugin_1a36d3369e6481b21d8450c012b21ea7a7) | Optional: Output thrust efficiency factor of the thruster.
`protected double `[`propellerEfficiency`](#classgazebo_1_1_thruster_plugin_1a0e8f044924d12715aba76aa95555641d) | Optional: Propeller angular velocity efficiency term.
`protected ignition::math::Vector3d `[`thrusterAxis`](#classgazebo_1_1_thruster_plugin_1a961eff0b01402bf7a56117a35e064b06) | The axis about which the thruster rotates.
`protected void `[`UpdateInput`](#classgazebo_1_1_thruster_plugin_1a8ede5b7013c52fd890a429f55a0d0c74)`(`[`ConstDoublePtr`](#_fin_plugin_8hh_1adec3148dfa71d908caf33660a62187d4)` & _msg)` | Callback for the input topic subscriber.

## Members

#### `public  `[`ThrusterPlugin`](#classgazebo_1_1_thruster_plugin_1a6b5841ff33686cc450313e03cf294d9c)`()` 

Constructor.

#### `public virtual  `[`~ThrusterPlugin`](#classgazebo_1_1_thruster_plugin_1a06d1a5a37d484a2ce88329fd2fed8f59)`()` 

Destructor.

#### `public virtual void `[`Load`](#classgazebo_1_1_thruster_plugin_1a1b4f788380387681886f65531ceb0f25)`(physics::ModelPtr _model,sdf::ElementPtr _sdf)` 

#### `public virtual void `[`Init`](#classgazebo_1_1_thruster_plugin_1a976abc5ac54372004630800a7d83aa8e)`()` 

#### `public virtual void `[`Reset`](#classgazebo_1_1_thruster_plugin_1a3a445ef9af6ff415eb3d2e319c232841)`()` 

Custom plugin reset behavior.

#### `public void `[`Update`](#classgazebo_1_1_thruster_plugin_1a4cd1505e012721530e09cc346500ff12)`(const common::UpdateInfo & _info)` 

Update the simulation state.

#### Parameters
* `_info` Information used in the update event.

#### `protected std::shared_ptr< `[`Dynamics`](#classgazebo_1_1_dynamics)` > `[`thrusterDynamics`](#classgazebo_1_1_thruster_plugin_1a2a5bdae0148178c1688362257e59dbfa) 

Thruster dynamic model.

#### `protected std::shared_ptr< `[`ConversionFunction`](#classgazebo_1_1_conversion_function)` > `[`conversionFunction`](#classgazebo_1_1_thruster_plugin_1aab369c9f214021b0e3372dd61907c257) 

Thruster conversion function.

#### `protected event::ConnectionPtr `[`updateConnection`](#classgazebo_1_1_thruster_plugin_1a23c4d67fd108db7dabc2727244934a30) 

Update event.

#### `protected physics::LinkPtr `[`thrusterLink`](#classgazebo_1_1_thruster_plugin_1a141de7a7aedb56861b9046ee7897399f) 

Pointer to the thruster link.

#### `protected transport::NodePtr `[`node`](#classgazebo_1_1_thruster_plugin_1afedb1c79f0a9c060cd4bc6c1ef541b68) 

Gazebo node.

#### `protected transport::SubscriberPtr `[`commandSubscriber`](#classgazebo_1_1_thruster_plugin_1ae4054a7444082b7f0195b3cf72bfad6f) 

Subscriber to the reference signal topic.

#### `protected transport::PublisherPtr `[`thrustTopicPublisher`](#classgazebo_1_1_thruster_plugin_1a8ad82769e76b0844a87763446f03a267) 

Publisher to the output thrust topic.

#### `protected double `[`inputCommand`](#classgazebo_1_1_thruster_plugin_1a617d0e909a0d82397d95954c8c103035) 

Input command, typically desired angular velocity of the rotor.

#### `protected double `[`thrustForce`](#classgazebo_1_1_thruster_plugin_1a3dd6123930d825ae14ca56b253b9c8a2) 

Latest thrust force in [N].

#### `protected common::Time `[`thrustForceStamp`](#classgazebo_1_1_thruster_plugin_1afc2f42b3a4d4dfe1d59bdb06a15bf8e7) 

Time stamp of latest thrust force.

#### `protected physics::JointPtr `[`joint`](#classgazebo_1_1_thruster_plugin_1a5df1a3ae7ee6363498bf3221d7c70f93) 

Optional: The rotor joint, used for visualization.

#### `protected double `[`clampMin`](#classgazebo_1_1_thruster_plugin_1ab2e98f8b4a89488d0455d7d57b84ec52) 

: Optional: Commands less than this value will be clamped.

#### `protected double `[`clampMax`](#classgazebo_1_1_thruster_plugin_1a58ee9e27895d9921cc40cd0c64aa086d) 

: Optional: Commands greater than this value will be clamped.

#### `protected double `[`thrustMin`](#classgazebo_1_1_thruster_plugin_1aad3011318655f542756926e0633de05e) 

: Optional: Minimum thrust force output

#### `protected double `[`thrustMax`](#classgazebo_1_1_thruster_plugin_1a7730c8c0b69432591ab15e42f4deef35) 

: Optional: Maximum thrust force output

#### `protected int `[`thrusterID`](#classgazebo_1_1_thruster_plugin_1a2e6fb5eaaa297788fabb51bd8dc578e3) 

Thruster ID, used to generated topic names automatically.

#### `protected std::string `[`topicPrefix`](#classgazebo_1_1_thruster_plugin_1acde9d0318e86dfbc9e6e2af723ea9c3b) 

Thruster topics prefix.

#### `protected double `[`gain`](#classgazebo_1_1_thruster_plugin_1a76067d3ea096103f7d6f3f43106e0e23) 

: Optional: Gain factor: Desired angular velocity = command * gain

#### `protected bool `[`isOn`](#classgazebo_1_1_thruster_plugin_1a86031b28be7600d3eedaecf3d11a9ea5) 

Optional: Flag to indicate if the thruster is turned on or off.

#### `protected double `[`thrustEfficiency`](#classgazebo_1_1_thruster_plugin_1a36d3369e6481b21d8450c012b21ea7a7) 

Optional: Output thrust efficiency factor of the thruster.

#### `protected double `[`propellerEfficiency`](#classgazebo_1_1_thruster_plugin_1a0e8f044924d12715aba76aa95555641d) 

Optional: Propeller angular velocity efficiency term.

#### `protected ignition::math::Vector3d `[`thrusterAxis`](#classgazebo_1_1_thruster_plugin_1a961eff0b01402bf7a56117a35e064b06) 

The axis about which the thruster rotates.

#### `protected void `[`UpdateInput`](#classgazebo_1_1_thruster_plugin_1a8ede5b7013c52fd890a429f55a0d0c74)`(`[`ConstDoublePtr`](#_fin_plugin_8hh_1adec3148dfa71d908caf33660a62187d4)` & _msg)` 

Callback for the input topic subscriber.

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

# class `gazebo::UmbilicalModelBerg` 

```
class gazebo::UmbilicalModelBerg
  : public gazebo::UmbilicalModel
```  

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public virtual void `[`OnUpdate`](#classgazebo_1_1_umbilical_model_berg_1a192a711adeb0f052eb0b07d67b4629f4)`(const common::UpdateInfo & _info,const ignition::math::Vector3d & _flow)` | Update Umbilical (and apply forces)
`protected  `[`UmbilicalModelBerg`](#classgazebo_1_1_umbilical_model_berg_1a3f1ce2888fe8ef1fa0da035c97926b48)`(sdf::ElementPtr _sdf,physics::ModelPtr _model)` | Protected constructor: Use the factory instead.

## Members

#### `public virtual void `[`OnUpdate`](#classgazebo_1_1_umbilical_model_berg_1a192a711adeb0f052eb0b07d67b4629f4)`(const common::UpdateInfo & _info,const ignition::math::Vector3d & _flow)` 

Update Umbilical (and apply forces)

#### `protected  `[`UmbilicalModelBerg`](#classgazebo_1_1_umbilical_model_berg_1a3f1ce2888fe8ef1fa0da035c97926b48)`(sdf::ElementPtr _sdf,physics::ModelPtr _model)` 

Protected constructor: Use the factory instead.

# class `gazebo::UmbilicalModelFactory` 

Factory singleton class that creates an [UmbilicalModel](#classgazebo_1_1_umbilical_model) from sdf.

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public `[`UmbilicalModel`](#classgazebo_1_1_umbilical_model)` * `[`CreateUmbilicalModel`](#classgazebo_1_1_umbilical_model_factory_1ac7a7245f47500ee02e68f84c5e7a5032)`(sdf::ElementPtr _sdf,physics::ModelPtr _model)` | Create a [ConversionFunction](#classgazebo_1_1_conversion_function) object according to its sdf Description.
`public bool `[`RegisterCreator`](#classgazebo_1_1_umbilical_model_factory_1a97c20262e741c090c7616f082a23869e)`(const std::string & _identifier,UmbilicalModelCreator _creator)` | Register an [UmbilicalModel](#classgazebo_1_1_umbilical_model) class with its creator.

## Members

#### `public `[`UmbilicalModel`](#classgazebo_1_1_umbilical_model)` * `[`CreateUmbilicalModel`](#classgazebo_1_1_umbilical_model_factory_1ac7a7245f47500ee02e68f84c5e7a5032)`(sdf::ElementPtr _sdf,physics::ModelPtr _model)` 

Create a [ConversionFunction](#classgazebo_1_1_conversion_function) object according to its sdf Description.

#### `public bool `[`RegisterCreator`](#classgazebo_1_1_umbilical_model_factory_1a97c20262e741c090c7616f082a23869e)`(const std::string & _identifier,UmbilicalModelCreator _creator)` 

Register an [UmbilicalModel](#classgazebo_1_1_umbilical_model) class with its creator.

# class `gazebo::UmbilicalPlugin` 

```
class gazebo::UmbilicalPlugin
  : public ModelPlugin
```  

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public  `[`UmbilicalPlugin`](#classgazebo_1_1_umbilical_plugin_1a057f26aba6131c97efcfad72864c1c96)`()` | Destructor.
`public  `[`~UmbilicalPlugin`](#classgazebo_1_1_umbilical_plugin_1afd11fddc7265c89ce53a665688ea4baa)`()` | Constructor.
`protected event::ConnectionPtr `[`updateConnection`](#classgazebo_1_1_umbilical_plugin_1a23741aa2b2775fb58db688c19b338c7f) | Pointer to the update event connection.
`protected gazebo::physics::ModelPtr `[`model`](#classgazebo_1_1_umbilical_plugin_1aa495d0dd46d56e18550dfa30ec6a5ccf) | Pointer to the model structure.
`protected gazebo::physics::WorldPtr `[`world`](#classgazebo_1_1_umbilical_plugin_1a9299893f7d97eb66ee07fb725ca165d4) | Pointer to the world plugin.
`protected gazebo::transport::NodePtr `[`node`](#classgazebo_1_1_umbilical_plugin_1a552cee3d43b51eb33048ad88120bf879) | Gazebo node.
`protected gazebo::transport::SubscriberPtr `[`flowSubscriber`](#classgazebo_1_1_umbilical_plugin_1a5f7d8aee1c7f91bcfdc680484a60b4db) | Subcriber to flow message.
`protected ignition::math::Vector3d `[`flowVelocity`](#classgazebo_1_1_umbilical_plugin_1a6b65710780f67008b0b167840d19d781) | Flow velocity vector read from topic.
`protected std::shared_ptr< `[`UmbilicalModel`](#classgazebo_1_1_umbilical_model)` > `[`umbilical`](#classgazebo_1_1_umbilical_plugin_1a02c19fdf4ddac48e3a46b5e72522c938) | Pointer to [UmbilicalModel](#classgazebo_1_1_umbilical_model) used in this plugin.
`protected virtual void `[`Load`](#classgazebo_1_1_umbilical_plugin_1af44b8802650eb0c0d9842558db614914)`(physics::ModelPtr _model,sdf::ElementPtr _sdf)` | Load plugin and its configuration from sdf.
`protected virtual void `[`OnUpdate`](#classgazebo_1_1_umbilical_plugin_1a27b0bf9ff8f9face03db37b7882e9195)`(const common::UpdateInfo &)` | Update callback from simulation.
`protected void `[`UpdateFlowVelocity`](#classgazebo_1_1_umbilical_plugin_1aafce9f28f1b7438e2585c9d5fe5d434c)`(ConstVector3dPtr & _msg)` | Reads flow velocity topic.

## Members

#### `public  `[`UmbilicalPlugin`](#classgazebo_1_1_umbilical_plugin_1a057f26aba6131c97efcfad72864c1c96)`()` 

Destructor.

#### `public  `[`~UmbilicalPlugin`](#classgazebo_1_1_umbilical_plugin_1afd11fddc7265c89ce53a665688ea4baa)`()` 

Constructor.

#### `protected event::ConnectionPtr `[`updateConnection`](#classgazebo_1_1_umbilical_plugin_1a23741aa2b2775fb58db688c19b338c7f) 

Pointer to the update event connection.

#### `protected gazebo::physics::ModelPtr `[`model`](#classgazebo_1_1_umbilical_plugin_1aa495d0dd46d56e18550dfa30ec6a5ccf) 

Pointer to the model structure.

#### `protected gazebo::physics::WorldPtr `[`world`](#classgazebo_1_1_umbilical_plugin_1a9299893f7d97eb66ee07fb725ca165d4) 

Pointer to the world plugin.

#### `protected gazebo::transport::NodePtr `[`node`](#classgazebo_1_1_umbilical_plugin_1a552cee3d43b51eb33048ad88120bf879) 

Gazebo node.

#### `protected gazebo::transport::SubscriberPtr `[`flowSubscriber`](#classgazebo_1_1_umbilical_plugin_1a5f7d8aee1c7f91bcfdc680484a60b4db) 

Subcriber to flow message.

#### `protected ignition::math::Vector3d `[`flowVelocity`](#classgazebo_1_1_umbilical_plugin_1a6b65710780f67008b0b167840d19d781) 

Flow velocity vector read from topic.

#### `protected std::shared_ptr< `[`UmbilicalModel`](#classgazebo_1_1_umbilical_model)` > `[`umbilical`](#classgazebo_1_1_umbilical_plugin_1a02c19fdf4ddac48e3a46b5e72522c938) 

Pointer to [UmbilicalModel](#classgazebo_1_1_umbilical_model) used in this plugin.

#### `protected virtual void `[`Load`](#classgazebo_1_1_umbilical_plugin_1af44b8802650eb0c0d9842558db614914)`(physics::ModelPtr _model,sdf::ElementPtr _sdf)` 

Load plugin and its configuration from sdf.

#### `protected virtual void `[`OnUpdate`](#classgazebo_1_1_umbilical_plugin_1a27b0bf9ff8f9face03db37b7882e9195)`(const common::UpdateInfo &)` 

Update callback from simulation.

#### `protected void `[`UpdateFlowVelocity`](#classgazebo_1_1_umbilical_plugin_1aafce9f28f1b7438e2585c9d5fe5d434c)`(ConstVector3dPtr & _msg)` 

Reads flow velocity topic.

# class `gazebo::UmbilicalSegment` 

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public physics::LinkPtr `[`link`](#classgazebo_1_1_umbilical_segment_1a963afcbc43ee1488b5445ad365a4ccab) | 
`public physics::LinkPtr `[`linkA`](#classgazebo_1_1_umbilical_segment_1a2393822c7d09df752db6760e969ce384) | 
`public physics::JointPtr `[`jointA`](#classgazebo_1_1_umbilical_segment_1a4bd1470650660e46276958afa6da098e) | 
`public physics::JointPtr `[`jointB`](#classgazebo_1_1_umbilical_segment_1a9eeb348f8684ccd14ada13447584fb15) | 
`public std::shared_ptr< `[`UmbilicalSegment`](#classgazebo_1_1_umbilical_segment)` > `[`prev`](#classgazebo_1_1_umbilical_segment_1ac5f9bc503bb4ffb2d2e055e542ad0d6a) | 
`public std::shared_ptr< `[`UmbilicalSegment`](#classgazebo_1_1_umbilical_segment)` > `[`next`](#classgazebo_1_1_umbilical_segment_1ae1d881262117ee5c620ec6792b955582) | 
`public inline  `[`UmbilicalSegment`](#classgazebo_1_1_umbilical_segment_1acd1d7bf99c3c1b4b2778bfc82383d139)`()` | 
`public  `[`UmbilicalSegment`](#classgazebo_1_1_umbilical_segment_1a166887767ceae016d2dc9653079f22c5)`(const std::string & _name,const std::string & _fromLink,const ignition::math::Pose3d & _fromPose,const ignition::math::Pose3d & _toPose,physics::ModelPtr _model)` | 
`public void `[`initSdfSegment`](#classgazebo_1_1_umbilical_segment_1a12a42cd56d35a6534e7f9e8fafcf2414)`()` | 

## Members

#### `public physics::LinkPtr `[`link`](#classgazebo_1_1_umbilical_segment_1a963afcbc43ee1488b5445ad365a4ccab) 

#### `public physics::LinkPtr `[`linkA`](#classgazebo_1_1_umbilical_segment_1a2393822c7d09df752db6760e969ce384) 

#### `public physics::JointPtr `[`jointA`](#classgazebo_1_1_umbilical_segment_1a4bd1470650660e46276958afa6da098e) 

#### `public physics::JointPtr `[`jointB`](#classgazebo_1_1_umbilical_segment_1a9eeb348f8684ccd14ada13447584fb15) 

#### `public std::shared_ptr< `[`UmbilicalSegment`](#classgazebo_1_1_umbilical_segment)` > `[`prev`](#classgazebo_1_1_umbilical_segment_1ac5f9bc503bb4ffb2d2e055e542ad0d6a) 

#### `public std::shared_ptr< `[`UmbilicalSegment`](#classgazebo_1_1_umbilical_segment)` > `[`next`](#classgazebo_1_1_umbilical_segment_1ae1d881262117ee5c620ec6792b955582) 

#### `public inline  `[`UmbilicalSegment`](#classgazebo_1_1_umbilical_segment_1acd1d7bf99c3c1b4b2778bfc82383d139)`()` 

#### `public  `[`UmbilicalSegment`](#classgazebo_1_1_umbilical_segment_1a166887767ceae016d2dc9653079f22c5)`(const std::string & _name,const std::string & _fromLink,const ignition::math::Pose3d & _fromPose,const ignition::math::Pose3d & _toPose,physics::ModelPtr _model)` 

#### `public void `[`initSdfSegment`](#classgazebo_1_1_umbilical_segment_1a12a42cd56d35a6534e7f9e8fafcf2414)`()` 

# class `gazebo::UnderwaterObjectPlugin` 

```
class gazebo::UnderwaterObjectPlugin
  : public ModelPlugin
```  

Gazebo model plugin class for underwater objects.

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public  `[`UnderwaterObjectPlugin`](#classgazebo_1_1_underwater_object_plugin_1ac875088ebde0583e6f3e07cdeaea53ae)`()` | Constructor.
`public virtual  `[`~UnderwaterObjectPlugin`](#classgazebo_1_1_underwater_object_plugin_1af97f83bac0327ebc2671839c56f44207)`()` | Destructor.
`public virtual void `[`Load`](#classgazebo_1_1_underwater_object_plugin_1acaa3bd6b66429cb588fbcba3ae70be74)`(gazebo::physics::ModelPtr _model,sdf::ElementPtr _sdf)` | 
`public virtual void `[`Init`](#classgazebo_1_1_underwater_object_plugin_1afbe0672e704e832adf5619fd7c34cd5c)`()` | 
`public virtual void `[`Update`](#classgazebo_1_1_underwater_object_plugin_1ad5893829b75bed2bb052bef467d6dcf4)`(const gazebo::common::UpdateInfo & _info)` | Update the simulation state.
`protected std::map< gazebo::physics::LinkPtr, `[`HydrodynamicModelPtr`](#_hydrodynamic_model_8hh_1ab7e72448c3e86f93ab214d73c0cd4414)` > `[`models`](#classgazebo_1_1_underwater_object_plugin_1abbc883398252e410563c657648743e3e) | Pairs of links & corresponding hydrodynamic models.
`protected ignition::math::Vector3d `[`flowVelocity`](#classgazebo_1_1_underwater_object_plugin_1ac5bf6578ef4434438ba7d7647b69b971) | Flow velocity vector read from topic.
`protected gazebo::event::ConnectionPtr `[`updateConnection`](#classgazebo_1_1_underwater_object_plugin_1a1a4d81782ad2d21fc01598e0d9b42d27) | Update event.
`protected gazebo::physics::WorldPtr `[`world`](#classgazebo_1_1_underwater_object_plugin_1a9f16fc2908d17c0975331cc825d14cb0) | Pointer to the world plugin.
`protected gazebo::physics::ModelPtr `[`model`](#classgazebo_1_1_underwater_object_plugin_1a896d92ed527a0d9f7b47208614eaba0c) | Pointer to the model structure.
`protected gazebo::transport::NodePtr `[`node`](#classgazebo_1_1_underwater_object_plugin_1a5422d922731696d2767e5be09c2cb5c2) | Gazebo node.
`protected std::string `[`baseLinkName`](#classgazebo_1_1_underwater_object_plugin_1a08b0e6dfab6a63945ea6d1c71c858df1) | Name of vehicle's base_link.
`protected gazebo::transport::SubscriberPtr `[`flowSubscriber`](#classgazebo_1_1_underwater_object_plugin_1adb22008a9f57f11659e2b2a18d57bcc6) | Subcriber to flow message.
`protected bool `[`useGlobalCurrent`](#classgazebo_1_1_underwater_object_plugin_1a0bfd19ce74a42666f26fefa0ded488f3) | Flag to use the global current velocity or the individually assigned current velocity.
`protected std::map< std::string, gazebo::transport::PublisherPtr > `[`hydroPub`](#classgazebo_1_1_underwater_object_plugin_1a33989646c81bc47fe86dae3052846ea2) | Publishers of hydrodynamic and hydrostatic forces and torques in the case the debug flag is on.
`protected virtual void `[`Connect`](#classgazebo_1_1_underwater_object_plugin_1a7497acca39dc0a4f338bd863b002ec33)`()` | Connects the update event callback.
`protected void `[`UpdateFlowVelocity`](#classgazebo_1_1_underwater_object_plugin_1a22bb6d230cc76b4a838ffffe5a6ba722)`(ConstVector3dPtr & _msg)` | Reads flow velocity topic.
`protected virtual void `[`PublishCurrentVelocityMarker`](#classgazebo_1_1_underwater_object_plugin_1a89d8430bc839e0ff477fd893be829060)`()` | Publish current velocity marker.
`protected virtual void `[`PublishIsSubmerged`](#classgazebo_1_1_underwater_object_plugin_1adc2e3f16a6fa8ce79497b5664fb66b82)`()` | Publishes the state of the vehicle (is submerged)
`protected virtual void `[`PublishRestoringForce`](#classgazebo_1_1_underwater_object_plugin_1ae5da81b93706dded6de765628f57ad05)`(gazebo::physics::LinkPtr _link)` | Publish restoring force.
`protected virtual void `[`PublishHydrodynamicWrenches`](#classgazebo_1_1_underwater_object_plugin_1af1b5370bf8ebd626fd9eafb2b46075b9)`(gazebo::physics::LinkPtr _link)` | Publish hydrodynamic wrenches.
`protected virtual void `[`GenWrenchMsg`](#classgazebo_1_1_underwater_object_plugin_1a6deb4663c719f288b671539020257bb0)`(ignition::math::Vector3d _force,ignition::math::Vector3d _torque,gazebo::msgs::WrenchStamped & _output)` | Returns the wrench message for debugging topics.
`protected virtual void `[`InitDebug`](#classgazebo_1_1_underwater_object_plugin_1a86136f608b56ecd79bd6530f92724a75)`(gazebo::physics::LinkPtr _link,`[`gazebo::HydrodynamicModelPtr`](#_hydrodynamic_model_8hh_1ab7e72448c3e86f93ab214d73c0cd4414)` _hydro)` | Sets the topics used for publishing the intermediate data during the simulation.

## Members

#### `public  `[`UnderwaterObjectPlugin`](#classgazebo_1_1_underwater_object_plugin_1ac875088ebde0583e6f3e07cdeaea53ae)`()` 

Constructor.

#### `public virtual  `[`~UnderwaterObjectPlugin`](#classgazebo_1_1_underwater_object_plugin_1af97f83bac0327ebc2671839c56f44207)`()` 

Destructor.

#### `public virtual void `[`Load`](#classgazebo_1_1_underwater_object_plugin_1acaa3bd6b66429cb588fbcba3ae70be74)`(gazebo::physics::ModelPtr _model,sdf::ElementPtr _sdf)` 

#### `public virtual void `[`Init`](#classgazebo_1_1_underwater_object_plugin_1afbe0672e704e832adf5619fd7c34cd5c)`()` 

#### `public virtual void `[`Update`](#classgazebo_1_1_underwater_object_plugin_1ad5893829b75bed2bb052bef467d6dcf4)`(const gazebo::common::UpdateInfo & _info)` 

Update the simulation state.

#### Parameters
* `_info` Information used in the update event.

#### `protected std::map< gazebo::physics::LinkPtr, `[`HydrodynamicModelPtr`](#_hydrodynamic_model_8hh_1ab7e72448c3e86f93ab214d73c0cd4414)` > `[`models`](#classgazebo_1_1_underwater_object_plugin_1abbc883398252e410563c657648743e3e) 

Pairs of links & corresponding hydrodynamic models.

#### `protected ignition::math::Vector3d `[`flowVelocity`](#classgazebo_1_1_underwater_object_plugin_1ac5bf6578ef4434438ba7d7647b69b971) 

Flow velocity vector read from topic.

#### `protected gazebo::event::ConnectionPtr `[`updateConnection`](#classgazebo_1_1_underwater_object_plugin_1a1a4d81782ad2d21fc01598e0d9b42d27) 

Update event.

#### `protected gazebo::physics::WorldPtr `[`world`](#classgazebo_1_1_underwater_object_plugin_1a9f16fc2908d17c0975331cc825d14cb0) 

Pointer to the world plugin.

#### `protected gazebo::physics::ModelPtr `[`model`](#classgazebo_1_1_underwater_object_plugin_1a896d92ed527a0d9f7b47208614eaba0c) 

Pointer to the model structure.

#### `protected gazebo::transport::NodePtr `[`node`](#classgazebo_1_1_underwater_object_plugin_1a5422d922731696d2767e5be09c2cb5c2) 

Gazebo node.

#### `protected std::string `[`baseLinkName`](#classgazebo_1_1_underwater_object_plugin_1a08b0e6dfab6a63945ea6d1c71c858df1) 

Name of vehicle's base_link.

#### `protected gazebo::transport::SubscriberPtr `[`flowSubscriber`](#classgazebo_1_1_underwater_object_plugin_1adb22008a9f57f11659e2b2a18d57bcc6) 

Subcriber to flow message.

#### `protected bool `[`useGlobalCurrent`](#classgazebo_1_1_underwater_object_plugin_1a0bfd19ce74a42666f26fefa0ded488f3) 

Flag to use the global current velocity or the individually assigned current velocity.

#### `protected std::map< std::string, gazebo::transport::PublisherPtr > `[`hydroPub`](#classgazebo_1_1_underwater_object_plugin_1a33989646c81bc47fe86dae3052846ea2) 

Publishers of hydrodynamic and hydrostatic forces and torques in the case the debug flag is on.

#### `protected virtual void `[`Connect`](#classgazebo_1_1_underwater_object_plugin_1a7497acca39dc0a4f338bd863b002ec33)`()` 

Connects the update event callback.

#### `protected void `[`UpdateFlowVelocity`](#classgazebo_1_1_underwater_object_plugin_1a22bb6d230cc76b4a838ffffe5a6ba722)`(ConstVector3dPtr & _msg)` 

Reads flow velocity topic.

#### `protected virtual void `[`PublishCurrentVelocityMarker`](#classgazebo_1_1_underwater_object_plugin_1a89d8430bc839e0ff477fd893be829060)`()` 

Publish current velocity marker.

#### `protected virtual void `[`PublishIsSubmerged`](#classgazebo_1_1_underwater_object_plugin_1adc2e3f16a6fa8ce79497b5664fb66b82)`()` 

Publishes the state of the vehicle (is submerged)

#### `protected virtual void `[`PublishRestoringForce`](#classgazebo_1_1_underwater_object_plugin_1ae5da81b93706dded6de765628f57ad05)`(gazebo::physics::LinkPtr _link)` 

Publish restoring force.

#### Parameters
* `_link` Pointer to the link where the force information will be extracted from

#### `protected virtual void `[`PublishHydrodynamicWrenches`](#classgazebo_1_1_underwater_object_plugin_1af1b5370bf8ebd626fd9eafb2b46075b9)`(gazebo::physics::LinkPtr _link)` 

Publish hydrodynamic wrenches.

#### Parameters
* `_link` Pointer to the link where the force information will be extracted from

#### `protected virtual void `[`GenWrenchMsg`](#classgazebo_1_1_underwater_object_plugin_1a6deb4663c719f288b671539020257bb0)`(ignition::math::Vector3d _force,ignition::math::Vector3d _torque,gazebo::msgs::WrenchStamped & _output)` 

Returns the wrench message for debugging topics.

#### Parameters
* `_force` Force vector 

* `_torque` Torque vector 

* `_output` Stamped wrench message to be updated

#### `protected virtual void `[`InitDebug`](#classgazebo_1_1_underwater_object_plugin_1a86136f608b56ecd79bd6530f92724a75)`(gazebo::physics::LinkPtr _link,`[`gazebo::HydrodynamicModelPtr`](#_hydrodynamic_model_8hh_1ab7e72448c3e86f93ab214d73c0cd4414)` _hydro)` 

Sets the topics used for publishing the intermediate data during the simulation.

#### Parameters
* `_link` Pointer to the link 

* `_hydro` Pointer to the hydrodynamic model

Generated by [Moxygen](https://sourcey.com/moxygen)