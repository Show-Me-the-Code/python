# make with baudi SDK
import requests
import pyaudio
import wave
import base64
import json
import win32api

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 8000
RECORD_SECONDS = 3
WAVE_OUTPUT_FILENAME = "out.wav"


def make_audio():
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)
    print('*recording')
    frames = []
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)
    print('*done recording')
    stream.stop_stream()
    stream.close()
    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()


CC_URL = "https://openapi.baidu.com/oauth/2.0/token?" \
         "grant_type=client_credentials&" \
         "client_id=&" \
         "client_secret=&"

TOKEN = ""
API = 'http://vop.baidu.com/server_api'


def get_token():
    resp = requests.post(CC_URL)
    print(resp.json())


def speech_to_text():
    with open(WAVE_OUTPUT_FILENAME, 'rb') as file:
        data = file.read()
    params = {
        "format": 'wav',
        "rate": RATE,
        "channel": CHANNELS,
        "token": TOKEN,
        "cuid": "",
        "len": len(data),
        "speech": base64.b64encode(data).decode(),
    }

    headers = {
        'Content-Type': 'application/json;',
    }
    resp = requests.post(url=API, data=json.dumps(params), headers=headers)
    # print(resp.json())
    return resp.json()['result']


def make_action(texts):
    maps = {
        '百度': 'http://www.baidu.com',
        '网易': 'http://www.163.com'
    }
    target = ''
    for text in texts:
        if text.find('百度') != -1:
            target = '百度'
        elif text.find('网易') != -1:
            target = '网易'
    if target:
        win32api.ShellExecute(0, 'open', maps[target], '', '', 1)
    else:
        print('Match failed:', texts)


if __name__ == '__main__':
    make_audio()
    texts = speech_to_text()
    make_action(texts)