"""
Позволяет зайти по логину-паролю или создать нового пользователя (а так же выйти из аккаунта)
Позволяет выбрать календарь, узнать ближайшие события, события из промежутка времени а так же
Создать событие или удалить событие
После создания события можно добавить туда пользователей
Если нас добавили в событие или удалили мы получаем уведомление.

в main можно использовать ТОЛЬКО interface
"""
import unittest
from datetime import datetime, timedelta
from Event import Event
from User import User
from Calendar import Calendar

class Interface:

    def __init__(self):
        self.users = {}
        self.current_user = None
        self.logged_in = False

    def create_user(self, login, password):
        if login not in self.users:
            new_user = User(login, password)
            self.users[login] = new_user
            print(f"User '{login}' created successfully.")
        else:
            print('User with this login already exists')

    def login(self, login, password):
        if login in self.users and self.users[login].password == User.hash_password(password):
            self.current_user = self.users[login]
            self.logged_in = True
            print(f"Logged in as {login}.")
        else:
            print("Invalid login or password.")

    def logout(self):
        if self.logged_in:
            print(f"Logged out from {self.current_user.login}.")
            self.current_user = None
            self.logged_in = False
        else:
            print('No user is logged in now')

    def choose_calendar(self):
        if self.logged_in:
            print(f"Selected calendar for {self.current_user.login}.")
        else:
             print(f'Please log in')

    def view_upcoming_events(self):
        if self.logged_in:
            print('Upcoming events:')
        else:
            print(f'Please log in')

    def view_interval_events(self, start_time, end_time):
        if self.logged_in:
            print('Events in the specified interval:')
        else:
            print(f'Please log in')

    def create_event(self, name, description, start_time, is_recurring=False, recurrence_type=None):
        if self.logged_in:
            new_event = Event(name, description, self.current_user, start_time, is_recurring, recurrence_type)
            self.current_user.calendar.add_event(new_event)
            print(f'Event {new_event.name} created')
        else:
            print(f'Please log in')

    def delete_event(self, event):
        if self.logged_in:
            self.current_user.calendar.remove_event(event)
            print(f'Event {event.name} deleted ')
        else:
            print(f'Please log in')

    def add_participant(self, event, participant):
        if self.logged_in:
            event.add_participant(participant)
            print(f"User '{participant}' added to '{event.name}'")
        else:
            print(f'Please log in')

    def delete_participant(self, event, participant):
        if self.logged_in:
            event.remove_participant(participant)
            print(f"User '{participant}' removed from event '{event.name}'")
        else:
            print(f'Please log in')


class TestInterface(unittest.TestCase):
    def setUp(self):
        self.interface = Interface()
        self.user1 = User("user1", "password1")
        self.user2 = User("user2", "password2")
        self.calendar = Calendar("TestCalendar")
        self.event = Event("TestEvent", "EventDescription", self.user1, [self.user2], datetime.now())
        self.interface.users = {"user1": self.user1, "user2": self.user2}
        self.interface.current_user = self.user1
        self.interface.logged_in = True
        self.user1.calendar = self.calendar
        self.user1.calendar.add_event(self.event)

    def test_create_user(self):
        self.interface.create_user("newuser", "newpassword")
        self.assertIn("newuser", self.interface.users)

    def test_login(self):
        self.interface.login("user1", "password1")
        self.assertTrue(self.interface.logged_in)
        self.assertEqual(self.interface.current_user, self.user1)

    def test_logout(self):
        self.interface.logout()
        self.assertFalse(self.interface.logged_in)
        self.assertIsNone(self.interface.current_user)

    def test_choose_calendar(self):
        self.interface.choose_calendar()


    def test_view_upcoming_events(self):
        self.interface.view_upcoming_events()


    def test_view_interval_events(self):
        start_time = datetime.now()
        end_time = start_time + timedelta(days=7)
        self.interface.view_interval_events(start_time, end_time)


    def test_create_event(self):
        self.interface.create_event("NewEvent", "NewEventDescription", datetime.now())


    def test_delete_event(self):
        self.interface.delete_event(self.event)


    def test_add_participant(self):
        event = Event("AnotherEvent", "EventDescription", self.user1, [], datetime.now())
        self.interface.add_participant(event, "user3")


    def test_delete_participant(self):

        self.interface.delete_participant(self.event, "user2")



if __name__= "__main__":
    unittest.main()


