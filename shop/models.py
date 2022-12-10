from django.core.validators import MaxValueValidator
from django.db import models
from django.template.defaultfilters import slugify


class Wick(models.Model):
    name = models.CharField('Назва', max_length=500)
    price = models.DecimalField('Ціна', max_digits=6, decimal_places=2, default=0)
    promotion = models.IntegerField('Акція в %', validators=[MaxValueValidator(99)], default=0)
    description = models.CharField('Опис', max_length=1000, default='')
    image = models.ImageField('Фото')
    diameter = models.DecimalField('Ширина', max_digits=4, decimal_places=1, default=0)
    booster = models.BooleanField('Бустер', default=False)
    draft = models.BooleanField('Наявність', default=False)
    url = models.SlugField(max_length=130)

    def __str__(self):
        return f'{self.name} - {self.diameter}см: бустер-{self.booster}'

    def save(self, *args, **kwargs):
        self.url = slugify(self.name)
        super(Wick, self).save(*args, **kwargs)


class User(models.Model):
    user_name = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=32)
