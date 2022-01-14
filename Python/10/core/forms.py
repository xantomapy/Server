from django.forms import ModelForm

from core.models import TaskList, Task


class TaskListForm(ModelForm):

    class Meta:
        model = TaskList
        fields = ['name']


class TaskForm(ModelForm):

    class Meta:
        model = Task
        fields = ['name', 'is_done']
