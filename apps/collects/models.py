from django.db import models
from django.contrib.auth.models import User


class Collect(models.Model):
    occasion = (
        ('birth day', 'день рождение'),
        ('marry', 'свадьба'),
    )

    author_fees = models.CharField(max_length=90, verbose_name='Автор сбора')
    title = models.CharField(max_length=90, verbose_name='Название')
    choice_occasion = models.CharField(verbose_name='Повод', choices=occasion)
    description = models.TextField(verbose_name='Описание', max_length=400)
    target_amount = models.DecimalField(max_length=15, decimal_places=2, verbose_name='Нужно собрать')
    collected_amount = models.DecimalField(max_length=15, decimal_places=2, verbose_name='Собранная сумма', default=0)
    contributors_count_donations = models.PositiveIntegerField(default=0, verbose_name='Количество участников')
    image_cover = models.ImageField(upload_to='cover', verbose_name='Обложка сбора')
    end_date = models.DateTimeField(verbose_name='Дата и время завершения сбора')

    class Meta:
        verbose_name = 'Групповой сбор'
        verbose_name_plural = 'Групповые сборы'

    def __str__(self):
        return self.title


class Payment(models.Model):
    collect = models.ForeignKey(Collect, on_delete=models.CASCADE, verbose_name='Групповой сбор')
    contributor = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Участник')
    amount = models.DecimalField(max_length=10, decimal_places=2, verbose_name='Сумма')
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Платёж сбора'
        verbose_name_plural = 'Платёжи сборов'

    def __str__(self):
        return self.collect
