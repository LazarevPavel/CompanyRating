import pandas as pd
import numpy as np
from Subject import Subject




def Data_prepare(IN):
    #-----------------------------------------

    #Читаем из файла данные об оценках
    data = pd.read_excel(IN, 0)
    data = data.values

    #Заполняем оценки с их числовыми коэффициентами
    Expert_marks = {}
    for i in range(len(data)):
        Expert_marks.update( {data[i][1].upper(): [data[i][2] , data[i][3] , data[i][4] , data[i][5]]} )

    #-----------------------------------------------

    #Считываем из файла данные о внутренней и внешней сторонах компаний
    data_IN = pd.read_excel(IN, 1)
    data_OUT = pd.read_excel(IN, 2)

    data_IN = data_IN.values
    data_OUT = data_OUT.values


    #Заполняем данные о внещней и внутренней сторонах компаний
    Subjects_list = []

    for i in range(1, len(data_IN)):
        name = data_IN[i][0]

        IN_crits = {}
        for j in range(1, len(data_IN[i])):
            IN_crits.update( {data_IN[0][j]: data_IN[i][j] } )

        OUT_crits = {}
        for j in range(1, len(data_OUT)):
            if(data_OUT[j][0] == name):
                for k in range(1, len(data_OUT[j])):
                    OUT_crits.update( {data_OUT[0][k]: data_OUT[j][k] } )

        subject = Subject(name , IN_crits , OUT_crits)
        Subjects_list.append(subject)

    #--------------------------------------------------------

    #Считываем из файла данные о коэффициентах экспертов для внутренней части
    data = pd.read_excel(IN, 3)
    data = data.values

    #Заполняем данные о коэффициентах экспертов
    Expert_coefs_IN = {}

    for i in range(len(data)):
        Expert_coefs_IN.update( {data[i][0]: [ data[i][1] , data[i][2] , data[i][3] , data[i][4] ] } )

    #-----------------------------------------------------------

    # Считываем из файла данные о коэффициентах экспертов для внешней части
    data = pd.read_excel(IN, 4)
    data = data.values

    # Заполняем данные о коэффициентах экспертов
    Expert_coefs_OUT = {}

    for i in range(len(data)):
        Expert_coefs_OUT.update({data[i][0]: [data[i][1], data[i][2], data[i][3], data[i][4]]})

    # -----------------------------------------------------------

    return Expert_marks, Subjects_list, Expert_coefs_IN, Expert_coefs_OUT