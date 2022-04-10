from django.db import models

# Create your models here.

class Slider(models.Model):
    """Class for constructing pool of images for sliders."""

    image = models.ImageField(upload_to='slider_img/')
    title = models.CharField(max_length=150, verbose_name="Заголовок")
    text = models.CharField(max_length=250, verbose_name="Описание")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Слайд"
        verbose_name_plural = "Слайды"
