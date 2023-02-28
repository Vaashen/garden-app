import spacy

nlp = spacy.load('en_core_web_sm')

gardenpathSentences = [
    "The complex houses married and single soldiers and their families.",
    "The horse raced past the barn fell.",
    "The man wistling tunes pianos", 
    "The government plans to raise taxes were defeated",
    'The complex houses married and single soldiers and their families'
]

for x in gardenpathSentences:
    doc = nlp(x)

    [token.orth_ for token in doc]
    print([(token, token.orth_, token.orth) for token in doc])
    
    print([(w.text, w.pos_) for w in doc])


# Entity 1
# CCONJ - coordinating conjunction
# #it made sense because it is being used to connect the words in the sentence

# Entity 2
# PART - particular
# in a sense it does make sense, because the content of the sentence is referring to thegovernment plans  
