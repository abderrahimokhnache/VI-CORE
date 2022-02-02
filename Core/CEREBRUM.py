import random , Sandbox , os
from Qalm import json_pen
from nltk.tokenize import word_tokenize,sent_tokenize

class Think():

    def __init__(self,master_input):
        tag , response = Think.features_json(master_input)
        if not tag :
            tag,response = Think.noaction(master_input)
        elif not tag :
            """add other db"""
            tag, response = ("not categorized" , ["Not in the system"])
        self.output = random.choice(response)
        self.tag = tag


    @staticmethod
    def features_json(master_input):
        features_file = json_pen('Sandbox/dep/features.json', "r")['$schema']
        for feature in features_file :
            if Think.check_patterns_match(feature,master_input) :
                __import__('Sandbox.%s' % feature['feature'])
                teg_exe = Think.exec_and_return((f'Sandbox.{feature["feature"]}.execute("{master_input}")'))
                if feature["exe-resp"]:
                    return teg_exe 
                return (feature['feature'], feature['responses'])
        return (False , ["Not in features"])

    @staticmethod
    def noaction(master_input):
        load = json_pen("Sandbox/dep/intents.json",'r')
        for tag in load['intents'] :
            if Think.check_patterns_match(tag,master_input) :
                return(tag['tag'] , tag['responses'])
        return (None , ["Not in intents"])

    @staticmethod
    def check_patterns_match(tag,master_input):
        get_patter = lambda :[each_string.lower() for each_string in tag['patterns']]
        check = lambda: any([pattern in master_input for pattern in get_patter()])
        return check()

    @staticmethod
    def exec_and_return(expression):
        exec(f"""locals()['temp'] = {expression}""")
        return locals()['temp']
