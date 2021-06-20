"""
created on June 01 21 23:00:00
@author: Amir Koulivand

Osint Commands
"""

import components.osint.find
from PyInquirer import prompt
import bootsrap.common

class osint_cli():

  def __init__(self):
    print("Loaded Osint CLI")

  def define(self):
    return [
      {
        'command': 'find.word',
        'callback': self.find_word,
      },
      {
        'command': 'find.geo',
        'callback': self.find_geo,
      }
    ]

  def find_geo(self):
    questions = [
      {
        'type': 'input',
        'name': 'latlng',
        'message': 'Where are you want ? (Lat & Lng of any where : 35.700,51.387)',
      }
    ]

    input = prompt(questions)
    geo = input['latlng'].split(',')
    results = components.osint.find.allocate_geo(geo[0], geo[1])

    separator = "\n\n"
    print(separator.join(results))

    print("\n-------------------------------------------------------------------------\n\n")

    self.find_geo()

  def find_word(self):
    questions = [
      {
        'type': 'input',
        'name': 'word',
        'message': 'What are you want ? (Orange, Iran, Osint and ...)',
      }
    ]

    input = prompt(questions)
    results = components.osint.find.allocate_word(input['word'])

    separator = "\n\n"
    print(separator.join(results))

    print("\n-------------------------------------------------------------------------\n\n")

    self.find_word()
