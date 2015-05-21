'''
An alternate fraction system (still imports gcd from fractions though)
'''

from fractions import gcd #the function is simple enough that it can be moved into this file if needed. 
#Until then, we rely on that system for one calculation

from math import sqrt

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
                '''Returns the reciprocal of the fraction (does not modify the object itself)'''
                if self.a != 0:
                        return Fraction(self.b, self.a)
                else:
                        return Fraction("Undefined", "Undefined")
        def reciprocate(self):
                '''Modifies the instance into its reciprocal (and doesn't return anything)'''
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
        def printMixed(self):
                '''Returns a mixed fraction ie. 5/3 > 1 2/3 and -5/3 > -1 2/3'''
                if self.a == 0:
                        return "0"
                a = abs(self.a)
                count = 0
                while a / self.b > 0:
                        count += 1
                        a -= self.b
                if abs(self.a) != self.a and count != 0:
                        count = count * -1
                elif abs(self.a) != self.a and count == 0:
                        a = a * -1
                if count != 0:
                        return str(count) + " " + str(a) + "/" + str(self.b)
                else:
                        return str(a) + "/" + str(self.b)
        def square(self):
                '''Returns the square of the fraction'''
                #return Controller().multiply(self, self) #Deprecated Method
                return self * self
        def printSqrtDecimal(self):
                '''Prints in decimal form, eg. root 3/2 > 1.22474487139'''
                return sqrt(self.a) / sqrt(self.b)
        def __mul__(frA, frB):
                '''Multiplies two fractions together'''
                a = frA.a * frB.a
                b = frA.b * frB.b
                inst = Fraction(a, b)
                inst.reduce()
                return inst
        def __add__(frA, frB):
                '''Adds two fractions'''
                aS = [frA.a, frB.a]
                bS = [frA.b, frB.b]
                if bS[0] != bS[1]:
                        k = bS[0] * bS[1]
                        #aS[0] = aS[0] * (k / bS[0])
                        for x in range(0, 2):
                                aS[x] = aS[x] * (k / bS[x])
                                bS[x] = k
                fr = Fraction(aS[0] + aS[1], bS[0])
                fr.reduce()
                return fr
        def __div__(frA, frB):
                '''Multiplies two fractions together'''
                return Fraction.__mul__(frA, frB.getReciprocal())
        def __sub__(frA, frB):
                '''Subtracts two fractions'''
                return Fraction.__add__(frA, Fraction(frB.a * -1, frB.b))

class Controller:
        '''DEPRECATED: Creates a Controller instance, currently used to easily get Fractions and perform operations between them'''
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
        def add(self, frA, frB):
                '''Adds two fractions'''
                aS = [frA.a, frB.a]
                bS = [frA.b, frB.b]
                if bS[0] != bS[1]:
                        k = bS[0] * bS[1]
                        #aS[0] = aS[0] * (k / bS[0])
                        for x in range(0, 2):
                                aS[x] = aS[x] * (k / bS[x])
                                bS[x] = k
                fr = self.getFraction(aS[0] + aS[1], bS[0])
                fr.reduce()
                return fr
        def subtract(self, frA, frB):
                '''Subtracts two fractions'''
                return self.add(frA, Fraction(frB.a * -1, frB.b))

def getController():
        '''Gets a controller instance'''
        return Controller()
