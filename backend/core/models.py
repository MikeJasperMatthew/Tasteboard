from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Style(models.Model):
    theme = models.CharField(max_length=20)

class Board(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=360)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    style = models.ForeignKey(Style, on_delete=models.CASCADE, default='')
    #foreign keys here

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
    board = models.ForeignKey(Board, on_delete=models.CASCADE, default='') 

class Authentication(models.Model):
    username = models.CharField(max_length=12)
    password = models.CharField(max_length=12) #placeholder
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='') 
    
class Reviews(models.Model):

    review = models.CharField(max_length=7500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    media = models.ForeignKey(Media, on_delete=models.CASCADE, default='')

class BoardComments(models.Model):
    board_comment = models.CharField(max_length=2500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='') 
    board = models.ForeignKey(Board, on_delete=models.CASCADE, default='') 

class BoardMediaComments(models.Model):
    board_media_comment = models.CharField(max_length=2500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    media = models.ForeignKey(Media, on_delete=models.CASCADE, default='')


class Profie(models.Model):
    description = models.CharField(max_length=360)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #pfp = models.ImageField(blank=True, null=True) #CHANGE LATER!!!

# class Friends(models.Model):
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)