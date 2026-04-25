import random
class PowerBall:
	def __init__(self, numOfBalls = 0):
		self.numOfBalls = numOfBalls

	def returnNumbers(self):
		self.numOfBalls += 1
		return f'{random.randrange(1, 100, 2)}'

	def count(self):
		if self.numOfBalls == 9:
			return False
		else:
			return True

ballCount = 0
num1 = PowerBall()
print(num1.returnNumbers())
print(num1.count())
print(num1.returnNumbers())
print(num1.count())
print(num1.returnNumbers())
print(num1.count())
print(num1.returnNumbers())
print(num1.count())
print(num1.returnNumbers())
print(num1.count())
print(num1.returnNumbers())
print(num1.count())
print(num1.returnNumbers())
print(num1.count())
print(num1.returnNumbers())
print(num1.count())
print(num1.returnNumbers())
print(num1.count())