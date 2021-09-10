# Script takes an input media file and can optionally trim
# from the start or end of a video clip.
#
# Command :
#    trim_video <path_to_filename> <start_offset> <end_offset>
#
# If you don't want a start or end offset, set them to 0.
#
# For example, if you want to trim 10 seconds off the start and
# 5 off the end, you'd do the following:
#    trim_video <path_to_filename> 10 5

import math
import subprocess
import sys

def get_duration(input_video):
    """Based on https://stackoverflow.com/a/62516360/1366973"""
    cmd = ["ffprobe", "-i", input_video, "-show_entries", "format=duration",
           "-v", "quiet", "-of", "csv=p=0"]
    return float(subprocess.check_output(cmd).decode("utf-8").strip())


def trim_video(input_filename, start_offset, length, output_filename):
    """Based on https://stackoverflow.com/a/62516360/1366973"""
    print('Trimming file...')
    cmd = ["ffmpeg", "-i", input_filename, "-ss", str(start_offset),
           "-t", str(length), "-c", "copy", "-hide_banner", "-loglevel",
           "error", output_filename]
    subprocess.call(cmd)
    print('File trimmed and saved as: ' + output_filename)

args = sys.argv
if len(args) != 4:
  print('Command requires exactly three arguments: file, start_offset, end_offset')
  sys.exit(0)

# TODO: Arg checking
filename = args[1]
start_offset = int(args[2])
end_offset = int(args[3])

duration = math.floor(get_duration(filename))
print('Duration of file: ' + str(duration))

length = duration - start_offset - end_offset

output_filename = filename[:-4] + '-truncated' + filename[-4:]

trim_video(filename, start_offset, length, output_filename)
