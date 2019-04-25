# struct `gazebo::IMUParameters` 

[IMUParameters](#structgazebo_1_1_i_m_u_parameters) stores all IMU model parameters. A description of these parameters can be found here: [https://github.com/ethz-asl/kalibr/wiki/IMU-Noise-Model-and-Intrinsics](https://github.com/ethz-asl/kalibr/wiki/IMU-Noise-Model-and-Intrinsics).

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public double `[`gyroscopeNoiseDensity`](#structgazebo_1_1_i_m_u_parameters_1a25f7a443bbabe24709fef7902f253686) | Gyroscope noise density (two-sided spectrum) [rad/s/sqrt(Hz)].
`public double `[`gyroscopeRandomWalk`](#structgazebo_1_1_i_m_u_parameters_1ae252c3f9cc0692111ce5d34603db2c1b) | Gyroscope bias random walk [rad/s/s/sqrt(Hz)].
`public double `[`gyroscopeBiasCorrelationTime`](#structgazebo_1_1_i_m_u_parameters_1ab9fa9588c7a67ae9c38e71910a510661) | Gyroscope bias correlation time constant [s].
`public double `[`gyroscopeTurnOnBiasSigma`](#structgazebo_1_1_i_m_u_parameters_1aa90e85c829fb5a8a7079c670feaa1513) | Gyroscope turn on bias standard deviation [rad/s].
`public double `[`accelerometerNoiseDensity`](#structgazebo_1_1_i_m_u_parameters_1a2b4bca730c38f081af8c9b73f4b6bad4) | Accelerometer noise density (two-sided spectrum) [m/s^2/sqrt(Hz)].
`public double `[`accelerometerRandomWalk`](#structgazebo_1_1_i_m_u_parameters_1a2d6b2fd03ddb35a1e61653745bbfb8fb) | Accelerometer bias random walk. [m/s^2/s/sqrt(Hz)].
`public double `[`accelerometerBiasCorrelationTime`](#structgazebo_1_1_i_m_u_parameters_1ae3ee5ba06f1f4c1982bfd85d50edf07d) | Accelerometer bias correlation time constant [s].
`public double `[`accelerometerTurnOnBiasSigma`](#structgazebo_1_1_i_m_u_parameters_1ad9ed56456fb2bfbe95d4caeb73631613) | Accelerometer turn on bias standard deviation [m/s^2].
`public double `[`orientationNoise`](#structgazebo_1_1_i_m_u_parameters_1a6c283963ffe5ce1e1552238d3bd00541) | Standard deviation of orientation noise per axis [rad].
`public inline  `[`IMUParameters`](#structgazebo_1_1_i_m_u_parameters_1a458153650853d5e46e0c8ebfbcc3982f)`()` | Constructor.

## Members

#### `public double `[`gyroscopeNoiseDensity`](#structgazebo_1_1_i_m_u_parameters_1a25f7a443bbabe24709fef7902f253686) 

Gyroscope noise density (two-sided spectrum) [rad/s/sqrt(Hz)].

#### `public double `[`gyroscopeRandomWalk`](#structgazebo_1_1_i_m_u_parameters_1ae252c3f9cc0692111ce5d34603db2c1b) 

Gyroscope bias random walk [rad/s/s/sqrt(Hz)].

#### `public double `[`gyroscopeBiasCorrelationTime`](#structgazebo_1_1_i_m_u_parameters_1ab9fa9588c7a67ae9c38e71910a510661) 

Gyroscope bias correlation time constant [s].

#### `public double `[`gyroscopeTurnOnBiasSigma`](#structgazebo_1_1_i_m_u_parameters_1aa90e85c829fb5a8a7079c670feaa1513) 

Gyroscope turn on bias standard deviation [rad/s].

#### `public double `[`accelerometerNoiseDensity`](#structgazebo_1_1_i_m_u_parameters_1a2b4bca730c38f081af8c9b73f4b6bad4) 

Accelerometer noise density (two-sided spectrum) [m/s^2/sqrt(Hz)].

#### `public double `[`accelerometerRandomWalk`](#structgazebo_1_1_i_m_u_parameters_1a2d6b2fd03ddb35a1e61653745bbfb8fb) 

Accelerometer bias random walk. [m/s^2/s/sqrt(Hz)].

#### `public double `[`accelerometerBiasCorrelationTime`](#structgazebo_1_1_i_m_u_parameters_1ae3ee5ba06f1f4c1982bfd85d50edf07d) 

Accelerometer bias correlation time constant [s].

#### `public double `[`accelerometerTurnOnBiasSigma`](#structgazebo_1_1_i_m_u_parameters_1ad9ed56456fb2bfbe95d4caeb73631613) 

Accelerometer turn on bias standard deviation [m/s^2].

#### `public double `[`orientationNoise`](#structgazebo_1_1_i_m_u_parameters_1a6c283963ffe5ce1e1552238d3bd00541) 

Standard deviation of orientation noise per axis [rad].

#### `public inline  `[`IMUParameters`](#structgazebo_1_1_i_m_u_parameters_1a458153650853d5e46e0c8ebfbcc3982f)`()` 

Constructor.

