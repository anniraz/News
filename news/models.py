from cProfile import label
from statistics import mode
from django.db import models
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField


class Category(models.Model):
    name = models.CharField(max_length=140)
    image = models.ImageField(blank=True, null=True)
    url = models.SlugField(null=True, unique=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('show_category', kwargs={
            'category_id':self.pk
        })

    class Meta:
        verbose_name_plural = "Категории"
        ordering = ['-id']

class Tags(models.Model):
    title = models.CharField(max_length=255,null=True,blank=True)  


    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural='Теги'     

class News(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True ,verbose_name='Категория')
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    image = models.ImageField(upload_to=" media/", blank=True, null=True, verbose_name='Картина')
    description = RichTextUploadingField(verbose_name='Описание')
    url = models.SlugField(null=True, unique=True, verbose_name='URL' )                                                                                                                                                                                                                      
    tags=models.ManyToManyField(Tags, verbose_name='Теги')

    def __str__(self):
        return self.title
    
    def get_absolue_url(self):
        return f'update/{self.id}'

    class Meta:
        verbose_name_plural = "Новости"
        ordering = ['-id']
    


class SocialSidebar(models.Model):
    social_name = models.CharField(max_length=255,blank=True, null=True,)
    link_address = models.CharField(max_length=255,blank=True,null=True,)
    icon = models.ImageField( upload_to = 'news/',blank=True, null=True,)
    background = models.CharField(max_length=8 ,blank=True,null=True,)

    