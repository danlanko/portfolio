from __future__ import unicode_literals
from ckeditor.fields import RichTextField
from django.utils import timezone
from django.db import models
# Create your models here.

class Blog_Categorie(models.Model):
    category = models.CharField(max_length=50)
    catgory_image = models.ImageField(upload_to='blog_cat_image')

    def save(self, *args, **kwargs):
        # delete old file when replacing by updating the file
        try:
            this = Blog_Categorie.objects.get(id=self.id)
            if this.catgory_image != self.catgory_image:
                this.catgory_image.delete(save=False)
        except:
            pass  # when new photo then we do nothing, normal case
        super(Blog_Categorie, self).save(*args, **kwargs)

    def __str__(self):

        return (self.category)

class Blog(models.Model):
    category = models.ForeignKey(Blog_Categorie)
    title = models.CharField(max_length=250,)
    date = models.DateField(default=timezone.now)
    image = models.ImageField(upload_to='blog_img')
    content = RichTextField()

    def save(self, *args, **kwargs):
        # delete old file when replacing by updating the file
        try:
            this = Blog.objects.get(id=self.id)
            if this.image != self.image:
                this.image.delete(save=False)
        except:
            pass  # when new photo then we do nothing, normal case
        super(Blog, self).save(*args, **kwargs)

    def __str__(self):
        return (self.title)

class Portfolio_Categorie(models.Model):
    port_category =  models.CharField(max_length=250)

    def __str__(self):
        return (self.port_category)

class Portfolio(models.Model):
    port_category = models.ForeignKey(Portfolio_Categorie)
    title = models.CharField(max_length=50)
    live_demo = models.URLField(help_text='Url Field')
    portfolio_image1 = models.ImageField(upload_to='portfolio_img',)

    def save(self, *args, **kwargs):
        # delete old file when replacing by updating the file
        try:
            this = Portfolio.objects.get(id=self.id)
            if this.portfolio_image1 != self.portfolio_image1:
                this.portfolio_image1.delete(save=False)
        except:
            pass  # when new photo then we do nothing, normal case
        super(Portfolio, self).save(*args, **kwargs)

    def __str__(self):
        return (self.title)


class Testimonial(models.Model):
    name = models.CharField(max_length=250)
    testimony = models.TextField()
    job_rank = models.CharField(max_length=300)
    image = models.ImageField(upload_to='testimony', blank=True, null=True)

    def __str__(self):
        return (self.name)

class Technologies(models.Model):
    technology = models.CharField(max_length=50)

    def __str__(self):
        return (self.technology)

class Studying(models.Model):
    studying_what = models.CharField(max_length=50)

    def __str__(self):
        return (self.studying_what)
