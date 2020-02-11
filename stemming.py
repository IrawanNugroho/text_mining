# Importing Porterstemmer from nltk library
# Checking for the word ‘giving’
print("porter stemmer") 
from nltk.stem import PorterStemmer
pst = PorterStemmer()
pst.stem("waiting")
# print("waiting: ", pst.stem("waiting"))

# Checking for the list of words
stm = ["giving", "given", "gave"]
for word in stm :
   print(word+ ":" +pst.stem(word))

# Importing LancasterStemmer from nltk
print("\n\nlancaster stemmer")
from nltk.stem import LancasterStemmer
lst = LancasterStemmer()
stm = ["giving", "given", "gave"]
for word in stm :
 print(word+ ":" +lst.stem(word))