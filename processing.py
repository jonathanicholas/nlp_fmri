from nltk.stem import WordNetLemmatizer
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
import string

'''
functions to process documents. Performs preprocessing and then returns document
as dict: documents[document] = list of words
'''

def preProcess(word):
    lemmatizer = WordNetLemmatizer()
    stemmer = PorterStemmer()
    punctuation = set(string.punctuation)
    word = word.lower() # make all words lowercase
    word = ''.join(char for char in word if char not in punctuation) #remove punctuation
    word = word.rstrip()
    word = unicode(word, errors='ignore')
    #word = lemmatizer.lemmatize(word) #run lemmatizer and stemmer (questionable performance)
    #word = stemmer.stem(word)
    if word not in stopwords.words("english"): #remove stopwords
        return word
    else:
        return False

def getDocuments(texts, delimiter):
    documents = {}
    for text in texts:
        index = 0
        words = []
        print "Processing words in %s..." %(text)
        script = open(text, 'r')
        if delimiter == ',':
            for word in script.read().split(','):
                index += 1
                word = preProcess(word)
                if word:
                    words.append(word)
        else:
            for word in script.read().split():
                index += 1
                word = preProcess(word)
                if word:
                    words.append(word)

        if text != 'texts/AD_TD_half_4letters/.DS_Store':
            documents[text] = words
    return documents
