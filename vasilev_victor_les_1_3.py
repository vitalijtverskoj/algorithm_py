"""По введенным пользователем координатам двух точек вывести уравнение прямой вида y=kx+b, проходящей через эти точки.
"""

def line_equation (x1,y1,x2,y2):
    k = (y1 - y2) / (x1 - x2)
    b = y2 - k * x2
    return print(f'Уравнение прямой y = {round(k,1)}x + {round(b,1)}')


if __name__ == '__main__':
    print('Введите координаты точки A: ')
    x1 = float(input('x1 = '))
    y1 = float(input('y1 = '))
    print('Введите координаты точки B')
    x2 = float(input('x2 = '))
    y2 = float(input('y2 = '))
    line_equation(x1,y1,x2,y2)
