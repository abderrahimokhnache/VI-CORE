import re
def clear(sent , wordlist) :
    newlist = [word for word in sent.split() if word not in wordlist]
    newsent = ''
    for word in newlist:
        newsent+=" "+word 
    return newsent
def free(txt):
    subject_serv= txt.split("for")[1]
    subject_serv = subject_serv.split("on")
    subject = subject_serv[0]
    serv = subject_serv[1]
    return serv , subject

def get_context(sent):
    result = re.findall('(search for|look for|find) (.*) (in|on) (.*)' ,sent)[0]
    service = result[3]
    term = result[1]
    return service , term

    

