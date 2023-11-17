# import necessary packages

import cv2
import numpy as np
import mediapipe as mp
import urllib.request
import tensorflow as tf
import threading


NOT_STARTED = 0
BEFORE_STARTED = 1
BEFORE_FINISHED = 2
AFTER_STARTED = 3

check = NOT_STARTED

def take_picture(frame, img_counter) -> None:
    
        img_name = f'new_Image_{img_counter}.jpg'
        cv2.imwrite(img_name, frame) 
       
        return
        

def callback_before_finished():
    print("callback_before..")

    global check
    check = BEFORE_FINISHED

def callback_after_finished():
    print("callback_after..")

    global check
    check = NOT_STARTED


def V_recognition():
    # initialize mediapipe
    mpHands = mp.solutions.hands
    hands = mpHands.Hands(max_num_hands=1, min_detection_confidence=0.7)
    mpDraw = mp.solutions.drawing_utils

    # Load the gesture recognizer model
    model = tf.keras.models.load_model('mp_hand_gesture')

    # Load class names
    f = open('gesture.names', 'r')
    classNames = f.read().split('\n')
    f.close()
    print(classNames)


    # Initialize the webcam
    # cap = cv2.VideoCapture(0)

    # replace with camera URL
    url='http://10.0.1.42/cam-hi.jpg'
    img_counter = 0
    
    global check
    check = NOT_STARTED

    while True:
        # Read each frame from the webcam
        #_, frame = cap.read()


        # load an image from the camera server
        img_resp=urllib.request.urlopen(url)
        # use numpy to turn the image into an array of values
        imgnp=np.array(bytearray(img_resp.read()),dtype=np.uint8)
        # use openCV to turn the array of values into an openCV image
        frame = cv2.imdecode(imgnp,-1)

        x, y, c = frame.shape

        # Flip the frame vertically
        frame = cv2.flip(frame, 1)
        framergb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Get hand landmark prediction
        result = hands.process(framergb)
        
        className = ''

        # post process the result
        # check if any hand is detected
        if result.multi_hand_landmarks:
            landmarks = []
            for handslms in result.multi_hand_landmarks:
                for lm in handslms.landmark:
                    lmx = int(lm.x * x)
                    lmy = int(lm.y * y)

                    landmarks.append([lmx, lmy])

                # Drawing landmarks on frames
                mpDraw.draw_landmarks(frame, handslms, mpHands.HAND_CONNECTIONS)

                # Predict gesture
                prediction = model.predict([landmarks])
               
                classID = np.argmax(prediction)
                className = classNames[classID]
                if className == "peace": 
                    if check == NOT_STARTED:   
                        check = BEFORE_STARTED
                        timer_before = threading.Timer(interval = 0.5, function = callback_before_finished)
                        timer_before.start()
                    elif check == BEFORE_FINISHED:            
                        check = AFTER_STARTED

                        img_counter += 1
                        take_picture(frame, img_counter)
                        print("image ", img_counter, " saved!" )
    
                        timer_after = threading.Timer(interval = 2, function = callback_after_finished)
                        timer_after.start()

                #print(className)

        # show the prediction on the frame
        cv2.putText(frame, className, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2, cv2.LINE_AA)

        # Show the final output
        cv2.imshow("Output", frame) 

        #press esc to quit all windows
        if cv2.waitKey(1) == 27:
            break

    # release the webcam and destroy all active windows
    #cap.release()
    

    cv2.destroyAllWindows()

print("opening...")
V_recognition()
