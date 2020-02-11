import pandas as pd
import numpy as np
import nltk
import os
import nltk.corpus

# sample text for performing tokenization
text = "In Brazil they drive on the right-hand side of the road. Brazil has a large coastline on the eastern side of South America"

# tokenization
# importing word_tokenize from nltk
from nltk.tokenize import word_tokenize
# Passing the string text into word tokenize for breaking the sentences
token = word_tokenize(text)
# print("list of token", token)
with open('token.txt', 'w') as f:
    print(token, file=f)

# finding the frequency distinct in the tokens
# Importing FreqDist library from nltk and passing token into FreqDist
from nltk.probability import FreqDist
fdist = FreqDist(token)
my_dict=dict()
for f in fdist:
    my_dict[f]=fdist[f]
with open('token_frequency.txt', 'w') as f:
    print(my_dict, file=f)

# To find the frequency of top 10 words
fdist1 = fdist.most_common(5)
# print("top 10 words", fdist1)
with open('token_top_10.txt', 'w') as f:
    print(fdist1, file=f)