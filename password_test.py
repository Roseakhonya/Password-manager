import unittest
from password import User
from password import Credentials

class TestUser(unittest.TestCase):
    '''
    A test class which defines test cases for the user class behaviours.
    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        Method executed before each user test cases.
        '''
        self.new_user = User()
    
    def test_init(self):
        '''
        Test case to test object initialization
        '''
        self.assertEqual(self.new_user.username)
        self.assertEqual(self.new_user.password)


    def test_save_user(self):
        '''
        test case to test if a new user object has been saved into the User list
        '''
        
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)

class TestCredentials(unittest.TestCase):
    '''
    Test class defining test cases for the credentials.
    ''' 