from django.db import models
import string
import random



def genUniqueCode(length:int=6):

	while True:
		choice = ''.join(random.choices(string.ascii_uppercase,k=length))
		if Room.objects.filter(code=choice).count() == 0:
			break;

	return choice


# Create your models here.
class Room(models.Model):
	code = models.CharField(max_length=10,default="",unique=True)
	host = models.CharField(max_length=50,unique=True)
	guest_can_pause = models.BooleanField(null=False,default=False)
	votes_to_skip = models.IntegerField(null=False,default=1)
	created_at = models.DateTimeField(auto_now_add=True)

	# def isHostThis(self,host:str): return self.host == host
