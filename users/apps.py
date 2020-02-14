from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'
    #Overriding: import signals craeted for Users/Profile functions
    def ready(self):
        import users.signals

