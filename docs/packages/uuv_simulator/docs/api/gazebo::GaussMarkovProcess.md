# class `gazebo::GaussMarkovProcess` 

Implementation of a Gauss-Markov process to model the current velocity and direction according to [1] [1] Fossen, Thor I. Handbook of marine craft hydrodynamics and motion control. John Wiley & Sons, 2011.

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public double `[`var`](#classgazebo_1_1_gauss_markov_process_1a1e4fb7902c13ed7f5ed4b081b8c750a1) | Process variable.
`public double `[`mean`](#classgazebo_1_1_gauss_markov_process_1ac245edf6d8fa0b6926cb8d83d29e3457) | Mean process value.
`public double `[`min`](#classgazebo_1_1_gauss_markov_process_1a5becb64490649244d6ee0370dd9e9952) | Minimum limit for the process variable.
`public double `[`max`](#classgazebo_1_1_gauss_markov_process_1a36c94fb3fd89d6b8ec095ff2fd61fd1a) | Maximum limit for the process variable.
`public double `[`mu`](#classgazebo_1_1_gauss_markov_process_1af0c51962ec2392d734c0ee79f45866a8) | Process constant, if zero, process becomes a random walk.
`public double `[`noiseAmp`](#classgazebo_1_1_gauss_markov_process_1a094afee00b782c741a5edfdea42f0644) | Gaussian white noise amplitude.
`public double `[`lastUpdate`](#classgazebo_1_1_gauss_markov_process_1a21d7006da353d3a20fdb0faba2a24da7) | Timestamp for the last update.
`public  `[`GaussMarkovProcess`](#classgazebo_1_1_gauss_markov_process_1af1e11c49f71e6fd8f260f69db1e45e61)`()` | Class constructor.
`public void `[`Reset`](#classgazebo_1_1_gauss_markov_process_1abb7d9286aa8162e074b64188908017fe)`()` | Resets the process parameters.
`public bool `[`SetModel`](#classgazebo_1_1_gauss_markov_process_1aa987aee49f6f4a2f460138c93b11d3e8)`(double _mean,double _min,double _max,double _mu,double _noise)` | Sets all the necessary parameters for the computation.
`public bool `[`SetMean`](#classgazebo_1_1_gauss_markov_process_1a02d2ce1deb17930eb2b6d87ffc93d3f0)`(double _mean)` | Set mean process value.
`public double `[`Update`](#classgazebo_1_1_gauss_markov_process_1a4fe5c320c4fbdf4c6e5211381cf6e96a)`(double _time)` | Update function for a new time stamp.
`public void `[`Print`](#classgazebo_1_1_gauss_markov_process_1a5933e94170a0b8ab0b32e8eaba5281bf)`()` | Print current model paramters.

## Members

#### `public double `[`var`](#classgazebo_1_1_gauss_markov_process_1a1e4fb7902c13ed7f5ed4b081b8c750a1) 

Process variable.

#### `public double `[`mean`](#classgazebo_1_1_gauss_markov_process_1ac245edf6d8fa0b6926cb8d83d29e3457) 

Mean process value.

#### `public double `[`min`](#classgazebo_1_1_gauss_markov_process_1a5becb64490649244d6ee0370dd9e9952) 

Minimum limit for the process variable.

#### `public double `[`max`](#classgazebo_1_1_gauss_markov_process_1a36c94fb3fd89d6b8ec095ff2fd61fd1a) 

Maximum limit for the process variable.

#### `public double `[`mu`](#classgazebo_1_1_gauss_markov_process_1af0c51962ec2392d734c0ee79f45866a8) 

Process constant, if zero, process becomes a random walk.

#### `public double `[`noiseAmp`](#classgazebo_1_1_gauss_markov_process_1a094afee00b782c741a5edfdea42f0644) 

Gaussian white noise amplitude.

#### `public double `[`lastUpdate`](#classgazebo_1_1_gauss_markov_process_1a21d7006da353d3a20fdb0faba2a24da7) 

Timestamp for the last update.

#### `public  `[`GaussMarkovProcess`](#classgazebo_1_1_gauss_markov_process_1af1e11c49f71e6fd8f260f69db1e45e61)`()` 

Class constructor.

#### `public void `[`Reset`](#classgazebo_1_1_gauss_markov_process_1abb7d9286aa8162e074b64188908017fe)`()` 

Resets the process parameters.

#### `public bool `[`SetModel`](#classgazebo_1_1_gauss_markov_process_1aa987aee49f6f4a2f460138c93b11d3e8)`(double _mean,double _min,double _max,double _mu,double _noise)` 

Sets all the necessary parameters for the computation.

#### Parameters
* `_mean` Mean value 

* `_min` Minimum limit 

* `_max` Maximum limit 

* `_mu` Process constant 

* `_noise` Amplitude for the Gaussian white noise 

#### Returns
True, if all parameters were valid

#### `public bool `[`SetMean`](#classgazebo_1_1_gauss_markov_process_1a02d2ce1deb17930eb2b6d87ffc93d3f0)`(double _mean)` 

Set mean process value.

#### Parameters
* `_mean` New mean value 

#### Returns
True, if value inside the limit range

#### `public double `[`Update`](#classgazebo_1_1_gauss_markov_process_1a4fe5c320c4fbdf4c6e5211381cf6e96a)`(double _time)` 

Update function for a new time stamp.

#### Parameters
* `_time` Current time stamp

#### `public void `[`Print`](#classgazebo_1_1_gauss_markov_process_1a5933e94170a0b8ab0b32e8eaba5281bf)`()` 

Print current model paramters.

