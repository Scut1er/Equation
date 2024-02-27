import cmath
import math


def clear(self):
    self.error_label.setText('')
    self.warning_label.setText('')
    self.text_x1.setText('')
    self.text_x2.setText('')
    self.input_a.setStyleSheet('')
    self.input_b.setStyleSheet('')
    self.input_c.setStyleSheet('')


def render_example(self, a, b, c):
    if a == b == c == 0:
        return self.example.setText(f'0x<sup>2</sup>+0x+0=0')
    if a % 1 == 0:
        a = int(a)
    if b % 1 == 0:
        b = int(b)
    if c % 1 == 0:
        c = int(c)
    arg1 = 'x<sup>2</sup>+'
    if c == 0:
        arg2 = 'x'
        c = ''
    elif c < 0:
        arg2 = 'x'
    else:
        arg2 = 'x+'
    if a == 0:
        arg1 = ''
    if b == 0:
        arg1 = arg1[:-1]
        arg2 = ''
    if a in [0, 1]:
        a = ''
    if b in [0, 1]:
        b = ''
    return self.example.setText(f'{a}{arg1}{b}{arg2}{c}=0')


def is_float(num):
    num = num.replace(',', '.')
    if len(num) > 10:
        return None
    try:
        num = float(num)
    except ValueError as e:
        num = None
    return num


def is_args_zero(a, b, c):
    if a == b == c == 0:
        return True
    return False


def solution(a, b, c):
    d = b ** 2 - (4 * a * c)
    if d >= 0:
        type = 'Real'
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        if x1 % 1 == 0:
            x1 = int(x1)
        if x2 % 1 == 0:
            x2 = int(x2)
    else:
        type = 'Complex'
        x1 = (-b + cmath.sqrt(d)) / (2 * a)
        x2 = (-b - cmath.sqrt(d)) / (2 * a)
    if x1 == x2:
        return [str(round(x1, 5))]
    else:
        if type == 'Complex':
            x1 = round(x1.real, 2) + round(x1.imag, 5) * 1j
            x2 = round(x2.real, 2) + round(x2.imag, 5) * 1j
            return [str(x1), str(x2), type]
        else:
            return sorted([str(round(x1, 5)), str(round(x2, 5)), type])
