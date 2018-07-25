.. UUV Simulator documentation master file, created by
   sphinx-quickstart on Thu Sep 28 11:58:00 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to UUV Simulator's documentation!
=========================================

The UUV Simulator is a package containing the implementation of Gazebo plugins
and ROS nodes necessary for the simulation of unmanned underwater vehicles, such
as ROVs (remotely operated vehicles) and AUVs (autonomous underwater vehicles).

To send questions and/or issues, please refer to the `repository's issues page <https://github.com/uuvsimulator/uuv_simulator/issues>`_.

Click `here <https://github.com/uuvsimulator/uuv_simulator>`_ to access the
GitHub repository.

.. image:: https://img.shields.io/gitter/room/nwjs/nw.js.svg
    :target: https://gitter.im/uuvsimulator

**Status of the master branch**

.. image:: https://travis-ci.org/uuvsimulator/uuv_simulator.svg?branch=master
    :target: https://travis-ci.org/uuvsimulator/uuv_simulator

Contents
--------

.. toctree::
  :glob:
  :maxdepth: 2

  installation
  quick_start
  tutorials/index
  documentation/index
  api/index
  faq
  license

Reference
---------

If you wish to use the UUV Simulator in a research project, please cite our paper ::

  @inproceedings{Manhaes_2016,
  	doi = {10.1109/oceans.2016.7761080},
  	url = {https://doi.org/10.1109%2Foceans.2016.7761080},
  	year = 2016,
  	month = {sep},
  	publisher = {{IEEE}},
  	author = {Musa Morena Marcusso Manh{\~{a}}es and Sebastian A. Scherer and Martin Voss and Luiz Ricardo Douat and Thomas Rauschenbach},
  	title = {{UUV} Simulator: A Gazebo-based package for underwater intervention and multi-robot simulation},
  	booktitle = {{OCEANS} 2016 {MTS}/{IEEE} Monterey}
  }

Other sources
^^^^^^^^^^^^^

SWARMs Project
""""""""""""""

* **17-05-2018** - Semi-autonomous manipulation demonstration with UUV Simulator

.. raw:: html

  <iframe width="560" height="315" src="https://www.youtube.com/embed/vKMR8-7WRF4?rel=0" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>


* **17-10-2016** - Preliminary results

.. raw:: html

  <iframe width="560" height="315" src="https://www.youtube.com/embed/6V_TR9i0k1Q" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>



Maritime Robot X Forum 2018
"""""""""""""""""""""""""""

You can also check the presentation made for the `Maritime RobotX Forum 2018 <http://www.robotx.org/>`_

.. raw:: html

  <iframe width="560" height="315" src="https://www.youtube.com/embed/eoq-Ro2Hnao" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>



To see the recording of the complete panel, check the video below

.. raw:: html

  <iframe width="560" height="315" src="https://www.youtube.com/embed/CXZtw-LeQsY" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>



Purpose of the project
----------------------

This software is a research prototype, originally developed for the EU ECSEL
Project 662107 `SWARMs <http://swarms.eu/>`_.

The software is not ready for production use. It has neither been developed nor
tested for a specific use case. However, the license conditions of the applicable
Open Source licenses allow you to adapt the software to your needs. Before using
it in a safety relevant setting, make sure that the software fulfills your
requirements and adjust it according to any applicable safety standards (e.g.
ISO 26262).

License
-------

UUV Simulator is open-sourced under the Apache-2.0 license. See the
`LICENSE <https://github.com/uuvsimulator/uuv_simulator/blob/master/LICENSE>`_
file for details.

For a list of other open source components included in UUV Simulator, see the
file `3rd-party-licenses.txt <https://github.com/uuvsimulator/uuv_simulator/blob/master/3rd-party-licenses.txt>`_.

Repositories
------------

* `uuv_simulator <https://github.com/uuvsimulator/uuv_simulator>`_
* `uuv_plume_simulator <https://github.com/uuvsimulator/uuv_plume_simulator>`_
* `netcdf_ros <https://github.com/uuvsimulator/netcdf_ros>`_
* `desistek_saga <https://github.com/uuvsimulator/desistek_saga>`_
* `eca_a9 <https://github.com/uuvsimulator/eca_a9>`_
* `rexrov2 <https://github.com/uuvsimulator/rexrov2>`_
* `uuv_simulation_evaluation <https://github.com/uuvsimulator/uuv_simulation_evaluation>`_
* `lauv_gazebo <https://github.com/uuvsimulator/lauv_gazebo>`_

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

Useful bibliography
===================

.. bibliography:: refs.bib
  :all:
  :style: plain
