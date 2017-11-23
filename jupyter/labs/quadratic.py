class QuadraticEquation(object):
    def __init__(self, a, b, c):
        if a == 0:
            raise ValueError("Coefficient 'a' cannot be 0 in a quadratic equation.")

        self.__a = float(a)
        self.__b = float(b)
        self.__c = float(c)

    @property
    def a(self):
        return self.__a

    @property
    def b(self):
        return self.__b

    @property
    def c(self):
        return self.__c

    def discriminant(self):
        return self.__b * self.__b - 4 * self.__a * self.__c

    def root1(self):
        if self.discriminant() < 0:
            return None
        return (-self.__b + self.discriminant() ** .5)/(2 * self.__a)

    def root2(self):
        if self.discriminant() < 0:
            return None
        return (-self.__b - self.discriminant() ** .5)/(2 * self.__a)

    def aTerm(self, a):
        if a == 1.0:
            return 'x^2'
        if a == -1.0:
            return '-x^2'
        return str(a) + 'x^2'

    def bTerm(self, b):
        if b < 0:
            if b == -1.0:
                return ' - x'
            return ' - ' + str(abs(b)) + 'x'
        if b == 0:
            return ''
        if b == 1.0:
            return ' + x'
        return ' + ' + str(abs(b)) + 'x'

    def cTerm(self, c):
        if c < 0:
            return ' - ' + str(abs(c))
        if c == 0:
            return ''
        return ' + ' + str(abs(c))

    def __str__(self):
        return self.aTerm(self.__a) + self.bTerm(self.__b) + self.cTerm(self.__c) + ' = 0'
