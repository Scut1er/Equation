import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from funcs import *


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('design.ui', self)
        QMainWindow.setFixedSize(self, 805, 550)
        self.pushButton.clicked.connect(self.equation)
        self.error_label.setStyleSheet('color: red')

    def equation(self):
        clear(self)
        a, b, c = is_float(self.input_a.text()), is_float(self.input_b.text()), is_float(self.input_c.text())
        if None in [a, b, c]:
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
        if is_args_zero(a, b, c):
            self.text_x1.setText('X - любое число')
            render_example(self, a, b, c)
            return
        if a == 0:
            if b == 0:
                self.text_x1.setText(f'Уравнение не имеет решений')
                render_example(self, a, b, c)
                return
            else:
                if c == 0:
                    self.text_x1.setText(f'X = 0')
                else:
                    self.text_x1.setText(f'X = {-c / b}')
                render_example(self, a, b, c)
                return
        if len(solution(a, b, c)) == 1:
            self.text_x1.setText(f'X = {solution(a, b, c)[0]}')
            render_example(self, a, b, c)
            return
        if solution(a, b, c)[-1] == 'Real':
            self.text_x1.setText(f'X<sub>1</sub> = {solution(a, b, c)[0]}')
            self.text_x2.setText(f'X<sub>2</sub> = {solution(a, b, c)[1]}')
            render_example(self, a, b, c)
            return
        if solution(a, b, c)[-1] == 'Complex':
            self.text_x1.setText(f'X<sub>1</sub> = {solution(a, b, c)[0][1:-1]}')
            self.text_x2.setText(f'X<sub>2</sub> = {solution(a, b, c)[1][1:-1]}')
            render_example(self, a, b, c)
            return


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
