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
    arg1 = 'x<sup>2</sup>'
    arg2 = 'x'
    if a == b == c == 0:
        return self.example.setText(f'0x<sup>2</sup>+0x+0=0')
    if a % 1 == 0:
        a = int(a)
    if b % 1 == 0:
        b = int(b)
    if c % 1 == 0:
        c = int(c)
    if a == 0:
        a = ''
        arg1 = ''
    if b == 0:
        b = ''
        arg2 = ''
    if c == 0:
        c = ''
    if a == 1:
        a = ''
    if b == 1:
        b = ''
    if a == -1:
        a = '-'
    if b == -1:
        b = '-'
    result = f'{a}{arg1}+{b}{arg2}+{c}=0'.replace('++', '+').replace('+-', '-').replace('+=', '=')
    if result[0] == '+':
        result = result[1:]

    return self.example.setText(result)


def is_float(num):
    num = num.replace(',', '.')
    if len(num) > 10:
        return None
    try:
        num = float(num)
    except ValueError:
        num = None
    return num


def is_args_zero(a, b, c):
    if a == b == c == 0:
        return True
    return False


def solution(a, b, c):
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
