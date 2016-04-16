from django.contrib import admin

# Register your models here.
from .models import *


admin.site.register(Question)
admin.site.register(Phpquestion)
admin.site.register(Userprof)
admin.site.register(Pythonquestion)
