from django.contrib import admin
from . models import MailMessage, Subscribers

# Register your models here.
admin.site.register(MailMessage)
admin.site.register(Subscribers)
