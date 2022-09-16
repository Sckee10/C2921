import random


class Student:
    def __init__(self, name):
        self.name = name
        self.progress = 0
        self.gladness = random.randint(20, 40)

    def rest(self):

        self.progress -= 5
        self.gladness += 10
        pass

    def study(self):

        self.progress += 10
        self.gladness -= 5
        pass


students = [
    Student(name="Andrey"),
    Student(name="Anton"),
    Student(name="Maxim"),
]


days = 1
end = False
while True:
    print(f"Day: {days}")
    for student in students:
        # Выбираем случайное действие студента
        action = random.choice([student.rest, student.study])
        action()
        if student.progress > 100:
            end = True
    if end:
        break
    days += 1

print(students[0].progress, students[1].progress, students[2].progress)
print("hi")
