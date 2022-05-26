from django.db import models


class Article(models.Model):
    author_name = models.CharField(verbose_name='author name', max_length=100, default=None)
    title = models.CharField('record title', max_length=200)
    text = models.TextField('record text')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'новость'
        verbose_name_plural = 'новости'