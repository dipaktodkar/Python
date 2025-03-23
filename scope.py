message="Welcome" #Global scope
def greet():
    message="Namaste" #Local Scope
    print(message)
print(message)
greet()