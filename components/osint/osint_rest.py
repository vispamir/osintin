"""
created on June 01 21 23:00:00
@author: Amir Koulivand

Osint Endpoints
"""

import wikipedia

class osint_rest():

  def __init__(self):
    print("Loaded Osint Rest")

  def define(self):
    return [
      {
        'path': '/osint/find',
        'method': 'get',
        'callback': self.find,
      },
      {
        'path': '/osint/find',
        'method': 'post',
        'callback': self.retrieve,
      }
    ]

  def find(self):
    return {
      'status': False,
    }

  def retrieve(self, request):
    return {
      'status': True,
      'result': wikipedia.summary(request['word']),
    }
