from Subject import *
import pandas as pd
import math
from xlwt import *


#Вывод результата в файл
def Write_to_Excel(OUT, Subjects_list):

    # Запись в файл
    wb = Workbook()
    ws = wb.add_sheet('Результат')

    vals = [ ['Объект', 'Внутренняя', 'Внешняя'] ]

    for sub in Subjects_list:
        temp = [sub.name , sub.Result_coef_IN, sub.Result_coef_OUT]
        print(temp)
        vals.append(temp)

    for i in range(len(vals)):
        for j in range(len(vals[i])):
            ws.write(i, j, vals[i][j])

    wb.save(OUT)
