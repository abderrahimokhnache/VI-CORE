import os

def execute(master_input=""):
     app = master_input.replace('open',"start")
     print(app)
     os.system(app)
