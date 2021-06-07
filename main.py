#version 0.1.1b
#variables
def introduction():
    print("Welcome to the beta program! Let's get started.")
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
introduction()
name = input("Please Enter Name: ")
say_hi()
age = input("What is your age?: ")
show_age()
