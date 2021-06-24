"""
created on June 01 21 23:00:00
@author: Amir Koulivand

Osint On WikiPedia
"""

import wikipedia

class wikipedia_osint():

  def __init__(self):
    print("Loaded WikiPedia Osint")

  def geo_find(self, lat, lng, asList):
    words = wikipedia.geosearch(35.700, 51.387)

    summaries = []
    for word in words:
      summaries.append(word + ': ' + self.word_find(word))

    if (asList):
      return summaries

    separator = "\n\n"
    return separator.join(summaries)

  def word_find(self, word):
    summary = wikipedia.summary(word)
    return summary
