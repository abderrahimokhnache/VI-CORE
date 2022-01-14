import webbrowser , re ,wikipedia , threading
from requests.exceptions import ConnectionError


def discription():
    discription_dict = {
            "tag": "search",
            "patterns": [ "search for" ,"googleit","wiki","wikipedia",
            "look for" , "find","search" , 'youtube' , 'google' ],
            "responses": ["here's what i found" , 'there you go']
        }

    return discription_dict  

def execute(search_term =''):
    if "search" in search_term and 'youtube' not in search_term:
        search_term = search_term.split("for")[-1]
        url = "https://google.com/search?q=" + search_term
        webbrowser.get().open(url)
        return "google" ,("Here is what I found for" + search_term + "on google")

    if "youtube" in search_term:
        search_term = search_term.split("for")[-1]
        search_term = search_term.replace("on youtube","").replace("search","")
        url = "https://www.youtube.com/results?search_query=" + search_term
        webbrowser.get().open(url)
        return 'youtube' ,("Here is what I found for " + search_term + "on youtube")