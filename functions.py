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
def query_yes_no(question):
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
    user_info()
    query_yes_no("Is the information above correct?: ")
def confirmation(user_name, user_age, user_location):
    print('Your name shows as:')
    print(user_name)
    print('Age:', user_age)
    print('Location:', user_location)
