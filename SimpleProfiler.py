from time import time, clock
import atexit

__author__ = 'azrafe7'
__date__ = '08 apr 2013'
__version__ = '0.1'

# function used for timing (time.time() or time.clock())
_timeit = time

_timings = {}
_default_values = [
	('name', ''), 
	('calls', 0), 
	('total_time', 0.0), 
	('average_time', 0.0)]


# use this to decorate the functions you want to profile
def profile(fn):
	def wrapper(*args, **kwargs):
		fn_name = fn.__name__
		_timings.setdefault(fn_name, dict(_default_values))
		
		# calc elapsed time
		t0 = _timeit()
		result = fn(*args, **kwargs)
		elapsed = _timeit()-t0

		# update timings
		timings = _timings[fn_name]
		timings['name'] = fn_name
		timings['calls'] += 1
		timings['total_time'] += elapsed
		timings['average_time'] = timings['total_time']/timings['calls']
	
		return result
		
	return wrapper

	
def leave():
	if len(_timings) <= 0: return	# exit early if no timings are available
	
	fields = [key for key, value in _default_values]
	
	header_format = "{0:>30} {1:>10} {2:>18} {3:>18}"
	header = header_format.format(*fields)
	print("\n" + header + "\n" + "".join([c if c == ' ' else '-' for c in header]))
	
	table_format = "{name:>30.30} {calls:>10} {total_time:>18.4f} {average_time:>18.4f}"
	for item in _timings.values():
		print(table_format.format(**item))
	print("")

# print timings on exit
atexit.register(leave)