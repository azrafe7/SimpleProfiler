SimpleProfiler
==============

A simpler profiler for Python functions.

Description
-----------
It works as a function decorator and writes out simple stats on standard output when the program terminates.

Usage
-----------
Import `profile` from `SimpleProfiler` and use it to decorate the functions that you want to profile/time.

Example
-----------

test.py:

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

	
Output:

              name      calls         total_time       average_time
              ----      -----         ----------       ------------
       doSomething         20             0.2290             0.0115
            doMath         30             2.7212             0.0907



PS: Change `range` to `xrange` in the test with Python < 3.0. 