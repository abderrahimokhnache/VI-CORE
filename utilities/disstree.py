from datetime import datetime
from Qalm import json_pen
ctime = datetime.today()
strtof = "{:%A-%B-%d-%Y,%H:%M:%S}"

def save(input_ , output):
    diss = {
        "input" : input_,
        'output' :output ,
        "@time": strtof.format(ctime)
    }
    json_pen("utilities/disstree.json" ,"a" , diss , "tree")

 