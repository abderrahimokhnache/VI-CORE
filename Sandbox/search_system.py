import webbrowser , re ,threading
from utilities.memory import get_converstion_info, save_search_history ,last_diss ,save_converstion_history

def discription():
    discription_dict = {
            "tag": "search",
            "patterns": [ "search for" ,"google it",
            "look for" , "find","search" ],
            "exe-resp":True
        }

    return discription_dict

services = [
    {"service":'youtube',
    'url' :"https://www.youtube.com/results?search_query="},
    {'service' :'google',
    'url':"https://google.com/search?q="}
]

def open_url(url):
    threading.Thread(target =webbrowser.get().open(url)).start()

def parse(sent):
    result = re.findall('(search for|look for|find) (.*) (in|on) (.*)' ,sent)[0]
    service = result[3]
    term = result[1]
    return service , term


from datetime import datetime

ctime = datetime.today()
strtof = "{:%H%M%S}"
ctime =int(strtof.format(ctime))

def execute(search_term =''):
    check = get_converstion_info("expact search", -1)
    if check :
        open_url('https://google.com/search?q='+search_term)
        return f'google search' ,[f"Here is what I found for {search_term} on google"]

    try :
        service , term  = parse(search_term)
        for tag in services :
            if tag['service'] == service:
                open_url(tag["url"]+term)
                save_search_history(service, term)
                return f'{service} search' ,[f"Here is what I found for {term} on {service}"]
    except IndexError  :
        if search_term =="search":
            save_converstion_history('expact search',"expaction")

            return "expact search" , ["what do you want to search for !"]

    return 'unkown service', ["i can't access the service"]

    if "google it" in search_term :
        tree = last_diss()['input']
        url = "https://google.com/search?q=" + tree
        webbrowser.get().open(url)
        return "google search" ,[f"Here is what I found for {tree} on google"]