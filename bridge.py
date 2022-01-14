from Core.CEREBRUM import think
from utilities.spark import Listen ,Talk
from utilities.disstree import save

while True:
	input_ = Listen()
	output_process = think(input_)
	Talk(output_process.output)
	save(input_, output_process.output)

