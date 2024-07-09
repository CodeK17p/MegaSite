from django.db import models

# Create your models here.
class News(models.Model):
    title = models.CharField('Заголовок', max_length=255)
    text = models.TextField('Текст')
    create_date = models.DateField('Дата')
    title = models.CharField('Источник', max_length=255, null=True, blank=True)

    def __str__(self):
        return self.title

class Blog(models.Model):
    title = models.CharField('Заголовок', max_length=255)
    text = models.TextField('Текст')
    create_date = models.DateField('Дата')
    image =  models.ImageField('Картинка',upload_to='blog',null=True, blank=True)
    def __str__(self):
        return self.title
