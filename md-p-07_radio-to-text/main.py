from recorder import Recorder
from pydub import AudioSegment
from pydub.silence import split_on_silence
import whisper
import time
import os
import glob


path = "https://audio.bfmtv.com/bfmbusiness_128.mp3?aw_0_1st.playerId=BFMBusiness_audio_web&aw_0_1st.aggregator=BFMBusiness_audio_web"
timestamp = time.strftime("%Y%m%d-%H%M%S")
output = f"./output/output_{timestamp}.mp3"

if __name__ == "__main__":
    rec = Recorder(path=path, output=output)
    rec.convert_to_mp3()

    sound_file = AudioSegment.from_mp3(output)
    audio_chunks = split_on_silence(sound_file, min_silence_len=1000, silence_thresh=-40 )
    count = len(audio_chunks)
    print("Audio split into " + str(count) + " audio chunks \n")

    # Call Whisper to transcribe audio
    model = whisper.load_model("base")
    transcript = ""
    for i, chunk in enumerate(audio_chunks):
        # If you have a long audio file, you can enable this to only run for a subset of chunks
        if i < 10 or i > count - 10:
            out_file = "chunk{0}.wav".format(i)
            print("\r\nExporting >>", out_file, " - ", i, "/", count)
            chunk.export(out_file, format="wav")
            result = model.transcribe(out_file)
            transcriptChunk = result["text"]
            print(transcriptChunk)
            
            # Append transcript in memory if you have sufficient memory
            transcript += " " + transcriptChunk
            

    #clear the chunk files
    for filename in glob.glob('*.wav'):
        os.remove(filename)

    for filename in glob.glob('output/*.mp3'):
        os.remove(filename)

    # Print the transcript
    print("Transcript: \n")
    print(transcript)
    print("\n")

