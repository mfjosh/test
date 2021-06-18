def introduction():
    print("Welcome to the beta program! Let's get started.  ")
def user_info():
    global user_name
    user_name = input("Please Enter Name: ")
    if user_name == '':
        print('you did not enter a name!')
    else:
        print(' ')
    global user_age
    user_age = input("What is your age?: ")
    if user_age =='':
        print('You must enter an age!')
    else:
        print(' ')
    global user_location
    user_location = input("Where do you live?: ")
    if user_location =='':
        print('You must enter a location!')
    else:
        print(' ')
    confirmation(user_name, user_age, user_location)
def user_info_query(question):
    yes = {'yes','y', 'ye', ''}
    no = {'no','n'}
    choice = input(question).lower()
    if choice in yes:
        print('Information Saved.')
    elif choice in no:
        main_seq()
    else:
        sys.stdout.write("Please respond with 'yes' or 'no'")
def main_seq():
    introduction()
    main_menu()
def confirmation(user_name, user_age, user_location):
    print('Your user information is shows as:')
    print('Name:', user_name)
    print('Age:', user_age)
    print('Location:', user_location)
def main_menu():       ## Your menu design here
    print (30 * "-" , "MENU" , 30 * "-")
    print ("1. Enter User Information")
    print ("2. Display User Information")
    print ("3. Delete User Information")
    print ("4. This is empty")
    print ("5. Exit")
    print (67 * "-")
loop=True
while loop:          ## While loop which will keep going until loop = False
    main_menu()    ## Displays menu
    choice = input("Enter your choice [1-5]: ")
    choice = int(choice)
    if choice==1:
        user_info()
        user_info_query("Is this information correct? (y/n): ")
        print("returning to previous menu")
    elif choice==2:
        confirmation(user_name, user_age, user_location)
        input("Press Enter to return to previous menu")
        ## You can add your code or functions here
    elif choice==3:
        del user_name
        user_name = ""
        del user_age
        user_age = ""
        del user_location
        user_location = ""
        confirmation(user_name, user_age, user_location)
        input("Press Enter to return to previous menu")
        ## You can add your code or functions here
    elif choice==4:
        print ("Menu 4 has been selected")
        input("Press Enter to return to previous menu")
        ## You can add your code or functions here
    elif choice==5:
        loop=False # This will make the while loop to end as not value of loop is set to False
        quit()
    else:
        # Any integer inputs other than values 1-5 we print an error message
        input("Wrong option selection. Enter any key to try again..")
