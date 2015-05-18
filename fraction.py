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
                while gcd(self.a, self.b) != 1:
                        k = gcd(self.a, self.b)
                        self.a = self.a / k
                        self.b = self.b / k
        def printFraction(self):
                print str(self.a) + "/" + str(self.b)
        def getReciprocal(self):
                if self.a != 0:
                        return Fraction(self.b, self.a)
                else:
                        return Fraction("Undefined", "Undefined")
        def reciprocate(self):
                if self.a != 0:
                        k = self.a
                        self.a = self.b
                        self.b = k
                else:
                        self.a = "Undefined"
                        self.b = "Undefined"
        def printDecimal(self):
                print float(self.a) / float(self.b)


class Controller:
        def __init__(self):
                pass
        def getFraction(self, a, b):
                return Fraction(a,b)
        def multiply(self, frA, frB):
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
                return self.multiply(frA, frB.getReciprocal())

def getController():
        return Controller()
