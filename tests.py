'''
A quick testing system I whipped up. There is probably a better way but for a first attempt I think I could have done worse.
'''

import fraction as f

testCase = 1 #Counts number of test cases
failed = [] #Remembers their numbers (not line numbers, test numbers)

def test(result, expected):
	'''The testing function'''
	global testCase, failed
	try:
		if result.a != expected.a and result.b != expected.b:
			print "Test Case: " + str(testCase) + " Test expected: " + str(expected.a) + "/" + str(expected.b) + " Received: " + str(result.a) + "/" + str(result.b)
			failed.append(testCase)
	except:
		if result != expected:
			print "Test Case: " + str(testCase) + " Test expected: " + expected + " Received: " + result
			failed.append(testCase)
	testCase += 1

def fra(a,b):
	'''Just a quick way to get a fraction for testing (easy to type in)'''
	return f.Fraction(a,b)
	
'''Enter test data beyond this point'''
	
s = f.getController()
a = s.getFraction(1,2)
b = s.getFraction(1,3)

test(a, fra(1,2))
test(b, fra(1,3))
test(s.add(a,b), fra(5,6))
test(s.subtract(a,b), fra(1,6))
test(s.multiply(a,b), fra(1,6))
test(s.divide(a,b), fra(3,2))

c = s.getFraction(7,3)
test(c, fra(7,3))

test(c.printMixed(), "2 1/3")




'''Beyond this point is summary code'''
print "------------------------------------------------------"
print "Number of Test Cases Failed: " + str(len(failed))
print "Test Cases Failed: " + str(failed)
