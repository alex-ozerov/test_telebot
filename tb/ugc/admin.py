from django.contrib import admin
from .forms import ProfileForm
from .models import Profile
# Register your models here.


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'user_id', 'username', 'firstname', 'lastname')
    form = ProfileForm


