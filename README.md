# Drop to Image

## Table of Contents
1. [Features Summary](#features)
2. [Requirements](#requirements)
3. [Installation](#installation)
4. [How to Use](#how-to-use)

<a name="features"></a>
## Features Summary


<a name="requirements"></a>
## Requirements

### Computational Requirements
- Python
- pip
- Arduino IDE
  - [ESP32 Library](https://raw.githubusercontent.com/espressif/arduino-esp32/gh-pages/package_esp32_index.json) installed if using ESP32

### Hardware Requirements
- Microcontroller
  - Arduino Uno/Nano
  - ESP32 with Arduino IDE
- Cables
  - USB Type A or C (computer)
  - USB Type Mini-B for Arduino Nano
  - USB Type A Male for Arduino Uno
  - USB Type Micro-C for ESP32


<a name="installation"></a>
## Installation
### On you computer
````
$ git clone https://github.com/CIDARLAB/drop2image.git
$ cd drop2image
$ pip install -r requirements.txt
$ python3 droplets_gui.py YourIPAdress
````

### On Arduino Yun
1. Open [Arduino_receive.ino](/Arduino_receive/Arduino_receive.ino) in Arduino IDE
2. Choose the right port under Tools
3. Upload the code to the board

### HTML GUI
````
$ cd drop2image
$ pip install -r requirements.txt
$ cd main
$ python3 main.py
````


<a name="how_to_use"></a>
## How to Use
### Python Version
1. Install [python3](https://www.python.org/downloads/windows/)
2. Install pip with the following command prompt
```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
```
3. 
### Local Website Version
