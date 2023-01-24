from django.contrib import admin
from .models import Cuento, Author, Favorite

admin.site.register(Cuento)
admin.site.register(Author)
admin.site.register(Favorite)
