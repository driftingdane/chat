from django.db import models
from django.urls import reverse


class ChatRoom(models.Model):
	room = models.CharField(null=False, max_length=50)
	description = models.CharField(null=True, max_length=200)
	created = models.DateField(auto_now=True)
	
	class Meta:
		verbose_name_plural = 'rooms'
	
	def get_absolute_url(self):
		return reverse('chat:room', args=[self.room])
	
	def __str__(self):
		return self.room
