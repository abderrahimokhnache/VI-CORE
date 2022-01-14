import speech_recognition as sr , playsound ,random ,os
from gtts import gTTS
from Qalm import pen_head

def Listen():
    try:
        r = sr.Recognizer() 
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration =0.10)
            audio = r.listen(source,10*100,10*100)
            master_input = r.recognize_google(audio)  # convert audio to text
    except Exception as e:
        pen_head("issues.log" ,"w" ,e.message)
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
        pen_head("issues.log" ,"w" ,e.message)