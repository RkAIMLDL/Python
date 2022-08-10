def count(list):
    even=0
    odd=0
    for i in list:
        if i%2==0:
            even+=1
        else:
             odd +=1
    return even,odd             


list=[11,14,15,16,18,20,22]
even,odd=count(list)
print('even : {} and odd : {}'.format(even,odd))