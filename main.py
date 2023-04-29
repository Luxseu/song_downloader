from pytube import YouTube, Playlist
import os.path
import math
import time
import re

def playlist(url, i):
    p = Playlist(f'{url}')
    d = len(p.videos)
    for video in p.videos:
        i += 1
        prc = math.trunc((i / d * 100))
        T = single(f"https://www.youtube.com/watch?v={video.video_id}", 1, d, i, prc)
    start()

def single(url, G, d, i, prc):
    for y in range(10):
        try:
            video = YouTube(f'{url}')
            T = downloader(video, d, i, prc, False)
        except:
            time.sleep(0.5)
        if T == True:
            break
        else:
            print(f"{str(i)}/{str(d)} {str(prc)}%   Failed, Retrying... ({y+1})")
    if G == 0:
        start()
    else:
        return True

def downloader(video, d, i, prc, T):
    try:
        re_char = re.sub(r'[\/\\\:\"\?\*\|\<\>]', ' ', video.title)
        if os.path.exists(f"Songs/{re_char}.mp3") == True:
            print(f"{str(i)}/{str(d)} {str(prc)}%   Downloaded   {re_char}.mp3")
            T = True
        else:
            x = video.streams.filter(only_audio=True).first()
            x.download(output_path="Songs", filename = re_char + ".mp3")
            print(f"{str(i)}/{str(d)} {str(prc)}%   Downloaded   {re_char}.mp3")
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