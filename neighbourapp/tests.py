from django.test import TestCase

# Create your tests here.
from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import Neighbour,User,Profile,Comment
import datetime as dt

class ImageTestClass(TestCase):
    '''
    images test method
    '''
    def setUp(self):

        self.user1 = User(username='dukunde')
        self.user1.save()
        
        
        self.image=Neighbour(title='leaves',description='beautiful',user=self.user1,likes="1",post="image")
        self.image.save_image()

 
    def test_instance(self):
        self.assertTrue(isinstance(self.image,Neighbour))

    def test_save_method(self):
        '''
        test image by save
        '''
        self.image.save_image()
        images=Neighbour.objects.all()
        self.assertTrue(len(images)>0) 
   

    def test_delete_method(self):
        '''
        test of delete image
        '''
       
        Neighbour.objects.all().delete()

   
    
    def test_filter_by_name(self):
        '''
        test of filter image by location
        '''
        self.image.save_image()
        img=self.image.filter_by_name(self.image.title)
        image=Neighbour.objects.filter(title=self.image.title)
        self.assertTrue(img,image)

class CommentTestClass(TestCase):

    def setUp(self):
     
        self.user1 = User(username='dukunde')
        self.user1.save()
        self.nature=Profile(2,user=self.user1,bio='Nature')
        self.nature.save_prof()

        self.james=Neighbour(2,title='James',description='beautiful',user=self.user1,likes="1",post="image")
        self.james.save_image()
      
        self.com=Comment(comment='leaves',comment_image=self.james,posted_by=self.nature,)
        self.com.save_com()

 
    def test_instance(self):

        self.assertTrue(isinstance(self.com,Comment))    
        
    def test_save_method(self):
        '''
        test image by save
        '''
        self.com.save_com()
        comm=Comment.objects.all()
        self.assertTrue(len(comm)>0) 
    def test_delete_method(self):
        '''
        test of delete image
        '''
  
        Comment.objects.all().delete()
   
class ProfileTestClass(TestCase):
    '''
    images test method
    '''
    def setUp(self):
        self.user1 = User(username='dukunde')
        self.user1.save()
        # self.image=Profile(name='leaves',description='beautiful',user=self.user1,likes="1",post="image")
        # self.image.save_image()
        self.nature=Profile(2,user=self.user1,bio='Nature')
        self.nature.save_prof()

 
    def test_instance(self):
        self.assertTrue(isinstance(self.nature,Profile))

         
    def test_save_method(self):
        '''
        test image by save
        '''
        self.nature.save_prof()
        comm=Profile.objects.all()
        self.assertTrue(len(comm)>0) 

    def test_delete_method(self):
        '''
        test of delete image
        '''
  
        Profile.objects.all().delete()