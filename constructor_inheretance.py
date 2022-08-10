class A:
    def __init__(self):
        print('in A init')
    def feature1(self):
        print('feature 1  working')
    def feature2(self):
        print('feature 2 working')


class B:
    def __init__(self):
        print('in B init')
    def feature1(self):
        print('feature 1_B working')
    def feature3(self):
        print('feature 3 working')


class C(A,B):
    def __init__(self):
        super().__init__()    # super cocept
        print('in c init')
        pass
    pass

a1=C()

a1.feature1()   #method resolution order -(it alwage give priority from left to right)
