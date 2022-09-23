import random
import time


class Human:
    def __init__(self, name):
        self.name = name
        self.gladness = 0
        self.money = 200
        self.car = None

    def nothing(self):
        print(
            f"{self.name} ничего не делает. Счастье: {self.gladness} Деньги: {self.money}")

    def rest(self):
        cost = 15
        # Проверяем достаточно ли денег
        # Если нет, то человек ничего не делает
        # Если есть, то действия ниже
        if self.money >= cost:
            self.gladness += random.randint(3, 5)
            # Уровень счастья не может быть больше 100
            if self.gladness >= 0:
                self.gladness = 100
            # =======================================
            self.money -= cost
            print(
                f"{self.name} отдыхает. Счастье: {self.gladness} Деньги: {self.money}")
        else:
            self.nothing()

    def work(self):
        self.gladness -= random.randint(2, 5)
        # Уровень счастья не может быть меньше 0
        if self.gladness <= 0:
            self.gladness = 0
        # =======================================
        self.money += 20
        print(f"{self.name} работает. Счастье: {self.gladness} Деньги: {self.money}")

    # Добавить использование функции drive машины
    def drive(self):
        if self.car:
            self.car.drive()


class Car:
    def __init__(self, brend, price):
        self.brend = brend
        self.price = price
        self.owner = None

    def drive(self):
        if self.owner:
            print("Car is driving")

    def buy(self, human):
        # Проверяем есть ли у машины хозяин
        # Проверяем хватит ли человеку денег
        # Связываем машину с человеком
        # В принт выводим кто купил какую машину
        if not self.owner:
            if human.money >= self.price:
                human.money -= self.price
                self.owner = human
                self.owner.car = self
                print(f"{human.name} купил {self.brend}")
            else:
                print(
                    f"{human.name} не хватает {self.price - human.money} на покупку {self.brend}")
        else:
            print(f"У {self.brend} уже есть хозяин {self.owner.name}")
class Pet:
    def __init__(self, name1, species, price1):
        self.name1 = name1
        self.species = species
        self.price1 = price1
        self.owner = None
    def buy1(self, human):

        if not self.owner:
            if human.money >= self.price1:
                human.money -= self.price1
                self.owner = human
                self.owner.pet = self
                print(f"{human.name} купил {self.species}")
            else:
                print(
                    f"{human.name} не хватает {self.price - human.money} на покупку {self.species}")
        else:
            print(f"У {self.species} уже есть хозяин {self.owner.name}")
    def play(self):
        if self.owner:
            print("Pet is happy now.")



humans = [
    Human(name="Andrey"),
    Human(name="Anton"),
    Human(name="Maxim"),
]

cars = [
    # Создать 3 машины
    Car("Audi", 200),
    Car("Bentli", 100),
    Car("Nissan", 700),
]
pets = [

    Pet("amogus", "dog", 50),
    Pet("bebra", "pig", 100),
    Pet("vanya2014", "cat", 50),
]

days = 1
while True:
    print(f"Day: {days}")
    for human in humans:
        action = random.choice([human.nothing, human.rest, human.work])
        action()

        if random.randint(1, 100) <= 5:
            car = random.choice(cars)
            car.buy(human)
        if random.randint(1, 100) <= 5:
            pet = random.choice(pets)
            pet.buy1(human)

    days += 1
    time.sleep(0.1)
