"""
created on June 01 21 23:00:00
@author: Amir Koulivand

Osint Commands
"""

import wikipedia
from PyInquirer import prompt

class osint_cli():

  def __init__(self):
    print("Loaded Osint CLI")

  def define(self):
    return [
      {
        'command': 'find',
        'callback': self.find,
      }
    ]

  def find(self):
    questions = [
      {
        'type': 'input',
        'name': 'word',
        'message': 'What are you want ? (Orange, Iran, Osint and ...)',
      }
    ]

    input = prompt(questions)

    print(wikipedia.summary(input['word']) + "\n\n")

    self.find()
