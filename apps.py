from django.apps import AppConfig  # Imports the AppConfig class, which is used to configure Django apps.

# Configuration class for the Books app
class BooksConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'  # Specifies the default field type for auto-generated primary keys.
    name = 'Books'  # Defines the name of the app as 'Books'. This is the label used to reference the app throughout your Django project.

