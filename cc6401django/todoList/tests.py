from django.test import TestCase, Client
from models import Task

# Create your tests here.

class Tests(TestCase):
    
    def test_create_new_task(self):
        # arrange
        task = Task(description = "tarea_1")
        # act
        task.save()
        saved_task = Task.objects.all()[0]
        # assert
        self.assertEquals(task.description, saved_task.description)
    
