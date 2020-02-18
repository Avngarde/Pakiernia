from django.contrib import admin
from users.models import ExercisesOwnedByUser, Training


admin.site.register(ExercisesOwnedByUser)
admin.site.register(Training)
