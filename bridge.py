from Core.CEREBRUM import Think
from utilities.spark import Listen ,Talk
from utilities.disstree import save



greet = Talk("Ready for you sir")
while True:
	input_ = Listen()
	output_process = Think(input_)
	Talk(output_process.output)
	save(output_process.tag,input_, output_process.output)

