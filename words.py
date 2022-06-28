import spacy
nlp = spacy.load('en_core_web_sm')

file_name = 'mostcommon.txt'
file_text = open(file_name).read()
file_doc = nlp(file_text)

"""types_of_words = []

for token in file_doc:
    if token.pos_ not in types_of_words:
        print(token.pos_)
        types_of_words.append(token.pos_)"""

prop_nouns = []
verbs = []
determiner = [] 
conjunction =[]
CCOnj = [] 
AUXverb = []
pronouns = []
adjective = []
adverbs = []
nouns = []
number = []
sconjunction = []

for token in file_doc:
    if token.pos_ == 'PROPN':
        prop_nouns.append(token)
    if token.pos_ == 'VERB':
        verbs.append(token)
    if token.pos_ == 'DET':
        determiner.append(token)
    if token.pos_ == 'ADP':
        conjunction.append(token)
    if token.pos_ == 'CCONJ':
        CCOnj.append(token)
    if token.pos_ == 'AUX':
        AUXverb.append(token)
    if token.pos_ == 'PRON':
        pronouns.append(token)
    if token.pos_ == 'SCONJ':
        sconjunction.append(token)
    if token.pos_ == 'NUM':
        number.append(token)
    if token.pos_ == 'NOUN':
        nouns.append(token)
    if token.pos_ == 'ADJ':
        adjective.append(token)
    if token.pos_ == 'ADV':
        adverbs.append(token)

print([token.text for token in CCOnj])
print([token.text for token in sconjunction])
print([token.text for token in prop_nouns])
print([token.text for token in verbs])
print([token.text for token in determiner])
print([token.text for token in conjunction])
print([token.text for token in CCOnj])
print([token.text for token in AUXverb])
print([token.text for token in pronouns])
print([token.text for token in adjective])
print([token.text for token in adverbs])
print([token.text for token in nouns])
print([token.text for token in number])
print([token.text for token in sconjunction])

