"""
created on June 01 21 23:00:00
@author: Amir Koulivand

Osint Endpoints
"""

import components.osint.find

class osint_rest():

  def __init__(self):
    print("Loaded Osint Rest")

  def define(self):
    return [
      {
        'path': '/osint/version',
        'method': 'get',
        'callback': self.version,
      },
      {
        'path': '/osint/find-word',
        'method': 'post',
        'callback': self.find_word,
      },
      {
        'path': '/osint/find-geo',
        'method': 'post',
        'callback': self.find_geo,
      }
    ]

  def version(self):
    return {
      'version': '1.0.0 ',
    }

  def find_geo(self, request):
    return {
      'status': True,
      'result': components.osint.find.allocate_geo(request['lat'], request['lng'], True),
    }

  def find_word(self, request):
    return {
      'status': True,
      'result': components.osint.find.allocate_word(request['word']),
    }
