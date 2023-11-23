from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Organisation(models.Model):
    name = models.CharField(max_length=75)
    code = models.CharField(max_length=75)
    org_type = models.CharField(max_length=75)

class Department(models.model):
    name = models.CharField(max_length=75)
    code = models.CharField(max_length=75)
    organisation = models.ForeignKey(Organisation,on_delete=models.CASCADE)

class Auditor(models.model):
    organisation = models.ForeignKey(Organisation,on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='auditor')

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
    
class Claimer(models.model):
    organisation = models.ForeignKey(Organisation,on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='auditor')
    department = models.ForeignKey(Department,on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.TextField(max_length=500, blank=True)
    phone = models.IntegerField
    organisation = models.ForeignKey(Organisation,on_delete=models.CASCADE, null=True)



