"""
created on June 01 21 23:00:00
@author: Amir Koulivand

Main File
"""

import os
import imp
import sys
import logging

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

def loadInterface():
  try:
    interface = sys.argv[1]
    components = loadComponents('interface')

    if interface in components:
      components[interface].run()
  except:
    print("Enter valid interface type.")

def main():
  loadInterface()

def log():
  logging.basicConfig()
  logging.getLogger().setLevel(logging.DEBUG)
  requests_log = logging.getLogger("requests.packages.urllib3")
  requests_log.setLevel(logging.DEBUG)
  requests_log.propagate = True

if __name__ == '__main__':
  main()