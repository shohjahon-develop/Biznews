from django.db import models
from django.utils import timezone
from django.urls import reverse
# Create your models here.

# class News(models.Model):
#     class Status(models.TextChoices):
#         Draft = "DF", "Draft"
#         Published = "PB", "Published"
#     name=models.CharField(max_length=40)
#     sana=models.DateField()
#     bio=models.TextField()
#     # created_time = models.DateTimeField(auto_now_add=True)
#     # updated_time = models.DateTimeField(auto_now=True)
#     status = models.CharField(max_length=2,
#                               choices=Status.choices,
#                               default=Status.Draft)
#     img=models.ImageField(upload_to='index/img')
#     # published_time = models.DateTimeField(default=timezone.now)
#
#
#     # class Meta:
#     #     ordering = ["-updated_time"]
#
#
#     def __str__(self):
#         return self.name
class News(models.Model):
    name = models.CharField(max_length=300)
    sana = models.DateField(auto_now=True)
    img = models.ImageField(upload_to='index/img')
    bio = models.TextField()


    def __str__(self):
        return self.name

class Gun(models.Model):
    Draft = "DF", "Draft"
    Published = "PB", "Published"
    name=models.CharField(max_length=40)
    sana=models.DateField()
    bio=models.TextField()
    img=models.ImageField(upload_to='index/img')

    def __str__(self):
        return self.name


class Dodge(models.Model):
    Draft = "DF", "Draft"
    Published = "PB", "Published"
    name=models.CharField(max_length=40)
    sana=models.DateField()
    bio=models.TextField()
    img=models.ImageField(upload_to='index/img')

    def __str__(self):
        return self.name


class Tank(models.Model):
    Draft = "DF", "Draft"
    Published = "PB", "Published"
    name=models.CharField(max_length=40)
    sana=models.DateField()
    bio=models.TextField()
    img=models.ImageField(upload_to='index/img')

    def __str__(self):
        return self.name


class Awm(models.Model):
    Draft = "DF", "Draft"
    Published = "PB", "Published"
    name=models.CharField(max_length=300)
    bio=models.TextField()
    img =models.ImageField(upload_to='index/img')

    def __str__(self):
        return self.name


class Train(models.Model):
    Draft = "DF", "Draft"
    Published = "PB", "Published"
    name = models.CharField(max_length=100)
    date = models.DateField()
    bio= models.TextField()
    img=models.ImageField(upload_to='index/img')

    def __str__(self):
        return self.name


class Products(models.Model):
    Draft = "DF", "Draft"
    Published = "PB", "Published"
    name = models.CharField(max_length=40)
    price = models.IntegerField()
    date = models.DateField(auto_now=True)
    bio = models.TextField()
    img = models.ImageField(upload_to='single/img')


    def __dir__(self):
        return self.name

class Bmw(models.Model):
    Draft = "DF", "Draft"
    Published = "PB", "Published"
    name = models.CharField(max_length=50)
    price= models.IntegerField()
    bio = models.TextField()
    img = models.ImageField(upload_to='single/img')

    def __dir__(self):
        return self.name

class Add(models.Model):
    Draft = "DF", "Draft"
    Published = "PB", "Published"
    name = models.CharField(max_length=40)
    img = models.ImageField(upload_to='single/img')

    def __dir__(self):
        return self.name

class Game(models.Model):
    Draft = "DF", "Draft"
    Published = "PB", "Published"
    name = models.CharField(max_length=40)
    bio = models.TextField()
    img = models.ImageField(upload_to='single/img')
    date = models.DateField(auto_now=True)

    def __dir__(self):
        return self.name


class Snew(models.Model):
    class Status(models.TextChoices):
        Draft = "DF","Draft"
        Published = "PB","Published"
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    body = models.TextField()
    image = models.ImageField(upload_to="snew/images")
    published_time = models.DateTimeField(default=timezone.now)
    created_time= models.DateTimeField(auto_now_add=True)
    updated_time=models.DateTimeField(auto_now=True)
    status=models.CharField(max_length=2,
                                choices=Status.choices,
                                default=Status.Draft)

    class Meta:
        ordering = ["-published_time"]

    def __str__(self):
        return self.title



class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=250)
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __dir__(self):
        return self.name


class Newslet(models.Model):
    email = models.EmailField(max_length=250)

    def __str__(self):
        return self.email


class Comment(models.Model):
    name = models.CharField(max_length=200)
    message = models.TextField()
    email = models.EmailField(max_length=300)
    web = models.URLField()

    def __str__(self):
        return self.name

class Mahsulot(models.Model):

    class Status(models.TextChoices):
        Yaroqli = "YR","Yaroqli"
        Yaroqsiz = "YS","Yaroqsiz"
    name = models.CharField(max_length=300)
    price = models.IntegerField()
    bio = models.TextField()
    slug = models.SlugField(max_length=300)
    date = models.DateTimeField(default=timezone.now)
    img = models.ImageField(upload_to='Mahsulot/img')
    status = models.CharField(max_length=2,
                              choices=Status.choices,
                              default=Status.Yaroqli)
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("mahsulotsDetail", args=[self.slug])






class Bot(models.Model):
    class Status(models.TextChoices):
        Yaroqli = "YR","Yaroqli"
        Yaroqsiz = "YS","Yaroqsiz"
    name = models.CharField(max_length=300)
    bio = models.TextField()
    img = models.ImageField(upload_to='index/img')
    date = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(max_length=300)
    status = models.CharField(max_length=2,
                              choices=Status.choices,
                              default=Status.Yaroqli)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("botsDetail", args=[self.slug])







class Lorem(models.Model):
    class Status(models.TextChoices):
        Yaroqli = "YR","Yaroqli"
        Yaroqsiz = "YS","Yaroqsiz"
    name = models.CharField(max_length=300)
    bio = models.TextField()
    img = models.ImageField(upload_to='category/img')
    date = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(max_length=300)
    status = models.CharField(max_length=2,
                              choices=Status.choices,
                              default=Status.Yaroqli)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("loremsDetail", args=[self.slug])





































