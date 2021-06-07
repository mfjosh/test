#version 0.1
def say_hi():
    if name == '':
        print('you did not enter a name!')
    else:
        print("Hello",name)
def show_age():
    if age =='':
        print('You must enter an age!')
    else:
        print('So you are',age)



#Main program sequence
print("Welcome to the program! Let's get started.")
name = input("Please Enter Name: ")
say_hi()
age = input("What is your age?: ")
show_age()
