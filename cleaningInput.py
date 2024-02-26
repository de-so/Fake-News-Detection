import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.wordnet import WordNetLemmatizer


def clear_input(input_text: str) -> str:
    lemmatizer=WordNetLemmatizer()
    stop_words = stopwords.words('english')
    filter_sentence = ''
    sentence = input_text
    sentence = re.sub(r'[^\w\s]', '', str(sentence))
    words = nltk.word_tokenize(str(sentence))
    for word in words:
        if word not in stop_words:
            filter_sentence += ' ' + str(lemmatizer.lemmatize(word)).lower()
    input_text = filter_sentence.strip()
    return input_text


