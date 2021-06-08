"""
created on June 01 21 23:00:00
@author: Amir Koulivand

Common bootsrap
"""

import os
import imp

def loadComponents(extention):
  componentObjects = {}
  components = os.listdir('./components')

  for component in components:
    for root, dirs, files in os.walk('./components/' + component):
      for file in files:
        if file.endswith('_' + extention + '.py'):
          componentPath = os.path.join(root, file)
          componentFile = imp.load_source(component + '_' + extention, componentPath)
          componentObject = getattr(componentFile, component + '_' + extention)
          componentObjects[component] = componentObject()

  return componentObjects