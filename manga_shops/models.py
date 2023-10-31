from django.db import models

class Manga_shops(models.Model):
    GENRE = (
        ('Хоррор', 'Хоррор'),
        ('Комедия','Комедия'),
        ('Фантастика','Фантастика'),
        ('Драмма','Драмма'),
        ('Боевые искусства','Боевые искусства')
    )
    title = models.CharField('Укажите название манги', max_length=100)
    description = models.TextField('Укаэите описание манги')
    image = models.ImageField('Загрузите фото', upload_to='manga/')
    genre = models.CharField('Укажите жанр', max_length=100, choices=GENRE)
    author = models.CharField('Укажите автора', max_length=100)
    cost = models.PositiveIntegerField('Укажите цену')
    year = models.DateTimeField('Укажите дату выпуска манги', null=True)

    def __str__(self):
        return f'{self.title}.{self.genre}'
class ReviewManga(models.Model):
    STARS = (
        ('*', '*'),
        ('* *', '* *'),
        ('* * *', '* * *'),
        ('* * * *', '* * * *'),
        ('* * * * *', '* * * * *')
    )
    manga_select = models.ForeignKey(Manga_shops, on_delete=models.CASCADE,
                                    related_name='comment_object')
    text_comment = models.TextField()
    rate_stars = models.CharField(max_length=20, choices=STARS)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.manga_select} - {self.rate_stars}'