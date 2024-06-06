import os
from yt_dlp import YoutubeDL

playlist_url = "https://music.youtube.com/playlist?list=PL1l2jOpaFSXdEpnRtZhbw8rCS-DXlxzcr&si=Mho4NQRuj3UstBVe"

if not os.path.exists("youtube_music_playlist"):
    os.makedirs("youtube_music_playlist")

ydl_opts = {
    'outtmpl': 'youtube_music_playlist/%(title)s.%(ext)s',
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '320',
    }],
    'no_duplicates': True,
    'ignoreerrors': True,
}

with YoutubeDL(ydl_opts) as ydl:
    ydl.download([playlist_url])
    print("Download completed.")