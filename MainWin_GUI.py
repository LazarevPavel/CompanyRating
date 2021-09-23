from PyQt5 import QtWidgets
import Interface.MainWindow as Design_MainWin
from os.path import exists
from Start_work import *
from Export_result import *




class Main_Frame(QtWidgets.QMainWindow, Design_MainWin.Ui_MainWindow):
    '''Класс главного окна'''

    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле MainWindow.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.File_input_button.clicked.connect(self.browse_file_input)    #Привязка к кнопке функции поиска входного файла
        self.File_output_button.clicked.connect(self.browse_file_output)  #Привязка к кнопке функции указания директории для выходного файла
        self.Calculate_button.clicked.connect(self.Calculate)             #Привязка к кнопке функции, начинающей весь рассчёт
        self.Subjects_list = []


    #-----------------------------------------------------------------------

    #Функция для ручного поиска входного файла по проводнику
    def browse_file_input(self):
        file = QtWidgets.QFileDialog.getOpenFileName(self, "Выберите файл")  #Открывается окно поиска по "проводнику"
        if file:             #Если файл был выбран
            file = file[0]   #Берём путь до файла
            self.File_url_input.setText(file)  #Вставляем путь в поле ввода

    # -----------------------------------------------------------------------

    #Функция для ручного указания директории для выходного файла
    def browse_file_output(self):
        directory = QtWidgets.QFileDialog.getExistingDirectory()  #Открывается окно поиска по "проводнику"
        if directory:
            directory_path = ''
            for char in directory:
                directory_path += char                    #Берём путь до директории
            self.File_url_output.setText(directory)     #И помещаем в поле для ввода

    # -----------------------------------------------------------------------

    #Вывод ошибки в область ошибок
    def Show_error(self, error_str):
        self.Finish_label.setText('Возникли проблемы!')  # Меняем статус
        self.Finish_label.setStyleSheet('color: #ff0000')  # и его цвет
        self.Problems_text.setPlainText(error_str)

    # -----------------------------------------------------------------------

    #Функция, запускающая алгоритм расчёта
    def Calculate(self):
        IN = self.File_url_input.toPlainText()                        #Берём путь до файла из текствого поля
        OUT = self.File_url_output.toPlainText()  # Берём путь до директории выходного файла
        OUT += '/' + self.Edit_filename_output.toPlainText() + '.xls'  # Добавляем имя файла к пути сохранения


        #Если входной файл, указанный пользователем, существует
        if exists(IN):
            self.Finish_label.setText('Обрабатываю данные...')
            #ЗАПУСКАЕМ АЛГОРИТМ РАСЧЁТА
            error_str, self.Subjects_list = Start_work(IN)
        else:
            error_str = "Некорректно указан путь до входного файла."

        #Если проблем не возникло
        if(error_str == True):
            Write_to_Excel(OUT, self.Subjects_list)
            self.Finish_label.setStyleSheet('color: rgb(0, 170, 0);')
            self.Finish_label.setText('Готово!')  # По выполнении уведомляем пользователя надписью ниже главной кнопки

        #Если же проблемы всё-таки возникли
        elif (type(' ') == type(error_str)):
            self.Show_error(error_str)

    # -----------------------------------------------------------------------