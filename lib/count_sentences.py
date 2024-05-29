#!/usr/bin/env python3

class MyString:

  def __init__(self, value = ""):
    self._value = value
    
  def get_value(self):
    return self._value

  def set_value(self, stringVal):
    if (type(stringVal) == str):
      self._value = stringVal
    else:
      print("The value must be a string.")

  value = property(get_value, set_value)

  def is_sentence(self):
    return self._value.endswith(".")

  def is_question(self):
    return self._value.endswith("?")

  def is_exclamation(self):
    return self._value.endswith("!")

  def count_sentences(self):
    value = self.value
    for punc in ['!','?']:
        value = value.replace(punc, '.')
    
    sentences = [s for s in value.split('.') if s]
    
    return len(sentences)