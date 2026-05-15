import nltk
from nltk import word_tokenize, pos_tag
from nltk.corpus import stopwords

def extract_nouns(text):
    tokens = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    return [w.lower() for w, p in pos_tag(tokens) if p.startswith('NN') and len(w) > 2 and w.lower() not in stop_words]