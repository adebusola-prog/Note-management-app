from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.urls import reverse

class ActiveManager(models.Manager):

   def get_queryset(self):
      return super().get_queryset().filter(is_delete=False)

class InActiveManager(models.Manager):

   def get_queryset(self):
      return super().get_queryset().filter(is_delete=True)

class UserProfile(models.Model):
   username=models.OneToOneField(User, on_delete= models.CASCADE)
   first_name= models.CharField(max_length=50)
   last_name= models.CharField(max_length=50)
   email= models.EmailField(max_length=50)
   profile_pics= models.ImageField(upload_to= "images", blank=True, null=True)

   def __str__(self):
      return self.first_name + " " + self.last_name

   def get_absolute_url(self):
      return reverse('profile', args=[str(self.id)])


   @property
   def imageURL(self):
      try:
         url= self.profile_pics.url
      except:
         url= ''
      return url

class Category(models.Model):
   name=models.CharField(max_length=20)

   def __str__(self):
      return self.name


class Note(models.Model):
   category= models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
   user_profile=models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True, blank=True)
   title= models.CharField(max_length=50)
   text=models.TextField()
   image = models.ImageField(upload_to= "images", blank=True, null=True)
   pdf= models.FileField(help_text= "You can upload your files here" )
   created_time=models.DateTimeField(auto_now_add=True)
   updated_time=models.DateTimeField(auto_now_add=True)
   is_pin=models.BooleanField(default=False)
   is_delete= models.BooleanField(default=False)

   objects = models.Manager()
   active_objects= ActiveManager()
   inactive_objects= InActiveManager()

   def __str__(self):
      return self.title

   @property
   def image_URL(self):
      try:
         url= self.image.url
      except:
         url= ''
      return url
   
   class Meta:
      ordering=['-is_pin', '-created_time']


