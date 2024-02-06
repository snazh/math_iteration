class Function:
    pass


class Polynomial(Function):
    def __init__(self, coeffs):
        self.coeffs = coeffs

    def __str__(self):
        terms = [f" + {abs(coeff)}x^{len(self.coeffs) - power}" if coeff > 0
                 else f" - {abs(coeff)}x^{len(self.coeffs) - power}"
                 for power, coeff in enumerate(self.coeffs, 1)]
        return "".join(terms)[2:-3] + ' = 0'

    def function_value(self, value):
        if value == 0.0:
            return self.coeffs[-1]  # Correctly return the constant term
        terms = (coeff*value**(len(self.coeffs)-power) for power, coeff in enumerate(self.coeffs, 1))
        print(sum(terms))
        return sum(terms)


class Iteration:
    def __init__(self, funcType, accuracy):
        self.funcType = funcType
        self.accuracy = accuracy

    def half_division(self, coeffs, a, b):

        match self.funcType:
            case 1:  # Polynomial function
                obj = Polynomial(coeffs)
                while (b - a) > 2 * self.accuracy:

                    c = (b + a) / 2

                    if obj.function_value(a) < 0 or obj.function_value(c) < 0:

                        b = c
                    else:
                        a = c
                x = (a + b) / 2
                return x

    def chords_method(self, coeffs, a, b):
        match self.funcType:
            case 1:
                obj = Polynomial(coeffs)
                while abs(b - a) > self.accuracy:
                    c = a - ((b - a) * obj.function_value(a) / (obj.function_value(b) - obj.function_value(a)))
                    if obj.function_value(a) < 0 or obj.function_value(c) < 0:
                        a = c
                    else:
                        b = c
                x = (a + b) / 2
                return x


if __name__ == '__main__':
    '''
    Instructions: 
    1) function Types:
        1 - Polynomial function  
    '''
    pol = (1, 0, -1.34, 1.2)
    print(Polynomial(pol))
    object1 = Iteration(funcType=1, accuracy=0.0001)

    print(object1.chords_method(pol, a=-2, b=0))
    print(object1.half_division(pol, a=-2, b=0))
#          3x^3 - 4x^2 + 5x + 0.1
