from Core.CEREBRUM import Think
from utilities.spark import Listen ,Talk
from utilities.memory import save_todisstree

greet = Talk("Ready for you sir")

while True:

	input_ = Listen()
	output_process = Think(input_)
	Talk(output_process.output)
	save_todisstree(output_process.tag,input_, output_process.output)

