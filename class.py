class student:

    def __init__(self,name,rollno,brand,cpu,ram) -> None:
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop(brand,cpu,ram)

    def show(self):
        print(self.name, self.rollno)
        self.lap.show()

    class Laptop:

        def __init__(self,brand,cpu,ram):
            self.brand = brand
            self.cpu = cpu
            self.ram = ram

        def show(self):
            print(self.brand, self.cpu, self.ram)

s1 = student('Rahul',2,"HP","Ryzen 3",8)
s2 = student('Khyati',1,"HP","i5",16)

s1.show()
s2.show()

