from Core.CEREBRUM import think
from utilities.spark import Listen ,Talk


while True:
	output =Listen()
	output_process = think(output)
	Talk(output_process.output)
