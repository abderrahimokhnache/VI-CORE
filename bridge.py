from Core.CEREBRUM import Think
from utilities.spark import Listen ,Talk
from utilities.memory import save_todisstree

class wakeup:
	
	@staticmethod
	def onlyspeechrecog():
		greet = Talk("Ready for you sir")
		while True:
			input_ = Listen()
			output_process = Think(input_)
			Talk(output_process.output)
			save_todisstree(output_process.tag,input_, output_process.output)
	
	@staticmethod
	def cli(**karwgs):
		greet = print("Ready for you sir")
		while True:
			input_ = input("$ ")
			output_process = Think(input_)
			if karwgs['talk']:
				Talk(output_process.output)
			save_todisstree(output_process.tag,input_, output_process.output)
			print(output_process.output)
	
	@staticmethod
	def gui():
		pass

	@staticmethod
	def server():
		pass

if __name__ == "__main__":
		init =wakeup()
		init.onlyspeechrecog()