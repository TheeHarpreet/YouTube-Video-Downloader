from pytubefix import YouTube
from sys import argv

#takes all of the things you input into the command line so [1] takes the first line in command
link = argv[1]
yt = YouTube(link)

print("Title: ", yt.title)

ytVidDownload = yt.streams.get_highest_resolution()

ytVidDownload.download('C:/Users/Aman/Videos/Download YT Videos')