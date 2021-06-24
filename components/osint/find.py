"""
created on June 01 21 23:00:00
@author: Amir Koulivand

Osint Find
"""

import bootsrap.common

def allocate_geo(lat, lng, asList = False):
  results = []
  components = bootsrap.common.loadComponents('osint')
  for component in components:
    if hasattr(components[component], 'geo_find'):
      result = components[component].geo_find(lat, lng, asList)
      print(result)
      if hasattr(result, "__len__"):
        result = bootsrap.common.invokeAlter('osint', result)
      else:
        result = bootsrap.common.invokeAlter('osint', [result])

      results.append(result)

  return results

def allocate_word(word):
  results = []
  components = bootsrap.common.loadComponents('osint')
  for component in components:
    if hasattr(components[component], 'word_find'):
      result = components[component].word_find(word)
      results.append(result)

  results = bootsrap.common.invokeAlter('osint', results)

  return results