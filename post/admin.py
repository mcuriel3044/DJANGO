from django.contrib import admin
#import the Postmodel
from .models import Post

# Register your models here.
admin.site.register(Post)