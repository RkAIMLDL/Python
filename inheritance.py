
from unicodedata import name


class A:
    def grandparant(self):
        print('grandparent class')
        pass
    pass

class B(A):
    def parent(self):
        print('parent class')
        pass
    pass

class C(B,A):
    def children(self):
        print('children class')

a1=A
a2=B
a3=C

a1.grandparant()