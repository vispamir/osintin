"""
created on June 01 21 23:00:00
@author: Amir Koulivand

CLI Interface
"""

from __future__ import print_function, unicode_literals
from PyInquirer import prompt, print_json

class cli_interface():

  def __init__(self):
    print('CLI Interface loaded')

  def run(self):
    questions = [
      {
        'type': 'input',
        'name': 'first_name',
        'message': 'What\'s your first name',
      }
    ]

    answers = prompt(questions)
    print_json(answers)
