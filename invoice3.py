class Invoice:
	#Define variables for self
	def __init__(self, client, total):
		self.client = client
		self.total = total
	#Format function
	def __str__(self):
		return f'Invoice from {self.client} for {self.total}'

	def __repr__(self):
		return f'Invoice <value: client: {self.client}, total: {self.total}>'

#Instantiate
inv = Invoice('Google', 500)
#Call function
print(str(inv))
print(repr(inv))