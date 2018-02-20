#encoding=utf-8
import wave
from pyaudio import PyAudio,paInt16
from aip import AipSpeech
import win32api

framerate=16000
NUM_SAMPLES=2000
channels=1
sampwidth=2
TIME=5
chunk=2014

APP_ID="10838516"
API_KEY="KQskXIDQaZ8L8kiqgpnKutrg"
SECRET_KEY="msFNNbMZs88FdGSjRR06Lu4rj16ya983"

client=AipSpeech(APP_ID,API_KEY,SECRET_KEY)

def save_wave_file(filename,data):
    '''save the date to the wavfile'''
    wf=wave.open(filename,'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(sampwidth)
    wf.setframerate(framerate)
    wf.writeframes(b"".join(data))
    wf.close()

def my_record():
    pa=PyAudio()
    stream=pa.open(format = paInt16,channels=1,
                   rate=framerate,input=True,
                   frames_per_buffer=NUM_SAMPLES)
    my_buf=[]
    count=0
    while count<TIME*5:#控制录音时间
        string_audio_data = stream.read(NUM_SAMPLES)
        my_buf.append(string_audio_data)
        count+=1
        print('.')
    save_wave_file('01.wav',my_buf)
    stream.close()


def play():
    wf=wave.open(r"01.wav",'rb')
    p=PyAudio()
    stream=p.open(format=p.get_format_from_width(wf.getsampwidth()),channels=
    wf.getnchannels(),rate=wf.getframerate(),output=True)
    while True:
        data=wf.readframes(chunk)
        if data=="":break
        stream.write(data)
    stream.close()
    p.terminate()
# 读取文件
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()
    
if __name__ == '__main__':
    my_record()
    print('Over!') 
    play()
    a=client.asr(get_file_content('01.wav'), 'wav', 16000, {'lan': 'zh',})
    print a
    key=a.get('result')[0]
    
    if '百度'in key:
        win32api.ShellExecute(0,'open','http://www.baidu.com','','',1)
    elif '邮箱'in key:
        win32api.ShellExecute(0,'open','http://mail.126.com','','',1)
