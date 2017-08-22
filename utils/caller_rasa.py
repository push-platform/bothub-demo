import io
from future.utils import PY3
import cloudpickle
from rasa_nlu.training_data import Message
import spacy
import json
s = spacy.load("en_core_web_sm", parse=False)

def interpreter(lang, message, model_path):
    classifier_file = str(model_path, "utf_8") + "/intent_classifier.pkl"
    with io.open(classifier_file, 'rb') as f:  # pragma: no test
        if PY3:
            t = cloudpickle.load(f, encoding="latin-1")
        else:
            t = cloudpickle.load(f)

    message = Message(str(message, "utf_8"), {"intent": {"name": "", "confidence": 0.0}, "entities": []}, time=None)
    message.set("spacy_doc", s(message.text))
    message.set("text_features", message.get("spacy_doc").vector)
    t.process(message)
    
    return str(message.as_dict())

# a = interpreter(b"en_core_web_sm", b"my message test bla bla", b"/Users/victor/projetos/elixir/phoenix/ralixir/utils/models/model_20170822-135323")
# print(a)