# from ffpyplayer.player import MediaPlayer
# import time

# player = MediaPlayer(".\\audio\\out.mp3")
# # val = ''
# # while val !='eof':
# #     frame, val = player.get_frame(show=False)
# player.close_player()
import wave

from playsound import playsound
from genaudio import Genaudio

Genaudio().generate("WELCOME")
playsound("./audio/out.mp3")