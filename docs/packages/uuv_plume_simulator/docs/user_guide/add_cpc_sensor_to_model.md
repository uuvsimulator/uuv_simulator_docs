To measure the particle concentration using the algorithm described in [`Tian, 2010`](https://ieeexplore.ieee.org/abstract/document/5456812/), the vehicle must have a sensor unit from the chemical particle concentration available in the [`uuv_sensor_ros_plugins`](../packages/uuv_simulator/docs/packages/uuv_sensor_ros_plugins.md).
A number of URDF snippets to initialize this sensor in the URDF robot description can be found in the [sensor package](https://github.com/uuvsimulator/uuv_simulator/blob/master/uuv_sensor_plugins/uuv_sensor_ros_plugins/urdf/chemical_concentration_snippets.xacro).
One example of implementation is already presented in the description of the [`rexrov2`](../packages/rexrov2/intro.md) vehicle in the declaration of its [sensor units](https://github.com/uuvsimulator/rexrov2/blob/master/rexrov2_description/urdf/rexrov2_sensors.xacro) as shown below 

```xml
<!-- Mount chemical particle concentration sensor -->
<xacro:default_chemical_concentration_sensor_macro
  namespace="${namespace}"
  parent_link="${namespace}/base_link"
  inertial_reference_frame="${inertial_reference_frame}">
  <origin xyz="0 0 0" rpy="0 0 0"/>
</xacro:default_chemical_concentration_sensor_macro>
```

A sample of the output in `rviz` and `rqt` can be seen below.
Feel free to check the sample [plume script](https://github.com/uuvsimulator/uuv_plume_simulator/blob/master/uuv_plume_simulator/scripts/set_demo_turbulent_plume) and the [URDF sensor snippets](https://github.com/uuvsimulator/uuv_simulator/blob/master/uuv_sensor_plugins/uuv_sensor_ros_plugins/urdf/chemical_concentration_snippets.xacro) to see the input arguments that can be changed to modify both the plume and concentration sensor settings.

![Plume](../images/tutorial_plume.png)

![Plume RViz](../images/gazebo_plume_rviz.png)

![Plume RViz Sensor](../images/gazebo_plume_rviz_sensor.png)
