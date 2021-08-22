from django.db import models
class NRI(models.Model):
    id=models.AutoField(primary_key=True)
    details=models.CharField(max_length=200)
    des=models.URLField()
    publish=models.CharField(max_length=20)
    image=models.URLField()
    posttime=models.IntegerField()

# Create your models here.
