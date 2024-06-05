"""
Пользователь - имеет логин и пароль, а так же календарь.
у пользователя есть итендифекатор начинающийся с @
"""
from datetime import datetime , timedelta
from Calendar import Calendar
import unittest
class User:
    def __init__(self,login,password):
        self.login = login
        self.password = self.hash_password(password)
        self.calendar = Calendar(self)
        self.identifier = '@' + str(id(self))

    def hash_password(self, password):

        return hash(password)

class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User('test_user','password123')
    def test_user_functions(self):
        self.assertEqual(self.user.login,'test_user')
        self.assertNotEqual(self.user.password,'password123')
        self.assertIsInstance(self.user.calendar,Calendar)
        self.assertTrue(self.user.identifier.startswith('@'))

    def test_password_hashing(self):
        hashed_password = self.user.hash_password("password123")
        self.assertNotEqual(hashed_password,'password123')



if __name__= "__main__":
    unittest.main()