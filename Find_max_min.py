
#Формируем макссимальную и минимальную четвёрки чисел для обеих сторон
def Find_and_create_max_min(Expert_marks, Subjects_list):

    max_num = -1
    min_num = 10

    max_vector_IN = {}
    min_vector_IN = {}

    #Идём по всем узлам и значениям четвёрок чисел по каждому критерию
    for crit in Expert_marks.keys():
        #Берём самое максимальное (минимальное) число из всех четвёрок чисел по всем компаниям
        max_num = max(max_num, max(Expert_marks[crit]))
        min_num = min(min_num, min(Expert_marks[crit]))

    for crit in Subjects_list[0].IN_crits.keys():
        #создаём максимальную и минимальную четвёрки чисел
        max_vector_IN.update( {crit: [max_num, max_num, max_num, max_num] } )
        min_vector_IN.update( {crit: [min_num, min_num, min_num, min_num] } )

    #--------------------------------------------------------------

    max_num = -1
    min_num = 10

    max_vector_OUT = {}
    min_vector_OUT = {}

    # Идём по всем узлам и значениям четвёрок чисел по каждому критерию
    for crit in Expert_marks.keys():
        # Берём самое максимальное (минимальное) число из всех четвёрок чисел по всем компаниям
        max_num = max(max_num, max(Expert_marks[crit]))
        min_num = min(min_num, min(Expert_marks[crit]))

    for crit in Subjects_list[0].OUT_crits.keys():
        # создаём максимальную и минимальную четвёрки чисел
        max_vector_OUT.update({crit: [max_num, max_num, max_num, max_num]})
        min_vector_OUT.update({crit: [min_num, min_num, min_num, min_num]})

    #-----------------------------------------------------------------

    return max_vector_IN, min_vector_IN, max_vector_OUT, min_vector_OUT