import os
from joblib import load
import string
from nltk.corpus import stopwords


def clean_text(text):
    text = text.lower()
    tokens = [char for char in text if char not in string.punctuation]
    text = "".join(tokens)
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in text.split() if word not in stop_words]
    text = " ".join(tokens)
    return text


def fake_or_not(text):
    module_dir = os.path.dirname(__file__)
    file = os.path.join(module_dir, 'model_trained/lr.joblib')
    lr = load(file)
    cleaned_text = clean_text(text)
    prediction = lr.predict([cleaned_text])
    return prediction[0]
