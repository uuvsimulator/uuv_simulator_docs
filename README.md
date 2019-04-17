# Documentation files for the UUV simulator packages

This package contains the documentation files to generate the [documentation pages](https://uuvsimulator.github.io/).

In you are willing to contribute to this package, please check the instructions in [CONTRIBUTING](CONTRIBUTING.md)

## Purpose of the project

This software is a research prototype, originally developed for the EU ECSEL
Project 662107 [SWARMs](http://swarms.eu/).

The software is not ready for production use. However, the license conditions of the
applicable Open Source licenses allow you to adapt the software to your needs.
Before using it in a safety relevant setting, make sure that the software
fulfills your requirements and adjust it according to any applicable safety
standards (e.g. ISO 26262).

## Installation

### Requirements

Install the dependencies

```
sudo apt install python3-pip
sudo pip3 install virtualenv
```

### Activate the virtual environment and install the dependencies

```
virtualenv -p python3 venv
pip install -r requirements.txt
```

### Clone uuv_simulator.github.io into the output folder

```
git clone https://github.com/uuvsimulator/uuvsimulator.github.io.git site
```

### Install `moxygen`

1. Install [`npm`](https://linuxize.com/post/how-to-install-node-js-on-ubuntu-18.04/)
2. Install [`moxygen`](https://github.com/sourcey/moxygen)

Run 

```
> moxygen --anchors --groups --output api-%s.md /path/to/doxygen/xml
```

## License

UUV Simulator is open-sourced under the Apache-2.0 license. See the
[LICENSE](LICENSE) file for details.
