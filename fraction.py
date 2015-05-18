'''
An alternate fraction system (still imports gcd from fractions though)
'''

from fractions import gcd #the function is simple enough that it can be moved into this file if needed. 
#Until then, we rely on that system for one calculation

class Fraction:
        def __init__(self, a, b):
                if b == 0:
                        a = "Undefined"
                        b = "Undefined"
                self.a = a
                self.b = b
                if abs(a) != a and abs(b) != b or abs(a) == a and abs(b) != b:
                        self.a = self.a * -1
                        self.b = self.b * -1
                self.reduce()
        def reduce(self):
                '''Reduces fraction down to lowest terms ie. 3/6 > 1/2'''
                while gcd(self.a, self.b) != 1:
                        k = gcd(self.a, self.b)
                        self.a = self.a / k
                        self.b = self.b / k
        def printFraction(self):
                '''Returns the standard way of writing fractions ie. 3/6'''
                return str(self.a) + "/" + str(self.b)
        def getReciprocal(self):
                '''Returns the reciprocal of the fraction (does not modify the object itself'''
                if self.a != 0:
                        return Fraction(self.b, self.a)
                else:
                        return Fraction("Undefined", "Undefined")
        def reciprocate(self):
                '''Modifies the object into its reciprocal (and doesn't return anything)'''
                if self.a != 0:
                        k = self.a
                        self.a = self.b
                        self.b = k
                else:
                        self.a = "Undefined"
                        self.b = "Undefined"
        def printDecimal(self):
                '''Returns the decimal form of the fraction ie. 1/2 > 0.5'''
                return float(self.a) / float(self.b)


class Controller:
        def __init__(self):
                pass
        def getFraction(self, a, b):
                '''Returns a fraction of the form a/b'''
                return Fraction(a,b)
        def multiply(self, frA, frB):
                '''Multiplies two fractions together'''
                a = frA.a * frB.a
                b = frA.b * frB.b
                inst = Fraction(a, b)
                inst.reduce()
                #while gcd(a, b) != 1:
                #       k = gcd(a, b)
                #       a = a / k
                #       b = b / k
                #return Fraction(a,b)
                return inst
        def divide(self, frA, frB):
                '''Divides two fractions'''
                return self.multiply(frA, frB.getReciprocal())

def getController():
        return Controller()
