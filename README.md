# Fly your tello using your old gaming controller
Control your tello with a gaming controller supported by pygame using the repository 'DJITelloPy'.
DJITelloPy repository link: https://github.com/damiafuentes/DJITelloPy

![image](https://user-images.githubusercontent.com/82200669/164916832-5ac991d6-1196-4c4e-9c7d-8a842a14ee99.png)

I personally used a playstation dualshock 3 controller.

The repository contains the program itself as well as a video compiler for the video recordings you can make with the program.

## This project was largely done thanks to pygame.org

Link: www.pygame.org/docs/ref/joystick.html

PRO TIP: Use the example program given in the following link to check your controller's inputs

## 3 STEPS ON HOW TO USE THE PROGRAM:
1. Have your desired gaming controller connected to your computer. Make sure your computer reads its input.
2. Turn on the tello and connect to its wifi.
3. Run the program.

## ABOUT THE PROGRAM:

Make sure the tello you're using has at least SDK 3.0 by updating its firmware in order to use all of the following functions accordingly.

The current button and axis alignments are:
- button 0 (X): flip backwards
- button 1 (◯): flip right
- button 2 (△): flip left
- button 3 (□): flip forward
- button 4 (L1): take photos (using cv2 and DJITelloPy command get_frame_read() )
- button 5: (R1): record a "video" - you may compile the video using the video compiler that follows (uses cv2 and DJITelloPy command get_frame_read() ). Note that using this can take up a lot of memory
- button 6: (SELECT): Emergencylands (all motors are turned off - a hard landing) if the tello is flying and reboots it if not.
  HOW TO MAKE A SMOOTH REBOOT: In your DjiTelloPy-repository, go to "tello.py" and edit the variable "RETRY_COUNT" to a value higher than 3. Make sure your computer automatically connects to the tello's wifi.
- button 7: (START): Takeoff (can easily be replaced with 'throwfly') if the tello is not flying and lands (slowly decreases motor speeds over time for a soft landing) if flying
- button 8: (LEFT THUMBSTICK DOWN PRESS): NO ASSIGNED FUNCTION
- button 9: (RIGHT THUMBSTICK DOWN PRESS): NO ASSIGNED FUNCTION
- axis [0,1] (LEFT THUMBSTICK): rotate left/right; fly upward/downward
- axis [2,3] (RIGHT THUMBSTICK): fly left/right; fly forward/backward
- axis [4] (L2): While pressed down, use the tello downward camera (IR-sensitive). When not pressed down, use the tello forward camera (colored)
- axis[5] (R2): NO ASSIGNED FUNCTION

NO HAT ALIGNMENTS ARE USED IN THE PROGRAM.

FYI: The pygame window will show data given by the tello through the DJITelloPy command get_own_udp_object()

## TELLO SDK 3.0 guides:

A quick help to understand the commands being sent to the drone would be to check this guide:
https://dl.djicdn.com/downloads/RoboMaster+TT/Tello_SDK_3.0_User_Guide_en.pdf

Mission Pad an Flight Map guide sdk 3.0: https://dl.djicdn.com/downloads/RoboMaster+TT/RoboMaster_TT_Mission_Pad_and_Flight_Map_User_Guide_en.pdf

## A LITTLE HELP TO USE PLAYSTATION CONTROLLERS:

To run a playstation controller, further requirements are needed to run the program.
If you want to use a playstation 3 or 4-controller, try your luck with the following links:

A wired PS4-controller: https://www.youtube.com/watch?v=a3JaBBD2U2o

A wired PS3-controller: https://www.youtube.com/watch?v=1ZaZVvnV5D4

There is in fact ways to also use fx a playstation 2 controller however caution is advised to prevent you from downloading malicious code.
