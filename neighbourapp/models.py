from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.core.validators import MaxValueValidator
# Create your models here.
class Neighbour(models.Model):
    # title=models.CharField(max_length=30)
    # description=models.TextField(max_length=300)
    # image=models.ImageField(upload_to='images_galleries/')
    # user=models.ForeignKey(User,on_delete=models.CASCADE, blank=True,related_name="images")
    # # comments=models.TextField(blank=True)
    # post = HTMLField(null=True)
    # # comments=models.ForeignKey(Comment)
    # likes=models.IntegerField(default=0)
    # link=models.TextField(max_length=130)
    # pub_date=models.DateTimeField(auto_now_add=True,null=True)
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
    def find_by_id(cls,id):
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
    neighborhood=models.ForeignKey(Neighbour,null=True)
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

class Comment(models.Model):
    posted_by=models.ForeignKey(Profile, on_delete=models.CASCADE,null=True)
    # comment_image=models.ForeignKey(Project,on_delete=models.CASCADE,null=True)
    comment=models.CharField(max_length=20,null=True)

    def save_com(self):
        self.save()

    def get_comment(self,id):
        comments=Comment.objects.filter(image_id=id)
        return comments
    def __str__(self):
        return self.posted_by

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
    location=models.ForeignKey(Neighbour, on_delete=models.CASCADE,null=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    # comment_image=models.ForeignKey(Project,on_delete=models.CASCADE,null=True)
    bussiness_email=models.EmailField(max_length=200,null=True)
    post_date=models.DateTimeField(auto_now_add=True)
    bussiness=models.CharField(max_length=200)

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