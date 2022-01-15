from tkinter.tix import Tree
import webbrowser , re ,wikipedia , threading
import Qalm
def discription():
    discription_dict = {
            "tag": "search",
            "patterns": [ "search for" ,"google it",
            "look for" , "find","search" ],
            "responses": ["here's what i found" , 'there you go']
            ,"exe-resp":True
        }

    return discription_dict  

def execute(search_term =''):
    if "google it" in search_term :
        tree =Qalm.json_pen("utilities/disstree.json" , "r")["tree"][-1]['input']
        url = "https://google.com/search?q=" + tree
        webbrowser.get().open(url)
        return "google search" ,f"Here is what I found for {tree} on google"        


    if len(search_term) == len("search") :
        return None

    if "search" in search_term and 'youtube' not in search_term:
        search_term = search_term.split("for")[-1]
        url = "https://google.com/search?q=" + search_term
        webbrowser.get().open(url)
        return "google search" ,f"Here is what I found for {search_term} on google"

    if "youtube" in search_term:
        search_term = search_term.split("for")[-1]
        search_term = search_term.replace("on youtube","")
        url = f"https://www.youtube.com/results?search_query={search_term}"
        webbrowser.get().open(url)
        return 'youtube search' ,f"Here is what I found for {search_term} on youtube"
