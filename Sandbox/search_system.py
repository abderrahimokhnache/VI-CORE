import webbrowser , re ,threading
from utilities.memory import save_search_history 

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
    trad=threading.Thread(target =webbrowser.get().open(url)).start()


def parse(sent):
    result = re.findall('(search for|look for|find) (.+) (in|on) (.+)' ,sent)[0]
    service = result[3]
    term = result[1]
    return service , term



def execute(search_term =''):
    try : 
        service , term  = parse(search_term)
        for tag in services :
            if tag['service'] == service:
                open_url(tag["url"]+term)
                save_search_history(service, term)
                return f'{service} search' ,[f"Here is what I found for {term} on {service}"]
    except IndexError :
        """add search service if not found in the dict"""
        return 'issue', ["sorry am having some issues with that try agein"]
    return 'unkown service', ["i can't access the service"]