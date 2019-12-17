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
    def setUp(self):
        '''
        Method that runs before each credentials test case.
        '''
        self.new_credential = Credentials
    
    def tearDown(self):
        '''
        method that clears everything once the test case has been executed.
        '''
        Credentials.credentials_list = []

    def test_init(self):
        '''
        Test case to check if a new credential is well  initialized
        '''
        self.assertEqual(self.new_credential.account)
        self.assertEqual(self.new_credential.userName)
        self.assertEqual(self.new_credential.password)

    def save_credential_test(self):
        '''
        test case to test if a given credential is saved onto the credentials list.
        '''
        self.new_credential.save_details()
        self.assertEqual(len(Credentials.credentials_list),1)

    def test_save_many_accounts(self):
        '''
        test to check if we can save more than one credential on our credentials list
        '''
        self.new_credential.save_details()
        test_credential = Credentials() 
        test_credential.save_details()
        self.assertEqual(len(Credentials.credentials_list),2)

    def test_delete_credential(self):
        '''
        test method to test if we can erase a credential from the list
        '''
        self.new_credential.save_details()
        test_credential = Credentials() 
        test_credential.save_details()

        self.new_credential.delete_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)

    def test_find_credential(self):
        '''
        test to try and retrieve a given credential"
        '''
        self.new_credential.save_details()
        test_credential = Credentials() 
        test_credential.save_details()

        get_credential = Credentials.find_credential()

        self.assertEqual(get_credential.account,test_credential.account)

     def test_credential_exist(self):
        '''
        test to check existence of a specific credential.
        '''
        self.new_credential.save_details()
        get_credential = Credentials() 
        get_credential.save_details()
        credential_is_found = Credentials.if_credential_exist()
        self.assertTrue(credential_is_found)

    def test_display_all_saved_credentials(self):

        '''
        method which lists all available credentials
        '''

        self.assertEqual(Credentials.display_credentials(),Credentials.credentials_list)



if __name__ == "__main__":
    unittest.main() 


