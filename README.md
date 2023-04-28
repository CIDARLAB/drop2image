# Drop to Image

## Table of Contents
1. [Features Summary](#features)
2. [Requirements](#requirements)
3. [How to Use](#how-to-use)

<a name="features"></a>
## Features Summary
This software is designed to take an image (that was drawn or uploaded on GUI), find closest color from coler pallet, and send to Arduino in order to create an image using Microfluidics

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


<a name="how_to_use"></a>
## How to Use
### Arduino 
1. Open [Serial_Arduino.ino](/Serial_Arduino/Serial_Arduino.ino) in Arduino IDE
2. Choose Board and Port that corresponds to your Arduino/ESP under Tools

![tools](/img/Screen%20Shot%202023-04-28%20at%206.37.26.png)
3. Upload the code to the board using <img src="img/Screen%20Shot%202023-04-28%20at%206.39.33.png" width=20 align=center>

### Python Version
1. Install [python3](https://www.python.org/downloads/windows/)
2. Install pip with the following command prompt
```
$ curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
$ python get-pip.py
```
3. Clone this repository
```
$ git clone https://github.com/CIDARLAB/drop2image.git
$ cd drop2image
```
4. Install required libraries and Run the program
```
$ pip install -r requirements.txt
$ python3 pixel_art_gui.py
```
![pixel_art_gui](/img/IMG_2779.jpg)

5. **To draw an image**, Choose color and click on each pixel
  - default color is gray
  - if you color a pixel as skip, that pixel will be ignored when saved

6. **To save an image**, Click on Save
  - When you click save, it will save to your current directory
  - When you click save as, you can choose where to save

7. **To fetch images**, Click on Partition Mosaic
  - Save images in concat_image directory
  - Follow the name convention filename_[row]_[column].png
  - Example images are already in the directory
  - Make sure to delete example images when you are creating your own
  - This also supports .jpeg

8. **To load an image**, Click on Load
  - When Load is clicked, pop-up window to select the image will show up
  - Choose an image, then it will be resized, parsed, and shown on the pixel grid

9. **To send color information to Arduino**, Choose the device in drop-down and Click Send
  - If you are a Windows user, device usually starts with `COM`
  - If you are a Mac user, device usually starts with `/dev/cu.`
  - It will send the index of color in the color set
  - To make sure that send is working, click on Serial Monitor at top-left cornor

  ![serial_monitor](/img/Screen%20Shot%202023-04-28%20at%206.31.20.png)

### Local Website Version
1. Follow the same step up to step 3 in Python Version
2. Install required libraries and Run the program
````
$ cd drop2image
$ pip install -r requirements.txt
$ cd main
$ python3 main.py
````
![html_gui](/img/Screen%20Shot%202023-04-28%20at%206.50.28.png)

3. **To Upload an Image**, Click on Upload Image button and choose your image file

![upload](/img/Screen%20Shot%202023-04-28%20at%206.52.17.png)
![upload](/img/Screen%20Shot%202023-04-28%20at%206.53.28.png)

4. **To Save an Image**, Click on Save Image
5. **To Draw an Image**, Choose color from color set and Draw
  - Default color is black
  - Default size of grid is 50x50