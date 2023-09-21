
from django.db import models
from embed_video.fields import EmbedVideoField

class Video(models.Model):
    title = models.CharField(max_length = 100)
    added = models.DateTimeField(auto_now_add = True)
    modelVideo = EmbedVideoField()
    #url = EmbedVideoField()
    def _str_(self):
       return str(self.title) 
   
    class Meta:
        ordering = ['-added']

