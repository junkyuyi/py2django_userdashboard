from __future__ import unicode_literals

from django.db import models
from ..loginandregistration.models import User

# Create your models here.
class MessageManager(models.Manager):
	def addMessage(self, user_to, user_from, message):
		if len(message) > 0:
			Message.objects.create(	user_to=User.userManager.get(id=user_to),
									user_from=User.userManager.get(id=user_from),
									message=message)

	def getAll (self, request, user_id):
		user = User.userManager.getOneUser(user_id)
		allMessages = Message.objects.filter(user_to=user_id).prefetch_related('comment_set').order_by('-created_at')
		context = {	'user':user,
					'allMessages':allMessages}
		return context


class Message(models.Model):
	user_to = models.ForeignKey(User, related_name="user_to")
	user_from = models.ForeignKey(User, related_name="user_from")
	message = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = models.Manager()
	messageManager = MessageManager()

class CommentManager(models.Manager):
	def addComment(self, message_id, user_id, comment):
		if len(comment) > 0:
			Comment.objects.create(	message=Message.objects.get(id=message_id),
									user=User.userManager.get(id=user_id),
									comment=comment)

class Comment(models.Model):
	user = models.ForeignKey(User)
	message = models.ForeignKey(Message)
	comment = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = models.Manager()
	commentManager = CommentManager()