import re
import json
import datetime
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class TextFormatter:

  @staticmethod
  def color_string(color, string):
      return color + string + bcolors.ENDC

class DataAnalyzer:
  def __init__(self, filepath):
    with open(filepath, 'r') as file:
       self.data = json.load(file)

  @staticmethod
  def split_sentences(text):
      return re.split(r'(?<=[.!?])\s+', text)

  def search(self, substring):
    print('\n')
    for segment in self.data['segments']:
      if substring in segment['text']:
        colored_str = TextFormatter.color_string(bcolors.OKGREEN, substring)
        segment_text = segment['text'].replace(substring, colored_str)
        timestamp = datetime.timedelta(seconds=segment['start'])

        print(f'String {colored_str} at [{timestamp}]: ', segment_text)
        print('')
    print('\n')


analyzer = DataAnalyzer('data/salarios_abril.json')
analyzer.search('programador')
analyzer.search('comerc')
