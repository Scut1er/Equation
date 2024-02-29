import cmath
import math


def clear(self):  # очистка элементов интерфейса
    self.error_label.setText('')
    self.warning_label.setText('')
    self.text_x1.setText('')
    self.text_x2.setText('')
    self.input_a.setStyleSheet('')
    self.input_b.setStyleSheet('')
    self.input_c.setStyleSheet('')


def render_example(self, a, b, c):  # рендер строки с отображением уравнения
    def is_int(n):
        if n % 1 == 0:
            return int(n)
        return n

    arg1 = 'x<sup>2</sup>'
    arg2 = 'x'
    if a == b == c == 0:
        return self.example.setText(f'0x<sup>2</sup>+0x+0=0')
    a, b, c = is_int(a), is_int(b), is_int(c)
    if a in [0,1]:
        a = ''
        if a == 0:
            arg1 = ''
    if b in [0, 1]:
        b = ''
        if b == 0:
            arg2 = ''
    if c == 0:
        c = ''
    if a == -1:
        a = '-'
    if b == -1:
        b = '-'
    result = f'{a}{arg1}+{b}{arg2}+{c}=0'.replace('++', '+').replace('+-', '-').replace('+=', '=')
    if result[0] == '+':
        result = result[1:]
    return self.example.setText(result)


def is_float(num):  # проверка коэффициента на допустимость, форматирование во float
    num = num.replace(',', '.')
    if len(num) > 10:
        return None
    try:
        num = float(num)
    except ValueError:
        num = None
    return num


def uniq_solution(self, a, b, c):  # проверка коэффициентов на уникальные случаи решения уравнения
    if a == b == c == 0:
        return self.text_x1.setText('X - любое число')
    if a == b == 0:
        return self.text_x1.setText(f'Уравнение не имеет решений')
    if a == c == 0:
        return self.text_x1.setText(f'X = 0')
    if a == 0:
        return self.text_x1.setText(f'X = {-c / b}')
    return False


def solution(a, b, c):  # решение уравнения с помощью дискриминанта
    d = b ** 2 - (4 * a * c)
    if d >= 0:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        if x1 % 1 == 0:
            x1 = int(x1)
        if x2 % 1 == 0:
            x2 = int(x2)
        if x1 == x2:
            return [str(round(x1, 5))]
        else:
            return sorted([str(round(x1, 3)), str(round(x2, 3))])
    else:
        x1 = (-b + cmath.sqrt(d)) / (2 * a)
        x2 = (-b - cmath.sqrt(d)) / (2 * a)
        x1 = round(x1.real, 2) + round(x1.imag, 3) * 1j
        x2 = round(x2.real, 2) + round(x2.imag, 3) * 1j
        return [str(x1), str(x2)]
