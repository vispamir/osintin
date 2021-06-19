"""
created on June 01 21 23:00:00
@author: Amir Koulivand

Osint On WikiPedia
"""

import wikipedia

class wikipedia_osint():

  def __init__(self):
    print("Loaded WikiPedia Osint")

  def find(self, word):
    summary = wikipedia.summary(word)
    return summary
    # links = wikipedia.page(word).links
    # print(links)
    
    # separator = "\n\n"
    # return separator.join(links)
