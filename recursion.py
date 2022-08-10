import sys
sys.setrecursionlimit(2000)
print(sys.setrecursionlimit)
i=0
def greet():
 
    global i
    i+=1
    print('hello',i)
    greet()
greet()    