#Simple function
def greet():
    print("Hola")
    print("Que tal?")
    print("chau")

greet()

#FUnction that allows for input

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How are you today {name}?")
greet_with_name("Gian")

#Function with more than 1 input

def greet_with_2_parameters(name, location):
    print(f"Hey! {name} where are you?")
    print(f"Im in {location}")
greet_with_2_parameters(location = "Buenos Aires", name = "Gian") # keyboard argument vs positional argument