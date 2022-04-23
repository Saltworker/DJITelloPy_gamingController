import cv2
import os
import time


### Run this function directly to convert langer amounts of images to video ###
def image_to_video(imagefolder, videoname, fps):

    ### Select a folder which images shall be compiled to a video ###
    image_folder = f'Resources/Video/{imagefolder}'

    ### Select a name for your video - time is currently included ###
    ### NOTE: If desired, remove the section "_{time.time()}" to remove time from video name ###
    video_name = videoname

    images = [img for img in os.listdir(image_folder) if img.endswith(".jpg")]
    frame = cv2.imread(os.path.join(image_folder, images[0]))
    height, width, layers = frame.shape

    ### Explaination: cv2.videoWriter([Video location + video name], 0, [Framerate: 30], [resolution: size] ###
    ### NOTE: To move video compiling location, edit {dirNameVid} and select another location for location of the compiled video ###
    video = cv2.VideoWriter(f'Resources/Video/{video_name}_{time.time()}.avi', 0, fps, (width, height))

    for image in images:
        video.write(cv2.imread(os.path.join(image_folder, image)))

    cv2.destroyAllWindows()
    video.release()

### NOTE: tello default framerate = 'middel' = 15 ###
### tello framerate in the program 'Tello_gamingcontroller' is 'high' = 30 ###
### Resolution is relatively irrelevant in terms of video quality. ###
### HOWEVER it can somewhat be used as a zoom-function ###
### Bitrate (Mbps) can be played around with. If the camera footage isn't of importance: ###
### Leave it in auto (default) to prevent you tello camera POV from freezing. ###

### EXAMPLES: ###############################################
#image_to_video(1650101797.8316865, 'Testflight', 15)       #
#image_to_video(1650722894.7688913, 'golfcourse_11', 15)    #
#image_to_video(1650723203.147218, 'golfcourse_12', 15)     #
#image_to_video(1650723223.528957, 'golfcourse_13', 15)     #
#############################################################
