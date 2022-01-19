import re

def clear(sent , wordlist) :
    newlist = [word for word in sent.split() if word not in wordlist]
    newsent = ''
    for word in newlist:
        newsent+=" "+word 
    return newsent




    

