
import sys
from Core.CEREBRUM import Think
from utilities.spark import Listen ,Talk
from utilities.memory import save_todisstree
class wakeup:

    @staticmethod
    def onlyspeechrecog():
        greet = Talk("Ready for you sir")
        while True:
            input_ = Listen()
            if input_ != " ":
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
    try:
        if sys.argv[1] == "cli":
            init.cli(talk =sys.argv[2])
    except :
        if sys.argv[1] != "cli":
            init.onlyspeechrecog()
