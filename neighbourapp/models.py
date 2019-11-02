from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.core.validators import MaxValueValidator
# Create your models here.
class Neighbour(models.Model):
    name=models.CharField(max_length=30)
    location=models.TextField(max_length=300)
    image=models.ImageField(upload_to='images_galleries/')
    # user=models.ForeignKey(User,on_delete=models.CASCADE, blank=True,related_name="images")
    count=models.IntegerField(default=0,blank=True)

    def create_neighbourhood(self):
        self.save()
    def delete_neighbourhood(self):
        self.delete()
   
    @classmethod
    def filter_by_busines_id(cls,id):
        hood=cls.objects.filter(id=id)
        return hood 

    def __str__(self):
        return self.name

class Profile(models.Model):
    class Meta:
        db_table='profile'
    # profile_pic=models.ImageField(upload_to='picture/',null=True,blank=True)
    # user=models.OneToOneField(User, on_delete=models.CASCADE,blank=True,related_name="profile")
    # bio=models.TextField(max_length=200,null=True,default="bio")
    # contact=models.TextField(max_length=200,null=True)

    profile_pic=models.ImageField(upload_to='picture/',null=True,blank=True)
    user=models.OneToOneField(User, on_delete=models.CASCADE,blank=True,related_name="profile")
    name=models.CharField(max_length=200,null=True,default="bio")
    email=models.EmailField(max_length=200,null=True)

    location=models.CharField(max_length=100,null=True)
    neighborhood=models.ForeignKey(Neighbour, on_delete=models.CASCADE,null=True)
    def save_prof(self):
        self.save()

    def delete_prof(self):
        self.delete()

    @classmethod
    def get_by_id(cls,id):
        profile=cls.objects.get(user=id)
        return profile

    @classmethod
    def find_by_id(cls,id):
        profile=cls.objects.filter(user=id).first()
        return profile

    def __str__(self):
        return self.user.username


class NewsLetterRecients(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()

class Post(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField(max_length=100)
    location=models.ForeignKey(Neighbour,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    date_posted=models.DateTimeField(auto_now_add=True)
    def save_post(Self):
        self.save()
    @classmethod
    def get_location_contacts(cls,location):
        contacts=Post.objects.filter(location__pk=location)
        return contacts
    def __str__(self):
        return f'{self.title},{self.post_hood.neighborhood_name}'
 

class Business(models.Model):
    owner=models.CharField(max_length=40)
    bussiness=models.CharField(max_length=200)
    location=models.ForeignKey(Neighbour, on_delete=models.CASCADE,null=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    # comment_image=models.ForeignKey(Project,on_delete=models.CASCADE,null=True)
    bussiness_email=models.EmailField(max_length=200,null=True)
    post_date=models.DateTimeField(auto_now_add=True)
    

    def create_bussiness(self):
        self.save()
    def delete_bussiness(self):
        self.save()

    @classmethod
    def search_by_business(cls,search_term):
        search_term=cls.objects.filter(business__icontains=search_term)
        return search_term
    def __str__(self):
        return self.owner

class Rates(models.Model):
    design=models.PositiveIntegerField(default=0,validators=[MaxValueValidator(10)])
    usability=models.PositiveIntegerField(default=0,validators=[MaxValueValidator(10)])
    content=models.PositiveIntegerField(default=0,validators=[MaxValueValidator(10)])
    user =models.ForeignKey(User,on_delete=models.CASCADE)
    project=models.IntegerField(default=0)