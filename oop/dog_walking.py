class Dog:

	species = "mammals"

	is_hungry= True

	def __init__(self, name, age):
		self.name= name
		self.age= age

	def reply(self):
		print("{} is {}").format(self.name, self.age)

	def eat(self):
		is_hungry = False

	def walk(self):
		print("{} is walking!").format(self.name)

#larry.reply(), fletcher.reply(), larry.reply()

class Pets:

	dogs = []

	def __init__(self, dogs):
		self.dogs= dogs

#initialization	
tom =Dog("Tom", 6)
fletcher = Dog("Fletcher", 7)
larry = Dog("Larry", 9)

list_dogs = [tom, fletcher, larry]

a_pet = Pets(list_dogs)

#output
"""
print("I have " + str(len(list_dogs)) + " dogs")
tom.reply()
fletcher.reply()
larry.reply()
print("And they are all {} of course").format(Dog.species)
"""

print("\n")
print("$$$")
for dog in a_pet.dogs:
	dog.walk()









#print(Dog.mammals)
