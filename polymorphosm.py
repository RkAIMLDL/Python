#polymorphism -(many form)  one thing can take multiple form
#duck oveloading
#method overloading
#method overriding

#duck method
class pycharm:
    def execute(self):
        print('compiling')
        print('running')
        pass
    pass

class editor:
    def execute(self):
        print('spell ckeck')
        print('convention ckeck')
        print('compiling')
        print('running')


class laptop:
    def code(self,ide):
        ide.execute()


ide=editor()

lap=laptop()
#lap.code(ide)


#syntetic suger


class student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2

    def __add__(self,other):
        m1=self.m1+other.m1
        m2=self.m2+other.m2
        s3=student(m1,m2)
        return s3
    def __gt__(self,other):
        r1=self.m1+self.m2
        r2=other.m1+other.m2

        if r1>r2:
            return True
        else:
            return False
    def __str__(self) :
        return self.m1,self.m2


                



s1=student(30,39)
s2=student(77,33)
s3=s1+s2
print(s3.__str__())
print(s1.__str__())


if s1>s2:
    print('s1 win')
else:
    print('s2 win')



#overloading and overriding
class A:

    def show(self):
        print('in A show')


class B(A):
    def show(self):
        print('in B show')


a=B()

a.show()   # overindigly show in B instead of A 



class student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
        
    def sum(self,a=None,b=None,c=None):
        s=0
        if a!=None and b!=None and c!=None:
            s=a+b+c
        elif a!=None and b!=None:
            s=a+b
        else  :
             s=a


s1=student(13,56)
print(s1.sum(12,3,6))