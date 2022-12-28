import subprocess

linksFile = open('piese.txt', 'r')
links = linksFile.readlines()

for link in links:
    print('STEFAN### Dowloading current link ' + link)
    subprocess.run(["youtube-dl", "-x", "--audio-format", "mp3", "-o", "output\\%(title)s.%(ext)s", link])
    