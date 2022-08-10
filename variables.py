class car:
    def __init__(self):
        self.mil=10
        self.com='BMW'     #} instance varible
        pass

c1=car()
c2=car()
c1.mil=8
car.wheel=5    #class variable
print(c1.com,c1.mil,c1.wheel)
print(c2.com,c2.mil,c2.wheel)