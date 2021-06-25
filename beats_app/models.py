from django.db import models

from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
'''

class Beat(models.Model):
	title = models.CharField(max_length = 32)
	author = models.CharField(max_length = 32)
	published_on = models.TimeField()
	is_liked = models.BooleanField(default = False)
	user = models.ForeignKey(User, on_delete = models.CASCADE)

	def __str__(self):
		return self.title


	def like(self):
		self.is_liked = True

class Label(models.Model):
	name = models.CharField(max_length = 32)
	owner = models.CharField(max_length = 64)
	beat = models.ForeignKey(Beat, on_delete = models.CASCADE)

	def __str__(self):
		return self.name

'''