from functools import reduce


num=[2,4,5,78,14,16]
even=list(filter(lambda n:n%2==0,num))
double=list(map(lambda n:n*2,even))
sum=reduce(lambda a,b:a+b,double)
print(even)
print(double)
print(sum)