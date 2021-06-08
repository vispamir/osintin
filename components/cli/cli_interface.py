"""
created on June 01 21 23:00:00
@author: Amir Koulivand

CLI Interface
"""

from __future__ import print_function, unicode_literals
from PyInquirer import prompt
import bootsrap.common

class cli_interface():

  def __init__(self):
    print('CLI Interface loaded')

  def _get_command(self, cli_command):
    components = bootsrap.common.loadComponents('cli')
    for component in components:
      commands = components[component].define()
      for command in commands:
        if command['command'] == cli_command:
          return command['callback']

  def run(self):
    questions = [
      {
        'type': 'input',
        'name': 'command',
        'message': 'Which Command',
      }
    ]

    input = prompt(questions)
    callback = self._get_command(input['command'])

    try:
      callback()
    except:
      print('Command handler not found.')
      self.run()