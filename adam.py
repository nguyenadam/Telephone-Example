def telephone(phrase):

  # making small modification to the input
  phrase = list(phrase)
  phrase[0] = chr(ord(phrase[0]) + 1)
  return "".join(phrase)