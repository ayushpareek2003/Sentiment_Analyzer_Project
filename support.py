import nltk 
nltk.download('stopwords') 
from nltk.corpus import stopwords
from keras.preprocessing.text import Tokenizer
import re 
from tensorflow.keras.preprocessing.sequence import pad_sequences


def pre_process(text):
    stop_words = stopwords.words('english') 
    text_cleaning_re = "@\S+|https?:\S+|http?:\S|[^A-Za-z0-9]+" 

    text = re.sub(text_cleaning_re, ' ', str(text).lower()).strip()

    tokens = []
    for token in text.split():
        if token not in stop_words:
            tokens.append(token)
    text=" ".join(tokens)

    tokenizer = Tokenizer()
    tokenizer.fit_on_texts(text) 


    x_train = pad_sequences(tokenizer.texts_to_sequences(text),maxlen = 35)

    return x_train


def decode_sentiment(score):
    return 1 if score>0.5 else 0
