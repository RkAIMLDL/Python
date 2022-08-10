from sqlalchemy import false


class computer:
    def __init__(self):
        self.name='rushikesh'
        self.age=21
        pass
    def update(self):
        self.age=20
        pass
    def compare(self,other):
        if self.age==other.age:
            return True
        else:
            return False    


c1=computer()
c2=computer()

c1.name='rishi'
c1.age=20
c1.update()

if c1.compare(c2):
    print('they are equal')
else:
    print('they are not equal')    

print(c1.age)
print(c2.age)
