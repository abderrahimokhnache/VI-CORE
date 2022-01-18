from datetime import datetime
from lib2to3.pytree import convert
from Qalm import json_pen
ctime = datetime.today()
strtof = "{:%A-%B-%d-%Y,%H:%M:%S}"

def last_diss():
    return Qalm.json_pen("utilities/disstree.json", "r")["tree"][-1]

def save_todisstree(tag,input_ , output):
    diss = {
        "tag" :tag,
        "input" : input_,
        'output' :output ,
        "@time": strtof.format(ctime)
    }
    json_pen("utilities/memory.json" ,"a" , diss , "tree")

def save_search_history(service, term):
    track = {'service': service, "term": term, "@time": strtof.format(ctime)}
    json_pen("Sandbox/dep/search_history.json", "a", track, "$schema")

def save_converstion_history(name,part):
    track = {"name": name,
     "part":[ part],
     "@time": strtof.format(ctime)}
    json_pen('Sandbox/dep/conversation_history.json',"a",track , "history")

def get_converstion_info(name,part):
    convert = json_pen('Sandbox/dep/conversation_history.json',"r")['history']
    for conv in convert :
        if conv['name'] == name:
            return True
