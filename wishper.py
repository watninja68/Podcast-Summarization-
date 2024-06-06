import whisper
import requests
from pydub import AudioSegment
import librosa
import numpy as np

model = whisper.load_model("base")

def download_audio(url, save_path):
    response = requests.get(url)
    with open(save_path, 'wb') as file:
        file.write(response.content)

def split_audio(audio, chunk_length_ms=60000):
    chunks = []
    duration_ms = len(audio)
    for start in range(0, duration_ms, chunk_length_ms):
        end = min(start + chunk_length_ms, duration_ms)
        chunks.append(audio[start:end])
    return chunks

def transcribe_chunk(chunk):
    chunk.export("chunk.mp3", format="mp3")
    y, sr = librosa.load("chunk.mp3", sr=None)
    response = model.transcribe(y)
    print(response["text"])
    return response["text"]

def transcribe_long_audio(file_path, chunk_length_ms=60000):
    audio = AudioSegment.from_file(file_path)
    chunks = split_audio(audio, chunk_length_ms)
    full_transcription = ""

    for i, chunk in enumerate(chunks):
        print(f"Transcribing chunk {i + 1} of {len(chunks)}")
        transcription = transcribe_chunk(chunk)
        full_transcription += transcription + " "
    return full_transcription.strip()

url = "https://huggingface.co/datasets/reach-vb/random-audios/resolve/main/4469669-10.mp3"
file_path = "downloaded_audio.mp3"

download_audio(url, file_path)

transcription = transcribe_long_audio(file_path)
print(transcription)
