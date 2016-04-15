# encoding = utf-8

# use pyAudio
# brew install portaudio
# pip install pyaudio

import wave, pyaudio
from datetime import datetime
from tools import dxbaiduaudio
import webbrowser

CHUNK = 1024
FORMAT = pyaudio.paInt16
RATE = 8000
CHANNELS = 1
RECORD_SECONDS = 5

def record_wave(to_dir=None):
    if to_dir is None:
        to_dir = "./"

    pa = pyaudio.PyAudio()
    stream = pa.open(format = FORMAT,
                     channels = CHANNELS,
                     rate = RATE,
                     input = True,
                     frames_per_buffer = CHUNK)

    print("* recording")

    save_buffer = []
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        audio_data = stream.read(CHUNK)
        save_buffer.append(audio_data)

    print("* done recording")

    # stop
    stream.stop_stream()
    stream.close()
    pa.terminate()

    # wav path
    file_name = datetime.now().strftime("%Y-%m-%d_%H_%M_%S")+".wav"
    if to_dir.endswith('/'):
        file_path = to_dir + file_name
    else:
        file_path = to_dir + "/" + file_name

    # save file
    wf = wave.open(file_path, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(pa.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    # join 前的类型
    wf.writeframes(b''.join(save_buffer))
    wf.close()

    return file_path

def browser_open_text(text):
    if text is None:
        return

    url = "http://www.baidu.com"
    if text.startswith("谷歌") or text.startswith("google"):
        url = "http://www.google.com"
    elif text.startswith("必应") or text.startswith("bing"):
        url = "http://cn.bing.com"

    webbrowser.open_new_tab(url)

if __name__ == "__main__":
    to_dir = "./"
    file_path = record_wave(to_dir)

    text = dxbaiduaudio.wav_to_text(file_path)
    browser_open_text(text)
