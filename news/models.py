from django.db import models


class Post(models.Model):
    name = models.CharField('Название', max_length=256)
    content = models.TextField('Контент')
    image = models.ImageField('Изображение', upload_to='news/', null=True, blank=True)
    date_created = models.DateField('Дата публикации')
    tags = models.ManyToManyField('Tag', verbose_name='Теги')

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return self.name


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.CharField(max_length=256)
    text = models.TextField()
    date = models.DateField()

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return f'{self.author} - {self.date}'


class Tag(models.Model):
    name = models.CharField(max_length=256)

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.name
