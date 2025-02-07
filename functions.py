# Built-in functions/standard library functions


y= max(45,65,90,76,12,7)
print("The maximum value is", y)

x= min(15,3,24,67,54,5)
print("Minimum value is", x)

#User-defined functions
def name():
    print("Ian")
name() #Calling a function


def multiply():
    x = 10
    y = 2
    print(x * y)
multiply()


#Parameter/Variable and argument/Value
def add(a,b):

    print(a+b)
add(10,20)
add(7,7)


def employee( name,gender,position,salary,age):
    print(name,gender,position,salary,age)

employee("Sung Jinwoo","Male","CEO",1000000,25)
employee("Chae inhin","Female","Vice-CEO",700000,23)
employee("Gobta kun","Male","Supervisor",500000,30)
employee("Diablo sensei","Female","manager",100000,25)
employee("Eren yeegur","Male","Manager",100000,25)







#A program that displays details of 5 students
#Should be user Defined Function with Parameter
#Fullname ,Age ,Course, gender


def details(fullname,age,course,gender):
    print(fullname,age,course,gender)

details("anna simp",19,"MIT","female")
details("Noone Noose",18,"Cyber security","female")
details("Yoro shiku",20,"MIT","male")
details("Letta ingne",18,"Analysis","female")
details("Sung jin",21,"Java script","male")












