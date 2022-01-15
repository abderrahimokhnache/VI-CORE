import os

def discription():
	discription_dict = {
            "tag": "third party apps",
            "patterns": ["open"],
            "responses": ["Done " , "Got it"]
            ,"exe-resp":False
        }
	return discription_dict 

def execute(master_input=""):
     app = master_input.replace('open',"start")
     print(app)
     os.system(app)
