import speech_recognition as sr , playsound ,random ,os
from gtts import gTTS
# from utilities.logger import log
from urllib import request

def Listen():
    master_input = " "
    try:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)
            master_input = r.recognize_google(audio)
    except Exception as e:
        # log(e)
        pass
    return master_input.lower()


def Talk(master_input):

    try :
        master_input = str(master_input)
        tts = gTTS(text=master_input, lang='en')
        r = random.randint(1,20000000)
        audio_file = 'temp' + str(r) + '.mp3'
        tts.save(audio_file)
        playsound.playsound(audio_file)
        os.remove(audio_file)
    except Exception as e:
        # log(e)
        pass