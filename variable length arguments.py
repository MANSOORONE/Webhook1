#First program that can give more than one value

print("My First Program")
print()

def fun1(*a):
    print(a)
    print(type(a))

fun1()
fun1(1,2,3,4,5)
fun1(1,"naresh","python")
print()

#second programe to find maximum number

print("My second program")
print()

def maximum(*n):
    m=0
    for value in n:
        if value>m:
            m=value
    return m
    
result1=maximum()
result2=maximum(10,20)
result3=maximum(1,2,3,4,5,6,7,8,9)
print(result1,result2,result3,sep="\n")
print()

#My third program to add number values 

print()
print("My third program")

def add(*n):
    s=0
    for value in n:
        s=s+value
    return s
def main():
    res1=add(10,20)
    res2=add(1,2,3,4)
    res3=add(100,200,300,400,500)
    print(res1,res2,res3)

main()

print()

#My 4th Program

print("My fourth program")
print()

def fun1(*p,q):
    print(p,q)

def fun2(q,*p):
    print(q,p)

def fun3(p,*q,r=100):
    print(p,q,r)

fun1(10,20,30,40,50,q=500)
fun2(10,20,30,40,50)
fun3(10)
fun3(10,20,30,40,50)
fun3(10,20,30,40,50,r=200)
