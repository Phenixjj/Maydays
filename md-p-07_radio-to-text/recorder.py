import subprocess
import os


class Recorder():
    def __init__(self, path: str, output: str):
        self.path = path
        self.output = output

    def convert_to_mp3(self):
        # Convert the audio file to wav format
        # command = ["ffmpeg", "-i", self.path, "-f", "segment", "-segment_time", "20", self.output]
        command = ["ffmpeg", "-i", self.path, "-t", "40",self.output]
        subprocess.run(command, check=True)
