import os
import whisper

class SpeechToText():
    def __init__(self, dir_path: str):
        self.dir_path = dir_path

    def convert_and_transcribe(self):
        model = whisper.load_model("base")
        for filename in os.listdir(self.dir_path):
            if filename.endswith(".mp3"):
                result = model.transcribe(filename)
                print(result["text"])