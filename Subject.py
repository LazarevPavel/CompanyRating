
class Subject:

    def __init__(self, name, IN_crits, OUT_crits):
        self.name = name
        self.IN_crits = IN_crits
        self.OUT_crits = OUT_crits
        self.Complex_mark_IN = []
        self.Complex_mark_OUT = []
        self.Lenght_to_best_IN = {}
        self.Lenght_to_best_OUT = {}
        self.Lenght_from_best_IN = 0
        self.Lenght_from_best_OUT = 0
        self.Lenght_to_worst_IN = {}
        self.Lenght_to_worst_OUT = {}
        self.Lenght_from_worst_IN = 0
        self.Lenght_from_worst_OUT = 0
        self.Result_coef_IN = 0
        self.Result_coef_OUT = 0


    #Перевод буквенной оценки в набор 4-х чисел
    def Transform_marks_to_numbers(self, Expert_marks):

        for some_crit in self.IN_crits.keys():
            self.IN_crits[some_crit] = Expert_marks[self.IN_crits[some_crit].upper()].copy()

        for some_crit in self.OUT_crits.keys():
            self.OUT_crits[some_crit] = Expert_marks[self.OUT_crits[some_crit].upper()].copy()


    #Нормализация все ABCD
    def Normalize_ABCD(self, max_vector_IN, max_vector_OUT):

        for crit in self.IN_crits.keys():
            for i in range(len(self.IN_crits[crit])):
                self.IN_crits[crit][i] = self.IN_crits[crit][i] / max(max_vector_IN[crit])

        for crit in self.OUT_crits.keys():
            for i in range(len(self.OUT_crits[crit])):
                self.OUT_crits[crit][i] = self.OUT_crits[crit][i] / max(max_vector_OUT[crit])


    #Высчитываем комплексные оценки
    def Calc_complex_mark(self):

        for i in range(4):
            sum_IN = 0
            sum_OUT = 0

            for crit in self.IN_crits.keys():
                sum_IN += self.IN_crits[crit][i]
                sum_OUT += self.OUT_crits[crit][i]

            self.Complex_mark_IN.append(sum_IN)
            self.Complex_mark_OUT.append(sum_OUT)


    #Считаем итоговые коэффициенты
    def Calc_result_coefs(self):
        self.Result_coef_IN = self.Lenght_from_worst_IN / (self.Lenght_from_best_IN + self.Lenght_from_worst_IN)
        self.Result_coef_OUT = self.Lenght_from_worst_OUT / (self.Lenght_from_best_OUT + self.Lenght_from_worst_OUT)