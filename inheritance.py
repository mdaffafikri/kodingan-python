class Ortu():
    def __init__(self,last_name,hair_color):
        self.last_name = last_name
        self.hair_color = hair_color

    def show(self):
        print(self.last_name + " hair color is " + self.hair_color)

class Child(Ortu):
    def __init__(self, last_name, hair_color, badge):
        Ortu.__init__(self, last_name, hair_color)
        self.badge = badge 

    def show(self):
        print(self.last_name + " warna rambut "+ self.hair_color + " and have " +self.badge+" badge")

riolu = Child("lucario", "black", str(3))
riolu.show()