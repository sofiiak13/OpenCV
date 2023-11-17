# OpenCVGestureRecognition
Gesture recognition program that takes a picture with a webacam when it detects a V/peace sign!

Before running the program make sure you have the following packages installed: 

python3 (version = 3.11) and then you can run

pip3 install numpy

pip3 install mediapipe

pip3 install tensorflow

Hardware that can be was tested with this project: MacOS, MS Windows

There are two ways you could use this program:

First, download a "hand-gesture-recognition-code" folder. The actual code would be in the GestureDetection.py file. 

If you would like to run your program with esp32 camera, then click on this https://github.com/derekja/espcam link to find the instructions for connecting the camera properly.

You also have an option to run this with your own webcam. In this case, you would need to go to GestureDetection.py and uncomment lines 56, 67 and 135 as well comment out lines 59 and 71-75. 

In order to run a program you can either use your code editor or terminal/command prompt.

For Code Editor:
  Double click on GestureDetection.py to open it in the code editor of your choice. Then, run the file without debugging.

For command prompt:
  Open command prompt and navigate to hand-gesture-recognition-code and from this folder run the folllowing command:
    python3 GestureDetection.py
    
Note: try running the file a secod time if it doesn't work properly for the first time.

Allow the program access to your camera.

After following this instructions you should see an output window pop up with live video from your webcam. 

Note: you may need to wait for about 5 seconds for script to run, please be patient :)

In the output window, you should be able to see an landmark of your hand (if you are showing one). This program proccesses only one hand at a time, please keep that in mind. The Gesture library already has 10 gestures available for usage:
['okay', 'peace', 'thumbs up', 'thumbs down', 'call me', 'stop', 'rock', 'live long', 'fist', 'smile'] 

So you can experimet with showing different signs to the camera. You should be able to see the name of the gesture in the top-left corner of the output window.
Once the program detects a peace/V sign it will instantly take a picture with your webcam and save it to the same folder in which GestureDetection.py is located (in our case the image will be saved to hand-gesture-recognition-code). It will also print "image  {n}  saved!" in the terminal once the image is saved.

Credits Note: this program was built using the code provided in https://techvidvan.com/tutorials/hand-gesture-recognition-tensorflow-opencv/ .
