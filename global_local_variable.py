a=3
print(id(a))
def something():
  
    x=globals()['a']
    print(id(a))
    print('Inside',a)
something()
x=locals()['a']     
print('outside: ',a)    
