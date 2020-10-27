import utils.get_input

# overview: a pet with pet name, it's type and age
class Pet():
    # initialize pet attribute
    def __init__(self, name, animal_type, age):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age

    # return pet's name
    def get_name(self):
        return self.__name

    # return pet's animal type
    def get_animal_type(self):
        return self.__animal_type

    # return pet's age
    def get_age(self):
        return self.__age

    # set pet's name eq name
    def set_name(self, name):
        self.__name = name

    # set pet's animal type eq animal type
    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type

    # set pet's age eq age
    def set_age(self, age):
        self.__age = age

    def to_string(self):
        return "Pet: {" + "name: " + self.__name + ", animal_type: " + self.__animal_type + ", age: " + self.__age + "}"

if __name__ == '__main__':
    name = input("Enter pet's name: ")
    animal_type = input("Enter pet's animal type: ")
    age = utils.get_input.number("Enter pet's age: ")

    pet = Pet(name,animal_type,age)
    print(pet.to_string())