## Animal is-a object
class Animal(object):
	def truth(self):
		print "Mammals are the coolest"

## Dog is-a animal
class Dog(Animal):
	def __init__(self, name):
		## Dog has-a name
		self.name = name
	
	def bark(self):
		print "Dogs like to bark."

## Cat is-a animal
class Cat(Animal):
	def __init__(self, name):
		## Cat has-a name
		self.name = name

## Person is a object
class Person(object):
	def __init__(self, name):
		## Person has-a name
		self.name = name
		
		## Person has-a pet
		self.pet = None
	
	def truth(self):
		return "Mammals are the coolest"

## Employee is-a Person
class Employee(Person):
	def __init__(self, name, salary):
		## Call the __init__ method of Employee's base class (Person)
		super(Employee, self).__init__(name)
		## Employee has-a salary
		self.salary = salary
		
## Fish is-a object
class Fish(object):
	pass

## Salmon is-a Fish
class Salmon(Fish):
	pass

## Halibut is-a Fish
class Halibut(Fish):
	pass
	
