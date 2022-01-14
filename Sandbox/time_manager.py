from datetime import datetime

date = datetime.today().date().strftime("%Y:%m:%d")
time=datetime.today().strftime("%H:%M %p")
P= datetime.today().strftime("%H:%M %p").split(' ')

def discription():
	discription_dict = {
            "tag": "time",
            "patterns": [ "what time is it" , "time" , "what's the time" ],
            "responses": [ f"it is {time} ", f"the time is {time} " ]
        }
	return discription_dict

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

	return part_of_the_day(P[1] ,P[0].split(':')[0] ) , time , date
