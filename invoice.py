#Define new class
class Invoice:
	#define new function within class. Keyword self is used when a function has no input params.
	def greeting(self):
		return 'Hi there'

#instantiate class
inv_one = Invoice()
#Print class function
print(inv_one.greeting())