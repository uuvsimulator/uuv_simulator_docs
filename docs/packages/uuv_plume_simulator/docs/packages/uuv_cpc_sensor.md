![Version](https://img.shields.io/badge/version-0.3.1-brightgreen.svg)

> Link to the `uuv_plume_simulator` repository [here](https://github.com/uuvsimulator/uuv_plume_simulator)

# Description

The uuv_cpc_sensor package

# Launch files

## [`start_cpc_sensor.launch`](https://github.com/uuvsimulator/uuv_plume_simulator/tree/master/uuv_cpc_sensor/launch/start_cpc_sensor.launch)

> **Arguments**

* **uuv_name**
* **latitude_ref** (*default:* `0`)
* **longitude_ref** (*default:* `0`)
* **odom_topic** (*default:* `pose_gt`)
* **gps_topic** (*default:* `gps`)
* **gamma**
* **gain**
* **radius**
* **update_rate** (*default:* `1`)
* **use_geo_coordinates**
* **reference_salinity_value** (*default:* `35.0`)
* **salinity_unit** (*default:* `ppt`)
* **sensor_frame_id** (*default:* `$(arg uuv_name)/base_link`)
* **publish_salinity** (*default:* `true`)
* **use_odom** (*default:* `false`)
* **use_gps** (*default:* `false`)

