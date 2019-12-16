import random
import string

class User:
    '''
    This creates user class which generates new instances of a user
    '''
    user_list = []

    def _init_(self, username, password):
      '''
      function that define the properties for user objects
      '''
      self.username = username
      self.password = password

    def save_user(self):
        '''
        A function that saves a  new user instance into the user list
        '''
        User.user_list.append(self)

    @classmethod
    def display_user(cls):
        return cls.user_list
        '''
        A method that displays username
        '''
    def delete_user(self):
        User.user_list.remove(self)
        '''
        A method that deletes a saved username
        '''

    class Credentials():
        '''
        Create a credentials class to create new objects of credentials
        '''
        credentials_list = []
    def __init__(self, account, userName, password):
        '''
        A function to define the user credentials"
        '''
        self.account = account
        self.username = userName
        self.password = password

    def save_details(self):
        '''
        A function that saves a new credential property to the credentials list
        '''
        Credentials.credentials_list.append(self)

    def delete_credentials(self):
        '''
        A function which deletes a credential from the existing one
        '''
    
    @classmethod
    def find_credential(cls, account):
        '''
        A function that tries to find out a certain credential from the user account
        '''
        for credential in cls.credentials_list:
            if credential.account == account:
                return credential
    @classmethod
    def if_credential_exist(cls,account):
        '''
        a function to check if the credential entered exists on the list and it returns true or false
        '''
        
    
    




     