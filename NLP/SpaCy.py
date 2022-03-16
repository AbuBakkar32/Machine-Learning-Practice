# pip install -U spacy
# python -m spacy download en_core_web_sm
import spacy

# Load English tokenizer, tagger, parser and NER
nlp = spacy.load("en_core_web_sm")

# Process whole documents
text = ("When Sebastian Thrun started working on self-driving cars at "
        "Google in 2007, few people outside of the company took him "
        "seriously. “I can tell you very senior CEOs of major American "
        "car companies would shake my hand and turn away because I wasn’t "
        "worth talking to,” said Thrun, in an interview with Recode earlier "
        "this week.")
doc = nlp(text)

# Analyze syntax
print("Noun phrases:", [chunk.text for chunk in doc.noun_chunks])
print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])
print("Prepositions:", [token.lemma_ for token in doc if token.pos_ == "ADP"])
print("Adjectives:", [token.lemma_ for token in doc if token.pos_ == "ADJ"])
print("Auxiliary:", [token.lemma_ for token in doc if token.pos_ == "AUX"])
print("Conjunctions:", [token.lemma_ for token in doc if token.pos_ == "CCONJ"])
print("Pronouns:", [token.lemma_ for token in doc if token.pos_ == "PRON"])
print("Punctuations:", [token.lemma_ for token in doc if token.pos_ == "PUNCT"])

# Find named entities, phrases and concepts
for entity in doc.ents:
    print(entity.text, entity.label_)
print("*" * 100)
for token in doc:
    print(token.pos_ + " = " + token.lemma_)
# for token in doc:
#     print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
#           token.shape_, token.is_alpha, token.is_stop)
