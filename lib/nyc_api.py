
import requests
import json

class GetPrograms:

  def get_programs(self):
    URL = "http://data.cityofnewyork.us/resource/uvks-tn5n.json"

    programs_list = []
    programs = json.loads(self.get_programs())
    for program in programs:
            programs_list.append(program["agency"])


    response = requests.get(URL)
    return response.content

# programs = GetPrograms().get_programs()
# print(programs)