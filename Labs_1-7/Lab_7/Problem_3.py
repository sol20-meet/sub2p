# Write a simple class that defines a person
# with attributes of first_name, last_name
# and has a method signature of "speak" which
# prints the object as "Jefferson, Thomas".

class Person:
  def __init__(self, name, family):
    self.first_name = name
    self.last_name = family
  def speak(self):
  	print("My name is "+ self.first_name + " " + self.last_name)

me = Person("Sol", "2.0")
you = Person("George", "AbuDawwod")

me.speak()

