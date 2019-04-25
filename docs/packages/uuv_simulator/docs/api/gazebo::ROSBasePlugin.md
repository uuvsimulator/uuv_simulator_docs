# class `gazebo::ROSBasePlugin` 

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public  `[`ROSBasePlugin`](#classgazebo_1_1_r_o_s_base_plugin_1a0435db27811265bd28476844b1aebb7d)`()` | Class constructor.
`public virtual  `[`~ROSBasePlugin`](#classgazebo_1_1_r_o_s_base_plugin_1a085d18e1e808fae36b6bf3dce476c7e5)`()` | Class destructor.
`public bool `[`InitBasePlugin`](#classgazebo_1_1_r_o_s_base_plugin_1a74ff905293eb8caa7becbc5404a97fc6)`(sdf::ElementPtr _sdf)` | Initialize base plugin.
`public bool `[`OnUpdate`](#classgazebo_1_1_r_o_s_base_plugin_1a02aa79b255cb8f0847998f774cb03b32)`(const common::UpdateInfo &)` | Update callback from simulation.
`public bool `[`AddNoiseModel`](#classgazebo_1_1_r_o_s_base_plugin_1abd97192b9712ae6a05d41d158c05f57a)`(std::string _name,double _sigma)` | Add noise normal distribution to the list.
`protected std::string `[`robotNamespace`](#classgazebo_1_1_r_o_s_base_plugin_1a9a9e059aec0a41dd012223d3ea3c9fe9) | Robot namespace.
`protected std::string `[`sensorOutputTopic`](#classgazebo_1_1_r_o_s_base_plugin_1a818f107bc9e165a3cc8016fd6859f86a) | Name of the sensor's output topic.
`protected physics::WorldPtr `[`world`](#classgazebo_1_1_r_o_s_base_plugin_1a24f910550057c819c246f5c3f74dae5a) | Pointer to the world.
`protected event::ConnectionPtr `[`updateConnection`](#classgazebo_1_1_r_o_s_base_plugin_1a1d7b676bec7c29b2bd021b47ecd32bb5) | Pointer to the update event connection.
`protected common::Time `[`lastMeasurementTime`](#classgazebo_1_1_r_o_s_base_plugin_1ac3798d56f9ea70175d99ab80106b4319) | (Simulation) time when the last sensor measurement was generated.
`protected double `[`updateRate`](#classgazebo_1_1_r_o_s_base_plugin_1adbcb691eba2efdd0156d5422bd1cf03f) | Sensor update rate.
`protected double `[`noiseSigma`](#classgazebo_1_1_r_o_s_base_plugin_1aef76766a171b7b9c0c236ff5987800f9) | Noise standard deviation.
`protected double `[`noiseAmp`](#classgazebo_1_1_r_o_s_base_plugin_1a6a7695e4dc91f9504a3ee88d5da94102) | Noise amplitude.
`protected bool `[`gazeboMsgEnabled`](#classgazebo_1_1_r_o_s_base_plugin_1a03fadaa69a0c77dc81153d5059c2cfb4) | Flag set to true if the Gazebo sensors messages are supposed to be published as well (it can avoid unnecessary overhead in case) the sensor messages needed are only ROS messages.
`protected std::default_random_engine `[`rndGen`](#classgazebo_1_1_r_o_s_base_plugin_1ac9f7d735298e4c0017e34ff652295fd3) | Pseudo random number generator.
`protected std::map< std::string, std::normal_distribution< double > > `[`noiseModels`](#classgazebo_1_1_r_o_s_base_plugin_1aec1fe60d8e12867115754d7f89689da2) | Normal distribution describing the noise models.
`protected std_msgs::Bool `[`isOn`](#classgazebo_1_1_r_o_s_base_plugin_1a217d66ec1fe4002468300e0c409bfb32) | Flag to control the generation of output messages.
`protected boost::shared_ptr< ros::NodeHandle > `[`rosNode`](#classgazebo_1_1_r_o_s_base_plugin_1a6b907bcd7669d3907f3c78e654fcca88) | ROS node handle for communication with ROS.
`protected transport::NodePtr `[`gazeboNode`](#classgazebo_1_1_r_o_s_base_plugin_1a6444bffce26cd7c1d31ab1b3abd990c7) | Gazebo's node handle for transporting measurement messages.
`protected ros::Publisher `[`rosSensorOutputPub`](#classgazebo_1_1_r_o_s_base_plugin_1aff7eafda5f899aa2304a870d1418a300) | Gazebo's publisher for transporting measurement messages.
`protected transport::PublisherPtr `[`gazeboSensorOutputPub`](#classgazebo_1_1_r_o_s_base_plugin_1a00461d61554c0a38b03892488a43eefb) | Gazebo's publisher for transporting measurement messages.
`protected ros::ServiceServer `[`changeSensorSrv`](#classgazebo_1_1_r_o_s_base_plugin_1a4a9b8a250d6c0c4e8148fa96c8dcc395) | Service server object.
`protected ros::Publisher `[`pluginStatePub`](#classgazebo_1_1_r_o_s_base_plugin_1a0a405302b38096d97a25c18879de03ee) | ROS publisher for the switchable sensor data.
`protected ignition::math::Pose3d `[`referenceFrame`](#classgazebo_1_1_r_o_s_base_plugin_1aa788862de11b763facdf51ac105c535d) | Pose of the reference frame wrt world frame.
`protected ros::Subscriber `[`tfStaticSub`](#classgazebo_1_1_r_o_s_base_plugin_1a0d5b3d85ee84ddd0e722a4e1dbd83d83) | ROS subscriber for the TF static reference frame.
`protected std::string `[`referenceFrameID`](#classgazebo_1_1_r_o_s_base_plugin_1a02ca6231d0a2961fe6a63002de9a5ad4) | Frame ID of the reference frame.
`protected bool `[`isReferenceInit`](#classgazebo_1_1_r_o_s_base_plugin_1a9004a71899294df66fe56bd6adcc187c) | Flag set to true if reference frame initialized.
`protected physics::LinkPtr `[`referenceLink`](#classgazebo_1_1_r_o_s_base_plugin_1a34ff72f4617839866a593d0c1a00f375) | Reference link.
`protected bool `[`IsOn`](#classgazebo_1_1_r_o_s_base_plugin_1a8c02e25afa29c264aa3a262b277a3723)`()` | Returns true if the plugin is activated.
`protected void `[`PublishState`](#classgazebo_1_1_r_o_s_base_plugin_1a0185c958f2ce8b30a1c5dc078bbd7b0e)`()` | Publish the current state of the plugin.
`protected bool `[`ChangeSensorState`](#classgazebo_1_1_r_o_s_base_plugin_1a47e246ab8e3e9fe1b7f032ee7bd8af16)`(uuv_sensor_ros_plugins_msgs::ChangeSensorState::Request & _req,uuv_sensor_ros_plugins_msgs::ChangeSensorState::Response & _res)` | Change sensor state (ON/OFF)
`protected void `[`GetTFMessage`](#classgazebo_1_1_r_o_s_base_plugin_1a465f66f7ecad8aa9e0f9e7d5fd0159d9)`(const tf::tfMessage::ConstPtr & _msg)` | Callback function for the static TF message.
`protected double `[`GetGaussianNoise`](#classgazebo_1_1_r_o_s_base_plugin_1ae1fd5e5059943e83865efa837e52e3a7)`(double _amp)` | Returns noise value for a function with zero mean from the default Gaussian noise model.
`protected double `[`GetGaussianNoise`](#classgazebo_1_1_r_o_s_base_plugin_1a69d2da0f2848ba0153756afbb331e447)`(std::string _name,double _amp)` | Returns noise value for a function with zero mean from a Gaussian noise model according to the model name.
`protected bool `[`EnableMeasurement`](#classgazebo_1_1_r_o_s_base_plugin_1af12a92a0ddf7c3c07163d32d6d95c655)`(const common::UpdateInfo & _info) const` | Enables generation of simulated measurement if the timeout since the last update has been reached.
`protected void `[`UpdateReferenceFramePose`](#classgazebo_1_1_r_o_s_base_plugin_1a768035af5fb258d9c07c4d7fd5049700)`()` | Updates the pose of the reference frame wrt the world frame.

## Members

#### `public  `[`ROSBasePlugin`](#classgazebo_1_1_r_o_s_base_plugin_1a0435db27811265bd28476844b1aebb7d)`()` 

Class constructor.

#### `public virtual  `[`~ROSBasePlugin`](#classgazebo_1_1_r_o_s_base_plugin_1a085d18e1e808fae36b6bf3dce476c7e5)`()` 

Class destructor.

#### `public bool `[`InitBasePlugin`](#classgazebo_1_1_r_o_s_base_plugin_1a74ff905293eb8caa7becbc5404a97fc6)`(sdf::ElementPtr _sdf)` 

Initialize base plugin.

#### `public bool `[`OnUpdate`](#classgazebo_1_1_r_o_s_base_plugin_1a02aa79b255cb8f0847998f774cb03b32)`(const common::UpdateInfo &)` 

Update callback from simulation.

#### `public bool `[`AddNoiseModel`](#classgazebo_1_1_r_o_s_base_plugin_1abd97192b9712ae6a05d41d158c05f57a)`(std::string _name,double _sigma)` 

Add noise normal distribution to the list.

#### `protected std::string `[`robotNamespace`](#classgazebo_1_1_r_o_s_base_plugin_1a9a9e059aec0a41dd012223d3ea3c9fe9) 

Robot namespace.

#### `protected std::string `[`sensorOutputTopic`](#classgazebo_1_1_r_o_s_base_plugin_1a818f107bc9e165a3cc8016fd6859f86a) 

Name of the sensor's output topic.

#### `protected physics::WorldPtr `[`world`](#classgazebo_1_1_r_o_s_base_plugin_1a24f910550057c819c246f5c3f74dae5a) 

Pointer to the world.

#### `protected event::ConnectionPtr `[`updateConnection`](#classgazebo_1_1_r_o_s_base_plugin_1a1d7b676bec7c29b2bd021b47ecd32bb5) 

Pointer to the update event connection.

#### `protected common::Time `[`lastMeasurementTime`](#classgazebo_1_1_r_o_s_base_plugin_1ac3798d56f9ea70175d99ab80106b4319) 

(Simulation) time when the last sensor measurement was generated.

#### `protected double `[`updateRate`](#classgazebo_1_1_r_o_s_base_plugin_1adbcb691eba2efdd0156d5422bd1cf03f) 

Sensor update rate.

#### `protected double `[`noiseSigma`](#classgazebo_1_1_r_o_s_base_plugin_1aef76766a171b7b9c0c236ff5987800f9) 

Noise standard deviation.

#### `protected double `[`noiseAmp`](#classgazebo_1_1_r_o_s_base_plugin_1a6a7695e4dc91f9504a3ee88d5da94102) 

Noise amplitude.

#### `protected bool `[`gazeboMsgEnabled`](#classgazebo_1_1_r_o_s_base_plugin_1a03fadaa69a0c77dc81153d5059c2cfb4) 

Flag set to true if the Gazebo sensors messages are supposed to be published as well (it can avoid unnecessary overhead in case) the sensor messages needed are only ROS messages.

#### `protected std::default_random_engine `[`rndGen`](#classgazebo_1_1_r_o_s_base_plugin_1ac9f7d735298e4c0017e34ff652295fd3) 

Pseudo random number generator.

#### `protected std::map< std::string, std::normal_distribution< double > > `[`noiseModels`](#classgazebo_1_1_r_o_s_base_plugin_1aec1fe60d8e12867115754d7f89689da2) 

Normal distribution describing the noise models.

#### `protected std_msgs::Bool `[`isOn`](#classgazebo_1_1_r_o_s_base_plugin_1a217d66ec1fe4002468300e0c409bfb32) 

Flag to control the generation of output messages.

#### `protected boost::shared_ptr< ros::NodeHandle > `[`rosNode`](#classgazebo_1_1_r_o_s_base_plugin_1a6b907bcd7669d3907f3c78e654fcca88) 

ROS node handle for communication with ROS.

#### `protected transport::NodePtr `[`gazeboNode`](#classgazebo_1_1_r_o_s_base_plugin_1a6444bffce26cd7c1d31ab1b3abd990c7) 

Gazebo's node handle for transporting measurement messages.

#### `protected ros::Publisher `[`rosSensorOutputPub`](#classgazebo_1_1_r_o_s_base_plugin_1aff7eafda5f899aa2304a870d1418a300) 

Gazebo's publisher for transporting measurement messages.

#### `protected transport::PublisherPtr `[`gazeboSensorOutputPub`](#classgazebo_1_1_r_o_s_base_plugin_1a00461d61554c0a38b03892488a43eefb) 

Gazebo's publisher for transporting measurement messages.

#### `protected ros::ServiceServer `[`changeSensorSrv`](#classgazebo_1_1_r_o_s_base_plugin_1a4a9b8a250d6c0c4e8148fa96c8dcc395) 

Service server object.

#### `protected ros::Publisher `[`pluginStatePub`](#classgazebo_1_1_r_o_s_base_plugin_1a0a405302b38096d97a25c18879de03ee) 

ROS publisher for the switchable sensor data.

#### `protected ignition::math::Pose3d `[`referenceFrame`](#classgazebo_1_1_r_o_s_base_plugin_1aa788862de11b763facdf51ac105c535d) 

Pose of the reference frame wrt world frame.

#### `protected ros::Subscriber `[`tfStaticSub`](#classgazebo_1_1_r_o_s_base_plugin_1a0d5b3d85ee84ddd0e722a4e1dbd83d83) 

ROS subscriber for the TF static reference frame.

#### `protected std::string `[`referenceFrameID`](#classgazebo_1_1_r_o_s_base_plugin_1a02ca6231d0a2961fe6a63002de9a5ad4) 

Frame ID of the reference frame.

#### `protected bool `[`isReferenceInit`](#classgazebo_1_1_r_o_s_base_plugin_1a9004a71899294df66fe56bd6adcc187c) 

Flag set to true if reference frame initialized.

#### `protected physics::LinkPtr `[`referenceLink`](#classgazebo_1_1_r_o_s_base_plugin_1a34ff72f4617839866a593d0c1a00f375) 

Reference link.

#### `protected bool `[`IsOn`](#classgazebo_1_1_r_o_s_base_plugin_1a8c02e25afa29c264aa3a262b277a3723)`()` 

Returns true if the plugin is activated.

#### `protected void `[`PublishState`](#classgazebo_1_1_r_o_s_base_plugin_1a0185c958f2ce8b30a1c5dc078bbd7b0e)`()` 

Publish the current state of the plugin.

#### `protected bool `[`ChangeSensorState`](#classgazebo_1_1_r_o_s_base_plugin_1a47e246ab8e3e9fe1b7f032ee7bd8af16)`(uuv_sensor_ros_plugins_msgs::ChangeSensorState::Request & _req,uuv_sensor_ros_plugins_msgs::ChangeSensorState::Response & _res)` 

Change sensor state (ON/OFF)

#### `protected void `[`GetTFMessage`](#classgazebo_1_1_r_o_s_base_plugin_1a465f66f7ecad8aa9e0f9e7d5fd0159d9)`(const tf::tfMessage::ConstPtr & _msg)` 

Callback function for the static TF message.

#### `protected double `[`GetGaussianNoise`](#classgazebo_1_1_r_o_s_base_plugin_1ae1fd5e5059943e83865efa837e52e3a7)`(double _amp)` 

Returns noise value for a function with zero mean from the default Gaussian noise model.

#### `protected double `[`GetGaussianNoise`](#classgazebo_1_1_r_o_s_base_plugin_1a69d2da0f2848ba0153756afbb331e447)`(std::string _name,double _amp)` 

Returns noise value for a function with zero mean from a Gaussian noise model according to the model name.

#### `protected bool `[`EnableMeasurement`](#classgazebo_1_1_r_o_s_base_plugin_1af12a92a0ddf7c3c07163d32d6d95c655)`(const common::UpdateInfo & _info) const` 

Enables generation of simulated measurement if the timeout since the last update has been reached.

#### `protected void `[`UpdateReferenceFramePose`](#classgazebo_1_1_r_o_s_base_plugin_1a768035af5fb258d9c07c4d7fd5049700)`()` 

Updates the pose of the reference frame wrt the world frame.

