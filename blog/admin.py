from django.contrib import admin
from beablogger.blog.models import Post, BlogComment

admin.site.register((Post, BlogComment))
