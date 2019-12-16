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
    






