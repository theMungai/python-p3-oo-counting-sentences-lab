#!/usr/bin/env python3
import re

class MyString:

  def __init__(self, value = ""):
    self._value = ""
    self.value = value

  @property
  def value(self):
    return self._value

  @value.setter
  def value(self, val):
    if not isinstance(val, str):
      print("The value must be a string.")
    else:
      self._value = val


  # INSTANCE METHOD
  def is_sentence(self):
    if self.value.endswith("."):
      return  True
    else:
      return False

  # INSTANCE METHOD
  def is_question(self):
    if self.value.endswith("?"):
      return True
    else:
      return False

  # INSTANCE METHOD
  def is_exclamation(self):
    if self.value.endswith("!"):
      return  True
    else:
      return False

  def count_sentences(self):
    sentences = re.split(r"[.!?]+", self.value)
    non_empty_sentences = [s.strip() for s in sentences if s.strip()]
    MyString.count = len(non_empty_sentences)
    return MyString.count


string = MyString("This is a string! It has three sentences. Right?")
string.count_sentences()