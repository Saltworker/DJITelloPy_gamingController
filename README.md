Control your tello with a gaming controller supported by pygame using the repository 'DJITelloPy'.
DJITelloPy repository link: https://github.com/damiafuentes/DJITelloPy

The repository contains the program itself as well as a video compiler for the video recordings you can make with the program.

This project is largely done thanks to pygame.org
Link: www.pygame.org/docs/ref/joystick.html
PRO TIP: Use the example program given in the following link to check your controller's inputs

3 STEPS ON HOW TO USE THE PROGRAM:
1. Have your desired gaming controller connected to your computer. Make sure your computer reads its input.
2. Turn on the tello and connect to its wifi.
3. run the program.

ABOUT THE PROGRAM:

![image](https://user-images.githubusercontent.com/82200669/164916832-5ac991d6-1196-4c4e-9c7d-8a842a14ee99.png)

NOTE: Make sure the tello you're using has at least SDK 3.0 by updating its firmware in order to use all of the following functions accordingly.
Lets you control your Tello-drone with any gaming controller that pygame supports.
I used a playstation dualshock 3 controller.
The current button and axis alignments are:
- button 0 (X): flip backwards
- button 1 (◯): flip right
- button 2 (△): flip left
- button 3 (□): flip forward
- button 4 (L1): take photos (using cv2 and get_frame_read() )
- button 5: (R1): record a "video" - compile this using the video compiler (using cv2 and get_frame_read() )
- button 6: (SELECT): Emergencylands (all motors are turned off; a hard landing) if the tello is flying and resets if not (TO RESET AUTOMATICALLY, CHECK THE PROGRAM FOR EXPLAINATION ON HOW TO)
- button 7: (START): Takeoff OR throwfly if the tello is not flying and lands (slowly decreases motor speeds over time for a soft landing) if flying
- button 8: (LEFT THUMBSTICK DOWN PRESS): NO FUNCTION
- button 9: (RIGHT THUMBSTICK DOWN PRESS): NO FUNCTION
- axis [0,1] (LEFT THUMBSTICK): fly left/right; fly forward/backward
- axis [2,3] (RIGHT THUMBSTICK): rotate left/right; fly upward/downward
- axis [4] (L2): When pressed down, use the tello downward camera (IR-sensitive). When not pressed down, use the tello forward camera (colored)
- axis[5] (R2): NO FUNCTION

NO HAT ALIGNMENTS ARE USED IN THE PROGRAM.

TELLO SDK 3.0 guides:

A quick help to understand the commands being sent to the drone would be to check this guide:
https://dl.djicdn.com/downloads/RoboMaster+TT/Tello_SDK_3.0_User_Guide_en.pdf

Mission Pad an Flight Map guide sdk 3.0: https://dl.djicdn.com/downloads/RoboMaster+TT/RoboMaster_TT_Mission_Pad_and_Flight_Map_User_Guide_en.pdf

A LITTLE HELP TO USE PLAYSTATION CONTROLLERS:

To run a playstation controller, further requirements are needed to run the program.
If you want to use a playstation 3 or 4-controller, try your luck with the following links:

A wired PS4-controller: https://www.youtube.com/watch?v=a3JaBBD2U2o

A wired PS3-controller: https://www.youtube.com/watch?v=1ZaZVvnV5D4

There is in fact ways to also use fx a playstation 2 controller but caution is advised to prevent you from downloading malicious code.
