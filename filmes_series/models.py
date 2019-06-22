from django.db import models

# Create your models here.


class Filme(models.Model):
    GENRE_CHOICE = [
        ('ACAO', 'Ação'),
        ('COMEDIA', 'Comédia'),
        ('HORROR', 'Horror'),
        ('ROMANCE', 'Romance'),
        ('DOCUMENTARIO', 'Documentário'),
        ('FANTASIA', 'Fantasia'),
        ('AVENTURA', 'Aventura')
    ]
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    year = models.DateField()
    genre = models.CharField(max_length=50, choices=GENRE_CHOICE, default='ACAO')
    cover = models.FileField(upload_to='capa', null=True, blank=True)

    def __str__(self):
        return self.title
