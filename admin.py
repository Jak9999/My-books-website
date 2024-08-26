from django.contrib import admin  # Imports the admin module, which allows you to customize and register models in the admin interface.
from .models import Books  # Imports the Books model from the current app's models.py file.

# Customizing the admin interface for the Discounts model
class DiscountsAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount')  # Specifies which fields of the Discounts model will be displayed in the admin list view.

# Customizing the admin interface for the Books model
class BooksAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')  # Specifies which fields of the Books model will be displayed in the admin list view.

# Registering the Books model with its custom admin class
admin.site.register(Books, BooksAdmin)  # Registers the Books model with the Django admin site using the BooksAdmin configuration.



