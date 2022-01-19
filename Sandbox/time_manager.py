from datetime import datetime

date = datetime.today().date().strftime("%Y:%m:%d")
time=datetime.today().strftime("%H:%M %p")
P= datetime.today().strftime("%H:%M %p").split(' ')

def part_of_the_day(P , H):

    if P == "AM" :
        return 'morinig'

    elif P == "PM" and int(H) > 20 :
        return 'night'

    elif P == "PM" and int(H) < 15 :
        return 'afternoon'
    else :
        return "day"


def execute(e=''):
        return ["time", [f"it is {time} ", f"the time is {time}"]]
