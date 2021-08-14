# converting mp4 video to gif
from moviepy.editor import *

# enter the name of your .mp4 video here
video = VideoFileClip("video.mp4")
# add the name.gif in which you want your final gif
video.write_gif("final.gif")
