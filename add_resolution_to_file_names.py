# Iterates recursively through the current directory and prints the resolution of any video files.

import ffmpeg
import os
import re

video_extensions = ['.mkv', '.avi', '.mp4']

# These directories don't use the proper plex naming format yet.
excludes = []

cwd = os.getcwd()
filenames = []
for root, dirs, files in os.walk(cwd):
  if any(exclude in root for exclude in excludes):
    continue
  for file in files:
    if re.search('\.(\d)+p\.', file):
      continue
    if any(file.endswith(extension) for extension in video_extensions):

      path = os.path.join(root, file)
      print(path)
      try:
        probe = ffmpeg.probe(path)
        video_streams = [stream for stream in probe["streams"] if stream["codec_type"] == "video"]
        height = str(video_streams[0]['height'])

        splittext = os.path.splitext(os.path.basename(file))
        file_without_extension = splittext[0]
        file_extension = splittext[1]
        updated_path = os.path.join(root, file_without_extension+"."+height+'p'+file_extension)
        existing_path = os.path.join(root, file)
        print("Renaming: " + existing_path + " to " + updated_path)
        os.rename(existing_path, updated_path)
      except Exception as e:
        print(e)
