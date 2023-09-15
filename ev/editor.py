# pip install moviepy
import moviepy.editor as mp
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import time
import os

if os.name == 'nt':
    os.system("cls")
else:
    os.system("clear")
    
welcome = """
|||||             ~ Video Editor ~            |||||
 ||||          Coded By : AmirTyper           ||||
  |||        My Instagram : @amir_typer       |||
   ||       https://github.com/AmirTyper      ||
    |                    V1                   |
"""
print(welcome)
time.sleep(1)
print("|-| Options: (1)Cut - (2)Replace Audio - (3)Extract Audio")
time.sleep(1)
voroody = input("|+| What do you want me to do for you? : ")

#Voroody in Persian means Input
if voroody == "1":
    #Cut
    x = input(r"|+| Write the name of your video file: ")
    x2 = int(input("|+| Set start time (in sec): "))
    x3 = int(input("|+| Set end time (in sec): "))
    x4 = input("|+| Set the name of your output file (with .mp4 at the end of it): ")
    print("\n")
    ffmpeg_extract_subclip(x, x2, x3, targetname=x4)
    print(f"\n[+_+] Everything is Done. Your output file is {x4} [+_+]")

elif voroody == "2":
    #Replace  Audio
    x5 = input(r"|+| Write the name of your video file: ")
    x6 = input(r"|+| Write the name of your audio file: ")
    x7 = input("|+| Set the name of your output file (with .mp4 at the end of it): ")
    print("\n")
    videoclip = mp.VideoFileClip(x5)
    background_music = mp.AudioFileClip(x6)
    new_clip = videoclip.set_audio(background_music)
    new_clip.write_videofile(x7)
    print(f"\n[+_+] Everything is Done. Your output file is {x7} [+_+]")

elif voroody == "3":
    #Extract Audio
    x8 = input(r"|+| Write the name of your video file: ")
    x9 = input("|+| Set the name of your output file (with .mp3 at the end of it): ")
    print("\n")
    video = mp.VideoFileClip(x8)
    video.audio.write_audiofile(x9)
    print(f"\n[+_+] Everything is Done. Your output file is {x9} [+_+]")
else:
    print("|!!| Error! Check out your input. There are only 3 options. Run the script and try again.")


