"""
created on June 01 21 23:00:00
@author: Amir Koulivand

Main File
"""

import sys
import logging
import bootsrap.common

def loadInterface():
  try:
    interface = sys.argv[1]
    components = bootsrap.common.loadComponents('interface')

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