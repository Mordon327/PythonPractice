#Define class Invoice
class Invoice:
	#Dunder method - Key word function that defines variables that are used in all this class's functions
	def __init__(self, client, total):
		#Defined variables that can be called in this class's functions where self is passed in
		self._client = client
		self.total = total
		#Using an underscore infront of a variable defines it as protected. Direct changes will not affect it.
		#Using two underscores infront of a variable defines it as private.
	#Formatter function that takes in all variables from init function and formats it
	def formatter(self):
		return f'{self._client} owes: ${self.total}'

	#Getter function for protected variable
	@property
	def client(self):
		return self._client
	
	#Setter function for protected variable
	@client.setter
	def client(self, client):
		self._client = client

#Instantiate class in local variables
google = Invoice('Google', 100)
snapchat = Invoice('SnapChat', 200)
#Print variables
print(google.formatter())
print(snapchat.formatter())
print(google.client)
google.client = 'Yahoo'
print(google.client)