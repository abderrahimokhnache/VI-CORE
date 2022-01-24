import chunk
from nltk.tokenize import word_tokenize,sent_tokenize ,PunktSentenceTokenizer
from nltk.corpus import stopwords,state_union
from nltk.stem import PorterStemmer
import nltk
def token(inputs):
    # input = "hi vi what time is it"
    return (sent_tokenize(inputs))

def sw():
    text = "token is showing this shit"
    stop_words = set(stopwords.words("english"))
    words = word_tokenize(text)
    filtered = [w for w in words if w not in stop_words]
    print(filtered)

def stem():
    ps = PorterStemmer()
    ex = ['python' , 'pythoner' 'pythoning']
    text ='its very importent to be pythonly when you are pythoning with python'
    re = [ps.stem(w) for w in token(text)]
    print(re)


def partofspeechtagging():
    sample = state_union.raw("2005-GWBush.txt")
    train_sample = state_union.raw("2006-GWBush.txt")

    costum_set_token = PunktSentenceTokenizer(train_sample)
    tokenized = costum_set_token.tokenize(sample)
    chunkgram = r"""Chunk:{<.*>+}
                    }<VB.?|IN|DT>+{ """
    # chunkgram = r"""Chunk:{<RB.?>*<VB.?>*<NNP>+<NN>?}"""
    chunkparser = nltk.RegexpParser(chunkgram)
    for n,i in enumerate(tokenized):
        words = word_tokenize(i)
        tagged = nltk.pos_tag(words)
        chunked = chunkparser.parse(tagged)
        chunked.pretty_print()
        # print(dir(chunked))
        break


# words = word_tokenize('search for css in youtube')
# tagged = nltk.pos_tag(words)
# chunkgram = r"""Chunk:{<VB.?>*}"""
# chunkparser = nltk.RegexpParser(chunkgram)
# chunked = chunkparser.parse(tagged)
# print(chunked)

# sw()
# partofspeechtagging()
# stem()







postags = """
    CC coordinating conjunction
    CD cardinal digit
    DT determiner
    EX existential there (like: “there is” … think of it like “there exists”)
    FW foreign word
    IN preposition/subordinating conjunction
    JJ adjective ‘big’
    JJR adjective, comparative ‘bigger’
    JJS adjective, superlative ‘biggest’
    LS list marker 1)
    MD modal could, will
    NN noun, singular ‘desk’
    NNS noun plural ‘desks’
    NNP proper noun, singular ‘Harrison’
    NNPS proper noun, plural ‘Americans’
    PDT predeterminer ‘all the kids’
    POS possessive ending parent’s
    PRP personal pronoun I, he, she
    PRP$ possessive pronoun my, his, hers
    RB adverb very, silently,
    RBR adverb, comparative better
    RBS adverb, superlative best
    RP particle give up
    TO, to go ‘to’ the store.
    UH interjection, errrrrrrrm
    VB verb, base form take
    VBD verb, past tense took
    VBG verb, gerund/present participle taking
    VBN verb, past participle taken
    VBP verb, sing. present, non-3d take
    VBZ verb, 3rd person sing. present takes
    WDT wh-determiner which
    WP wh-pronoun who, what
    WP$ possessive wh-pronoun whose
    WRB wh-abverb where, when
"""



import re

exampleString = '''
Jessica is 15 years old, and Daniel is 27 years old.
Edward is 97 years old, and his grandfather, Oscar, is 102. 
'''

ages = re.findall(r'\d{1,3}',exampleString)
names = re.findall(r'[A-Z][a-z]*',exampleString)

# print(ages)
# print(names)

example = 'search for youtube hkjhk in duckduckgo'
re.findall(r'@([a-zA-Z]+)','gfgfdAAA1234ZZZuijjk')
finel = re.findall('(search for) (.*) (in) (.*)' ,example)
# print(finel)
# print(re.findall('(search for|look for|find) (.+) (in|on) (.+)', sample))


def partofspeechtagging():
    sample = state_union.raw("2005-GWBush.txt")
    train_sample = state_union.raw("2006-GWBush.txt")

    costum_set_token = PunktSentenceTokenizer(train_sample)
    tokenized = costum_set_token.tokenize(sample)
    for i in tokenized:
        words = word_tokenize(i)
        tagged = nltk.pos_tag(words)
        namedEnt = nltk.ne_chunk(tagged,binary= 1)
        namedEnt.draw()

# partofspeechtagging()
# sample="search for css animatation on youtube"
def lemtze():
    from nltk.stem import WordNetLemmatizer
    lem = WordNetLemmatizer()
    print(lem.lemmatize('better' , "a"))

# from nltk.corpus import gutenberg

# sample = gutenberg.raw('bible-kjv.txt')

# tok = sent_tokenize(sample)

# print(tok[5:15] )













