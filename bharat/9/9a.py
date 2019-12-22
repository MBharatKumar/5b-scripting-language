class student:
    def __init__(self):
        self.name = 0
        self.age = 0

    def disp(self):
        print(self.name)
        print(self.age)
        print(self.marks)

    def accept(self):
        self.name = input("enter name")
        self.age = input("enter age")
        self.marks = input("enter marks in 3 subject with space between it ")
        self.marks = list((self.marks.split(' ')))

s1 = student()
s1.accept()
s1.disp()
