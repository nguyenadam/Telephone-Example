from spellchecker import SpellChecker

def telephone(phrase):
  
  spell = SpellChecker()

  # does some preprocessing
  words = [x.lower() for x in clean_sentence(phrase).split()]
  # find those words that may be misspelled
  misspelled = spell.unknown(words)

  for word in misspelled:
      # Get the one `most likely` answer
      words[words.index(word)] = (spell.correction(word))
  
  return " ".join(words)

# helper functions to preprocess phrase
def is_ok(c):
    return c.isalnum() or c in " '"

def clean_sentence(s):
    return "".join(filter(is_ok, s))