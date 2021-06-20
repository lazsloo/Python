class User:		# declare a class and give it name User
    def __init__(self):
        self.name = "Matt"
        self.email = "Matt@WickedSmaht.com"
        self.account_balance = 0
guido = User()
monty = User()
penis = User()
guido.name = "Guido"
monty.name = "Monty"
print(penis.email)	# output: Matt@WickedSmaht.com
print(penis.account_balance)	# output: 0, because you're poor
print(guido.name)	# output: Guido
print(penis.name)	# output: Matt
print(monty.name)	# output: Monty

class User:
    def __init__(self, username, email_address):# now our method has 2 parameters!
        self.name = username			# and we use the values passed in to set the name attribute
        self.email = email_address		# and the email attribute
        self.account_balance = 0		# the account balance is set to $0, so no need for a third parameter
    
    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
        self.account_balance += amount	# the specific user's account increases by the amount of the value received

    def make_withdrawl(self, amount):
        self.account_balance -= amount
# guido = User("Guido van Rossum", "guido@python.com")
# monty = User("Monty Python", "monty@python.com")
# print(guido.name)	# output: Guido van Rossum
# print(monty.name)	# output: Monty Python
# print(guido.email)
# print(monty.email)

# class User:		# here's what we have so far
#     def __init__(self, name, email):
#         self.name = name
#         self.email = email
#         self.account_balance = 0
#     # adding the deposit method
#     def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
#         self.account_balance += amount	# the specific user's account increases by the amount of the value received
guido = User("Guido", "Guido@gmail.com")
monty = User("Montey", "Monty@gmail.com")
guido.make_deposit(100)
guido.make_deposit(200)
monty.make_deposit(50)
guido.make_withdrawl(2)
print(f"{guido.name} account balance is: {guido.account_balance} wow boy you broke")	# output: 300
print(f"{monty.name} account balance is: {monty.account_balance} damn and I thought {guido.name} was broke but DAMN! you broker then a mutha fucka")	# output: 50c

def varargs(arg1, *args):
    print("Got ", arg1, " and ", args)
varargs("one") 			# output: Got one and ()
varargs("one", "two") # output: Got one and ('two',)
varargs("one", "two", "three", "four", "five", "six") # output: Got one and ('two', 'three')

def varargs(arg1, *args):
    for a in args:
        print(a)
varargs("one", "two", "three") # output: two, three (on separate lines)

class SLNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class SList:
    def __init__(self):
        self.head = None

my_list = SList()

class Parent:
    def method_a(self):
        print("invoking PARENT method_a!")
class Child(Parent):
    def method_a(self):
        print("invoking CHILD method_a!")
dad = Parent()
son = Child()
dad.method_a()
son.method_a() #notice this overrides the Parent method!

# We'll use the Person class to demonstrate polymorphism
# in which multiple classes inherit from the same class but behave in different ways
class Person:
    def pay_bill(self):
        raise NotImplementedError
# Millionaire inherits from Person
class Millionaire(Person):
    def pay_bill(self):
        print("Here you go! Keep the change!")
# Grad Student also inherits from the Person class
class GradStudent(Person):
    def pay_bill(self):
        print("Can I owe you ten bucks or do the dishes?")
b = Millionaire()
c = GradStudent()
b.pay_bill()
c.pay_bill()