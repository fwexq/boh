from django.db import models

# Create your models here.

class picture(models.Model):
    title = models.CharField('Название', max_length=50)
    opisanie = models.CharField('Описание', max_length=50)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d")



    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Картинка'
        verbose_name_plural='Картинки'