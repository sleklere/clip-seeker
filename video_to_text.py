import pytube
import whisper
import json
import os
from dotenv import load_dotenv

load_dotenv()

# Config
video_url = os.getenv('VIDEO_URL')
audio_language = os.getenv('AUDIO_LANG')
model = whisper.load_model("large", device="cuda")

video = pytube.YouTube(video_url)
audio = video.streams.get_audio_only()
audio.download(filename="tmp.mp4")

result = model.transcribe("tmp.mp4",verbose=True,word_timestamps=True,language=audio_language)

# Output to console, .txt and .json files
print(result)
f = open("transcript_large.txt", "w")
f.write(result["text"])
json_filename = 'test_data.json'
with open(json_filename, 'w') as f:
    json.dump(result, f, indent=4)