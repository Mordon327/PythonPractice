class Website:
	def __init__(self, title):
		self.title = title

class DifferentWebsite:
	title = 'My Class Title'

#Instance Attribute is shown with its behavior
ws = Website('My Website Title')
#Title of instance is displayed
print(ws.__dict__)

ws_two = Website("My Second Title")

print(ws_two.__dict__)

#Class Attribute is shown with its behavior
dw = DifferentWebsite()
#Title is not displayed due to the title being apart of the class and not the instance
print(dw.__dict__)
#Title is displayed
print(dw.title)