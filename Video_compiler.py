import cv2
import os
import time


### Run this function directly to convert langer amounts of images to video ###
def image_to_video():

    ### Select a folder which images shall be compiled to a video ###
    image_folder = 'Resources/Video/1650101797.8316865'

    ### Select a name for your video - time is currently included ###
    ### NOTE: If desired, remove the section "_{time.time()}" to remove time from video name ###
    video_name = 'Video'

    images = [img for img in os.listdir(image_folder) if img.endswith(".jpg")]
    frame = cv2.imread(os.path.join(image_folder, images[0]))
    height, width, layers = frame.shape

    ### Explaination: cv2.videoWriter([Video location + video name], 0, [Framerate: 30], [resolution: size] ###
    ### NOTE: To move video compiling location, edit {dirNameVid} and select another location for location of the compiled video ###
    video = cv2.VideoWriter(f'Resources/Video/{video_name}_{time.time()}.avi', 0, 30, (width, height))

    for image in images:
        video.write(cv2.imread(os.path.join(image_folder, image)))

    cv2.destroyAllWindows()
    video.release()

image_to_video()