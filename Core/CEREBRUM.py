import random , Sandbox , os
from tabnanny import check
from Qalm import json_pen
from nltk.tokenize import word_tokenize,sent_tokenize

class Think():
    check = lambda master_input,patterns :any([pattern in master_input for pattern in patterns])
    get_patter = lambda tag :[each_string.lower() for each_string in tag['patterns']]

    def __init__(self,input_):
        tag , response = Think.features_json(input_)
        if tag == None :
            tag,response = Think.noaction(input_)
        if tag == None:
            """add other db"""
            tag, response = ("not categorized" , ["Not in the system"])

        self.output = random.choice(response)
        self.tag = tag
    @staticmethod
    def features_json(master_input=''):
        features_file = json_pen('Sandbox/dep/features.json', "r")['$schema']
        for feature in features_file :
            if Think.check(master_input,Think.get_patter(feature)) :
                __import__('Sandbox.%s' % feature['tag'])
                teg_exe = Think.exec_and_return((f'Sandbox.{feature["tag"]}.execute("{master_input}")'))
                if feature["exe-resp"]:
                    return teg_exe
                return (feature['feature'], feature['responses'])

				
    @staticmethod
    def features(master_input=''):
        for file in os.listdir(Sandbox.__path__[0]):
            if ".py" in file and "__init__" not in file  :
                model = file.split(".")[0]
                __import__('Sandbox.%s'%model)
                tag =(Think.exec_and_return(('Sandbox.%s.discription()'%model)))
                if Think.check(master_input,Think.get_patter(tag)) :
                    teg_exe = Think.exec_and_return((f'Sandbox.{model}.execute("{master_input}")'))
                    if tag["exe-resp"]:
                        return teg_exe
                    return(tag['tag'] , tag['responses'])

        return (None , ["Not in features"])

    @staticmethod
    def noaction(master_input):
        load = json_pen("Sandbox/dep/intents.json",'r')
        for tag in load['intents'] :
            if Think.check(master_input,Think.get_patter(tag)) :
                return(tag['tag'] , tag['responses'])
        return (None , ["Not in intents"])

    @staticmethod
    def NLP(sentence):
        prrocess1= "what type of sentence is it"
        process2 = "is it an action"

    @staticmethod
    def exec_and_return(expression):
        exec(f"""locals()['temp'] = {expression}""")
        return locals()['temp']
