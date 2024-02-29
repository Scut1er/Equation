import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from funcs import *


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('design.ui', self)  # инициализация интерфеса из файла design.ui
        QMainWindow.setFixedSize(self, 805, 550)
        self.error_label.setStyleSheet('color: red')
        self.pushButton.clicked.connect(self.equation)  # подключение кнопки к функции equation

    def equation(self):  # главная функция решения уравнения
        clear(self)
        a, b, c = (is_float(self.input_a.text()),
                   is_float(self.input_b.text()),
                   is_float(self.input_c.text()))  # коэффициенты уравнения
        if None in [a, b, c]:  # введён недопустимый коэффициент
            self.error_label.setText('Введённые данные некорректны!')
            self.warning_label.setText('<sup>*</sup>Максимально допустимы 10-значные коэффициенты')
            self.example.setText(f'')
            if a is None:
                self.input_a.setStyleSheet('border: 1px solid red')
            if b is None:
                self.input_b.setStyleSheet('border: 1px solid red')
            if c is None:
                self.input_c.setStyleSheet('border: 1px solid red')
            return
        render_example(self, a, b, c)
        if uniq_solution(self, a, b, c) is False:  # уравнение не является особым случаем
            if len(solution(a, b, c)) == 1:  # уравнение имеет один корень
                self.text_x1.setText(f'X = {solution(a, b, c)[0]}')
                return
            else:  # уравнение имеет два корня
                self.text_x1.setText(f'X<sub>1</sub> = {solution(a, b, c)[0]}')
                self.text_x2.setText(f'X<sub>2</sub> = {solution(a, b, c)[1]}')
                return


if __name__ == '__main__':  # запуск приложения
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
