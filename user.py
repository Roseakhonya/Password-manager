from password import User
from user import Credentials

def create_new_user(username, password):
    '''
    Function to create a new user
    '''
    new_user = User(username,password)
    return new_user
def save_user(user):
    '''
    Function to save a new user
    h'''
    user.save_user
def display_user():
    '''
    A function that helps display a user
    '''
def login_user(username,password):
    '''
    A function in which a user is autheticated
    '''
    check_user = Credentials.verify_user(username,password)
    return check_user

def create_new_credentials(account, userName, password):
    '''
    A function which creates new credentials for the user account
    '''
    new_credential = Credentials(account, userName, password)
    return new_credential

def save_credentials(credentials):
    '''
    Function that saves the new credentials entered
    '''
    credentials.save_credentials()

def display_accounts_details():
    '''
    A function which returns all the saved credential
    '''
    return Credentials.display_credentials()

def delete_credential(credentials):
    '''
    function that deletes a credential from credential list
    '''
    credentials.delete_credentials()

def find_credential(account):
    '''
    A function which finds a specific credential from credential list
    '''
    return Credentials.if_credential_exist(account)

def generate_Password():
    '''
    A function that automatically  generate  passwords for users
    '''
    auto_password = Credentials.generate_Password()
    return auto_password

def main():
    print("Hi welcome to your password manager...\n tell us what you wish to do:\n CA ---  create new account  \n AH --- Account exists  \n")
    short_code=input("").lower().strip()

    if short_code == "ca":
        print("sign in")
        print('*' * 50)
        userName = input("userName: ")

        while True:
            print("ep - enter your password :n\ cp - create own password")
            choose_password= input().lower().strip

            if choose_password == "cp":
                password = input("Enter password\ n")
                break
            elif choose_password == "ep":
                password = generate_Password()
                break
            else:
                print("wrong password")

        save_user(create_new_user(userName,password))
        print(f"Hi {userName}, you have succesfully created your account! Your password is: {password}")

    elif short_code == "ah":
        print("Enter your User name and your Password to log in:")

        username = input("UserName: ")
        password = input("password: ")
        login = login_user(username,password)

        if login_user == login:
            print(f"Hi there, welcome to password manager application")  
            print('\n')
        
        while True:
            print("Kindly choose any of the short codes provided:\n cn - add new credential \n ds - Display all credentials \n rc - retrieve credental \n dl- Delete credential \n ex- Exit\n")
            short_code = input().lower().strip()

            if short_code == "cn":
                print("Create Credential")
                print("Account name ....")
                account = input().lower()
                print("Your username")
                userName = input()

                while True:
                    print(" ep - Key own pasword :\n  gp- To generate random password")
                    choose_password = input().lower().strip()

                    if choose_password == 'ep':
                        password = input("Enter your password\n")
                        break

                    elif choose_password == 'gp':
                        password = generate_Password()
                        break
                    else:
                        print("invalid! Try again")

                save_credentials(create_new_credential(account,userName,password))
                    print(f"Account Credential for: {account} - UserName: {userName} - Password:{password} successful!")
        
        elif short_code == "ds":
            if display_accounts_details():
                print("Your accounts are listed below: ")
                print('*' * 30)
                print('_' * 30)

                for account in display_accounts_details():
                    print(f" account:{account.account} \n Username:{userName}\n Password:{password}")
                    print('_'* 30)
                print('*' * 30)
                 else:
                print("No credentials found")

        elif short_code == "rc":
            print("Enter account")
            search_name = input().lower()

        if find_credential(search_name):
                search_credential = find_credential(search_name)
                print(f"Account Name : {search_credential.account}")
                print(f"User Name: {search_credential.userName} Password :{search_credential.password}")
            else:
                print("No match found")

        elif short_code == "dl":
            print("Type credential you wish to delete")
            search_name = input().lower()
            if find_credential(search_name):
                search_credential = find_credential(search_name)
                print("_"*50)
                search_credential.delete_credentials()
                print('\n')
                print(f"Your {search_credential.account} deleted.")
                print('\n')
            else:
                print(f"{search_credenttial.account} not found.")

    elif short_code == 'gp':
        password = generate_Password()
            print(f" {password} generated")
        elif short_code == 'ex':
            print("Thanks for your time")
            break
        else:
            print("Validate your details")
    else:
        print("Key in the correct details")


if __name__ == '__main__':
    password()


            


                
                
                    






