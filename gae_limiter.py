import logging
# from functools import wraps
import functools


class Limiter(object):
	"""docstring for Limiter"""
	# limit = staticmethod( limit )
	def __init__(self):
		super(Limiter, self).__init__()
		# pass
		# self.arg = arg
		
	def limit(self, limit_request, interval, per):
		"""
		Decorator to be use
		:param limit_value: the limit request number
		:param interval: num of years, months, days etc...
		:param interval_unit: str, year, month, day, hour, minute
		"""
		def actual_decorator(func):
			
			@functools.wraps(func)
			def wrapper(*args, **kwargs):
				# all limiter logic here
				logging.info(per)
					
				return func(*args, **kwargs)
			return wrapper
		return actual_decorator
