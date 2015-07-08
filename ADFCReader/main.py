__author__ = 'Fabian'


from docReader import *
from excelWriter import *


def main():

    reader = DocReader()
    cities = reader.read_from_file()

    writer = excelWriter()
    writer.write_to_excel(cities)



if __name__ == '__main__':

    main()

