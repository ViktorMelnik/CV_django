from django.db import models

# Create your models here.
class Artical(models.Model):
    title = models.CharField("Project name", max_length=70, default='Project name')
    anons = models.CharField("About project", max_length=250, default='About project')
    full_text = models.TextField("Project")
    img = models.ImageField('height_field=300, width_field=300')
    img = models.ImageField(upload_to='static/img')
    date = models.DateTimeField("Publish date")
    
    
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'
