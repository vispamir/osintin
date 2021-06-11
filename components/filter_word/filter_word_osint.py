"""
created on June 01 21 23:00:00
@author: Amir Koulivand

Filter Words
"""

class filter_word_osint():

  def __init__(self):
    print("Loaded Filter Word")

  def alter(self, text):
    words = ['bastard', 'fuck', 'wanker']
    for word in words:
      text = text.replace(word, '[...]')

    return text