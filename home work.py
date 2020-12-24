#for loop
'''
for i in range(1,11):
    print(i)
'''
#while loop
'''
x = 1
while x<=10:
    print(x)
    x+=1
'''    
#factorial of a number-5-5*4*3*2*1
'''
x = int(input("Enter a Number : "))
result = 1
for i in range(1,x+1):
    result = result*i
print(result)
'''
'''
x = int(input("Enter a Number : "))
result = 1
while x>=1:
    result = result*x
    x-=1
print(result)
'''
#fibonacci series 0 1 1 2 3
'''
f=0
s=1
print(f)
print(s)
i=1
while i<=8:
    t=f+s
    print(t)
    f,s=s,t
    i+=1
'''
'''
for i in range(8):
    t=f+s
    print(t)
    f,s=s,t
'''    
#check wether number is prime or not
x = int(input("Enter Number : "))

for i in range(2,x):
    if x%i==0:
        print("not prime")
        break
else:
    print("Prime")


    
#find sum of digits of a number

#find the reverse of a number
