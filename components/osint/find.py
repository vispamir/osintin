"""
created on June 01 21 23:00:00
@author: Amir Koulivand

Osint Find
"""

import bootsrap.common

def allocate(word):
  results = []
  components = bootsrap.common.loadComponents('osint')
  for component in components:
    if hasattr(components[component], 'find'):
      result = components[component].find(word)
      results.append(result)

  results = bootsrap.common.invokeAlter('osint', results)

  return results