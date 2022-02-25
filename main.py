class Tank():

    def __init__(self, Name, Age, Speed, weight, The_country):
        self.Name = Name
        self.Age = Age
        self.Speed = Speed
        self.weight = weight
        self.The_country = The_country

    def fire(self):
        print(self.Name.title() + 'стрельнул')

    def ride(self):
        print(self.Name.title() + 'поехал')

    def stop(self):

        print(self.Name.title() + 'остановился')

    def turn_right(self):
        print(self.Name.title + 'повернул на право')

    def turn_left(self):
        print(self.Name.title + 'повернул на лево')

T_34 = Tank('T_34 ', 82, 54, 26, 'Russia')
T_90 = Tank('Владимир', 30, 70, 46, 'Russia')
T_14 = Tank('Армато ', 3, 82, 53, 'Russia')
M_1 = Tank('Abrams ', 42, 60, 54, 'USA')

