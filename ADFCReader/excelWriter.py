__author__ = 'Fabian'


from docReader import *
import xlwt

class excelWriter():

    def __init__(self):
        pass

    def write_to_excel(self, city_list):
        wb = xlwt.Workbook()
        for city in city_list:
            row = 0
            ws = wb.add_sheet(city.city_name)
            for x in range(0, city.street_list.__len__()):

                ws.write(row, 0, city.street_list[x])
                ws.write(row, 1, city.code_list[x])
                row += 1

        wb.save('example2.xls')

