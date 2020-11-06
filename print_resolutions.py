# Iterates recursively through the current directory and prints the resolution of any video files.

import ffmpeg
import os

video_extensions = [ ".avi", ".mkv", ".mp4"]

cwd = os.getcwd()
filenames = []
for root, dirs, files in os.walk(cwd):
  for file in files:
    if any(file.endswith(extension) for extension in video_extensions):
      path = os.path.join(root, file)
      probe = ffmpeg.probe(path)
      video_streams = [stream for stream in probe["streams"] if stream["codec_type"] == "video"]
      filenames.append(file + ' - ' + str(video_streams[0]['coded_width']) + "x" + str(video_streams[0]['coded_height']))

filenames.sort()

for filename in filenames:
  print(filename)
