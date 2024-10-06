Name = "yazeed"
Age = 25

def HelloWorld():
  print(f"hello, {Name}. You are {Age} years old")

def addTwoNumbers(a,b):
 return a+b

total = addTwoNumbers(5,10)
print(total)

class person:
    def __init__(self, Name, Age):
        self.Name = Name
        self.Age = Age

    def details(self):
      print(f"Name: {self.Name}, Age: {self.Age}")
