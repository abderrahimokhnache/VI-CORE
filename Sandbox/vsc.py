from pynput import mouse, keyboard
from pynput.keyboard import Listener , Key
from utilities import spark
import time

kb = keyboard.Controller()
mouse = mouse.Controller()

def discription():
    discription_dict = {
            "tag": "system control",
            "patterns": [ "system control" ,"system control over voice" , "voice command","scov"],
            "responses": ["just opened" , 'starting ']
            ,"exe-resp":False
        }
    return discription_dict  

def execute(search_term =''):
    while True :
        voice =spark.Listen()
        if any([l for l in ["move left" ,"moved left" , "left","mov left"] if l in voice]) :
            mouse.move(-80,0)
        if  any([l for l in ["move right" ,"moved right" , "right","mov right"] if l in voice]) :
            mouse.move(80,0)
        if  any([l for l in ["typing" , "voice typing" ,'voice type' , 'type via voice' ,'type'] if l in voice]) :
            while "stop typing" not in spark.Listen() :
                voice= listen()
                if 'stop typing' in voice :
                    return 0
                else :
                    kb.type(voice)
        if 'click' in voice or "push" in voice:
            mouse.click(Button.left, 1)
        if 'click right' in voice or "push right" in voice:
            mouse.click(Button.right, 1)
        if 'scroll up' in voice :
            mouse.scroll(0, 2)
        if 'scroll down' in voice :
            mouse.scroll(0, -2)
        if 'exit system control' == voice or 'exit vsc' == voice :
            return 0
        else :pass
