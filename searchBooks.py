#import spacy
import spacy
nlp = spacy.load('en_core_web_lg')
from spacy.matcher import PhraseMatcher

textTosearch = open("masterpiecesOfTheMastersOfFiction.txt", "r", encoding="utf8").read()
docTosearch = nlp(textTosearch)
matcher = PhraseMatcher(nlp.vocab, attr="LOWER")

searchPhrase = ['']

search = input("Enter a search term: ").strip()

searchPhrase.append(search)

searchPatterns = [nlp.make_doc(text) for text in searchPhrase]

matcher.add('phrase-matching', None, *searchPatterns)

characterMatches = matcher(docTosearch)

print(characterMatches)

for matchIndex, start, end in characterMatches:
    match = docTosearch[start:end]
    print(match.text, '\t|\t', match.label_, '\t|\t', match.sent, '\t|\t', start, end)



