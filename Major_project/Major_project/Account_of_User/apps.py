from django.apps import AppConfig


class AccountOfUserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Account_of_User'

    def ready(self):
        import Account_of_User.signal
