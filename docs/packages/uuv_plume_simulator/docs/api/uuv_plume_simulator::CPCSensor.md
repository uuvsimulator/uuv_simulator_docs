# class `uuv_plume_simulator::CPCSensor` 

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public  `[`CPCSensor`](#classuuv__plume__simulator_1_1_c_p_c_sensor_1a1472cc5596ca8af358a4a2a887c94935)`()` | Class constructor.
`public  `[`~CPCSensor`](#classuuv__plume__simulator_1_1_c_p_c_sensor_1a6c28c6d5b2f1788372ce74be9ac48d31)`()` | Class destructor.
`protected bool `[`updatingCloud`](#classuuv__plume__simulator_1_1_c_p_c_sensor_1a32ace61c89476eb6309a4507936b5257) | Flag to ensure the cloud and measurement update don't coincide.
`protected double `[`gamma`](#classuuv__plume__simulator_1_1_c_p_c_sensor_1a853b8d456c24b321b952359c9a61489b) | Gamma velocity parameter for the smoothing function.
`protected double `[`gain`](#classuuv__plume__simulator_1_1_c_p_c_sensor_1ad676c2b912f8b148b57070cda5b1c384) | Sensor gain.
`protected double `[`smoothingLength`](#classuuv__plume__simulator_1_1_c_p_c_sensor_1a285eb79145cfd715291f808eaac32afb) | Radius of the kernel to identify particles that will be taken into account in the concentration computation.
`protected std::string `[`salinityUnit`](#classuuv__plume__simulator_1_1_c_p_c_sensor_1a1a2bed3e78efa3c7d002d266c775029f) | Salinity unit to be used. Options are.
`protected double `[`saturation`](#classuuv__plume__simulator_1_1_c_p_c_sensor_1a4925a0273447a20a2a45749c2b739bf3) | Sensor saturation.
`protected bool `[`useGeoCoordinates`](#classuuv__plume__simulator_1_1_c_p_c_sensor_1a9f12bbbc0bb4734e3e319fc940b0b0e6) | Flag that will allow storing the geodetic coordinates with the measurement message.
`protected bool `[`publishSalinity`](#classuuv__plume__simulator_1_1_c_p_c_sensor_1ae9007729f28c92ac5d8a11190cdeb8bd) | Flag to activate publishing the simulated salinity.
`protected double `[`referenceSalinityValue`](#classuuv__plume__simulator_1_1_c_p_c_sensor_1a91278f224f4dc69aaa839eb517dd5a46) | Default salinity value for the fluid e.g. sea water.
`protected double `[`plumeSalinityValue`](#classuuv__plume__simulator_1_1_c_p_c_sensor_1a7bbe4a621ed6c6be8d7ee87769c154f6) | Default salinity value for the plume.
`protected bool `[`updateMeasurement`](#classuuv__plume__simulator_1_1_c_p_c_sensor_1a2de0395b9721e726347601543cfcd03d) | Set to true to avoid particle update.
`protected double `[`updateRate`](#classuuv__plume__simulator_1_1_c_p_c_sensor_1a5091b83afd0468f9f9926e19329c33ee) | Output topic's update rate.
`protected std::string `[`sensorFrameID`](#classuuv__plume__simulator_1_1_c_p_c_sensor_1aee44faae4c264c656d8ebd248d2292a4) | Name of the sensor frame.
`protected bool `[`areParticlesInit`](#classuuv__plume__simulator_1_1_c_p_c_sensor_1af7b8775cc7edf1f37b10d2324f002146) | Flag set to true after the first set of plume particles is received.
`protected bool `[`useOdom`](#classuuv__plume__simulator_1_1_c_p_c_sensor_1ab9602b92be015516bb35879f6b1539fe) | Flag set if the sensor position update must be read from the vehicle's odometry input topic.
`protected bool `[`useGPS`](#classuuv__plume__simulator_1_1_c_p_c_sensor_1a42362a4faafe57c53e52930f32d5b757) | Flag set if the sensor position update must be read from the vehicle's GPS topic.
`protected bool `[`useTFUpdate`](#classuuv__plume__simulator_1_1_c_p_c_sensor_1a6e5f2a338e6158a8e65288489d2f43d0) | Flag set if the TF update wrt the sensor frame ID.
`protected geometry_msgs::Vector3 `[`cartPos`](#classuuv__plume__simulator_1_1_c_p_c_sensor_1a624487ac7c4af59a54344608be0e9002) | Measured Cartesian position.
`protected geographic_msgs::GeoPoint `[`geoPos`](#classuuv__plume__simulator_1_1_c_p_c_sensor_1a2eaeb701f45906596c91eb81b0799423) | Measured geodetic position.
`protected ros::Subscriber `[`particlesSub`](#classuuv__plume__simulator_1_1_c_p_c_sensor_1a10ca6338f7e6ed74c814aecd89908df9) | Subscriber for the plume particle point cloud.
`protected ros::Subscriber `[`odometrySub`](#classuuv__plume__simulator_1_1_c_p_c_sensor_1a1113a6a302688220ec6e900897847e08) | Subscriber for odometry topic.
`protected ros::Subscriber `[`gpsSub`](#classuuv__plume__simulator_1_1_c_p_c_sensor_1a22257bbc83b40e7b502e3c423fa25572) | Subscriber to the GPS update topic.
`protected ros::Publisher `[`concentrationPub`](#classuuv__plume__simulator_1_1_c_p_c_sensor_1aeacfcb3e55ddf1da3df33dfd7132dad1) | Output topic for particle concentration.
`protected ros::Publisher `[`salinityPub`](#classuuv__plume__simulator_1_1_c_p_c_sensor_1a606721a0bb469e7c369d166ec7298027) | Output topic for salinity.
`protected std::shared_ptr< ros::NodeHandle > `[`nodeHandle`](#classuuv__plume__simulator_1_1_c_p_c_sensor_1acc3ddc9eda68743989953933a8bdb6dd) | ROS node handle.
`protected tf2_ros::Buffer `[`tfBuffer`](#classuuv__plume__simulator_1_1_c_p_c_sensor_1a2b75335de225523e6ddadaab786c6376) | TF buffer instance.
`protected std::shared_ptr< tf2_ros::TransformListener > `[`tfListener`](#classuuv__plume__simulator_1_1_c_p_c_sensor_1ab6950f90194ecfd62ab0bbd54fd81f7c) | TF listener pointer.
`protected GeographicLib::LocalCartesian `[`projection`](#classuuv__plume__simulator_1_1_c_p_c_sensor_1ae9c6808ab2ad5b13a72fb511eac3ab94) | Local Cartesian projection.
`protected uuv_plume_msgs::ParticleConcentration `[`concentrationMsg`](#classuuv__plume__simulator_1_1_c_p_c_sensor_1a8cfe5eff941369e1e33e26064764abbb) | Plume concentration message.
`protected uuv_plume_msgs::Salinity `[`salinityMsg`](#classuuv__plume__simulator_1_1_c_p_c_sensor_1a2e35ed0c7c463da2602b5ac9f1da282e) | Salinity message.
`protected ros::Timer `[`updateTimer`](#classuuv__plume__simulator_1_1_c_p_c_sensor_1a9c173307f263aa9b9b7c7f2342d5ce94) | Sensor update timer.
`protected std::default_random_engine `[`rndGen`](#classuuv__plume__simulator_1_1_c_p_c_sensor_1a32296108956e0909056e72ea5c3fe873) | Pseudo random number generator.
`protected std::normal_distribution< double > `[`noiseModel`](#classuuv__plume__simulator_1_1_c_p_c_sensor_1a43cfa91f2d9b5285545e7986b5a15962) | Normal distribution describing the noise model.
`protected double `[`noiseAmp`](#classuuv__plume__simulator_1_1_c_p_c_sensor_1aff1cf4cad2ccf96800db7f6a16f271cc) | Noise amplitude.
`protected double `[`noiseSigma`](#classuuv__plume__simulator_1_1_c_p_c_sensor_1a051b51ad3230fe9ee57f94aa80605cb1) | Noise standard deviation.
`protected void `[`OnSensorUpdate`](#classuuv__plume__simulator_1_1_c_p_c_sensor_1aa0112facdab526f2e99a62772a7613cb)`(const ros::TimerEvent &)` | Update the output concentration and salinity topics.
`protected void `[`OnPlumeParticlesUpdate`](#classuuv__plume__simulator_1_1_c_p_c_sensor_1ae4cac538822b672d2045a11f4d406336)`(const sensor_msgs::PointCloud::ConstPtr & _msg)` | Update callback from the plume particles.
`protected void `[`OnOdometryUpdate`](#classuuv__plume__simulator_1_1_c_p_c_sensor_1a6348d873f88079a8af2303d76eede010)`(const nav_msgs::Odometry::ConstPtr & _msg)` | Update the odometry callback.
`protected void `[`OnGPSUpdate`](#classuuv__plume__simulator_1_1_c_p_c_sensor_1a428cc881985682f78876aa44866a6c7e)`(const sensor_msgs::NavSatFix::ConstPtr & _msg)` | Update the GPS update callback.

## Members

#### `public  `[`CPCSensor`](#classuuv__plume__simulator_1_1_c_p_c_sensor_1a1472cc5596ca8af358a4a2a887c94935)`()` 

Class constructor.

#### `public  `[`~CPCSensor`](#classuuv__plume__simulator_1_1_c_p_c_sensor_1a6c28c6d5b2f1788372ce74be9ac48d31)`()` 

Class destructor.

#### `protected bool `[`updatingCloud`](#classuuv__plume__simulator_1_1_c_p_c_sensor_1a32ace61c89476eb6309a4507936b5257) 

Flag to ensure the cloud and measurement update don't coincide.

#### `protected double `[`gamma`](#classuuv__plume__simulator_1_1_c_p_c_sensor_1a853b8d456c24b321b952359c9a61489b) 

Gamma velocity parameter for the smoothing function.

#### `protected double `[`gain`](#classuuv__plume__simulator_1_1_c_p_c_sensor_1ad676c2b912f8b148b57070cda5b1c384) 

Sensor gain.

#### `protected double `[`smoothingLength`](#classuuv__plume__simulator_1_1_c_p_c_sensor_1a285eb79145cfd715291f808eaac32afb) 

Radius of the kernel to identify particles that will be taken into account in the concentration computation.

#### `protected std::string `[`salinityUnit`](#classuuv__plume__simulator_1_1_c_p_c_sensor_1a1a2bed3e78efa3c7d002d266c775029f) 

Salinity unit to be used. Options are.

* `ppt` (parts per thousand)

* `ppm` (parts per million)

* `psu` (practical salinity unit)

#### `protected double `[`saturation`](#classuuv__plume__simulator_1_1_c_p_c_sensor_1a4925a0273447a20a2a45749c2b739bf3) 

Sensor saturation.

#### `protected bool `[`useGeoCoordinates`](#classuuv__plume__simulator_1_1_c_p_c_sensor_1a9f12bbbc0bb4734e3e319fc940b0b0e6) 

Flag that will allow storing the geodetic coordinates with the measurement message.

#### `protected bool `[`publishSalinity`](#classuuv__plume__simulator_1_1_c_p_c_sensor_1ae9007729f28c92ac5d8a11190cdeb8bd) 

Flag to activate publishing the simulated salinity.

#### `protected double `[`referenceSalinityValue`](#classuuv__plume__simulator_1_1_c_p_c_sensor_1a91278f224f4dc69aaa839eb517dd5a46) 

Default salinity value for the fluid e.g. sea water.

#### `protected double `[`plumeSalinityValue`](#classuuv__plume__simulator_1_1_c_p_c_sensor_1a7bbe4a621ed6c6be8d7ee87769c154f6) 

Default salinity value for the plume.

#### `protected bool `[`updateMeasurement`](#classuuv__plume__simulator_1_1_c_p_c_sensor_1a2de0395b9721e726347601543cfcd03d) 

Set to true to avoid particle update.

#### `protected double `[`updateRate`](#classuuv__plume__simulator_1_1_c_p_c_sensor_1a5091b83afd0468f9f9926e19329c33ee) 

Output topic's update rate.

#### `protected std::string `[`sensorFrameID`](#classuuv__plume__simulator_1_1_c_p_c_sensor_1aee44faae4c264c656d8ebd248d2292a4) 

Name of the sensor frame.

#### `protected bool `[`areParticlesInit`](#classuuv__plume__simulator_1_1_c_p_c_sensor_1af7b8775cc7edf1f37b10d2324f002146) 

Flag set to true after the first set of plume particles is received.

#### `protected bool `[`useOdom`](#classuuv__plume__simulator_1_1_c_p_c_sensor_1ab9602b92be015516bb35879f6b1539fe) 

Flag set if the sensor position update must be read from the vehicle's odometry input topic.

#### `protected bool `[`useGPS`](#classuuv__plume__simulator_1_1_c_p_c_sensor_1a42362a4faafe57c53e52930f32d5b757) 

Flag set if the sensor position update must be read from the vehicle's GPS topic.

#### `protected bool `[`useTFUpdate`](#classuuv__plume__simulator_1_1_c_p_c_sensor_1a6e5f2a338e6158a8e65288489d2f43d0) 

Flag set if the TF update wrt the sensor frame ID.

#### `protected geometry_msgs::Vector3 `[`cartPos`](#classuuv__plume__simulator_1_1_c_p_c_sensor_1a624487ac7c4af59a54344608be0e9002) 

Measured Cartesian position.

#### `protected geographic_msgs::GeoPoint `[`geoPos`](#classuuv__plume__simulator_1_1_c_p_c_sensor_1a2eaeb701f45906596c91eb81b0799423) 

Measured geodetic position.

#### `protected ros::Subscriber `[`particlesSub`](#classuuv__plume__simulator_1_1_c_p_c_sensor_1a10ca6338f7e6ed74c814aecd89908df9) 

Subscriber for the plume particle point cloud.

#### `protected ros::Subscriber `[`odometrySub`](#classuuv__plume__simulator_1_1_c_p_c_sensor_1a1113a6a302688220ec6e900897847e08) 

Subscriber for odometry topic.

#### `protected ros::Subscriber `[`gpsSub`](#classuuv__plume__simulator_1_1_c_p_c_sensor_1a22257bbc83b40e7b502e3c423fa25572) 

Subscriber to the GPS update topic.

#### `protected ros::Publisher `[`concentrationPub`](#classuuv__plume__simulator_1_1_c_p_c_sensor_1aeacfcb3e55ddf1da3df33dfd7132dad1) 

Output topic for particle concentration.

#### `protected ros::Publisher `[`salinityPub`](#classuuv__plume__simulator_1_1_c_p_c_sensor_1a606721a0bb469e7c369d166ec7298027) 

Output topic for salinity.

#### `protected std::shared_ptr< ros::NodeHandle > `[`nodeHandle`](#classuuv__plume__simulator_1_1_c_p_c_sensor_1acc3ddc9eda68743989953933a8bdb6dd) 

ROS node handle.

#### `protected tf2_ros::Buffer `[`tfBuffer`](#classuuv__plume__simulator_1_1_c_p_c_sensor_1a2b75335de225523e6ddadaab786c6376) 

TF buffer instance.

#### `protected std::shared_ptr< tf2_ros::TransformListener > `[`tfListener`](#classuuv__plume__simulator_1_1_c_p_c_sensor_1ab6950f90194ecfd62ab0bbd54fd81f7c) 

TF listener pointer.

#### `protected GeographicLib::LocalCartesian `[`projection`](#classuuv__plume__simulator_1_1_c_p_c_sensor_1ae9c6808ab2ad5b13a72fb511eac3ab94) 

Local Cartesian projection.

#### `protected uuv_plume_msgs::ParticleConcentration `[`concentrationMsg`](#classuuv__plume__simulator_1_1_c_p_c_sensor_1a8cfe5eff941369e1e33e26064764abbb) 

Plume concentration message.

#### `protected uuv_plume_msgs::Salinity `[`salinityMsg`](#classuuv__plume__simulator_1_1_c_p_c_sensor_1a2e35ed0c7c463da2602b5ac9f1da282e) 

Salinity message.

#### `protected ros::Timer `[`updateTimer`](#classuuv__plume__simulator_1_1_c_p_c_sensor_1a9c173307f263aa9b9b7c7f2342d5ce94) 

Sensor update timer.

#### `protected std::default_random_engine `[`rndGen`](#classuuv__plume__simulator_1_1_c_p_c_sensor_1a32296108956e0909056e72ea5c3fe873) 

Pseudo random number generator.

#### `protected std::normal_distribution< double > `[`noiseModel`](#classuuv__plume__simulator_1_1_c_p_c_sensor_1a43cfa91f2d9b5285545e7986b5a15962) 

Normal distribution describing the noise model.

#### `protected double `[`noiseAmp`](#classuuv__plume__simulator_1_1_c_p_c_sensor_1aff1cf4cad2ccf96800db7f6a16f271cc) 

Noise amplitude.

#### `protected double `[`noiseSigma`](#classuuv__plume__simulator_1_1_c_p_c_sensor_1a051b51ad3230fe9ee57f94aa80605cb1) 

Noise standard deviation.

#### `protected void `[`OnSensorUpdate`](#classuuv__plume__simulator_1_1_c_p_c_sensor_1aa0112facdab526f2e99a62772a7613cb)`(const ros::TimerEvent &)` 

Update the output concentration and salinity topics.

#### `protected void `[`OnPlumeParticlesUpdate`](#classuuv__plume__simulator_1_1_c_p_c_sensor_1ae4cac538822b672d2045a11f4d406336)`(const sensor_msgs::PointCloud::ConstPtr & _msg)` 

Update callback from the plume particles.

#### `protected void `[`OnOdometryUpdate`](#classuuv__plume__simulator_1_1_c_p_c_sensor_1a6348d873f88079a8af2303d76eede010)`(const nav_msgs::Odometry::ConstPtr & _msg)` 

Update the odometry callback.

#### `protected void `[`OnGPSUpdate`](#classuuv__plume__simulator_1_1_c_p_c_sensor_1a428cc881985682f78876aa44866a6c7e)`(const sensor_msgs::NavSatFix::ConstPtr & _msg)` 

Update the GPS update callback.

