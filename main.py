#pass generator

import random
def func1(param):
    f = ""
    for i in param:
        f += i
    return f
def func2(param):
    f = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    oo=random.choice(f)
    for i in param:
        oo += i
    return oo
dataset='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!#$%&()*+-./:;<=>?{|}'
a="abcdefghijklmnopqrstuvwxyz"
A="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num="0123456789"
sym="!#$%&()*+-./:;<=>?{|}"
l=int(input("Enter the passwordwords size : "))
if l<6:
    print ("It should contains at least 6 caracters !")
elif l>50:
    print ("It must be inferior or equals 50 !")
else:
    p1=random.choice(a)
    p2=random.choice(A)
    p3=random.choice(num)
    p4=random.choice(sym)
    p5=random.sample(dataset,l-5)
    p5=random.sample(dataset,l-5)
    p5=random.sample(dataset,l-5)
    p5=func1(p5)
    p=[p1,p2,p3,p4,p5]
    random.shuffle(p)
    random.shuffle(p)
    random.shuffle(p)
    password=func2(p)
    print ("The password Generated is :\n",password)

  