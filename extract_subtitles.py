# Iterates through all mp4 files in the current folder and extacts
# their primary subtitle track as a .srt.

import os

video_extensions = [".mp4"]

cwd = os.getcwd()
for root, dirs, files in os.walk(cwd):
  for file in files:
    if any(file.endswith(extension) for extension in video_extensions):
      try:
        splittext = file.split('.')
        file_without_extension = splittext[0]
        subtitle_name = file_without_extension + ".srt"
        command = 'ffmpeg -i "' + file + '" "' + subtitle_name + '"'
        print(command)
        os.system(command)
      except Exception as e:
        print(e)
