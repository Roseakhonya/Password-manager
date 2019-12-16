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
    '''
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

def create_new_credential(account, userName, password):
    '''
    A function which creates new credentials for new user
    '''
    new_credential = Credentials(account, userName, password)
    return new_credential
