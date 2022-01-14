import json , random , Core.Sandbox , os
from Qalm import json_pen
from utilities.logger import logerr

class Think():
	
	def __init__(self,input_):
		try :
			tag , response = Think.tokenize(input_)
		except Exception as e :
			logerr(e)
			tag , response = "unknown" , ["Sorry i didn't get that !"] 
		self.output = random.choice(response)
		self.tag = tag

	@staticmethod
	def tokenize(master_input=''):
		load = json_pen("Core/Sandbox/dep/intents.json",'r')
		check = lambda master_input,patterns :any([pattern in master_input for pattern in patterns]) 
		get_patter = lambda tag :[each_string.lower() for each_string in tag['patterns']]
		
		for tag in load['intents'] :
			#see if the input in the intents file
			if check(master_input,get_patter(tag)) :
		 		return(tag['tag'] , tag['responses'])

		#see if the input in any of the skills discription
		for file in os.listdir(Core.Sandbox.__path__[0]):
			if ".py" in file and "__init__" not in file  :
				#getting the model name
				model = file.split(".")[0]
				#importing the model
				__import__('Core.Sandbox.%s'%model)
				#gettting the discription dict
				tag =(Think.exec_and_return(('Core.Sandbox.%s.discription()'%model)))
				#looking for hte user input inside the dict patterns 
				if check(master_input,get_patter(tag)) :
						#if there's a match the userinput will be giving as an arg for the execute func
						eval((f'Core.Sandbox.{model}.execute(master_input)'))
						return(tag['tag'] , tag['responses'])
	@staticmethod
	def exec_and_return(expression):
	    exec(f"""locals()['temp'] = {expression}""")
	    return locals()['temp']


