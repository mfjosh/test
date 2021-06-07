def say_hi():
    if name == '':
        print('you did not enter a name!')
    else:
        print("Hello",name)

name = input("Please Enter Name: ")
say_hi()
