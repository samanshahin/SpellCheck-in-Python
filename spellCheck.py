import spacy
import contextualSpellCheck as csc
# I forgot any libraries, load it then

nlp = spacy.load('en_core_web_sm') 
# the language library is about 450 MB but first time loaded, it doesn't need to be loaded again!
# for bigger projects, use en_core_web_lg (around 780 MB) 
csc.add_to_pipe(nlp)
doc = nlp('a sampel sentense that hass errors and need spel checking.')

if(doc._.contextual_spellCheck and doc._.performed_spellCheck):
    print('SpellCheck is done. Here\'s the result:')
if(len(doc._.suggestions_spellCheck) > 1):
    print('There are some errors! here\'s the list of wrong words and their correct case:')
    for d in doc._.suggestions_spellCheck.keys():
        print(f"{d} >> {doc._.suggestions_spellCheck[d]}")
print('The essay should be like this:')
print(doc._.outcome_spellCheck)
