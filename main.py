# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtWidgets, QtChart, QtGui #Подключаем библиотеки PyQT для отрисовки окон и графиков
from numpy import * # библиотеки для использования матриц
from scipy.integrate import * # библиотеки для численного решения системы урний

t = [] # массив временных промежутков для расчета системы уравнений и построения графика
series = [] # массив линий ресующахся на графике


class Ui_Form(object): # класс нашей формы
    def __init__(self): # основной конструктор 
        self.label = QtWidgets.QLabel(Form) # создаем элементы подписи размерностей у полей
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_6 = QtWidgets.QLabel(Form)

        self.t = QtWidgets.QDoubleSpinBox(Form) # созда ем элементы числовых полей для ввода значений
        self.k = QtWidgets.QDoubleSpinBox(Form)
        self.N = QtWidgets.QDoubleSpinBox(Form)
        self.F = QtWidgets.QDoubleSpinBox(Form)
        self.fi = QtWidgets.QDoubleSpinBox(Form)
        self.w = QtWidgets.QDoubleSpinBox(Form)

        self.btn_pause = QtWidgets.QPushButton(Form) # создаем кнопку паузы
        self.btn_start = QtWidgets.QPushButton(Form) # создаем кнопку старт

        self.chartView = QtChart.QChartView(Form) # создаем поле для графиков
        self.chart = self.chartView.chart() # получаем ссылку на график из chartView
        self.axisX = QtChart.QValueAxis() # создаем ось Х
        self.axisY = QtChart.QValueAxis() # создаем ось У

    def setupUi(self, Form): # функция расстоновки созданных элементов на FORM
        Form.setObjectName("Form") #задание внетреннего имени для Form
        Form.resize(800, 600) # задание размера окна
        self.w.setGeometry(QtCore.QRect(140, 530, 100, 22)) # установка геометрии элемента(координата на форме по х, координита на форме по у, ширина , высота )
        self.w.setDecimals(4) # установка количества знаков после запятой для числового поля
        self.w.setMinimum(0.0) # установка мин значения для числового поля
        self.w.setMaximum(100.0) # установка макс значения для числового поля
        self.w.setProperty("value", 5 / (2 * 3.1415)) # установка начального значения
        self.w.setObjectName("w")
        self.label.setGeometry(QtCore.QRect(140, 513, 100, 13))
        self.label.setObjectName("label")
        self.fi.setGeometry(QtCore.QRect(140, 570, 100, 22))
        self.fi.setDecimals(4)
        self.fi.setMinimum(0.0)
        self.fi.setMaximum(100.0)
        self.fi.setProperty("value", 3.1415)
        self.fi.setObjectName("fi")
        self.label_2.setGeometry(QtCore.QRect(140, 553, 100, 13))
        self.label_2.setObjectName("label_2")
        self.btn_start.setGeometry(QtCore.QRect(370, 530, 100, 23))
        self.btn_start.setObjectName("btn_start")
        self.btn_pause.setGeometry(QtCore.QRect(370, 570, 100, 23))
        self.btn_pause.setObjectName("btn_pause")
        self.F.setGeometry(QtCore.QRect(20, 570, 100, 22))
        self.F.setDecimals(2)
        self.F.setMinimum(0.0)
        self.F.setMaximum(10000.0)
        self.F.setProperty("value", 10.0)
        self.F.setObjectName("F")
        self.label_3.setGeometry(QtCore.QRect(20, 553, 100, 13))
        self.label_3.setObjectName("label_3")
        self.chartView.setGeometry(QtCore.QRect(20, 10, 761, 501))
        self.chartView.setObjectName("chartView")
        self.chartView.setRenderHint(QtGui.QPainter.Antialiasing)
        self.chartView.setFocusPolicy(QtCore.Qt.NoFocus)
        self.chart.legend().setVisible(False)
        # self.chart.setAnimationOptions(QtChart.QChart.AllAnimations)
        self.label_4.setGeometry(QtCore.QRect(20, 514, 100, 16))
        self.label_4.setObjectName("label_4")
        self.N.setGeometry(QtCore.QRect(20, 531, 100, 22))
        self.N.setDecimals(0)
        self.N.setMinimum(2.0)
        self.N.setProperty("value", 5.0)
        self.N.setObjectName("N")
        self.k.setGeometry(QtCore.QRect(255, 530, 100, 22))
        self.k.setDecimals(3)
        self.k.setMinimum(0.0)
        self.k.setMaximum(100.0)
        self.k.setProperty("value", 1.0)
        self.k.setObjectName("k")
        self.label_5.setGeometry(QtCore.QRect(255, 513, 100, 13))
        self.label_5.setObjectName("label_5")
        self.t.setGeometry(QtCore.QRect(679, 533, 100, 22))
        self.t.setDecimals(0)
        self.t.setMinimum(1.0)
        self.t.setMaximum(10000.0)
        self.t.setProperty("value", 20.0)
        self.t.setObjectName("t")
        self.label_6.setGeometry(QtCore.QRect(679, 516, 100, 16))
        self.label_6.setObjectName("label_6")

        # add Axis
        self.chart.addAxis(self.axisX, QtCore.Qt.AlignBottom) # привязка созданной оси self.axisX к графику в расоположение внизу
        self.chart.addAxis(self.axisY, QtCore.Qt.AlignLeft) # привязка созданной оси self.axisY к графику в расоположение слева

        self.retranslateUi(Form) # вызов функции для задания текста на лейблы с подписями
        QtCore.QMetaObject.connectSlotsByName(Form) # добавление системных эвентов на форму (закрытие и т.д)

        Form.setTabOrder(self.N, self.F) # уствновка порядка обхода элементов при табуляции
        Form.setTabOrder(self.F, self.w)
        Form.setTabOrder(self.w, self.fi)
        Form.setTabOrder(self.fi, self.k)
        Form.setTabOrder(self.k, self.t)
        Form.setTabOrder(self.t, self.btn_start)
        Form.setTabOrder(self.btn_start, self.btn_pause)

    def retranslateUi(self, Form): # функция для задания текста на лейблы с подписями
        _translate = QtCore.QCoreApplication.translate # встроенный элемент для использования переводов на разные языки (необязателен) сформирован автоматически
        Form.setWindowTitle(_translate("Form", "N маятников на пружинах")) # задание текста на лейблы
        self.label.setText(_translate("Form", "w, рад"))
        self.label_2.setText(_translate("Form", "fi, рад"))
        self.btn_start.setText(_translate("Form", "Старт"))
        self.btn_pause.setText(_translate("Form", "Стереть"))
        self.label_3.setText(_translate("Form", "F, Н"))
        self.label_4.setText(_translate("Form", "N"))
        self.label_5.setText(_translate("Form", "k, Н/м"))
        self.label_6.setText(_translate("Form", "t"))


def on_t_editing_finished(): # функция вызываемая при завершении редактирования поля т (времени)
    set_t() # обновляем временной интервал
    ui.chart.axisX().setRange(0, ui.t.value()) # изменяем размер оси х в соответствие с новым т


def on_start_clicked(): # функция обработчик нажатия на кнопку старт
    if not ui.btn_pause.isEnabled(): # проверка на первичное нажатие старт
        result = system_calculation() # получение расчета системы уравнений
        for k in range(0, int(ui.N.value())): # для каждого маятника
            series.append(QtChart.QLineSeries()) # мы создаем линию на графике
            for i in range(0, len(t)):
                series[k].append(t[i], result[:, k][i]) # добавляем полученные точки
            ui.chart.addSeries(series[k]) # добавляем линию на график
            series[k].attachAxis(ui.axisX) # добавляем к линии текушие оси
            series[k].attachAxis(ui.axisY)

    set_disabled_splin_boxes(True) # отключаем фозможность редактирования числовых полей
    ui.btn_start.setDisabled(True)  # блокируем кнопку старт
    ui.btn_pause.setDisabled(False) #  активируем кнопку стоп


def on_pause_clicked(): # функция обработчик кнопки стоп
    ui.btn_start.setDisabled(False) # активирует кнопку старт
    ui.btn_pause.setDisabled(True) # блокирует кнопку стоп
    set_disabled_splin_boxes(False) # активирует числовые поля
    for k in range(0, int(ui.N.value())): # очищает все линии графика
        series[k].clear()


def set_disabled_splin_boxes(value): # функция для отключения возмежности редактирования полей формы
    ui.N.setDisabled(value)
    ui.F.setDisabled(value)
    ui.w.setDisabled(value)
    ui.fi.setDisabled(value)
    ui.k.setDisabled(value)


def set_t(): # функция установки временного промежутка для расчетов
    global t # используем глобальную переменную
    t = arange(0, ui.t.value(), 0.1) # устанавливаем новый промежуток от 0 до значения поля формы т с шагом 0,1


def system_calculation(): # основная функция расчета модели 
    global t # глобальный интервал времени
    N = int(ui.N.value()) # значение количества маятников из цифрового поля
    F0 = ui.F.value() # амплитуда внешней периодической силы из числового поля
    w = ui.w.value() # частота внешней силы из числового поля
    fi = ui.fi.value() # сдвиг по фазе внешней силы из числового поля
    k = ui.k.value() # жесткость пружин из числового поля
    set_t() # обеовление интервала времени
    Y0 = [0] # массив размера N начальных значений 
    for i in range(1, N): # перебераем кол маятников
        Y0.append(0) # задаем ноль

    def f(Y, t): # функция систамы уравнений
        FY = [F0 * cos(w * t + fi) + k * (Y[1] - Y[0])] # левый маятник
        for i in range(1, N - 1):
            FY.append(k * (Y[i - 1] - 2 * Y[i] + Y[i + 1])) # средние маятники
        FY.append(k * (Y[N - 2] - Y[N - 1])) # правый маятник
        return FY

    return odeint(f, Y0, t) # возврат функции для расчета дифф уравнений из библиотеки scipy


if __name__ == "__main__": #  функция мейн точка фхода программы
    import sys # системная библиотека для окна

    app = QtWidgets.QApplication(sys.argv) # основной обработчик приложения (отвечает за цикл отрисовки)
    Form = QtWidgets.QWidget() # создается виджет(зона) под форму
    ui = Ui_Form() # создается нашь класс формы
    ui.setupUi(Form) # устанавливаем на виджет наши ui контроллы (кнопки поля ...)
    ui.btn_start.clicked.connect(on_start_clicked) # соединяем функцию on_start_clicked с нажатием на кнопку старт на форме
    ui.btn_pause.clicked.connect(on_pause_clicked) # --//-- тоже для кнопки пауза
    ui.t.editingFinished.connect(on_t_editing_finished) # соединяем функцию on_t_editing_finished с эвентом что мы закончили редактировать поле t
    ui.btn_pause.setDisabled(True) # желаем кнопку паузы отключеной
    Form.show() # показываем форму
    sys.exit(app.exec_()) # обработчик цикла приложения
