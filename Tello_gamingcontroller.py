import pygame
from djitellopy import tello
import cv2
import time
import os

#############################################################################################################
#   A quick help to understand the commands being sent to the drone would be to check this guide:           #
#   Tello SDK 3.0: https://dl.djicdn.com/downloads/RoboMaster+TT/Tello_SDK_3.0_User_Guide_en.pdf            #
#   Mission Pad an Flight Map guide sdk 3.0:                                                                #
#   https://dl.djicdn.com/downloads/RoboMaster+TT/RoboMaster_TT_Mission_Pad_and_Flight_Map_User_Guide_en.pdf#
#############################################################################################################

### Imports controllerbinds ###
pygame.init()
pygame.joystick.init()
joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]

### Connects to the tello drone and gets its get_frame_read ###
me = tello.Tello()
me.connect(wait_for_state=True)
me.send_command_with_return('setfps high') # Use 'low' for 5fps, 'middle' for 15fps and 'high' for 30fps
me.send_command_with_return('setresolution high') # Use 'low' for 480p and 'high' for 720p
me.send_command_with_return('setbitrate 0') # Use '0' for auto Mbps spanning 1-5Mbps, '1' for 1Mbps, '2' for 2Mbps...
#NOTE: Default camera settings: fps = 'middle', resolution = 'high', bitrate = '0' (auto)
me.streamon()

### Important variables for some of the functions ###
recording = False
downvision = False

global img
global dirNameVid

# Define some colors.
BLACK = pygame.Color('black')
WHITE = pygame.Color('white')


#################################################################################
### Initializing the controller-binds was done thanks to the following link:  ###
### https://www.pygame.org/docs/ref/joystick.html                             ###
#################################################################################

# This is a simple class that will help us print to the screen.
# It has nothing to do with the joysticks, just outputting the
# information.
class TextPrint(object):
    def __init__(self):
        self.reset()
        self.font = pygame.font.Font(None, 20)

    def tprint(self, screen, textString):
        textBitmap = self.font.render(textString, True, BLACK)
        screen.blit(textBitmap, (self.x, self.y))
        self.y += self.line_height

    def reset(self):
        self.x = 10
        self.y = 10
        self.line_height = 15

    def indent(self):
        self.x += 10

    def unindent(self):
        self.x -= 10

# Set the width and height of the tello_input screen (width, height).
screen = pygame.display.set_mode((500, 700))

pygame.display.set_caption("My Game")

# Used to manage how fast the screen updates.
clock = pygame.time.Clock()

# Get ready to print.
textPrint = TextPrint()

#############################################################
### Forever loop for reading controller input with Pygame ###
#############################################################

done = False

while not done:
    #
    # EVENT PROCESSING STEP
    #
    # Possible joystick actions: JOYAXISMOTION, JOYBALLMOTION, JOYBUTTONDOWN,
    # JOYBUTTONUP, JOYHATMOTION
    for event in pygame.event.get(): # User did something.
        if event.type == pygame.QUIT: # If user clicked close.
            done = True # Flag that we are done so we exit this loop.

    # Get count of joysticks.
    joystick_count = pygame.joystick.get_count()

    for i in range(joystick_count):
        joystick = pygame.joystick.Joystick(i)
        joystick.init()

        try:
            jid = joystick.get_instance_id()
        except AttributeError:
            # get_instance_id() is an SDL2 method
            jid = joystick.get_id()


        try:
            guid = joystick.get_guid()
        except AttributeError:
            # get_guid() is an SDL2 method
            pass

        # Usually axis run in pairs, up/down for one, and left/right for
        # the other.
        axes = joystick.get_numaxes()

        for i in range(axes):
            axis = joystick.get_axis(i)

        buttons = joystick.get_numbuttons()

        for i in range(buttons):
            button = joystick.get_button(i)
            #########if joystick.get_button(0) == 1:

        hats = joystick.get_numhats()

        # Hat position. All or nothing for direction, not a float like
        # get_axis(). Position is a tuple of int values (x, y).
        for i in range(hats):
            hat = joystick.get_hat(i)

        #######################################################################
        ### Runs Pygame-window and get_frame_read() through "Result"-window ###
        #######################################################################
        img = me.get_frame_read().frame
        img = cv2.resize(img, (1280, 720))  # Give the recording a specific resolution - FYI The drone has a 720p camera.
        cv2.imshow("Result", img)
        cv2.waitKey(1)

        #######################################################################################################
        ### The following section covers keybinds meant to control the tello drone with the "Pygame window" ###
        #######################################################################################################

        ### Own controllerbinds are set underneath here: ###
        # Controller keys open for use:
        # joystick.get_button(8)
        # joystick.get_button(9)
        # joystick.get_axis(5)
        # joystick.get_hat(1)

        if pygame.key.get_focused() == True:

            ### The Controllers symbols (X, O, □, △; A, B, X, Y; Whatever the combination may be) are utilized for each direction of flipping the drone ###
            if joystick.get_button(0) == 1:
                me.send_command_with_return("flip b")
            if joystick.get_button(1) == 1:
                me.send_command_with_return("flip r")
            if joystick.get_button(2) == 1:
                me.send_command_with_return("flip l")
            if joystick.get_button(3) == 1:
                me.send_command_with_return("flip f")

            ### Takes a photo from the drone POV - from the "Result"-window ###
            ### NOTE: There is no cooldown when taking images - pressing gently is advised ###
            if joystick.get_button(4) == 1:
                dirNameImg = 'Resources/Images' # Configure name of folder (for images inside project)
                if not os.path.exists(dirNameImg):
                    os.makedirs(dirNameImg)
                    print("Directory ", dirNameImg, " created ")
                cv2.imwrite(f'{dirNameImg}/{time.time()}.jpg', img)
                print("A picture was taken")

            ### Video recorder - remember to compile it.
            ### This can be done either with the automatic function, "Video_compiler.py" ###
            if joystick.get_button(5) == 1 and recording == False:
                dirNameVid = f'Resources/Video/{time.time()}' ### Configure name of folder (for images and a video inside project) ###
                if not os.path.exists(dirNameVid) and recording == False:
                    os.makedirs(dirNameVid)
                    print("Directory ", dirNameVid, " created ")
                    recording = True
            if recording == True:
                cv2.imwrite(f'{dirNameVid}/{time.time()}.jpg', img)
            if joystick.get_button(5) == 0 and recording == True:
                recording = False

            ### 2 in 1: Will emergency land while flying and reboot while the tello drone isn't flying ###
            if joystick.get_button(6) == 1:
                if me.is_flying == True:
                    ### NOTE: Meant for use in dire situations: Turns off all motors resulting in the drone falling down - use wisely ###
                    me.send_command_with_return("emergency")
                    me.is_flying = False
                    time.sleep(0.2)
                else:
                    ### The reboot function ###
                    ### Make sure to give yourself time by manually changing the amount of retries tello.py does ###
                    ### to more than 3 or even more if needed to connect to the drone without exiting the program. ###
                    ### WHERE TO FIND: "tello.py" l. 33 - RETRY_COUNT = X number of retries after a failed command. ###
                    ### ALSO: Make sure your computer automatically connects to you desired drone to make a smooth reboot. ###
                    me.streamoff()
                    me.reboot()
                    me.connect(wait_for_state=True)
                    me.streamon()

            ### 2 in 1: Will takeoff if not flying and land if flying ###
            if joystick.get_button(7) == 1:
                if me.is_flying == True:
                    me.send_command_with_return("land")
                    me.is_flying = False
                    time.sleep(0.2)
                else:
                    me.send_command_with_return("takeoff")
                    me.is_flying = True
                    time.sleep(0.2)

            ### This section lets you switch between the front camera and downward IR camera ###
            ### NOTE: The program start with using the front camera or 'downvision 0' ##
            if joystick.get_axis(4) < 0 and downvision == False:
                #me.set_video_direction(0)
                me.send_command_with_return('downvision 0')
                downvision = True
            elif joystick.get_axis(4) > 0 and downvision == True:
                #me.set_video_direction(1)
                me.send_command_with_return('downvision 1')
                downvision = False

            ### Utilizes the two joysticks and their axes as the four dimensions of travel for the Tello drone ###
            me.send_rc_control(int(joystick.get_axis(0) * 100), int(joystick.get_axis(1) * (-100)),
                               int(joystick.get_axis(3) * (-100)), int(joystick.get_axis(2) * 100))
        else:
            ### OPTIONAL: When tabbed out of the Pygame-window, the Tello drone will only do the following: (is set to rotate) ###
            me.send_rc_control(0, 0, 0, 20)

        ####################################################################################################
        ### The following covers the pygame-window "My game". This window will show input from the tello ###
        ####################################################################################################

        screen.fill(WHITE)
        textPrint.reset()

        data = me.get_current_state()
        data_string = data.values()

        # Conversion functions for state protocol fields
        ### Yoinked directly from the "tello.py" repository ###
        STATE_FIELDS = (
            # Tello EDU with mission pads enabled only
            'mid', 'x', 'y', 'z', 'mpry',
            # 'mpry': (custom format 'x,y,z')
            # Common entries
            'pitch', 'roll', 'yaw',
            'vgx', 'vgy', 'vgz',
            'templ', 'temph',
            'tof', 'h', 'bat', 'baro',
            'time', 'agx', 'agy', 'agz',

        )

        for i in range(len(data)):
            tello_data = list(data_string)[i]
            tello_info = list(STATE_FIELDS)[i]
            textPrint.tprint(screen, "tello {} value: {}".format(tello_info, str(tello_data)))
        textPrint.unindent()

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

        # Depending on your screen hz clock.tick can be adjusted.
        clock.tick(144)
### The following closes the two windows opened by the program once the pygame window is closed ###
pygame.quit()
cv2.destroyAllWindows()
