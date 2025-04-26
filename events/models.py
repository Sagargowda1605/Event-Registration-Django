from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


#Since i am using the abastrctuser here the username,email,password will already defined on the User model
#  you dont have define it if you defone that here you are over riding it 
class User(AbstractUser):
    name=models.CharField(max_length=100,null=True)
    email = models.EmailField(unique=True)
    Bio=models.TextField(blank=True,null=True)
    participant=models.BooleanField(default=True,null=True)
    #avatar=


    # this is used because isntead of the username field while login we are making the use the email
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]

class Event(models.Model):
    name=models.CharField(max_length=100)
    Event_date=models.DateField()
    descritpion=models.TextField(null=True,blank=True)
    participants=models.ManyToManyField(User,blank=True,related_name="events")
    created_on=models.DateField(auto_now_add=True)
    updated_on=models.DateField(auto_now=True)


    def __str__(self):
        return self.name
    
class Submission(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    title=models.CharField(max_length=100)
    details=models.TextField(blank=True,null=True)
    event=models.ForeignKey(Event,unique=True,on_delete=models.SET_NULL,null=True)
    submited_on=models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.event) + '__' + str(self.user)


 