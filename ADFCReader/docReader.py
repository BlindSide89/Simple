__author__ = 'Fabian'
# -*- coding: utf-8 -*-

import codecs
import sys



class Stadt_ADFC():

    def __init__(self, city_name):

        self.city_name = city_name
        self.code_list = []
        self.street_list = []

    def add_street_code_pair(self, pair):
        x = pair.split("»")

        self.code_list.append(x[0].lstrip())
        self.street_list.append(x[1].lstrip())

class DocReader():

    def __init__(self):
        pass

    def read_from_file(self, path: str="G:\Workplace\PythonWorkspace\Simple\ADFCReader\\adfc.txt") -> Stadt_ADFC:


        returnCities = []
        f = codecs.open(path, 'r', 'utf-8')
        current_stadt = 0
        for line in f:

            s = line[0]
            if not s.isspace():
                if current_stadt == 0:
                    current_stadt = Stadt_ADFC(line)
                else:
                    returnCities.append(current_stadt)
                    current_stadt = Stadt_ADFC(line)
            else:
                current_stadt.add_street_code_pair(line)

        #for city in returnCities:
         #   print(city.city_name)
         #   for street in city.street_list:
         #       print(street)

        return returnCities


