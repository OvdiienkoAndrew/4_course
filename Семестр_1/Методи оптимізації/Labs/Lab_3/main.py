import math

class Point:
    def __init__(self, x=0, y=0):
        self.__x = float(str(x).replace(' ','').replace(',','.'))
        self.__y = float(str(y).replace(' ','').replace(',','.'))

    def get_x(self):
        return self.__x
    def get_y(self):
        return self.__y
    def set_x(self, x):
        self.__x = x
    def set_y(self, y):
        self.__y = y

    def __str__(self):
        return '(' +str(self.get_x()) + '; ' + str(self.get_y()) + ')'

    def f(self):
        return 2 * self.get_x() ** 2 + 2* self.get_y() * self.get_x() + self.get_y() ** 2 - 2*self.get_x() - 3* self.get_y()

    def fx(self):
        return 4 * self.get_x() + 2 * self.get_y() - 2

    def fy(self):
        return 2 * self.get_x() + 2 * self.get_y() - 3

    def fxx(self):
        return 4

    def fxy(self):
        return 2

    def fyy(self):
        return 2

    def fyx(self):
        return 2

    def g(self):
        return 0.5 * (self.get_y() - self.get_x() ** 2) ** 2 + (1 - self.get_x()) ** 2 + (1 - self.get_y()) ** 2

    def gx(self):
        return -2*(1-self.get_x()) - 2 * self.get_x() * (self.get_y() - self.get_x() ** 2)

    def gy(self):
        return -2*(1-self.get_y()) +  (self.get_y() - self.get_x() ** 2)

    def gxx(self):
        return 2 + 4 * self.get_x() ** 2 - 2 * (self.get_y() - self.get_x() ** 2)

    def gxy(self):
        return (-2) * self.get_x()

    def gyx(self):
        return (-2) * self.get_x()

    def gyy(self):
        return 3


    def diff(self, another):
        return math.sqrt(  (self.get_x() - another.get_x()) ** 2 +  (self.get_y() - another.get_y()) ** 2 )

def gradient_method_with_step_separation(function = 'f',point = Point(0,0),eps = 1e-5):


    last_point = Point(point.get_x(), point.get_y())
    lam = eps
    a =  lam

    while True:

        while True:


            was = True

            match (function):
                case 'f':
                    temp_point = Point(last_point.get_x() - a * last_point.fx(), last_point.get_y() - a * last_point.fy())
                    if temp_point.f() < last_point.f():
                        was = False
                case 'g':
                    temp_point = Point(last_point.get_x() - a * last_point.gx(), last_point.get_y() - a * last_point.gy())
                    if temp_point.g() < last_point.g():
                        was = False

            if not was:
                break

            a *= lam

        match (function):
            case 'f':
                point.set_x(last_point.get_x() - a * last_point.fx())
                point.set_y(last_point.get_y() - a * last_point.fy())

            case 'g':
                point.set_x(last_point.get_x() - a * last_point.gx())
                point.set_y(last_point.get_y() - a * last_point.gy())



        was = True
        if point.diff(last_point) < eps:
            match (function):
                case 'f':
                    if math.fabs(point.f() - last_point.f()) < eps:
                        norm_of_gradient = math.sqrt((point.fx()) ** 2 + (point.fy()) ** 2)
                        if norm_of_gradient < eps:
                            was = False

                case 'g':
                    if math.fabs(point.g() - last_point.g()) < eps:
                        norm_of_gradient = math.sqrt((point.gx()) ** 2 + (point.gy()) ** 2)
                        if norm_of_gradient < eps:
                            was = False


        if not was:
            break

        last_point = Point(point.get_x(), point.get_y())

def newton_method(function = 'f',point = Point(0,0),eps = 1e-5):
    last_point = Point(point.get_x(), point.get_y())

    match (function):
        case 'f':
            temp = last_point.fxx() * last_point.fyy() - last_point.fxy() * last_point.fyx()
            if temp == 0:
                raise ValueError("Визначник = 0.")

            det = 1 / temp

            while True:

                point.set_x(
                    last_point.get_x() - det * (
                    (last_point.fyy()*last_point.fx())
                    -
                    (last_point.fyx()*last_point.fy())
                    )
                )

                point.set_y(
                    last_point.get_y() - det * (
                    (-1) * (last_point.fxy()*last_point.fx())
                    +
                    last_point.fxx() * last_point.fy()
                    )
                )

                was = True
                if point.diff(last_point) < eps:

                    if math.fabs(point.f() - last_point.f()) < eps:
                        norm_of_gradient = math.sqrt((point.fx()) ** 2 + (point.fy()) ** 2)
                        if norm_of_gradient < eps:
                            was = False


                if not was:
                    break

                last_point = Point(point.get_x(), point.get_y())

        case 'g':
            temp = last_point.gxx() * last_point.gyy() - last_point.gxy() * last_point.gyx()
            if temp == 0:
                raise ValueError("Визначник = 0.")

            det = 1 / temp

            while True:
                print(point)
                point.set_x(
                    last_point.get_x() - det * (
                            (last_point.gyy() * last_point.gx())
                            -
                            (last_point.gyx() * last_point.gy())
                    )
                )

                point.set_y(
                    last_point.get_y() - det * (
                            (-1) * (last_point.gxy() * last_point.gx())
                            +
                            last_point.gxx() * last_point.gy()
                    )
                )

                was = True
                if point.diff(last_point) < eps:

                    if math.fabs(point.g() - last_point.g()) < eps:
                        norm_of_gradient = math.sqrt((point.gx()) ** 2 + (point.gy()) ** 2)
                        if norm_of_gradient < eps:
                            was = False

                if not was:
                    break

                last_point = Point(point.get_x(), point.get_y())

def main():
    eps = 1e-3

    x0 = 13
    y0 = 13

    print("Градієнтний метод з дробленням кроку")

    point = Point(0, 0)
    gradient_method_with_step_separation(function='f', point=point, eps=eps)
    print(f"\tf{point} = {point.f()};")

    point = Point(x0,y0)
    gradient_method_with_step_separation(function='g',point=point,eps=eps)
    print(f"\tg{point} = {point.g()}.")

    print("\n\nМетод Ньютона")

    point = Point(x0, y0)
    try:
        newton_method(function='f', point=point, eps=eps)
        print(f"\tf{point} = {point.f()};")
    except ValueError as e:
        print(e)

    point = Point(0,0)
    try:
        newton_method(function='g', point=point, eps=eps)
        print(f"\tg{point} = {point.g()}.")
    except ValueError as e:
        print(e)


if __name__ == '__main__':
    main()





