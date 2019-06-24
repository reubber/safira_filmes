from django.db import models

# Create your models here.


class Filme(models.Model):
    GENRE_CHOICE = [
        ('COMEDIA', 'Comédia'),
        ('ACAO', 'Ação'),
        ('HORROR', 'Horror'),
        ('ROMANCE', 'Romance'),
        ('DOCUMENTARIO', 'Documentário'),
        ('FANTASIA', 'Fantasia'),
        ('AVENTURA', 'Aventura')
    ]
    title = models.CharField(max_length=100, verbose_name="Título")
    description = models.CharField(max_length=255, verbose_name="Descrição")
    year = models.DateField(verbose_name="Ano")
    genre = models.CharField(max_length=50, choices=GENRE_CHOICE, default='ACAO', verbose_name="Gênero")
    cover = models.FileField(verbose_name="Imagem",upload_to='capa', null=True, blank=True)

    def __str__(self):
        return self.title
