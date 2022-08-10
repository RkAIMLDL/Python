#instance method
#class method
#static method



class student:
    school='telesco'
    #instance method
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
        pass
    #static method
    def avg(self):
        return (self.m1+self.m2+self.m3)/3
        pass
    @classmethod
    def info(cls):
        return cls.school

s1=student(30,31,32)  
s2=student(40,41,42)  

print(s1.avg())
print(student.info())

