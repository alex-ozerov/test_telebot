from django.contrib import admin
from .forms import ProfileForm
from .models import Profile, Message
# Register your models here.


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'external_id', 'name', 'firstname')
    form = ProfileForm


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'profile', 'text', 'created_at')


