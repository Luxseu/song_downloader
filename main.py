from pytube import YouTube, Playlist
import os.path
import math
import time
import re

W  = '\033[0m'  # white
R  = '\033[31m' # red
G  = '\033[32m' # green
O  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple

def playlist(url, i):
    p = Playlist(f'{url}')
    d = len(p.videos)
    for video in p.videos:
        i += 1
        prc = math.trunc((i / d * 100))
        single(f"https://www.youtube.com/watch?v={video.video_id}", 1, d, i, prc)
    start()

def single(url, G, d, i, prc):
    for y in range(5):
        video = YouTube(f'{url}')
        T = downloader(video, d, i, prc, False)
        if T == True:
            break
        else:
            print(f"{str(i)}/{str(d)} {str(prc)}%   {R}Failed, Retrying... ({y+1}){W}")
            time.sleep(0.5)
    if G == 0:
        start()

def downloader(video, d, i, prc, T):
    try:
        re_char = re.sub(r'[\/\\\:\"\?\*\|\<\>]', ' ', video.title)
        if os.path.exists(f"Songs/{re_char}.mp3") == True:
            print(f"{str(i)}/{str(d)} {str(prc)}%   {O}Already exists   {P}{re_char}.mp3{W}")
            T = True
        else:
            print("xd")
            x = video.streams.filter(only_audio=True).first()
            x.download(output_path="Songs", filename = re_char + ".mp3")
            print(f"{str(i)}/{str(d)} {str(prc)}%   {G}Downloaded{W}   {P}{re_char}.mp3{W}")
            T = True
    except:
        pass
    return T

def start():
    url = input("url:  ")
    word = "playlist"
    if url == "e":
        exit()
    elif word in url:
        playlist(url, 0)
    else:
        try:
            single(url, 0, 1, 1, 100)
        except:
            print("Invalid url")
            start()

start()