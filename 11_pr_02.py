#Q. create  a class pets  from  a class  animale  and
# futher create  class dog  from  pets  add a method  bark  to class dog
#ans:
class Animals:
    animalType = "Mammal"

class Pets:
    color = "White"

class Dog:
    @staticmethod
    def bark():
        print("Bow bow!")

d  = Dog()
d.bark()