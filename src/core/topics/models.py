from django.db import models


class Topic(models.Model):
    file = models.FileField(verbose_name='Изображение', blank=True, null=True)
    name_of_topic = models.CharField(max_length=250, blank=True, null=True)
    description_of_topic = models.CharField(max_length=250, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-id']
        db_table = "topics"

    def __str__(self):
        return '{}'.format(self.name_of_topic)
