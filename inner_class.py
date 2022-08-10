


class student:
    def __init__(self,name,rollnumber):
        self.name=name
        self.rollnumber=rollnumber
        self.lap=self.laptop()

        pass
    def show(self):
        print(self.name,self.rollnumber)
        self.lap.show()
        pass
    class laptop:
        def __init__(self):
            self.brand='hp'
            self.core='i5'
            self.ram=8
            pass
        def show(self):
            print(self.brand,self.core,self.ram)
            pass
        pass
    pass

s1=student('rushikesh',37)
s2=student('hemantkumar',36)
s1.show()
        

