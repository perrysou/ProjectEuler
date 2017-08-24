import math


class Complex(object):
    def __init__(self, real=0.0, imaginary=0.0):
        self.real = real
        self.imaginary = imaginary
        
    def __add__(self, no):
        total = Complex()
        total.real = self.real + no.real
        total.imaginary = self.imaginary + no.imaginary
        return total

    def __sub__(self, no):
        diff = Complex()
        diff.real = self.real - no.real
        diff.imaginary = self.imaginary - no.imaginary
        return diff
        
    def __mul__(self, no):
        prod = Complex()
        prod.real = self.real * no.real - self.imaginary * no.imaginary
        prod.imaginary = self.real * no.imaginary + no.real * self.imaginary
        return prod
    
    def __div__(self, no):
        quo = Complex()
        quo.real = (self.real * no.real + self.imaginary * no.imaginary) / (no.real ** 2 + no.imaginary ** 2)
        quo.imaginary = (no.real * self.imaginary - self.real * no.imaginary) / (no.real ** 2 + no.imaginary ** 2)
        return quo
    
    def mod(self):
        mag = Complex()
        mag.real = math.sqrt(self.real ** 2 + self.imaginary ** 2)
        mag.imaginary = 0.0
        return mag

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result

if __name__ == '__main__':
    c = map(float, raw_input().split())
    d = map(float, raw_input().split())
    x = Complex(*c)
    y = Complex(*d)
    print '\n'.join(map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]))
