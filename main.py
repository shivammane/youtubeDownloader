import pytube
import os
from pytube import YouTube
inputs = list(map(str, input("copy links here : ").split()))
for i in inputs:
    video_url = i
    youtube = pytube.YouTube(video_url)
    video = youtube.streams.get_by_resolution(resolution='720p')
    print("\nDownloading...: " + youtube.title)
    video.download(
        f'C:\\Users\\{os.getlogin()}\\New folder')
    print("video --", youtube.title, "--downloaded")
print("Done !!!")
