# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtWidgets, QtChart, QtGui
from pylab import *
from scipy.integrate import *

t = []


class Ui_Form(object):
    def __init__(self):
        self.label = QtWidgets.QLabel(Form)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_6 = QtWidgets.QLabel(Form)

        self.t = QtWidgets.QDoubleSpinBox(Form)
        self.k = QtWidgets.QDoubleSpinBox(Form)
        self.N = QtWidgets.QDoubleSpinBox(Form)
        self.F = QtWidgets.QDoubleSpinBox(Form)
        self.fi = QtWidgets.QDoubleSpinBox(Form)
        self.w = QtWidgets.QDoubleSpinBox(Form)

        self.btn_pause = QtWidgets.QPushButton(Form)
        self.btn_start = QtWidgets.QPushButton(Form)

        self.timer = QtCore.QTimer(Form)

        self.drawingArea = QtWidgets.QWidget(Form)
        self.chartView = QtChart.QChartView(self.drawingArea)
        self.chart = self.chartView.chart()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 600)
        self.w.setGeometry(QtCore.QRect(140, 530, 100, 22))
        self.w.setDecimals(4)
        self.w.setMinimum(0.0)
        self.w.setMaximum(100.0)
        self.w.setProperty("value", 5 / (2 * 3.1415))
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
        self.drawingArea.setGeometry(QtCore.QRect(20, 10, 761, 501))
        self.drawingArea.setStyleSheet("border:1px solid black")
        self.drawingArea.setObjectName("drawingArea")
        self.chartView.setGeometry(QtCore.QRect(0, 0, 761, 501))
        self.chartView.setObjectName("chartView")
        self.chartView.setRenderHint(QtGui.QPainter.Antialiasing)
        self.chartView.setFocusPolicy(QtCore.Qt.NoFocus)
        self.chart.legend().setVisible(False)
        # self.chart.setTitle("Nested donuts demo")
        self.chart.setAnimationOptions(QtChart.QChart.AllAnimations)
        self.chart.createDefaultAxes()
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

        self.timer.setInterval(100)

        # self.timer.timeout.connect(self.onTimer)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        Form.setTabOrder(self.N, self.F)
        Form.setTabOrder(self.F, self.w)
        Form.setTabOrder(self.w, self.fi)
        Form.setTabOrder(self.fi, self.k)
        Form.setTabOrder(self.k, self.t)
        Form.setTabOrder(self.t, self.btn_start)
        Form.setTabOrder(self.btn_start, self.btn_pause)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "N маятников на пружинах"))
        self.label.setText(_translate("Form", "w, рад"))
        self.label_2.setText(_translate("Form", "fi, рад"))
        self.btn_start.setText(_translate("Form", "Старт"))
        self.btn_pause.setText(_translate("Form", "Стереть"))
        self.label_3.setText(_translate("Form", "F, Н"))
        self.label_4.setText(_translate("Form", "N"))
        self.label_5.setText(_translate("Form", "k, Н/м"))
        self.label_6.setText(_translate("Form", "t"))


def on_t_editing_finished():
    set_t()
    ui.chart.axisX.setRange(0, ui.t.value())


def on_start_clicked():
    if not ui.btn_pause.isEnabled():
        result = system_calculation()
        for k in range(0, int(ui.N.value())):
            series = QtChart.QLineSeries()
            for i in range(0, len(t)):
                series.append(t[i], result[:, k][i])
            ui.chart.addSeries(series)

    set_disabled_splin_boxes(True)
    # ui.timer.start()
    ui.btn_start.setDisabled(True)
    # ui.btn_pause.setText("Пауза")
    ui.btn_pause.setDisabled(False)


def on_pause_clicked():
    ui.btn_start.setDisabled(False)
    ui.btn_pause.setDisabled(True)
    set_disabled_splin_boxes(False)
    ui.chartView.update()
    # if ui.timer.isActive():
    #     ui.timer.stop()
    #     ui.btn_start.setDisabled(False)
    #     ui.btn_pause.setText("Стоп")
    # else:
    #     ui.btn_pause.setDisabled(True)
    #     ui.btn_pause.setText("Пауза")
    #     set_disabled_splin_boxes(False)
    #     # series->clear()
    #     ui.chartView.update()


def set_disabled_splin_boxes(value):
    ui.N.setDisabled(value)
    ui.F.setDisabled(value)
    ui.w.setDisabled(value)
    ui.fi.setDisabled(value)
    ui.k.setDisabled(value)
    ui.t.setDisabled(value)


def set_t():
    global t
    t = arange(0, ui.t.value(), 0.1)


def system_calculation():
    global t
    N = int(ui.N.value())
    F0 = ui.F.value()
    w = ui.w.value()
    fi = ui.fi.value()
    k = ui.k.value()
    set_t()
    Y0 = [0]
    for i in range(1, N):
        Y0.append(0)

    def f(Y, t):
        FY = [F0 * cos(w * t + fi) + k * (Y[1] - Y[0])]
        for i in range(1, N - 1):
            FY.append(k * (Y[i - 1] - 2 * Y[i] + Y[i + 1]))
        FY.append(k * (Y[N - 2] - Y[N - 1]))
        return FY

    return odeint(f, Y0, t)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    ui.btn_start.clicked.connect(on_start_clicked)
    ui.btn_pause.clicked.connect(on_pause_clicked)
    ui.t.editingFinished.connect(on_t_editing_finished)
    ui.btn_pause.setDisabled(True)
    Form.show()
    sys.exit(app.exec_())
