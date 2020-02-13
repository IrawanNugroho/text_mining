import nltk

def tokenization(text):
    list_token = nltk.word_tokenize(text.lower())
    return list_token

def my_pos(list_token):
    return nltk.pos_tag(list_token)

def chunking(list_tags):
    return nltk.ne_chunk(list_tags)


text = "In 2017, we published our article 25 Chatbot Platforms: A Comparative Table"
print(chunking(my_pos(tokenization(text))))


