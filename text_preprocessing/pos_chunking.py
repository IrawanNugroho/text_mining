import nltk

def tokenization(text):
    list_token = nltk.word_tokenize(text.lower())
    return list_token

def my_pos(list_token):
    list_tags = nltk.pos_tag(list_token)
    return list_tags

def named_entity_recognition(list_tags):
    chunk = nltk.ne_chunk(list_tags)
    return chunk

def chunking(list_tags):
    reg = "NP: {<DT>?<JJ>*<NN>}" 
    a = nltk.RegexpParser(reg)
    result = a.parse(list_tags)
    return result

text = "We saw the yellow dog"
print(chunking(my_pos(tokenization(text))))


