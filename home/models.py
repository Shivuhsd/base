from django.db import models
import uuid
from django.contrib.auth.models import User
# Create your models here.

class UserQuery(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    query = models.TextField()
    answer = models.TextField()
    model = models.CharField(max_length=100, null=False)
    time_stamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.query
    
    
class UserComment(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    comment = models.TextField()
    time_stamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name