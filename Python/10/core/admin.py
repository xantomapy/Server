from django.contrib import admin

from core.models import TaskList, Task


admin.site.register(TaskList)
admin.site.register(Task)
