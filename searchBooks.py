import spacy
nlp = spacy.load('en_core_web_lg')

text = "Buy milk, sugar and flingor"
doc = nlp(text)
print(doc)