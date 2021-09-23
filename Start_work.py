from Data_prepare import *
from Find_max_min import *


def Start_work(IN):

    #Считываем данные
    Expert_marks, Subjects_list, Expert_coefs_IN, Expert_coefs_OUT = Data_prepare(IN)

    #Перевели буквенный код оценок в численный
    for sub in Subjects_list:
        sub.Transform_marks_to_numbers(Expert_marks)

    #Формируем макссимальную и минимальную четвёрки чисел для обеих сторон
    max_vector_IN, min_vector_IN, max_vector_OUT, min_vector_OUT = Find_and_create_max_min(Expert_marks, Subjects_list)

    #Нормализуем все ABCD
    for sub in Subjects_list:
        sub.Normalize_ABCD(max_vector_IN, max_vector_OUT)

    #---------------------------------------------------------------
    #Нормализуем максимумы и минимумы
    max_num_IN = -1
    max_num_OUT = -1

    for i in range(4):
        for crit in max_vector_IN:
            max_num_IN = max(max_num_IN , max_vector_IN[crit][i])
            max_num_OUT = max(max_num_OUT , max_vector_OUT[crit][i])
        for crit in max_vector_IN:
            max_vector_IN[crit][i] /= max_num_IN
            min_vector_IN[crit][i] /= max_num_IN
            max_vector_OUT[crit][i] /= max_num_OUT
            min_vector_OUT[crit][i] /= max_num_OUT
    #----------------------------------------------------------------

    #Выводим взвешенные коэффициенты
    for i in range(4):
        for sub in Subjects_list:
            for crit in sub.IN_crits.keys():
                sub.IN_crits[crit][i] *= Expert_coefs_IN[crit][i]
                sub.OUT_crits[crit][i] *= Expert_coefs_OUT[crit][i]


    for i in range(4):
        for crit in Expert_coefs_IN.keys():
            max_vector_IN[crit][i] *= Expert_coefs_IN[crit][i]
            max_vector_OUT[crit][i] *= Expert_coefs_OUT[crit][i]
            min_vector_IN[crit][i] *= Expert_coefs_IN[crit][i]
            min_vector_OUT[crit][i] *= Expert_coefs_OUT[crit][i]

    #-----------------------------------------------------------------

    #Считаем комплексные оценки
    for sub in Subjects_list:
        sub.Calc_complex_mark()

    #-------------------------------------------------------------------

    #Считаем расстояние до наилучшего
    for sub in Subjects_list:
        for crit in max_vector_IN.keys():
            Sum_res = 0
            for i in range(4):
                Sum_res += (sub.IN_crits[crit][i] - max_vector_IN[crit][i])**2

            Sum_res /= 4
            Sum_res = Sum_res**(1/2)

            sub.Lenght_to_best_IN.update( {crit: Sum_res} )


    for sub in Subjects_list:
        for crit in max_vector_OUT.keys():
            Sum_res = 0
            for i in range(4):
                Sum_res += (sub.OUT_crits[crit][i] - max_vector_OUT[crit][i]) ** 2

            Sum_res /= 4
            Sum_res = Sum_res ** (1 / 2)

            sub.Lenght_to_best_OUT.update({crit: Sum_res})

#----------------------------------------------------------------------

    #Считаем расстояние от наилучшего
    for sub in Subjects_list:
        for crit in sub.IN_crits.keys():
            sub.Lenght_from_best_IN += sub.Lenght_to_best_IN[crit]
            sub.Lenght_from_best_OUT += sub.Lenght_to_best_OUT[crit]

#----------------------------------------------------------------------

    #Считает расстояние до наихудшего
    for sub in Subjects_list:
        for crit in min_vector_IN.keys():
            Sum_res = 0
            for i in range(4):
                Sum_res += (sub.IN_crits[crit][i] - min_vector_IN[crit][i])**2

            Sum_res /= 4
            Sum_res = Sum_res**(1/2)

            sub.Lenght_to_worst_IN.update( {crit: Sum_res} )


    for sub in Subjects_list:
        for crit in min_vector_OUT.keys():
            Sum_res = 0
            for i in range(4):
                Sum_res += (sub.OUT_crits[crit][i] - min_vector_OUT[crit][i]) ** 2

            Sum_res /= 4
            Sum_res = Sum_res ** (1 / 2)

            sub.Lenght_to_worst_OUT.update({crit: Sum_res})

    #---------------------------------------------------------------

    # Считаем расстояние от наихудшего
    for sub in Subjects_list:
        for crit in sub.IN_crits.keys():
            sub.Lenght_from_worst_IN += sub.Lenght_to_worst_IN[crit]
            sub.Lenght_from_worst_OUT += sub.Lenght_to_worst_OUT[crit]

    #----------------------------------------------------------------

    #Считаем итоговые коэффициенты
    for sub in Subjects_list:
        sub.Calc_result_coefs()

    #----------------------------------------------------------------

    for sub in Subjects_list:
        print(sub.name , '|   Внутренняя:', sub.Result_coef_IN , "|   Внешняя:", sub.Result_coef_OUT)


    return True, Subjects_list