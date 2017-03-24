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
    
    def test_new_task_view(self):
        # arrange
        self.client = Client()
        task = Task(description = "Tarea_1")
        # act
        response = self.client.post("/tasks", {task.to_doc()})
        # assert
        self.assertEquals(200, response.status_code)
