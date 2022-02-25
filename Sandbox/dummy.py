from utilities.text_op import clear
import clipboard
from PIL import ImageGrab

def execute(master_input=""):
    master_input=clear(master_input , ["hi" , "dummy"])
    if 'random png' in master_input :
        clipboard.copy("random png")
        return("dummy" ,["random png"])
    if "random image" in master_input :
        image = ImageGrab.grabclipboard()
        image.save('clipboard.jpg','JPG')
        return("dummy" ,["random png"])