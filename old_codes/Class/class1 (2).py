class Profile:
	"""my profile"""
	def __init__(self, first, last, age):
		self.first = first
		self.last = last
		self.age = age
	def intro(self):
		full_name = self.first + " " + self.last
		age = int(self.age)
		print(f"My name is {full_name.title()}.\nMy age is {self.age}.")
mf = Profile('harikesh', 'kumar', '21')
mf.intro()
		