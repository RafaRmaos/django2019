from django.contrib import admin

# Register your models here.
from .Area import Area
admin.site.register(Area)

from .Professor import Professor
admin.site.register(Professor)

from .Aluno import Aluno
admin.site.register(Aluno)