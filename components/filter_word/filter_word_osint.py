"""
created on June 01 21 23:00:00
@author: Amir Koulivand

Filter Words
"""

class filter_word_osint():

  def __init__(self):
    print("Loaded Filter Word")

  def alter(self, texts):
    words = ['bastard', 'fuck', 'wanker']
    for key, text in enumerate(texts):
      for word in words:
        texts[key] = text.replace(word, '[...]')

    return texts