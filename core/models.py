from django.db import models

# Create your models here.

class Board(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=360)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #foreign keys here

class Style(models.Model):
    theme = models.CharField(max_length=20)

class People(models.Model):
    username = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Authentication(models.Model):
    username = models.CharField(max_length=12)
    password = models.CharField(max_length=12) #placeholder
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class Reviews(models.Model):
    review = models.CharField(max_length=7500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class BoardComments(models.Model):
    board_comment = models.CharField(max_length=2500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class BoardMediaComments(models.Model):
    board_media_comment = models.CharField(max_length=2500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Media(models.Model):
    media_type = (
        ('GAME', 'Game'),
        ('ANIME', 'Anime'),
        ('ALBUM', 'Album'),
        ('TV', 'TV Show'),
        ('MOVIE', 'Movie'),
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Profie(models.Model):
    description = models.CharField(max_length=360)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #pfp = models.ImageField(blank=True, null=True) #CHANGE LATER!!!

class Friends(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)