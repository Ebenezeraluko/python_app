print(f"Student Information".upper())
print(f"-------------------")
class Student:
    def __init__(self, name, age, tracks, score):
        self.name = name
        self.age = int(age)
        self.tracks = tracks
        self.score = float(score)

    def change_name(self, name):
        self.name = name
        return self.name

    def change_age(self, age):
        self.age = int(age)
        return self.age

    def add_track(self, tracks):
        self.tracks = tracks
        return self.tracks

    def get_score(self):
        return self.score


Bob = Student(name="Bob", age=26, tracks=["FE", "BE"], score=20.90)
# Expected methods
print(f"Student new name:",Bob.change_name("Peter"))
print(f"Student new age:",Bob.change_age(34),"years old")
print(f"Student's track:",Bob.add_track("Full stack"))
print(f"Student's score",Bob.get_score())

