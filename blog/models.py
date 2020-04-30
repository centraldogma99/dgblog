from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib import messages
from mptt.models import TreeForeignKey, MPTTModel



class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()
        
    def unpublish(self):
        self.published_date = None
        self.save()
    
    def __str__(self):
        return self.title
    
    def approved_comments(self):
        return self.comments.filter(approved=True)
    
    
class Comment(MPTTModel):
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    approved = models.BooleanField(default = False)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    parent = TreeForeignKey('self',on_delete=models.CASCADE,related_name='children',null=True,blank=True)
    
    def __str__(self):
        return self.text
    
    def approve(self):
        self.approved = True
        
    class MPTTMeta:
        order_insertion_by = ["created_date"]


        