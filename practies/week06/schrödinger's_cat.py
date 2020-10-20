import random
class Cat:
    def __init__(self):
        self.cat = None

    def is_cat_dead(self):
        __temp = random.randint(0, 1)

        if __temp == 0:
            self.cat = False
        else:
            self.cat = True

        if(self.cat):
            print("Cat is dead!")
        else:
            print("Cat is not daed!")

if __name__ == "__main__":
    cat = Cat()
    cat.is_cat_dead()