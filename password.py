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



     