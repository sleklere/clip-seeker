import pytube
# import whisper
from faster_whisper import WhisperModel
import json
import os
from dotenv import load_dotenv
import time
import datetime

load_dotenv()

start_time = time.time()

# Config
video_url = os.getenv('VIDEO_URL')
audio_language = os.getenv('AUDIO_LANG')

video = pytube.YouTube(video_url)
audio = video.streams.get_audio_only()
audio.download(filename='tmp.mp4')

# whisper
# model = whisper.load_model('medium', device='cuda')
# result = model.transcribe('tmp.mp4',verbose=True,word_timestamps=True,language=audio_language)
                                            
# # Output to console, .txt and .json files
# print(result)
# f = open('test_transcript.txt', 'w')
# f.write(result['text'])
# json_filename = 'test_data.json'
# with open(json_filename, 'w') as f:
#     json.dump(result, f, indent=4)


# faster-whisper
model = WhisperModel('medium', device='cuda',compute_type='int8')
segments, info = model.transcribe('tmp.mp4',word_timestamps=True,language='es')
segments_list = list(segments)

filename = 'data/test_data'

f = open(filename + '.txt', 'w')
json_filename = filename + '.json'

result = {'text': '', 'segments': []}
result_text_only = ''

for segment in segments_list:
    print('[%.2fs -> %.2fs] %s' % (segment.start, segment.end, segment.text))
    formatted_segment = {'start': segment.start, 'end': segment.end,'text': segment.text}
    result['segments'].append(formatted_segment)
    result_text_only += segment.text

f.write(result_text_only)
with open(json_filename, 'w') as f:
    json.dump(result, f, indent=4)

print('Execution time: ' + datetime.timedelta(seconds= str(time.time() - start_time)))