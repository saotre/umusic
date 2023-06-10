from pydub import AudioSegment
import io


def wav_to_mp3(wav_data: bytes, path_to_mp3: str):
    s = io.BytesIO(wav_data)
    AudioSegment.from_wav(s).export(path_to_mp3, format="mp3")
