from SimpleProfiler import profile

ITERATIONS = 100000

@profile
def doSomething():
	for _ in range(ITERATIONS):
		pass

@profile
def doMath(x):
	sum = 0
	for i in range(ITERATIONS):
		sum += x * x * i
	return sum

def notProfiled(x, y):
	sum = 0
	for _ in range(ITERATIONS):
		sum += x * y
	return sum

	
if __name__ == "__main__":
	for _ in range(10):
		doSomething()
		notProfiled(123, 456)
		notProfiled(321, 0)
		doMath(3)
		doMath(7**7)
		doSomething()
		doMath(666)
