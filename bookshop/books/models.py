from django.contrib.auth.models import User
from django.db import models
# from users.models import CustomUser

class Category(models.Model):
    title = models.CharField(max_length=100)
    def __str__(self):
        return self.title

class Book(models.Model):
    img = models.ImageField('image')
    count = models.IntegerField(default=0)
    title = models.CharField(max_length=70)
    author = models.CharField(max_length=40)
    moreInfo = models.TextField()
    addTime = models.DateTimeField(auto_now_add=True)
    language = models.CharField(max_length=30)
    alphabet = models.CharField(max_length=20)
    page = models.IntegerField()
    coating = models.CharField(max_length=30)
    company = models.CharField(max_length=40)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # category = models.CharField(max_length=40, choices=(('Bezakli bolalar adabiyoti', 'Bezakli bolalar adabiyoti'),
    #                                                     ('Bolalar adabiyoti', 'Bolalar adabiyoti'),
    #                                                     ('Badiy adabiyotlar', 'Badiy adabiyotlar'),
    #                                                     ('Biznes', "Biznes"),
    #                                                     ('Shaxsiy rivojlanish', 'Shaxsiy rivojlanish'),
    #                                                     ('Psixologiya', 'Psixologiya'),
    #                                                     ("Ma'naviy va diniy", "Ma'naviy va diniy"),
    #                                                     ('Abituriyentlar uchun', 'Abituriyentlar uchun'),
    #                                                     ))
    searchCount = models.IntegerField(default=0, blank=True, null=True)
    sellCount = models.IntegerField(default=0, blank=True, null=True)
    rentPrice = models.IntegerField()
    sellingPrice = models.IntegerField()
    def __str__(self):
        return self.title

class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, blank=True, null=True)
    # user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.user}({self.date})"


class SocialMedia(models.Model):
    phone = models.CharField(max_length=20)
    telegram = models.CharField(max_length=40)
    instagram = models.CharField(max_length=40)
    def __str__(self):
        return self.phone

class TermsOfTrade(models.Model):
    title = models.CharField(max_length=100)
    mainText = models.TextField()
    def __str__(self):
        return self.title

class Adds(models.Model):
    img = models.ImageField('image')

class Bookmark(models.Model):
    # user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
