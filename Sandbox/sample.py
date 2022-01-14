import webbrowser

def discription():
    discription_dict = {
            "tag": "exact location",
            "patterns": [ "what is my exact location" ,"exact location" ],
            "responses": ["You must be somewhere near here, as per Google maps" , 'You should be here']
        }
    return discription_dict  

def execute(e=""):
        url = "https://www.google.com/maps/search/Where+am+I+?/"
        webbrowser.get().open(url)