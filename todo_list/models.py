from django.db import models

class todo(models.Model):
	complete=models.BooleanField(default=False)
	todotext=models.CharField(max_length=50)

	def __str__(self):
		return self.todotext