from datetime import datetime
from Qalm import json_pen
ctime = datetime.today()
strtof = "{:%A-%B-%d-%Y,%H:%M:%S}"

def save_todisstree(tag,input_ , output):
    diss = {
        "tag" :tag,
        "input" : input_,
        'output' :output ,
        "@time": strtof.format(ctime)
    }
    json_pen("utilities/memory.json" ,"a" , diss , "tree")
def save_():
    """
    todo
    """

    pass
 