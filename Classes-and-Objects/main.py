class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name = str(name)
        self.age = int(age)
        self.tracks = list(tracks)
        self.score = float(score)

    def change_name(self, name):
        print(str(name))

    def change_age(self, age):
        print(int(age))

    def add_track(self, tracks):
        self.tracks += [tracks]
        print(str(self.tracks))

    def get_score(self):
        print(float(self.score))


Bob = Student(name="Bob", age=26, tracks=["FE", "BE"], score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()
