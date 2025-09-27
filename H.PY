
class BioData:
  def __init__(self, name, age, gender, height, weight):
    self.name = name
    self.age = age
    self.gender = gender
    self.height = height
    self.weight = weight

import request

def sleep(self):
  print('{} is sleeping on the bed.'.format(self.name))

def coding(self):
    print('{} is coding on his pc.'. format(self.name))

def get_age(self):
    print('{} is {} years old.'.format(self.name, self.age))

def get_gender(self):
    print('{} is a {}.'.format(self.name, self.gender))

def get_height(self):
      print('{} is {} cm tall.'. format(self.name, self.height))

def get_weight(self):
    print('{} weighs {} kg.'.format(self.name, self.weight))

# Create an object of the class
person = BioData("Victor", 20, "Male", 185.4, 50)

# Example usage
print(person.name)
person.sleep()
person.coding()
person.get_age()
person.get_gender()
person.get_height()
person.get_weight()


