import json , random , Sandbox , os
from Qalm import json_pen
from utilities.logger import logerr

class Think():
	check = lambda master_input,patterns :any([pattern in master_input for pattern in patterns]) 
	get_patter = lambda tag :[each_string.lower() for each_string in tag['patterns']]	
	def __init__(self,input_):

		tag , response = Think.features(input_)
		self.output = random.choice(response)
		self.tag = tag

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
		return (master_input , ["Not in the system"])
		
	@staticmethod
	def noaction(master_input):
		load = json_pen("Sandbox/dep/intents.json",'r')
		for tag in load['intents'] :
			if Think.check(master_input,Think.get_patter(tag)) :
		 		return(tag['tag'] , tag['responses'])

	@staticmethod
	def exec_and_return(expression):
	    exec(f"""locals()['temp'] = {expression}""")
	    return locals()['temp']


