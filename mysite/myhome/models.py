from django.db import models

# Create your models here.


class intent(models.Model):
	intent_name=models.CharField(max_length=250)



class answers(models.Model):
	intent_id=models.ForeignKey(intent, on_delete=models.CASCADE)
	answer=models.CharField(max_length=2000)
	score=models.CharField(max_length=50,default="GOOD")

class questions(models.Model):
	intent_id=models.ForeignKey(intent, on_delete=models.CASCADE)
	questions=models.CharField(max_length=1000)







