import re
import json
import datetime

class bcolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"

json_file = open("test_data_1.json", "r")
result = json.load(json_file)


def split_sentences(text):
  return re.split(r'(?<=[.!?])\s+', text)  

def color_string(color, string):
  return color + string + bcolors.ENDC

def color_str_in_text(str, text, color):
  return text.replace(str, color_string(color, str))

def format_time(seconds):
  return datetime.timedelta(seconds=seconds)

def search(str, segments_list):
  print("\n")
  for segment in segments_list:
    segment_text = segment["text"]

    if str in segment_text:
      # format output
      colored_str = color_string(bcolors.OKGREEN, str)
      segment_text = segment_text.replace(str, colored_str)
      timestamp = format_time(segment["start"])

      print(f'String {colored_str} at [{timestamp}]: ', segment_text)
      print("")
  print("\n")

search("desarrollador", result["segments"])
